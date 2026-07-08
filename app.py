
import streamlit as st
from load.queries import fetch_dashboard_data
from transform.visuals import render_payment_chart
from extract.health_widget import render_health_metrics

st.set_page_config(page_title="Zaalima ETL Dashboard", layout="wide")
st.title("🚀 Zaalima ETL Data Platform")

# Render Pipeline Health
st.markdown("### System Health")
render_health_metrics()

# Render Data Visuals
st.markdown("### Data Insights")
df = fetch_dashboard_data()
if not df.empty:
    render_payment_chart(df)
else:
    st.warning("No data found in the warehouse.")
