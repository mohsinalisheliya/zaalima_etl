import streamlit as st

def render_payment_chart(df):
    st.subheader("Revenue by Status")
    st.bar_chart(data=df, x="status", y="total", use_container_width=True)

def render_export_button(df):
    st.markdown("---")
    st.subheader("Data Export")
    # Convert the pandas dataframe to CSV string
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name="zaalima_warehouse_export.csv",
        mime="text/csv",
    )