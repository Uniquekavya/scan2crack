import streamlit as st
import os

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Scan2Crack – ECE Edition",
    page_icon="🚀",
    layout="wide"
)

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE_DIR, "assets")

def img(path):
    p = os.path.join(ASSETS, path)
    if os.path.exists(p):
        st.image(p, use_container_width=True)

# ---------------- NAV BAR ----------------
nav1, nav2, nav3, nav4 = st.columns(4)

with nav1:
    if st.button("🏠 Home"):
        st.session_state.page = "home"

with nav2:
    if st.button("📄 Resume"):
        st.session_state.page = "resume"

with nav3:
    if st.button("🎯 Interview"):
        st.session_state.page = "interview"

with nav4:
    if st.button("🤖 AI"):
        st.session_state.page = "ai"

st.markdown("---")

# ======================================================
# =================== HOME PAGE ========================
# ======================================================
if st.session_state.page == "home":

    img("hero.jpg")

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

    c1, c2, c3 = st.columns(3)

    with c1:
        img("resume.jpg")
        st.markdown("### 📄 Resume Builder")
        st.write("ATS-friendly resumes for ECE students.")
        if st.button("Build Resume →"):
            st.session_state.page = "resume"

    with c2:
        img("interview.jpg")
        st.markdown("### 🎯 Interview Questions")
        st.write("500+ Core ECE interview Q&A.")
        if st.button("View Questions →"):
            st.session_state.page = "interview"

    with c3:
        img("ai.jpg")
        st.markdown("### 🤖 AI Interview Assistant")
        st.write("Ask doubts. Revise fast.")
        if st.button("Ask AI →"):
            st.session_state.page = "ai"

    st.markdown("---")

    st.markdown(
        "<h3 style='text-align:center;'>💳 Premium Plans</h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center;'>Resume ₹39 • Interview ₹99 • AI ₹149</p>",
        unsafe_allow_html=True
    )

# ======================================================
# ================= RESUME PAGE ========================
# ======================================================
elif st.session_state.page == "resume":

    st.header("📄 Resume Builder")
    st.warning("🔒 Locked – ₹39")

    st.write("• Industry standard ECE resume format")
    st.write("• Downloadable PDF")
    st.write("• ATS friendly")

    if st.button("Go to Payment"):
        st.session_state.page = "payment"

# ======================================================
# ================= INTERVIEW PAGE =====================
# ======================================================
elif st.session_state.page == "interview":

    st.header("🎯 Interview Questions")
    st.warning("🔒 Locked – ₹99")

    st.write("• Core ECE fundamentals")
    st.write("• Embedded + VLSI")
    st.write("• HR & Project questions")

    if st.button("Go to Payment"):
        st.session_state.page = "payment"

# ======================================================
# ================= AI PAGE ============================
# ======================================================
elif st.session_state.page == "ai":

    st.header("🤖 AI Interview Assistant")
    st.warning("🔒 Locked – ₹149")

    st.write("• Ask ECE interview questions")
    st.write("• Get concept explanations")
    st.write("• Viva preparation")

    if st.button("Go to Payment"):
        st.session_state.page = "payment"

# ======================================================
# ================= PAYMENT PAGE =======================
# ======================================================
elif st.session_state.page == "payment":

    st.header("💳 Scan & Pay")

    img("payment/upi_qr.png")

    st.info(
        """
        After payment:
        • Take screenshot  
        • Send to scan2crack.support@gmail.com  
        • Access will be unlocked manually  

        Automated payments coming soon.
        """
    )

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>MVP v1 • Built with ❤️ by Kav • Scan2Crack</div>",
    unsafe_allow_html=True
)
