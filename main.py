import streamlit as st
import home
import group
import graph
import image_create
import image_sample
import score


def main():
    st.set_page_config(
        page_title='2023 kakaobank SOHO Workshop',
        page_icon=None,
        layout='wide',
        initial_sidebar_state='auto'
    )
    st.sidebar.title('Navigation')
    # Home, Group, Graph, ImageCreate, ImageModification, Score, QuizGraph
    page = st.sidebar.radio('Go to', ('Home', 'Group', 'Graph', 'ImageCreate', 'ImageSample', 'Score'))

    if page == 'Home':
        home.render()
    elif page == 'Group':
        group.render()
    elif page == 'Graph':
        graph.render()
    elif page == 'ImageCreate':
        image_create.render()
    elif page == 'ImageSample':
        image_sample.render()
    elif page == 'Score':
        score.render()
    else:
        home.render()


if __name__ == '__main__':
    main()
