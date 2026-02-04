import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Scan2Crack – ECE Edition",
    page_icon="🚀",
    layout="wide"
)

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

hero_img = os.path.join(ASSETS_DIR, "hero.jpg")
resume_img = os.path.join(ASSETS_DIR, "resume.jpg")
interview_img = os.path.join(ASSETS_DIR, "interview.jpg")
ai_img = os.path.join(ASSETS_DIR, "ai.jpg")

# ---------------- HERO SECTION ----------------
if os.path.exists(hero_img):
    st.image(hero_img, use_container_width=True)

st.markdown(
    """
    <div style="text-align:center; padding:30px;">
        <h1 style="color:#6C63FF;">Scan2Crack – ECE Edition</h1>
        <h4>Crack Core ECE Interviews with Confidence</h4>
        <p>Resumes • Interview Q&A • AI Assistance</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- MAIN ACTION BUTTONS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📄 Build Resume", use_container_width=True):
        st.switch_page("Resume Builder")

with col2:
    if st.button("🎯 Interview Q&A", use_container_width=True):
        st.switch_page("Interview Q&A")

with col3:
    if st.button("🤖 AI Assistant", use_container_width=True):
        st.switch_page("AI Assistant")

st.markdown("---")

# ---------------- FEATURE CARDS ----------------
f1, f2, f3 = st.columns(3)

with f1:
    if os.path.exists(resume_img):
        st.image(resume_img, use_container_width=True)
    st.markdown("### 📄 Resume Builder")
    st.write("ATS-friendly resume templates made for ECE students.")
    if st.button("Create Resume →", key="go_resume"):
        st.switch_page("Resume Builder")

with f2:
    if os.path.exists(interview_img):
        st.image(interview_img, use_container_width=True)
    st.markdown("### 🎯 Interview Questions")
    st.write("500+ Core ECE, Embedded, VLSI & HR interview Q&A.")
    if st.button("View Questions →", key="go_interview"):
        st.switch_page("Interview Q&A")

with f3:
    if os.path.exists(ai_img):
        st.image(ai_img, use_container_width=True)
    st.markdown("### 🤖 AI Interview Assistant")
    st.write("Ask ECE interview questions and get instant answers.")
    if st.button("Ask AI →", key="go_ai"):
        st.switch_page("AI Assistant")

st.markdown("---")

# ---------------- PAYMENT CTA ----------------
st.markdown(
    "<h3 style='text-align:center;'>💳 Unlock Premium Features</h3>",
    unsafe_allow_html=True
)

st.markdown("<p style='text-align:center;'>Resume ₹39 • Interview ₹99 • AI ₹149</p>", unsafe_allow_html=True)

center_col = st.columns([3, 2, 3])[1]
with center_col:
    if st.button("View Pricing & Payment", use_container_width=True):
        st.switch_page("Payment")

st.markdown("---")

# ---------------- FOOTER ----------------
st.markdown(
    """
    <div style="text-align:center; padding:20px; color:gray;">
        MVP v1 • Built with ❤️ by Kav • Scan2Crack
    </div>
    """,
    unsafe_allow_html=True
)
