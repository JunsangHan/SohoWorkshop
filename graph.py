import streamlit as st
import networkx as nx
from pyvis.network import Network
import base64
import os


def render_sample():
    st.title('Graph')
    st.write('This is the Graph page. You can display graphs or charts here.')

    G = nx.Graph()
    G.add_node('A')
    G.add_node('B')
    G.add_node('C')
    G.add_node('D')

    G.add_edge('A', 'B')
    G.add_edge('A', 'C')
    G.add_edge('C', 'D')
    G.add_edge('D', 'B')

    net = Network(notebook=True)
    net.from_nx(G)
    net.save_graph('example.html')

    # Streamlit 에서 HTML 파일 불러오기
    with open('example.html', 'r') as f:
        html_string = f.read()

    # HTML 파일 삭제
    os.remove('example.html')

    # HTML 컴포넌트 추가
    st.components.v1.html(html_string, width=900, height=600, scrolling=False)
