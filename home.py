import base64

import streamlit as st


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """, unsafe_allow_html=True
    )


def render():
    add_bg_from_local('utils/merged.jpg')

    # page_bg_img = '''
    # <style>
    # body {
    # background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    # background-size: cover;
    # }
    # </style>
    # '''
    #
    # st.markdown(page_bg_img, unsafe_allow_html=True)

    # Add custom CSS for background image
    # st.markdown(
    #     """
    #     <style>
    #     .reportview-container {
    #         background: url("utils/merged.jpg");
    #         background-size: cover;
    #         background-repeat: no-repeat;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )
    st.title('2023 개인사업자 캠프 상반기 워크샵!')
