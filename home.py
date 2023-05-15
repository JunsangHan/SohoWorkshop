import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network

# CSV 파일 읽기
df = pd.read_csv('assets/people_data.csv')
# 그래프 생성 및 노드 추가
G = nx.Graph()

for index, row in df.iterrows():
    G.add_node(row['이름'], group=row['직군'], cell=row['셀'], domain1=row['도메인1'], domain2=row['도메인2'])

    # 같은 속성을 공유하는 노드 사이의 엣지 추가
for i, row_i in df.iterrows():
    for j, row_j in df.iterrows():
        if i != j:
            if row_i['직군'] == row_j['직군'] or row_i['셀'] == row_j['셀'] or row_i['도메인1'] == row_j['도메인1'] \
                    or row_i['도메인2'] == row_j['도메인2']:
                G.add_edge(row_i['이름'], row_j['이름'])


def create_filtered_graph(selected_names):
    nodes_to_keep = set(selected_names)
    for name in selected_names:
        nodes_to_keep.update(G.neighbors(name))
    sub_G = G.subgraph(nodes_to_keep).copy()
    return sub_G


def show_filtered_graph(_filtered_graph):
    # Pyvis 네트워크로 변환 및 시각화
    nt = Network(notebook=True, height='800px', width='100%', bgcolor='#222222', font_color='white')

    # Configure physics options
    nt.options = {
        "physics": {
            "stabilization": {
                "enabled": True,
                "iterations": 1000,
                "updateInterval": 50,
                "onlyDynamicEdges": False
            },
            "barnesHut": {
                "gravitationalConstant": -4000,
                "centralGravity": 0.2,
                "springLength": 200,
                "springConstant": 0.01,
                "damping": 0.9,
                "avoidOverlap": 1
            },
            "minVelocity": 0.5,
            "maxVelocity": 10,
        },
        "nodes": {
            "font": {"size": 15, "face": "tahoma"}
        },
        "edges": {
            "color": {"color": "#FFFFFF"},
            "font": {"size": 12, "face": "tahoma"},
            "arrows": {"to": {"enabled": False}}
        }
    }
    nt.from_nx(_filtered_graph)
    nt.show('people_graph.html')
    st.write("People Graph:")
    st.components.v1.html(nt.html, width=800, height=800, scrolling=False)


def render():
    st.title('2023 개인사업자 캠프 상반기 워크샵!')
    st.write('Welcome to the home page!')
