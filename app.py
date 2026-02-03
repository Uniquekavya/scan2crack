import streamlit as st
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Scan2Crack – ECE Edition",
    layout="wide",
    page_icon="🚀"
)

# ---------- GET PROJECT PATH ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# ---------- IMAGE PATHS ----------
hero_img = os.path.join(ASSETS_DIR, "hero.jpg")
resume_img = os.path.join(ASSETS_DIR, "resume.jpg")
interview_img = os.path.join(ASSETS_DIR, "interview.jpg")
ai_img = os.path.join(ASSETS_DIR, "ai.jpg")

# ---------- HERO SECTION ----------
st.image(hero_img, use_container_width=True)

st.markdown("""
<div style='text-align:center; padding:30px;'>
    <h1 style='color:#6C63FF;'>Scan2Crack – ECE Edition</h1>
    <h4>Crack Core ECE Interviews with Confidence</h4>
    <p>Resumes • Interview Q&A • AI Assistance</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- FEATURES ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.image(resume_img, use_container_width=True)
    st.markdown("### 📄 Resume Builder")
    st.write("ATS-friendly resumes tailored for ECE core & IT roles.")

with col2:
    st.image(interview_img, use_container_width=True)
    st.markdown("### 🎯 Interview Questions")
    st.write("Most repeated ECE interview questions with clear answers.")

with col3:
    st.image(ai_img, use_container_width=True)
    st.markdown("### 🤖 AI Interview Assistant")
    st.write("Ask doubts. Revise fast. Personal AI mentor.")

st.markdown("---")

# ---------- FOOTER ----------
st.markdown("""
<div style='text-align:center; padding:20px; color:gray;'>
    MVP v1 • Built with ❤️ by Kav • Scan2Crack
</div>
""", unsafe_allow_html=True)
