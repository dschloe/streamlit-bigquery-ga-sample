# streamlit_app.py
import streamlit as st
from utils import client

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.experimental_memo to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

def main():

    st.title("Streamlit Multi-Pages")
    st.subheader("Main Page")

    rows = run_query("SELECT word FROM `bigquery-public-data.samples.shakespeare` LIMIT 10")

    # Print results.
    st.write("Some wise words from Shakespeare:")
    for row in rows:
        st.write("✍️ " + row['word'])# streamlit_app.py

if __name__ == "__main__":
    main()

