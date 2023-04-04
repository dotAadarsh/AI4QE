from docarray import Document, DocumentArray
import streamlit as st
import openai
import re

def semantic(txt):
    if txt is not None:
        st.markdown(f"[View file]({txt})")
        d = Document(uri=txt).load_uri_to_text()
        with st.expander("Input text", expanded=False):
            st.write(d.text)
        da = DocumentArray(Document(text=s.strip())
                           for s in d.text.split('\n') if s.strip())
        da.apply(lambda d: d.embed_feature_hashing())

        query = st.text_input("Enter the query", "she entered the room")

        q = (
            Document(text=query)
            .embed_feature_hashing()
            .match(da, limit=5, exclude_self=True, metric='jaccard', use_scipy=True)
        )

        result_json = q.matches[:, ('text', 'scores__jaccard')]
        # st.sidebar.json(result_json)
        return result_json


def main():
    st.header("Semantic Document Search")
    st.caption("Powered by JinaAI")
    txt = st.text_input('Please enter .txt file URL',
                        'https://www.gutenberg.org/files/1342/1342-0.txt')

    result = semantic(txt)
    length = len(result[0])
    for i in range(length):
        value = str(result[1][i])
        match = re.search(r"'value':\s*([\d.]+)", value)
        if match:
            value = float(match.group(1))
            st.write(result[0][i] + f" Score: `{value}`")


if __name__ == '__main__':
    main()
