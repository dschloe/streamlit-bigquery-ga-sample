from google.oauth2 import service_account
from google.cloud import bigquery
import streamlit as st

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)