import streamlit as st
import tempfile
import os
from src.extractor import extract_text
from src.analyzer import (
    find_skills, calculate_score, check_resume_elements,
    check_resume_length, compare_with_job_description
)

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
        present_elements, missing_elements = check_resume_elements(resume_text)
        length_status, word_count = check_resume_length(resume_text)

        st.subheader("📊 Resume Score")
        st.metric(label="Score", value=f"{score}%")
        st.write(f"**Resume Length:** {length_status} ({word_count} words)")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Skills Found")
            for skill in matched:
                st.write(f"- {skill}")

        with col2:
            st.subheader("❌ Skills Missing")
            for skill in missing:
                st.write(f"- {skill}")

        st.divider()

        st.subheader("📋 Resume Quality Check")
        st.write("Companies also look for these important elements in a resume:")

        col3, col4 = st.columns(2)

        with col3:
            st.write("**✅ Present:**")
            for element in present_elements:
                st.write(f"- {element}")

        with col4:
            st.write("**⚠️ Missing (Consider Adding):**")
            for element in missing_elements:
                st.write(f"- {element}")

        st.divider()

        report_text = "===== RESUME ANALYSIS REPORT =====\n\n"
        report_text += "Skills Found:\n"
        for skill in matched:
            report_text += f"- {skill}\n"
        report_text += "\nSkills Missing:\n"
        for skill in missing:
            report_text += f"- {skill}\n"
        report_text += f"\nResume Score: {score}%\n"

        st.download_button(
            label="📥 Download Report",
            data=report_text,
            file_name="resume_report.txt",
            mime="text/plain"
        )

        st.divider()

        st.subheader("🎯 Compare With a Job Description (Optional)")
        st.write("Paste a job description below to see how well your resume matches it.")

        job_description = st.text_area("Paste Job Description Here", height=200)

        if st.button("Compare with Job Description"):
            if job_description.strip() == "":
                st.warning("Please paste a job description first.")
            else:
                jd_matched, jd_missing, jd_score = compare_with_job_description(resume_text, job_description)

                st.metric(label="Job Match Score", value=f"{jd_score}%")

                col5, col6 = st.columns(2)

                with col5:
                    st.write("**✅ Matching Keywords:**")
                    for word in jd_matched:
                        st.write(f"- {word}")

                with col6:
                    st.write("**❌ Missing Keywords:**")
                    for word in jd_missing:
                        st.write(f"- {word}")

    except ValueError as e:
        st.error(f"Error: {e}")

    finally:
        os.remove(temp_path)