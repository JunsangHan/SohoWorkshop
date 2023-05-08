import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network


def render_graph():
    # CSV 파일 읽기
    data = pd.read_csv('assets/people_data.csv')

    # 그래프 생성 및 노드 추가
    G = nx.Graph()

    for index, row in data.iterrows():
        G.add_node(row['이름'], cell=row['셀'], group=row['직군'], domain1=row['도메인1'], domain2=row['도메인2'])

        if not pd.isna(row['도메인1']):
            G.add_edge(row['이름'], row['도메인1'])

        if not pd.isna(row['도메인2']):
            G.add_edge(row['이름'], row['도메인2'])

    # Pyvis 네트워크로 변환 및 시각화
    nt = Network(notebook=True)
    nt.from_nx(G)
    nt.show('people_graph.html')
    st.write("People Graph:")
    st.components.v1.html(nt.html, width=800, height=800, scrolling=False)


def render():
    st.title('2023 개인사업자 캠프 상반기 워크샵!')
    st.write('Welcome to the home page!')

    # 조별 사람들의 데이터 생성
    data = {
        'A': ['simon.sung', 'july.jy', 'uno.s', 'loki.l', 'harper.ha'],
        'B': ['arnold.oh', 'jk.tabris', 'kyle.k', 'jerome.jung', 'benji.k'],
        'C': ['mason.chi', 'top.lee', 'ayla.y', 'alan.kim', 'scarlet.ryu'],
        'D': ['stan.lee', 'paul.wbc', 'tyler.sg', 'hank.j', 'aiden.l']
    }

    num_columns = len(data)
    cols = st.columns(num_columns)

    for i, (group, members) in enumerate(data.items()):
        with cols[i]:
            st.subheader(group)
            for member in members:
                st.write(member)

    render_graph()

