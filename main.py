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
        page_title='kakaobank Soho Workshop',
        page_icon=None,
        layout='wide',
        initial_sidebar_state='auto'
    )
    st.sidebar.title('페이지')

    df = load_data(st.secrets["menu_url"])

    # Convert the DataFrame to a dictionary
    pages_mapping = pd.Series(df.name.values, index=df.page).to_dict()

    # Get the list of display names from the dictionary
    display_pages = list(pages_mapping.values())

    # Show a selectbox in the sidebar with the display pages
    selected_page = st.sidebar.selectbox("Choose a page", display_pages)

    # Map back from the display name to the page name
    page = list(pages_mapping.keys())[list(pages_mapping.values()).index(selected_page)]

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
