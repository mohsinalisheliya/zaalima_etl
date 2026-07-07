import streamlit as st

def render_health_metrics(api_status="Online", s3_status="Connected"):
    col1, col2 = st.columns(2)
    col1.metric("API Connection", api_status)
    col2.metric("S3 Data Lake", s3_status)