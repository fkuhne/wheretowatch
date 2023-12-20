from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.tools import Tool
# from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import load_tools

from dotenv import load_dotenv
import streamlit as st

load_dotenv()

prompt = PromptTemplate(
    input_variables=['country','title'],
    template="""I am in {country} and want to watch the show {title} on TV.
Please, search really hard throughout the Internet and answer me where {title}
is currently airing. Use only TV channels or streaming services like, for
example, HBO, Netflix, Apple TV and so on, and disregard everything else.
Disregard any information about the show being available in another country
other than {country}. Before giving back the answer, make sure it is correct.
If you don't know or couldn't find the answer, say 'Sorry, but I don't know'.
"""
)

llm = OpenAI(temperature = 0)

tools = load_tools(["google-search"])

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=False
)

st.header('📺🍿 Where To Watch?')
st.divider()
st.warning('I’ve run out of credits for OpenAI API and your search will not work until I refill it.', icon="⚠️")
title = st.text_input('What is the name of the show?')
country = st.text_input('In which country?', 'Brazil')
question = prompt.format(country=country, title=title)
if st.button('Search'):
    with st.spinner('Searching...'):
        try:
            answer = agent.run(question)
            st.info("🟢 **{answer}**".format(answer=answer))
        except Exception as e:
            st.write("⚠️ We're a little busy crafting byte-sized popcorn insights 😣. Try again in a bit!")
            exception_type = type(e).__name__
            st.error("Exception type: {}".format(exception_type))

st.divider()
st.markdown("""⚠️ *:gray[Please note that this is an experimental project.  
You may face quota/rate limit warnings from Google or OpenAI cloud services.]*""")
st.divider()
st.markdown(
    """<div style="text-align: center; color: gray">
        Made by <a href="https://github.com/fkuhne" target="_blank">fkuhne</a>.
    </div>""",
    unsafe_allow_html=True
)
