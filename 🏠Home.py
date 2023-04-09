import streamlit as st
import streamlit.components.v1 as components

OpenAI_Key = st.secrets["OPENAI_KEY"]


st.set_page_config(
    page_title="AI4QE",
    page_icon="https://cdn-icons-png.flaticon.com/512/2617/2617909.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.markdown("> `Alpha version 1.1.3`")

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


## Introduction

AI4QE is an app which help to provide the Quality Education with the help of Artificial Intelligence.  It is mostly powered by [OpenAI](https://openai.com/). 

### Features/Tools

#### Internal Knowledge Tool

This tool helps in integrating contents from CSV file in which the staff members adds contents, with AI to provide multilingual transcript, summary, notes, blog and audio based features to enhance the students experience for a particular context created by staff members. 

**How this will be helpful?**

For students:

Transcript of the video: Students will be able to access the transcript of the video, which will help them better understand the content covered in the video. This feature will be especially helpful for students who prefer reading to watching videos or who want to quickly search for specific information covered in the video.

Multilingual support: It enabling students who are more comfortable with languages other than English to access the content in their preferred language. This feature will be particularly beneficial for international students and those studying in non-English speaking countries.

Generates blog from video: By generating blog from videos, it will provide students with an additional resource to review the material covered in the video. This feature will also help students who prefer reading to watching videos or who want to quickly review the material.

Chatbot for queries: The app's chatbot feature will enable students to ask questions related to the video content and receive immediate answers. This feature will help students clarify any doubts they may have about the material covered in the video.

Questions and notes generator: By generating questions and notes related to the video content, it will help students reinforce their understanding of the material and prepare for exams.

For staff members:

CSV integration: Staff members will be able to post links to videos and resources in a CSV file, which will be automatically integrated with the app. This feature will save staff members time and effort in uploading and managing content on the app.

Chatbot for queries: The app's chatbot feature will enable staff members to answer questions related to the video content and provide support to students. This feature will help staff members manage student queries more efficiently.

Questions and notes generator: The app's questions and notes generator feature will also help staff members prepare quizzes and assessments related to the video content, making the process more efficient and effective.


#### Summarizer
 
The summarizer tool supports various formats of file and helps in summarizing large texts. 

**How this will be helpful?**

- Saving time: One of the main benefits of a summarizer tool is that it can save time. Rather than having to read through an entire document or watch a long video, a user can quickly generate a summary that provides the key points or highlights of the content. This can be particularly helpful for busy professionals or students who have a lot of material to cover in a short amount of time.

- Improved understanding: Summarizer tools can also improve a user's understanding of the content by distilling complex or lengthy material into a more digestible format. By focusing on the main points and key ideas, a summary can help a user better comprehend the material and retain the information more effectively.

- Consistent quality: A summarizer tool can provide consistent quality summaries regardless of the original format of the content. Whether the content is in written form (such as a report or article), audio form (such as a podcast or recorded lecture), or video form, the summarizer tool can provide a summary that accurately captures the key points and main ideas.

- Accessibility: A summarizer tool can also make content more accessible to users who may have difficulty with certain formats, such as those with visual impairments or who struggle with reading lengthy documents. By providing a summary, the tool can make the content more manageable and easier to understand for these users.




### Tools & Software used

 - [Streamlit](https://streamlit.io/) is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time.

 - [Generative Pre-trained Transformer 3](https://beta.openai.com/docs/engines/gpt-3) is a model that uses deep learning to predict human-like text. It is the third-generation language prediction model in the GPT-n series created by OpenAI.

 - [Gitpod](https://www.gitpod.io/) - It allows you to define your project's configuration in code so you can launch a prebuilt development environment with one click.


### Try it out!

[Live Project - AI4QE](https://ai4qedu.streamlit.app/)

#### By using CDE

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/dotaadarsh/AI4QE)

Don't forget to change the API KEY from OpenAI in the .streamlit/secreats.toml file. The Gitpod will automatically build's the environment. Finally, enter the command as follows in the terminal to get the app running.

>    streamlit run app.py

""")
 