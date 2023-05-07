import streamlit as st
import pandas as pd


def render():
    st.title('2023 개인사업자 캠프 상반기 워크샵!')
    st.write('Welcome to the home page!')

    # 조별 사람들의 데이터 생성
    data = {
        'Group A': ['Person A1', 'Person A2', 'Person A3', 'Person A4', 'Person A5'],
        'Group B': ['Person B1', 'Person B2', 'Person B3', 'Person B4', 'Person B5'],
        'Group C': ['Person C1', 'Person C2', 'Person C3', 'Person C4', 'Person C5'],
        'Group D': ['Person D1', 'Person D2', 'Person D3', 'Person D4', 'Person D5']
    }

    # DataFrame 생성
    df = pd.DataFrame(data)

    # 조별 사람들의 데이터 표시
    st.write(df)
    '''
    columns = st.beta_columns(num_groups)
    for i, group in enumerate(st.session_state.displayed_members, 1):
    with columns[i-1]:
        st.subheader(f"조 {i}")
        for member in group:
            st.text(member)
    '''

