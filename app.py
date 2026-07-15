import streamlit as st
# ✨ NEW: Import the fetch_users_data function
from load.queries import fetch_dashboard_data, fetch_raw_data, fetch_users_data
from transform.visuals import render_payment_chart, render_export_button
from extract.health_widget import render_health_metrics

st.set_page_config(page_title="Zaalima ETL Dashboard", layout="wide")

def check_password():
    def password_entered():
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

if check_password():
    st.title("🚀 Zaalima ETL Data Platform")

    st.markdown("### System Health")
    render_health_metrics()

    st.markdown("### Data Insights")
    
    # ✨ NEW: Create distinct tabs for your different datasets!
    tab1, tab2 = st.tabs(["💰 Payment Analytics", "👥 User Directory"])
    
    # --- TAB 1: PAYMENTS ---
    with tab1:
        df_summary = fetch_dashboard_data()
        df_raw = fetch_raw_data()
        
        if not df_summary.empty:
            render_payment_chart(df_summary)
            render_export_button(df_raw)
        else:
            st.warning("No payment data found in the warehouse.")
            
    # --- TAB 2: USERS ---
    with tab2:
        df_users = fetch_users_data()
        
        if not df_users.empty:
            st.subheader("Registered Users")
            # Displays a beautiful, interactive table automatically
            st.dataframe(df_users, use_container_width=True, hide_index=True)
        else:
            st.warning("No user data found in the warehouse.")