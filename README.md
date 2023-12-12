# 📺🍿 Where To Watch?

A simple application to find out where your favorite show is airing.

Made with [Langchain](https://www.langchain.com/), [OpenAI](https://openai.com/), and [Streamlit](https://streamlit.io/).

## Live demo

https://wheretowatch.streamlit.app

## How to run

1. Grab an API key for [OpenAI](https://platform.openai.com/api-keys).

2. Configure a search engine in Google Cloud by following [these tips](https://python.langchain.com/docs/integrations/tools/google_search);

3. Create a file called `.env` with the following content:

```shell
OPENAI_API_KEY=your-key-here
GOOGLE_API_KEY=your-key-here
GOOGLE_CSE_ID=your-key-here
```

It is possible that you will need to [purchase credits from OpenAI](https://platform.openai.com/account/billing/overview), if you don't have any.

3. Install the dependencies:

```shell
pip install -r requirements.txt
```

4. Start the Streamlit app with:

```shell
streamlit run main.py
```

The webapp will show up in the browser.

## Detailed description

To be written.

## Links and references:

- [ReAct agent in langchain](https://python.langchain.com/docs/modules/agents/agent_types/react)
  - [About ReAct (reason + act)](https://react-lm.github.io/)
- [Google search integration with Langchain](https://python.langchain.com/docs/integrations/tools/google_search)
  - [Setting up a Programmable search engine in Google Cloud](https://stackoverflow.com/a/37084643)
- [Streamlit components](https://streamlit.io/components)
