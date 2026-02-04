import streamlit as st
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Scan2Crack – ECE Edition",
    layout="wide",
    page_icon="🚀"
)

# ---------- PATHS ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

hero_img = os.path.join(ASSETS_DIR, "hero.jpg")
resume_img = os.path.join(ASSETS_DIR, "resume.jpg")
interview_img = os.path.join(ASSETS_DIR, "interview.jpg")
ai_img = os.path.join(ASSETS_DIR, "ai.jpg")

# ---------- HERO SECTION ----------
if os.path.exists(hero_img):
    st.image(hero_img, use_container_width=True)

st.markdown("""
<div style='text-align:center; padding:30px;'>
    <h1 style='color:#6C63FF;'>Scan2Crack – ECE Edition</h1>
    <h4>Crack Core ECE Interviews with Confidence</h4>
    <p>Resumes • Interview Q&A • AI Assistance</p>
</div>
""", unsafe_allow_html=True)

# ---------- PRIMARY CTA ----------
col_cta1, col_cta2, col_cta3 = st.columns(3)

with col_cta1:
    if st.button("📄 Build Resume", use_container_width=True):
        st.switch_page("Resume")

with col_cta2:
    if st.button("🎯 Interview Q&A", use_container_width=True):
        st.switch_page("Interview Q&A")

with col_cta3:
    if st.button("🤖 AI Assistant", use_container_width=True):
        st.switch_page("AI Assistant")

st.markdown("---")

# ---------- FEATURES SECTION ----------
col1, col2, col3 = st.columns(3)

with col1:
    if os.path.exists(resume_img):
        st.image(resume_img, use_container_width=True)
    st.markdown("### 📄 Resume Builder")
    st.write("ATS-friendly resumes designed for ECE & IT roles.")
    if st.button("Create Resume →", key="resume_btn"):
        st.switch_page("Resume")

with col2:
    if os.path.exists(interview_img):
        st.image(interview_img, use_container_width=True)
    st.markdown("### 🎯 Interview Questions")
    st.write("Most repeated Core ECE, Embedded & VLSI questions.")
    if st.button("View Questions →", key="interview_btn"):
        st.switch_page("Interview Q&A")

with col3:
    if os.path.exists(ai_img):
        st.image(ai_img, use_container_width=True)
    st.markdown("### 🤖 AI Interview Assistant")
    st.write("Ask doubts, revise fast, get interview-ready answers.")
    if st.button("Ask AI →", key="ai_btn"):
        st.switch_page("AI Assistant")

st.markdown("---")

# ---------- SECONDARY CTA ----------
st.markdown(
    "<h3 style='text-align:center;'>🚀 Ready to unlock premium features?</h3>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

col_pay = st.columns([2, 1, 2])[1]
with col_pay:
    if st.button("💳 View Pricing & Payment", use_container_width=True):
        st.switch_page("Payment")

st.markdown("---")

# ---------- FOOTER ----------
st.markdown("""
<div style='text-align:center; padding:20px; color:gray;'>
    MVP v1 • Built with ❤️ by Kav • Scan2Crack  
    <br>
    Resume ₹39 • Interview ₹99 • AI ₹149
</div>
""", unsafe_allow_html=True)
