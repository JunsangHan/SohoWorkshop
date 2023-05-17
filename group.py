import streamlit as st


def render():
    st.title('조편성 👩🏻‍💻🧑🏼‍💻👨🏻‍💼👩🏼‍🔧')

    # 조별 사람들의 데이터 생성
    data = {
        'A': ['simon.sung', 'july.jy', 'uno.s', 'loki.l', 'harper.ha', 'joel.ho'],
        'B': ['arnold.oh', 'jk.tabris', 'kyle.k', 'jerome.jung', 'benji.k', 'olga.song'],
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
