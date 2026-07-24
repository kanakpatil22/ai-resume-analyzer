import streamlit as st
import tempfile
import os
from src.extractor import extract_text
from src.analyzer import find_skills, calculate_score

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume (PDF or DOCX) to check your skills match and score.")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])

if uploaded_file is not None:
    file_extension = os.path.splitext(uploaded_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    try:
        resume_text = extract_text(temp_path)
        matched, missing = find_skills(resume_text)
        score = calculate_score(matched, missing)

        st.subheader("📊 Resume Score")
        st.metric(label="Score", value=f"{score}%")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Skills Found")
            for skill in matched:
                st.write(f"- {skill}")

        with col2:
            st.subheader("❌ Skills Missing")
            for skill in missing:
                st.write(f"- {skill}")

    except ValueError as e:
        st.error(f"Error: {e}")

    finally:
        os.remove(temp_path)