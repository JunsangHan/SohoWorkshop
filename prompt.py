import streamlit as st
import openai


def render():
    prompt = st.text_input("Enter the prompt for the image edit")

    if prompt:
        openai.api_key = st.secrets["openai_api_key"]
        response = openai.Image.create(
            prompt=prompt,
            n=4,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        st.image(image_url)
        print(response['data'])
