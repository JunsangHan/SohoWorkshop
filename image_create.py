import streamlit as st
import openai


def render():
    st.title('보너스 페이지 👩‍🎨👨‍🎨🖼')
    st.text('\n')
    st.text('조별 미션 하느라 고생 많으셨습니다.')
    st.text('아래 입력창에 텍스트를 입력하면 AI가 그림을 그려서 보여줍니다.')
    st.text('조별 미션하면서 찍은 사진을 AI가 그려줄 수 있도록 텍스트를 입력해보세요.')
    st.text('포즈만 비슷해도 푸짐한 보너스 점수가!!')
    st.text('Hint: 영어로 입력해야 잘 그려줍니다. 번역기를 활용해보세요😃😄😆')
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
