import streamlit as st

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from os import environ
from llm_monitor import MonitorHandler


class MonitoringApp:

    def __init__(self):
        environ["GALILEO_CONSOLE_URL"] = "https://console.dev.rungalileo.io"
        environ["GALILEO_USERNAME"] = "galileo@rungalileo.io"
        environ["GALILEO_PASSWORD"] = "A11a1una!"
        environ["OPENAI_API_KEY"] = "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"

    def run_llm(self, llm, user_prompt):
        if user_prompt is None:
            st.write("Please provide a question.")
        else:
            prompt = PromptTemplate.from_template(
                "Answer the following question: {user_prompt}"
            )
            chain = LLMChain(llm=llm, prompt=prompt)
            result = chain.run(user_prompt=user_prompt)
            st.write(f"{result}\n")


def main():
    app = MonitoringApp()
    llm = ChatOpenAI(
        temperature=0,
        callbacks=[MonitorHandler(project_name=f"galileo_streamlit_application")],
    )
    # app.run_llm(llm, "Why is the sky blue?", metrics=False)
    run_streamlit_app(app, llm)


def run_streamlit_app(app, llm):
    st.markdown("""## Ask me anything""")
    st.markdown("""---""")
    user_question = st.text_input("Ask a Question")
    if st.button("Ask"):
        app.run_llm(llm, user_question)
    st.markdown("""---""")


if __name__ == "__main__":
    main()
