import streamlit as st
import pandas as pd


# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)


def render_group_score():
    df = load_data(st.secrets["group_score_url"])

    # Create a bar chart
    chart_data = pd.DataFrame(df[['name', 'score']].set_index('name'))
    st.bar_chart(chart_data)


def render_person_score():
    df = load_data(st.secrets["person_score_url"])
    if df.empty:
        st.header("아직 게임 시작 전입니다.")
    else:
        df = df.sort_values(by='점수', ascending=False).reset_index(drop=True)
        st.table(df)


def render_tabs():
    tab_group, tab_person = st.tabs(["조별 점수🏆", "개인별 점수🥇🥈🥉"])

    with tab_group:
        render_group_score()

    with tab_person:
        render_person_score()


def render():
    st.title('게임 🎮🎳🎲🎰')
    st.title('스코어 💰💵💶💳')
    st.write('\n')

    if st.button('Display'):
        render_tabs()
