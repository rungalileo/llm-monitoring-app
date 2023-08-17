import streamlit as st

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from llm_monitor import MonitorHandler


class MonitoringApp:

    def __init__(self):
        self.galileo_console_url = "https://console.dev.rungalileo.io/prompt-monitoring?" \
                   "dataframeColumns=&projectId=23dfca55-a0f9-4ecb-98a9-45f552fcf106"

    def run_llm(self, llm, user_prompt):
        if user_prompt is None:
            st.write("Please provide a question.")
        else:
            prompt = PromptTemplate.from_template("{user_prompt}")
            chain = LLMChain(llm=llm, prompt=prompt)
            result = chain.run(user_prompt=user_prompt)
            st.write(f"{result}\n")
            st.write(f"<a href='{self.galileo_console_url}'>Galileo Link</a>", unsafe_allow_html=True)


def run_streamlit_app(app, llm):
    st.markdown("""## Earnings Call Summarizer""")
    st.markdown(
        """Welcome! Acme has built this summarizer for you. 
            Please paste the earnings call and we'll summarize this for you.""")
    st.markdown("""---""")
    user_question = st.text_area("Enter an earnings call transcript")
    if st.button("Summarize Call"):
        app.run_llm(llm, user_question)
    st.markdown("""---""")


def main():
    app = MonitoringApp()
    llm = ChatOpenAI(
        temperature=0,
        callbacks=[MonitorHandler(project_name=f"fortune500_summaries")],
    )
    # app.run_llm(llm, "Why is the sky blue?", metrics=False)
    run_streamlit_app(app, llm)


if __name__ == "__main__":
    main()
