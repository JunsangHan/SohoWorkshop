import streamlit as st
import pandas as pd


# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)


def render():
    st.title('Score')
    if st.button('Update data'):
        df = load_data(st.secrets["public_gsheets_url"])

        # Print results.
        for row in df.itertuples():
            st.write(f"{row.name} has a :{row.score}:")

        # Create a bar chart
        chart_data = pd.DataFrame(df[['name', 'score']].set_index('name'))
        st.bar_chart(chart_data)
