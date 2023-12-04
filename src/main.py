from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = OpenAI(temperature = 0)
tools = load_tools(["serpapi"], llm=llm)


prompt = PromptTemplate(
    input_variables=['name'],
    template="""Consider that I want to watch a show in {country}. Look in TV
channels and streaming services and answer me in which channel this show is
airing: {name}. Before giving back the answer, make sure it is correct. But
more importantly, if you don't know the answer, just say 'I don't know'."""
)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=False)

question = prompt.format(name="The Simpsons", country="Brazil")

answer = agent.run(question)

st.write(answer)

