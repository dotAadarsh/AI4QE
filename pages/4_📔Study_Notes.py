import os
import openai
import streamlit as st


def generate_notes(openai, text_input):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{text_input}",
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    st.text(response.choices[0].text)


def main():

    st.header("Generate Notes")
    text_input = st.text_input(
        "Provide a topic and get study notes.", "Key points on DSA")
    openai_key = st.text_input("Please enter OpenAI key here")

    if openai_key:
        openai.api_key = openai_key
        generate_notes(openai, text_input)


if __name__ == '__main__':
    main()
