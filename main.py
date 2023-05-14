import streamlit as st
import home
import score
import graph
import image
import prompt
import sheet_test


def main():
    st.set_page_config(
        page_title='2023 kakaobank SOHO Workshop',
        page_icon=None,
        layout='wide',
        initial_sidebar_state='auto'
    )
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ('Home', 'Score', 'Graph'))

    if page == 'Home':
        home.render()
    elif page == 'Score':
        # score.render()
        # image.render()
        # prompt.render()
        sheet_test.render()
    else:
        graph.render_sample()


if __name__ == '__main__':
    main()
