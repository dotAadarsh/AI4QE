import streamlit as st
import streamlit.components.v1 as components

OpenAI_Key = st.secrets["OPENAI_KEY"]


st.set_page_config(
    page_title="AI4QE",
    page_icon="https://cdn-icons-png.flaticon.com/512/2617/2617909.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.markdown("> `Alpha version 1.1.2`")

with st.sidebar:
    components.html(
        """<a class="github-button" href="https://github.com/dotaadarsh/AI4QE" data-color-scheme="no-preference: dark_high_contrast; light: dark_high_contrast; dark: dark_high_contrast;" data-icon="octicon-star" aria-label="Star madmax-ak/Clang-cheatsheet on GitHub">Star</a>
<script async defer src="https://buttons.github.io/buttons.js"></script>
<a href="https://twitter.com/dotaadarsh?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @dotaadarsh</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
""",
        height=30,)

st.image("asserts/ai4qe.png")
st.markdown("""
# AI4QE

## *Artificial Intelligence for Quality Education*

This project is created for the [Hackatra hackathon](https://hackatra.devpost.com/). The problems statements can be found in this [Github repo](https://github.com/vruksheco/Hackatra).
Let's see what AI4QE does!

### Introduction

AI4QE is an app which help to provide the Quality Education with the help of Artificial Intelligence.  It is powered by [OpenAI](https://openai.com/), [HuggingFace](https://huggingface.co/), DocArray and Streamlit. 

 - **Text Summarizer** - It is a automatic text summarization page which supports different types of text data from different sources.
 - **Semantic Search** - Semantic search is a data searching technique in which a search query not only finds keywords, but also determines the intent and contextual meaning of the words a person is using for search. With the help of OpenAI it performs the [semantic search](https://beta.openai.com/docs/guides/search) on the given document and provide the best result.
 - **Study Notes** - This page will provides the study notes on the given query.  It is again fully powered by the OpenAI GPT-3 engine. 

### Tools & Software used

 - [Streamlit](https://streamlit.io/) is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time.
 - [Generative Pre-trained Transformer 3](https://beta.openai.com/docs/engines/gpt-3) is a model that uses deep learning to predict human-like text. It is the third-generation language prediction model in the GPT-n series created by OpenAI.
 - [Gitpod](https://www.gitpod.io/) - It allows you to define your project's configuration in code so you can launch a prebuilt development environment with one click.
 - [DocArray](https://docarray.jina.ai/) - The DocArray library is a way to store and transfer data that doesn't have a specific structure. This includes things like text, images, audio, and video. The library makes it easier to process and search this kind of data using a Pythonic API.
 - [docx2txt](https://pypi.org/project/docx2txt/) - A pure python-based utility to extract text and images from docx files.
 - [pdfplumber](https://pypi.org/project/pdfplumber/0.1.2/) - Plumb a PDF for detailed information about each char, rectangle, line, etc.
 - [txtai](https://github.com/neuml/txtai) - txtai executes machine-learning workflows to transform data and build AI-powered semantic search applications.

""")
 