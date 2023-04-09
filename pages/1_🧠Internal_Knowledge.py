import streamlit as st
import pandas as pd 
from streamlit_chat import message
from generate_transcript import generate_transcript
from generate_blog import create_content
import openai

openai.api_key = st.secrets["OPENAI_KEY"]


def main():

    st.header("Internal Knowledge")
    st.caption("Empower your students with knowledge at their fingertips")

    # Connect to the Google Sheet

    sheet_id = st.sidebar.text_input("Enter the sheet ID", "1HEzrlIGmNg6y0JPaV11ZEJzw3byq37Vf2DsD4hHFEIk")
    sheet_name = st.sidebar.text_input("Enter sheet name", "resources")

    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url, dtype=str).fillna("")

    # Use a text_input to get the keywords to filter the dataframe
    text_search = st.sidebar.text_input("Search videos by channel or speaker or keyword", value="ai")
    st.sidebar.markdown("[Example CSV file](https://docs.google.com/spreadsheets/d/1HEzrlIGmNg6y0JPaV11ZEJzw3byq37Vf2DsD4hHFEIk/edit?usp=sharing)")

    # Filter the dataframe using masks
    m1 = df["Channel"].str.contains(text_search)
    m2 = df["Title"].str.contains(text_search)
    m3 = df["Keywords"].str.contains(text_search)
    df_search = df[m1 | m2 | m3]
    # Another way to show the filtered results
    # Show the cards

    N_cards_per_row = 1
    if text_search:
        for n_row, row in df_search.reset_index().iterrows():
            i = n_row%N_cards_per_row
            if i==0:
                st.write("---")
                cols = st.columns(N_cards_per_row, gap="large")
            # draw the card
            with cols[n_row%N_cards_per_row]:
                st.caption(row['Date'])
                st.markdown(f"**{row['Channel'].strip()}**")
                butt = st.button(f"*{row['Title'].strip()}*")
                if butt:
                    transcript = ""
                    tab1, tab2, tab3 = st.tabs(["Video","Article", "Audio"])

                    with tab1:
                        st.header(row['Title'].strip())
                        st.video(row['Video'])
                        with st.expander("Transcript"):
                            whisper_response = generate_transcript(row['Video'])
                            transcript = whisper_response["text"]
                            st.write(transcript)

                    with tab2:
                        st.write(create_content(transcript))
                        
                    with tab3:
                        st.header("Listen to it")
                        st.audio(data="./audio.mp4")
    
if __name__ == "__main__":
    main()