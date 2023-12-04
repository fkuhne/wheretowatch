from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# llm = OpenAI(temperature = 0)
llm = HuggingFaceHub(
    repo_id="meta-llama/Llama-2-70b-hf",
    model_kwargs={"temperature": 0},

)

tools = load_tools(["serpapi"], llm=llm)

prompt = PromptTemplate(
    input_variables=['country','title'],
    template="""Consider that I want to watch a show in {country}. Look in TV
channels and streaming services and answer me in which channel this show is
airing: {title}. Before giving back the answer, make sure it is correct. But
more importantly, if you don't know the answer, just say 'Sorry, but I don't know'."""
)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=False)

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
color: '#f0f0f0';
}
</style>
<div class="footer">
<p>Made by <a href="https://https://github.com/fkuhne" target="_blank">fkuhne</a>.</p>
</div>
"""

st.header('📺🍿 Where To Watch?')
st.divider()
title = st.text_input('What is the name of the show?', 'Life of Brian')
country = st.text_input('In which country?', 'Croatia')
question = prompt.format(country=country, title=title)
st.markdown(footer,unsafe_allow_html=True)
if st.button('Search'):
    with st.spinner('Searching...'):
        answer = agent.run(question)
        st.write("**{answer}**".format(answer=answer))
