from docarray import Document, DocumentArray
import streamlit as st
import os
import openai
import jsonlines

def app(): 

    with st.expander("Resource file"):
        with jsonlines.open('/workspace/hackatra/asserts/resources.jsonl') as f:
            for line in f.iter():
                st.text(line)

    input_query = st.text_input("Enter your query", "neural")

    openai.api_key = st.secrets["OPENAI_API_KEY"]

    search_response = openai.Engine("davinci").search(
        search_model="davinci", 
        query=input_query, 
        max_rerank=5,
        file="file-yyPiWKEFK9tf5vhFNF7A4gki",
        return_metadata=True
    )

    st.json(search_response.data)

    st.text(search_response.data[0].text)
