import streamlit as st
import pdfplumber
from skills import skills_db

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    text = text.lower()

    found_skills = []

    for skill in skills_db:

        if skill in text:

            found_skills.append(skill)

    score = min(len(found_skills) * 5, 100)

    st.subheader("Detected Skills")

    if found_skills:

        for skill in found_skills:
            st.success(skill)

    else:
        st.warning("No skills detected")

    st.subheader("Resume Score")

    st.write(f"{score}/100")

    missing_skills = []

    for skill in skills_db:

        if skill not in found_skills:

            missing_skills.append(skill)

    st.subheader("Recommended Skills")

    for skill in missing_skills[:5]:

        st.write("➜", skill)