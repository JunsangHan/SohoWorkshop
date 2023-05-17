import streamlit as st
import pandas as pd
import home
import group
import graph
import image_create
import score


def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)


def main():
    st.set_page_config(
        page_title='2023 kakaobank SOHO Workshop',
        page_icon=None,
        layout='wide',
        initial_sidebar_state='auto'
    )
    st.sidebar.title('페이지')

    df = load_data(st.secrets["menu_url"])

    # Get the list of pages from the DataFrame
    pages = df['page'].tolist()

    # Show a selectbox in the sidebar with the pages
    page = st.sidebar.selectbox("Choose a page", pages)
    if page == 'Home':
        home.render()
    elif page == 'Group':
        group.render()
    elif page == 'Graph':
        graph.render()
    elif page == 'Bonus':
        image_create.render()
    elif page == 'Score':
        score.render()


if __name__ == '__main__':
    main()
