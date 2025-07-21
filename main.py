import streamlit as st
from summarizer import summarize_text
from parser_1 import extract_text_from_pdf
import os

st.set_page_config(page_title="AI Text Summarizer", layout="wide")
st.title("📝 AI-Powered Text Summarizer")

input_type = st.radio("Choose input type:", ["Text", "PDF Upload"])

if input_type == "Text":
    input_text = st.text_area("Paste your text here", height=300)
else:
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        input_text = extract_text_from_pdf("temp.pdf")
        st.success("PDF extracted successfully.")

if st.button("Summarize"):
    if input_text:
        with st.spinner("Generating summary..."):
            summary = summarize_text(input_text)
        st.subheader("📌 Summary")
        st.write(summary)
    else:
        st.warning("Please provide valid input.")