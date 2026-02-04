import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Scan2Crack – ECE Edition",
    page_icon="🚀",
    layout="wide"
)

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

hero_img = os.path.join(ASSETS_DIR, "hero.jpg")
resume_img = os.path.join(ASSETS_DIR, "resume.jpg")
interview_img = os.path.join(ASSETS_DIR, "interview.jpg")
ai_img = os.path.join(ASSETS_DIR, "ai.jpg")

# ---------------- SIDEBAR NAVIGATION (STABLE) ----------------
st.sidebar.title("🚀 Scan2Crack")

st.sidebar.page_link("app.py", label="🏠 Home")

st.sidebar.page_link("pages/Resume.py", label="📄 Resume Builder")
st.sidebar.page_link("pages/Interview_QA.py", label="🎯 Interview Q&A")
st.sidebar.page_link("pages/AI_Assistant.py", label="🤖 AI Assistant")
st.sidebar.page_link("pages/Payments.py", label="💳 Pricing & Payment")

st.sidebar.markdown("---")
st.sidebar.caption("MVP v1 • Scan2Crack")

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

# ---------------- FEATURE CARDS (NO PAGE_LINK HERE) ----------------
f1, f2, f3 = st.columns(3)

with f1:
    if os.path.exists(resume_img):
        st.image(resume_img, use_container_width=True)
    st.markdown("### 📄 Resume Builder")
    st.write("ATS-friendly resume templates made for ECE students.")
    st.info("➡ Open **Resume Builder** from the sidebar")

with f2:
    if os.path.exists(interview_img):
        st.image(interview_img, use_container_width=True)
    st.markdown("### 🎯 Interview Questions")
    st.write("500+ Core ECE, Embedded, VLSI & HR interview Q&A.")
    st.info("➡ Open **Interview Q&A** from the sidebar")

with f3:
    if os.path.exists(ai_img):
        st.image(ai_img, use_container_width=True)
    st.markdown("### 🤖 AI Interview Assistant")
    st.write("Ask ECE interview questions and get instant answers.")
    st.info("➡ Open **AI Assistant** from the sidebar")

st.markdown("---")

# ---------------- PAYMENT SECTION ----------------
st.markdown(
    "<h3 style='text-align:center;'>💳 Unlock Premium Features</h3>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Resume ₹39 • Interview ₹99 • AI ₹149</p>",
    unsafe_allow_html=True
)

st.info("➡ Open **Pricing & Payment** from the sidebar to continue")

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
