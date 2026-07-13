import streamlit as st

def render_health_metrics(api_status="Online", s3_status="Connected", records_pulled=0):
    st.subheader("🔌 Extraction Engine Health")

    col1, col2, col3 = st.columns(3)

    # API Status
    col1.metric(
        label="API Connection",
        value=api_status,
        delta="Healthy" if api_status == "Online" else "Check Required"
    )

    # S3 Status
    col2.metric(
        label="S3 Data Lake",
        value=s3_status,
        delta="Connected" if s3_status == "Connected" else "Disconnected"
    )

    # Records pulled
    col3.metric(
        label="Records Pulled",
        value=records_pulled,
        delta="Latest Run"
    )

    if api_status != "Online" or s3_status != "Connected":
        st.error("⚠️ Extraction Engine Issue Detected! Check logs immediately.")
    else:
        st.success("✅ Extraction Engine is fully operational.")