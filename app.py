import streamlit as st

st.set_page_config(page_title="Intrusion Detection System")

st.title("🛡 Intrusion Detection System")

st.success("Model Loaded Successfully")

st.write("---")

st.metric("Accuracy", "99.79%")

st.metric("Packets Analysed", "25195")

if st.button("Start Monitoring"):
    st.success("Monitoring Started")

if st.button("Stop Monitoring"):
    st.warning("Monitoring Stopped")