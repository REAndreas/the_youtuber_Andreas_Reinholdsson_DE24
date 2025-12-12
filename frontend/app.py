import streamlit as st
import requests
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

ASSETS_PATH = Path(__file__).parents[1]
url = f"https://youtuber-andreas-de24.azurewebsites.net/rag/query?code={os.getenv('API_KEY')}"


def layout():
    st.markdown("# The Youtuber")

    left_column, right_column = st.columns(2)

    left_column.markdown("Ask about data engineering topics")

    right_column.image(ASSETS_PATH / f"kokchun.png")
    
    text_input = st.text_input(label= "Ask a question")

    if st.button("Inquire") and text_input != "":
        response = requests.post(url, json={"prompt": text_input})

        data = response.json()

        st.markdown("## Question")
        st.markdown(text_input)

        st.markdown("## Answer")
        st.markdown(data["answer"])

        st.markdown("## Source")
        st.markdown(data["filepath"])


if __name__ == "__main__":
    layout()