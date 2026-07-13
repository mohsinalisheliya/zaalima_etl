import streamlit as st
from load.queries import fetch_dashboard_data
from transform.visuals import render_payment_chart
from extract.health_widget import render_health_metrics

# Page config must be the first Streamlit command
st.set_page_config(page_title="Zaalima ETL Dashboard", layout="wide")

def check_password():
    """Returns `True` if the user has the correct password."""
    def password_entered():
        # In production, this password should be loaded from .env!
        if st.session_state["password"] == "zaalima2026": 
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter Dashboard Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.error("😕 Password incorrect")
        return False
    return True

# --- The Gateway ---
if check_password():
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