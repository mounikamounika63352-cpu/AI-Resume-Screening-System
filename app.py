import streamlit as st

from utils.pdf_reader import extract_text
from utils.resume_parser import extract_name, extract_email, extract_phone
from utils.skill_extractor import extract_skills

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# -------------------------------
# TITLE
# -------------------------------

st.title("📄 AI Resume Screening System")

st.write("### Welcome to the AI Resume Screening System!")

# -------------------------------
# JOB DESCRIPTION
# -------------------------------

job_description = st.text_area(
    "Enter Job Description",
    placeholder="Example: Python, Java, SQL, Machine Learning, Pandas",
    height=150
)

# -------------------------------
# FILE UPLOAD
# -------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# -------------------------------
# BUTTON
# -------------------------------

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload a resume.")

    else:

        # Extract resume text
        resume_text = extract_text(uploaded_file)

        # Extract candidate details
        name = extract_name(resume_text)
        email = extract_email(resume_text)
        phone = extract_phone(resume_text)

        # Extract skills from resume
        resume_skills = extract_skills(resume_text)

        # Convert Job Description into skill list
        job_skills = [
            skill.strip().lower()
            for skill in job_description.split(",")
            if skill.strip()
        ]

        resume_lower = [skill.lower() for skill in resume_skills]

        matched_skills = []

        missing_skills = []

        for skill in job_skills:

            if skill in resume_lower:
                matched_skills.append(skill.title())
            else:
                missing_skills.append(skill.title())

        # Calculate Score
        if len(job_skills) == 0:
            match_score = 0
        else:
            match_score = (len(matched_skills) / len(job_skills)) * 100

        # -------------------------------
        # DISPLAY
        # -------------------------------

        st.success("Resume Parsed Successfully!")

        st.divider()

        st.subheader("👤 Candidate Details")

        st.write("### Name")
        st.write(name)

        st.write("### Email")
        st.write(email)

        st.write("### Phone")
        st.write(phone)

        st.divider()
        st.subheader("💻 Detected Skills")

        if resume_skills:

            for skill in resume_skills:
                st.success(skill)

        else:
            st.warning("No skills detected.")

        st.divider()

        st.subheader("✅ Matched Skills")

        if matched_skills:

            for skill in matched_skills:
                st.success(skill)

        else:
            st.error("No matching skills found.")

        st.divider()

        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.warning(skill)

        else:
            st.success("No missing skills!")

        st.divider()

        st.subheader("📊 Resume Match Score")

        st.metric(
            label="Match Percentage",
            value=f"{match_score:.2f}%"
        )

        # Recommendation

        st.subheader("🎯 Recommendation")

        if match_score >= 90:
            st.success("★★★★★ Excellent Candidate")

        elif match_score >= 75:
            st.success("★★★★ Good Candidate")

        elif match_score >= 50:
            st.warning("★★★ Average Candidate")

        else:
            st.error("★★ Needs Improvement")