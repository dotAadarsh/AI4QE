from datasets import load_dataset
from txtai.embeddings import Embeddings
import streamlit as st


ds = load_dataset("web_questions", split="train")
# Create embeddings index with content enabled. The default behavior is to only store indexed vectors.
embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2", "content": True})
# Map question to text and store content
embeddings.index([(uid, {"url": row["url"], "text": row["question"], "answer": ", ".join(row["answers"])}, None) for uid, row in enumerate(ds)])

def app():

  def question(text):
    return embeddings.search(f"select text, answer, score from txtai where similar('{text}') limit 1")

  query = st.text_input("Question please", "What is the timezone of NYC?")
  st.json(question(query))

