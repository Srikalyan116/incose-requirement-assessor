import streamlit as st
import requests

st.title("ISO 29148 Requirement Analyzer")
text = st.text_area("Enter Requirement")

if st.button("Analyze"):
    res = requests.post("http://localhost:8000/analyze", json={"text": text})
    st.json(res.json())
