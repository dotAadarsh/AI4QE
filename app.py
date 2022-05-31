#import libraries
import streamlit as st 
from multipage import MultiPage
from pages import summarizer, semantic_doc, semantic_web, study_notes
import streamlit.components.v1 as components

# Configures the default settings of the page.
st.set_page_config(
     page_title="AI4QE",
     page_icon="https://cdn-icons-png.flaticon.com/512/2617/2617909.png",
     layout="wide",
     initial_sidebar_state="expanded",
 )

st.sidebar.markdown("> `Alpha version 1.1.1`")
with st.sidebar:
     components.html(
    """<a class="github-button" href="https://github.com/dotaadarsh/AI4QE" data-color-scheme="no-preference: dark_high_contrast; light: dark_high_contrast; dark: dark_high_contrast;" data-icon="octicon-star" aria-label="Star madmax-ak/Clang-cheatsheet on GitHub">Star</a>
<script async defer src="https://buttons.github.io/buttons.js"></script>
<a href="https://twitter.com/madmax_ak?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-screen-name="false" data-show-count="false">Follow @madmax_ak</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
""",
    height=30,)

app = MultiPage() # Create an instance of the app 

st.image("asserts/ai4qe.png")
st.sidebar.title("AI4QE") 
st.sidebar.caption("AI for Quality Education")

# Calling all applications
app.add_page("Summarizer", summarizer.app)
app.add_page("Semantic-Doc", semantic_doc.app)
app.add_page("Semantic-Web", semantic_web.app)
app.add_page("Study Notes", study_notes.app)

# The main app
app.run()
