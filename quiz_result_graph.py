import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network


# 그래프를 생성합니다.
G = nx.Graph()


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
    nt.show('quiz_graph.html')
    st.components.v1.html(nt.html, width=600, height=600, scrolling=False)


def render():
    st.title('동료퀴즈 관계도 🤔🧐😄')
    st.header("퀴즈 맞추느라 고생 많으셨습니다")

    quiz_result_sheet_url = "https://docs.google.com/spreadsheets/d/1SIygrveRsmq3fRdULy9JIgsSEpXuiE4Oavh0egCk78M/edit#gid=727697584"
    sheet_url = quiz_result_sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
    df = pd.read_csv(sheet_url)

    # 노드와 엣지를 추가합니다.
    names = df.columns[1:]  # Update to exclude the first column

    for name in names:
        G.add_node(name)

    for index, row in df.iterrows():
        source = row[0]
        for i, value in enumerate(row[1:], start=1):  # Update to exclude the first column
            if value != 0:
                G.add_edge(source, names[i - 1], value=value)

    name_list = df['이름'].tolist()
    selected_names = st.multiselect('Select names:', name_list)

    if selected_names:
        filtered_graph = create_filtered_graph(selected_names)
        show_filtered_graph(filtered_graph)