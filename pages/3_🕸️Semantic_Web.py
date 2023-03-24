from docarray import Document, DocumentArray
import streamlit as st
import os
import openai
import jsonlines


def semantic_web(openai, input_query):

    try:
        search_response = openai.Engine("davinci").search(
            search_model="davinci",
            query=input_query,
            max_rerank=5,
            file="file-yyPiWKEFK9tf5vhFNF7A4gki",
            return_metadata=True
        )

        st.json(search_response.data)
        st.text(search_response.data[0].text)

    except:
        st.info("Error with the OpenAI Key")


def main():

    openai_key = st.text_input("Please enter OpenAI key here")
    if openai_key:
        openai.api_key = openai_key

        st.header("Semantic Web")
        input_query = st.text_input("Enter your query", "neural")

        with st.expander("Resource file"):
            with jsonlines.open('asserts/resources.jsonl') as f:
                for line in f.iter():
                    st.text(line)

        if input_query:
            semantic_web(openai, input_query)


if __name__ == '__main__':
    main()
