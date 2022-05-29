import os
import openai
import streamlit as st

def app(): 
    
  openai.api_key = st.secrets["OPENAI_API_KEY"]

  text_input = st.text_input("Provide a topic and get study notes.", "Key points on DSA")

  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"{text_input}",
    temperature=0.3,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  st.json(response)

