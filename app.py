import streamlit as st
import tempfile
import os
from src.extractor import extract_text
from src.analyzer import (
    find_skills, calculate_score, check_resume_elements,
    check_resume_length, compare_with_job_description, detect_ai_phrases,
    generate_improvement_suggestions
)
from src.config import SKILL_RESOURCES, DOMAINS

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #6C63FF;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 16px;
        color: #666;
        margin-bottom: 30px;
    }
    .stMetric {
        background-color: #F8F7FF;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #E0DFFF;
    }
    div[data-testid="stFileUploader"] {
        border: 2px dashed #6C63FF;
        border-radius: 12px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 📄 About This Tool")
    st.write(
        "This tool analyzes your resume, checks skill matches for your "
        "specific domain, evaluates resume quality, checks for AI-sounding "
        "phrases, and compares it against any job description."
    )
    st.markdown("---")
    st.markdown("### 🧭 How to Use")
    st.write("1. Select your domain/field")
    st.write("2. Upload your resume (PDF/DOCX)")
    st.write("3. View your score & missing skills")
    st.write("4. Paste a job description to compare")
    st.write("5. Download your report")
    st.markdown("---")
    st.caption("Built with ❤️ using Python & Streamlit")

st.markdown('<p class="main-title">📄 AI Resume Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload your resume to check your skills match, quality, and job fit — instantly.</p>', unsafe_allow_html=True)

selected_domain = st.selectbox("🎓 Select Your Domain/Field", list(DOMAINS.keys()))

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
use_sample = st.button("🎯 Try with Sample Resume (No Upload Needed)")

if uploaded_file is not None or use_sample:
    if use_sample and uploaded_file is None:
        temp_path = "data/sample_resumes/test_resume.pdf"
        is_temp_file = False
    else:
        file_extension = os.path.splitext(uploaded_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name
        is_temp_file = True

    try:
        with st.spinner("🔍 Analyzing your resume..."):
            resume_text = extract_text(temp_path)
            matched, missing = find_skills(resume_text, DOMAINS[selected_domain])
            score = calculate_score(matched, missing)
            present_elements, missing_elements = check_resume_elements(resume_text)
            length_status, word_count = check_resume_length(resume_text)
            flagged_phrases, ai_likelihood = detect_ai_phrases(resume_text)
            suggestions, priority_message = generate_improvement_suggestions(missing, missing_elements, score)

        st.markdown("### 📊 Overview")
        st.caption(f"Showing results for: **{selected_domain}**")

        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label="Resume Score", value=f"{score}%")
        with m2:
            st.metric(label="Skills Matched", value=f"{len(matched)} / {len(matched) + len(missing)}")
        with m3:
            st.metric(label="Resume Length", value=length_status)

        st.progress(int(score))

        st.markdown("---")
        if score >= 70:
            st.success("🎉 Great job! Your resume matches most of the required skills for this domain.")
            st.balloons()
        elif score >= 40:
            st.info("👍 Decent match! A few more skills could boost your score.")
        else:
            st.warning("⚠️ Your resume is missing many key skills for this domain. Check suggestions below.")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### ✅ Skills Found")
            with st.container(border=True):
                for skill in matched:
                    st.write(f"🟢 {skill}")

        with col2:
            st.markdown("#### ❌ Skills Missing")
            with st.container(border=True):
                for skill in missing:
                    if skill in SKILL_RESOURCES:
                        st.markdown(f"🔴 {skill} — [Learn here]({SKILL_RESOURCES[skill]})")
                    else:
                        st.write(f"🔴 {skill}")

        st.markdown("---")

        st.markdown("### 🤖 AI-Sounding Phrase Check")
        st.caption("This checks for common overused/robotic phrases often found in AI-written resumes. It is not a definitive AI-detection tool.")

        st.metric(label="AI-Sounding Phrase Score", value=f"{ai_likelihood}%")

        if flagged_phrases:
            with st.container(border=True):
                for phrase, suggestion in flagged_phrases:
                    st.markdown(f"**🔸 \"{phrase}\"** — {suggestion}")
        else:
            st.success("No common AI-sounding phrases detected!")

        st.markdown("---")

        st.markdown("### 📋 Resume Quality Check")
        st.caption("Companies also look for these important elements in a resume.")

        col3, col4 = st.columns(2)
        with col3:
            st.markdown("**✅ Present**")
            with st.container(border=True):
                for element in present_elements:
                    st.write(f"🟢 {element}")

        with col4:
            st.markdown("**⚠️ Missing (Consider Adding)**")
            with st.container(border=True):
                for element in missing_elements:
                    st.write(f"🟡 {element}")

        st.markdown("---")

        report_text = "===== RESUME ANALYSIS REPORT =====\n\n"
        report_text += f"Domain: {selected_domain}\n\n"
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

        st.markdown("---")
        st.markdown("### 💡 How to Improve Your Resume")
        st.info(priority_message)

        with st.container(border=True):
            for suggestion in suggestions:
                st.write(f"✅ {suggestion}")

        st.markdown("---")

        st.markdown("### 🎯 Compare With a Job Description")
        st.caption("Paste a job description below to see how well your resume matches a specific role.")

        job_description = st.text_area("Paste Job Description Here", height=180, label_visibility="collapsed", placeholder="Paste job description here...")

        if st.button("🔍 Compare with Job Description"):
            if job_description.strip() == "":
                st.warning("Please paste a job description first.")
            else:
                jd_matched, jd_missing, jd_score = compare_with_job_description(resume_text, job_description)

                st.metric(label="Job Match Score", value=f"{jd_score}%")
                st.progress(int(jd_score))

                col5, col6 = st.columns(2)
                with col5:
                    st.markdown("**✅ Matching Keywords**")
                    with st.container(border=True):
                        for word in jd_matched:
                            st.write(f"🟢 {word}")

                with col6:
                    st.markdown("**❌ Missing Keywords**")
                    with st.container(border=True):
                        for word in jd_missing:
                            st.write(f"🔴 {word}")

    except ValueError as e:
        st.error(f"Error: {e}")

    finally:
        if is_temp_file:
            os.remove(temp_path)