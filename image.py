import streamlit as st
from PIL import Image
import io
import requests
import base64
import openai
from io import BytesIO


def resize_image(image: Image.Image, max_size: int) -> Image.Image:
    """Resize the image so that its size does not exceed max_size in kilobytes"""

    while image_size(image) > max_size:
        # Decrease the size of the image by a factor of 0.9 each time the loop is run
        width, height = image.size
        image = image.resize((int(width * 0.9), int(height * 0.9)))

    return image


def image_size(image: Image.Image) -> int:
    """Return the size of the image in kilobytes"""

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return len(img_byte_arr) / 1024


def image_to_base64(image: Image.Image) -> str:
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return base64.b64encode(img_byte_arr).decode('utf-8')


def edit_image(image: str, prompt: str) -> str:
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = st.secrets["openai_api_key"]
    openai.Image.create_edit(
        image=open("otter.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A cute baby sea otter wearing a beret",
        n=2,
        size="1024x1024"
    )

    # url = "https://api.openai.com/v1/images/edits"
    #
    # headers = {
    #     "Content-Type": "application/json",
    #     "Authorization": f"Bearer {openai_api_key}"
    # }
    #
    # data = {
    #     "image": image,
    #     "prompt": prompt,
    #     "n": 1,
    #     "size": "1024x1024",
    #     "response_format": "url"
    # }
    #
    # response = requests.post(url, headers=headers, json=data)
    # response.raise_for_status()
    # print(response.json())
    #
    # return response.json()["urls"][0]


def render():
    st.title('Image Upload and Processing')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = image.convert("RGB")

        # Read the image file from disk and resize it
        # image = Image.open("image.png")
        width, height = 256, 256
        image = image.resize((width, height))

        # Convert the image to a BytesIO object
        byte_stream = BytesIO()
        image.save(byte_stream, format='PNG')
        byte_array = byte_stream.getvalue()

        openai.api_key = openai_api_key
        response = openai.Image.create_variation(
            image=byte_array,
            n=4,
            size="1024x1024"
        )
        print(response['data'][0]['url'])
        st.text = response['data'][0]['url']
        print(response['data'])


        # # Convert and resize image as before...
        #
        # # Convert the image to base64
        # img_b64 = image_to_base64(img)
        #
        # # Prompt for the image edit
        # prompt = st.text_input("Enter the prompt for the image edit")
        #
        # if prompt:
        #     # Edit the image using the OpenAI API
        #     edited_img_url = edit_image(img_b64, prompt)
        #
        #     # Display the original and edited images
        #     st.image(img, caption='Original Image')
        #     st.image(edited_img_url, caption='Edited Image')
