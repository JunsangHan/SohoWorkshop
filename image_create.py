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

        image_urls = [data['url'] for data in response['data']]
        st.image(image_urls, width=250)
        # st.image(image_urls, use_column_width=True)
        for url in image_urls:
            # st.text(url)
            st.text_area('Copy the URL below:', value=url, max_chars=None)
            st.write('\n')
