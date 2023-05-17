import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network


sheet_url = st.secrets["business_graph_url"].replace("/edit#gid=", "/export?format=csv&gid=")
df = pd.read_csv(sheet_url)

# 그래프 생성 및 노드 추가
G = nx.Graph()

for index, row in df.iterrows():
    G.add_node(row['이름'], group=row['직군'], cell=row['셀'], domain1=row['도메인1'], domain2=row['도메인2'], size=30)

# 같은 속성을 공유하는 노드 사이의 엣지 추가
for i, row_i in df.iterrows():
    for j, row_j in df.iterrows():
        if i != j:
            if row_i['직군'] == row_j['직군'] or row_i['셀'] == row_j['셀'] \
                    or row_i['도메인1'] == row_j['도메인1'] \
                    or row_i['도메인1'] == row_j['도메인2'] \
                    or row_i['도메인1'] == row_j['도메인3'] \
                    or row_i['도메인1'] == row_j['도메인4'] \
                    or row_i['도메인2'] == row_j['도메인2'] \
                    or row_i['도메인2'] == row_j['도메인3'] \
                    or row_i['도메인2'] == row_j['도메인4'] \
                    or row_i['도메인3'] == row_j['도메인3'] \
                    or row_i['도메인3'] == row_j['도메인4'] \
                    or row_i['도메인4'] == row_j['도메인4']:
                G.add_edge(row_i['이름'], row_j['이름'])
            elif row_i['직책'] == row_j['직책']:
                G.add_edge(row_i['이름'], row_j['이름'])


def create_filtered_graph(selected_names):
    nodes_to_keep = set(selected_names)
    for name in selected_names:
        nodes_to_keep.update(G.neighbors(name))
    sub_G = G.subgraph(nodes_to_keep).copy()
    return sub_G


def show_filtered_graph(_filtered_graph):
    # Pyvis 네트워크로 변환 및 시각화
    nt = Network(notebook=True, height='500px', width='100%', bgcolor='#ffffff', font_color='black')

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
            "scaling": {
                "min": 30,  # minimum size
                "max": 30,  # maximum size
            },
            "font": {"size": 22, "face": "tahoma"}
        },
        "edges": {
            "color": {"color": "#FFFFFF"},
            "font": {"size": 22, "face": "tahoma"},
            "arrows": {"to": {"enabled": False}}
        }
    }
    nt.from_nx(_filtered_graph)
    nt.show('people_graph.html')
    st.components.v1.html(nt.html, width=600, height=600, scrolling=False)


def render():
    st.title('개사캠의 관계도 🤔🧐😄')

    # Select names from the list
    st.header("재미로만 봐주세요 🙏🙏🙏")

    name_list = df['이름'].tolist()
    selected_names = st.multiselect('Select names:', name_list)

    if selected_names:
        filtered_graph = create_filtered_graph(selected_names)
        show_filtered_graph(filtered_graph)
    else:
        show_filtered_graph(G)
