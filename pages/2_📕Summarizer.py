import openai_summarize
import streamlit as st
import pdfplumber
import json
import requests
from bs4 import BeautifulSoup
from itranslate import itranslate as itrans
from languages import languages

OpenAI_Key = st.secrets["OPENAI_KEY"]

def summarizer(text):
    openai_summarizer = openai_summarize.OpenAISummarize(OpenAI_Key)
    text = text
    summary = openai_summarizer.summarize_text(text)
    return summary

def main():
    
    st.title('Text summarizer')

    Option = st.selectbox("Choose the format", ('Text Input', 'Upload PDF', 'Web Article'), index=2)

    if Option == 'Text Input':
        txt = st.text_area('Text to summarize', '''Blockchain defined: Blockchain is a shared, immutable ledger that facilitates the process of recording transactions and tracking assets in a business network. An asset can be tangible (a house, car, cash, land) or intangible (intellectual property, patents, copyrights, branding). Virtually anything of value can be tracked and traded on a blockchain network, reducing risk and cutting costs for all involved.''')
        if txt is not None:
            summarized_text = summarizer(txt)
            if summarized_text:
                st.success("Successfully summarized!")
                st.write(summarized_text)
                with st.expander("Translate"):
                    to_lang = st.selectbox("Select the language", languages.values())
                    dest = list(languages.keys())[list(languages.values()).index(to_lang)]
                    st.write("language: ", dest)
                    st.text_area("Translated Text", itrans(summarized_text, to_lang = dest))

    elif Option == 'Upload PDF':
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file:
            try:
                fulltext = ""
                with pdfplumber.open(uploaded_file) as pdf:
                    # loop over all the pages
                    for page in pdf.pages:
                        fulltext += page.extract_text()
                    summarized_text = summarizer(fulltext)
                    
                    if summarized_text:
                        st.success("Successfully summarized!")
                        st.write(summarized_text)

            except:
                st.error("Something went wrong!")

    elif Option == 'Web Article':   
        url = st.text_input("URL")
        if url:
            res = requests.get(url)
            html_page = res.content
            soup = BeautifulSoup(html_page, 'html.parser')
            text = soup.find_all(text=True)
            output = ''
            blacklist = [
                '[document]',
                'noscript',
                'header',
                'html',
                'meta',
                'head', 
                'input',
                'script',
                'style',
                'header_navMenu',
                'sponsor_message',
                'thread__wrapper',
            ]

            for t in text:
                if t.parent.name not in blacklist:
                    output += '{} '.format(t).strip()

            fulltext = output.strip()
            summarized_text = summarizer(fulltext)
            
            if summarized_text:
                st.success("Successfully summarized!")
                st.write(summarized_text)
            


if __name__ == "__main__":
    main()
