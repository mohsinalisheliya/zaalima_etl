import streamlit as st

def render_payment_chart(df):
    st.subheader("Revenue by Status")
    st.bar_chart(data=df, x="status", y="total", use_container_width=True)