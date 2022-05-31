from docarray import Document, DocumentArray
import streamlit as st
import os
import openai

def app(): 

    txt = st.text_input('PLeas enter .txt file URL', 'https://www.gutenberg.org/files/1342/1342-0.txt')

    if txt is not None:
        st.markdown(f"[View file]({txt})")         
        d = Document(uri=txt).load_uri_to_text()
        da = DocumentArray(Document(text=s.strip()) for s in d.text.split('\n') if s.strip())
        da.apply(lambda d: d.embed_feature_hashing())

        query = st.text_input("Enter the query", "she entered the room")

        q = (
            Document(text=query)
            .embed_feature_hashing()
            .match(da, limit=5, exclude_self=True, metric='jaccard', use_scipy=True)
        )
        
        st.json(q.matches[:, ('text', 'scores__jaccard')])