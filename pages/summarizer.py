import streamlit as st
import docx2txt
import pdfplumber
import os 
import openai
import json
from txtai.pipeline import Summary, Textractor
from txtai.workflow import UrlTask, Task, Workflow

def app():
        
    grade = st.sidebar.selectbox('Select your grade', ('First-Grade', 'Second-Grade', 'Third-Grade', 'Fourth-Grade', 'Fifth-Grade', 'Sixth-Grade', 'Seventh-Grade', 'Eith-Grade', 'Ninth-Grade', 'Tenth-Grade', 'Eleventh-Grade', 'Twelth-Grade'))
    page = st.sidebar.radio('Choose the page', ('Text summarizer', 'Semantic search'))

    if page == 'Text summarizer':

        openai.api_key = st.secrets["OPENAI_API_KEY"]

        st.title('Text summarizer')
        
        def summarizer(value) :

            response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Summarize this for a {grade} student:\n\n {value}",
            temperature=0.7,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
            st.json(response) 
            st.write(response["choices"][0]["text"])

        Option = st.selectbox("Choose the format", ('Text Input', 'Upload PDF', 'Web Article'))

        if Option == 'Text Input':
            txt = st.text_area('Text to summarize', '''Blockchain defined: Blockchain is a shared, immutable ledger that facilitates the process of recording transactions and tracking assets in a business network. An asset can be tangible (a house, car, cash, land) or intangible (intellectual property, patents, copyrights, branding). Virtually anything of value can be tracked and traded on a blockchain network, reducing risk and cutting costs for all involved.''')
            if txt is not None:
                summarizer(txt)

        elif Option == 'Upload PDF':
            docx_file = st.file_uploader("Choose a file")

            if docx_file is not None:
                file_details = {"filename":docx_file.name, "filetype":docx_file.type,
                                "filesize":docx_file.size}
                st.write(file_details)

                if docx_file.type == "text/plain":
                    # Read as string (decode bytes to string)
                    raw_text = str(docx_file.read(),"utf-8")
                    st.text(raw_text)

                elif docx_file.type == "application/pdf":

                    try:
                        with pdfplumber.open(docx_file) as pdf:
                            pages = pdf.pages[0]
                            extract = pages.extract_text()
                            st.write(extract)
                            summarizer(extract)

                    except:
                        st.write("None")

                else:   
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)

        elif Option == 'Web Article':

            class Application:
                """
                Main application.
                """

                def __init__(self):
                    """
                    Creates a new application.
                    """

                    textract = Textractor(paragraphs=True, minlength=100, join=True)
                    summary = Summary("sshleifer/distilbart-cnn-12-6")
                    self.workflow = Workflow([UrlTask(textract), Task(summary)])

                def run(self):
                    """
                    Runs a Streamlit application.
                    """ 

                    st.header("Article Summary")
                    st.markdown("This application builds a summary of an article.")

                    url = st.text_input("URL")
                    if url:
                        # Run workflow and get summary
                        summary = list(self.workflow([url]))[0]

                        # Write results
                        st.write(summary)
                        st.markdown("*Source: " + url + "*")


            @st.cache(allow_output_mutation=True)
            def create():
                """
                Creates and caches a Streamlit application.
                Returns:
                    Application
                """

                return Application()


            if __name__ == "__main__":
                os.environ["TOKENIZERS_PARALLELISM"] = "false"

                # Create and run application
                app = create()
                app.run()