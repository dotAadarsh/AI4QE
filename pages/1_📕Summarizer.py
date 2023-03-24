import streamlit as st
import docx2txt
import pdfplumber
import os
import openai
import json
# from txtai.pipeline import Summary, Textractor
# from txtai.workflow import UrlTask, Task, Workflow


def summarizer(value, openai):

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Summarize this for a {grade} student:\n\n {value}",
            temperature=0.7,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        st.success("Successfully Summarized 👇")
        st.write(response["choices"][0]["text"])
        with st.sidebar.expander("JSON Output"):
            st.json(response)
    except:
        st.info("OpenAI trial limit exceeded")


def main():

    st.title('Text summarizer')

    openai_key = st.text_input("Please enter OpenAI key here")
    openai.api_key = openai_key

    if openai_key:
        grade = st.sidebar.selectbox(
            'Select your grade', ('Primary', 'Middle', 'Secondary', 'College'))
        Option = st.selectbox("Choose the format",
                              ('Text Input', 'Upload PDF', 'Web Article'))

        if Option == 'Text Input':
            txt = st.text_area('Text to summarize', '''Blockchain defined: Blockchain is a shared, immutable ledger that facilitates the process of recording transactions and tracking assets in a business network. An asset can be tangible (a house, car, cash, land) or intangible (intellectual property, patents, copyrights, branding). Virtually anything of value can be tracked and traded on a blockchain network, reducing risk and cutting costs for all involved.''')
            if txt is not None:
                summarizer(txt)

        elif Option == 'Upload PDF':
            docx_file = st.file_uploader("Choose a file")

            if docx_file is not None:
                file_details = {"filename": docx_file.name, "filetype": docx_file.type,
                                "filesize": docx_file.size}
                with st.sidebar.expander("File Info"):
                    st.json(file_details)

                if docx_file.type == "text/plain":
                    # Read as string (decode bytes to string)
                    raw_text = str(docx_file.read(), "utf-8")
                    st.text_area("Extracted Text", raw_text)

                elif docx_file.type == "application/pdf":

                    try:
                        with pdfplumber.open(docx_file) as pdf:
                            pages = pdf.pages[0]
                            extract = pages.extract_text()
                            st.text_area("Extracted Text", extract)
                            summarizer(extract)

                    except:
                        st.write("None")

                else:
                    raw_text = docx2txt.process(docx_file)
                    st.text_area("Extracted Text", raw_text)

        elif Option == 'Web Article':
            url = st.text_input("URL")
            if url:
                summary = list(self.workflow([url]))[0]
                st.write("Output")
                st.write(summary)
                st.markdown("*Source: " + url + "*")

                textract = Textractor(
                    paragraphs=True, minlength=100, join=True)
                summary = Summary("sshleifer/distilbart-cnn-12-6")
                workflow = Workflow([UrlTask(textract), Task(summary)])

                url = st.text_input("URL")
                if url:
                    summary = list(self.workflow([url]))[0]
                    st.write("Output")
                    st.write(summary)
                    st.markdown("*Source: " + url + "*")


if __name__ == "__main__":
    main()
