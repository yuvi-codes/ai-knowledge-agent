import streamlit as st
from backend import pipeline
import PyPDF2

st.title("📄 AI Knowledge Base Agent")

uploaded_file = st.file_uploader("Upload a PDF (max 5MB)")
question = st.text_input("Ask a question about your PDF")

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = "".join([page.extract_text() for page in pdf_reader.pages])
    pipeline.process_pdf_and_store(text)
    st.success("PDF uploaded and processed!")

if question:
    answer = pipeline.answer_question(question)
    st.info(f"**Answer:** {answer}")
