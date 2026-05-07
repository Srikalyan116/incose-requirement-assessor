import streamlit as st
import requests

st.title("ISO 29148 Requirement Analyzer")
text = st.text_area("Enter Requirement")

if st.button("Analyze"):
    res = requests.post("http://localhost:8000/analyze", json={"text": text})
    st.json(res.json())
import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("🚀 AI Requirement Quality Analyzer (ISO 29148)")

text = st.text_area("Enter Requirement", height=120)

if st.button("Analyze Requirement"):

    res = requests.post(
        "http://localhost:8000/analyze",
        json={"text": text}
    )

    data = res.json()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Compliance Score")
        if "analysis" in data:
            st.metric(
                "Score",
                data["analysis"].get("compliance_score", "N/A")
            )

    with col2:
        st.subheader("⚠ Risk Level")
        st.write(data["analysis"].get("risk_level"))

    st.subheader("🔍 Issues")
    st.write(data["analysis"].get("issues"))

    st.subheader("💡 Improvements")
    st.write(data["analysis"].get("improvements"))

    st.subheader("✍ Rewritten Requirement")
    st.success(data["analysis"].get("rewritten_requirement"))

    st.subheader("📚 Retrieved Context")
    st.json(data["retrieved_context"])
