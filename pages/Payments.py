import streamlit as st
import os

st.set_page_config(page_title="Payment", layout="centered")

st.title("💳 Scan2Crack Premium Access")
st.caption("Simple • Affordable • Student-friendly")

st.markdown("---")

# =========================
# PRICING CARDS
# =========================

st.subheader("📄 Resume Builder")
st.write("✔ Industry-ready resume PDF")
st.markdown("### 💰 ₹5")

st.markdown("---")

st.subheader("📘 Interview Question Pack")
st.write("✔ 500+ ECE Interview Questions (PDF + Website)")
st.markdown("### 💰 ₹10")

st.markdown("---")

st.subheader("🤖 AI Interview Assistant")
st.write("✔ Ask unlimited ECE interview questions")
st.markdown("### 💰 ₹20")

st.markdown("---")

# =========================
# PAYMENT SECTION
# =========================
st.subheader("📲 Scan & Pay (UPI)")

QR_PATH = "assets/payment/upi_qr.png"

if os.path.exists(QR_PATH):
    st.image(
        QR_PATH,
        caption="Scan the QR to make payment",
        width="stretch"
    )
else:
    st.warning("⚠️ QR image not found. Please add it to assets/payment/upi_qr.png")

st.info("""
📌 **After payment:**
• Take a screenshot  
• Send it to **scan2crack.support@gmail.com**  
• Access will be enabled manually  

🚀 Automated payments coming soon.
""")

st.markdown("---")
st.caption("⚠️ This is an early-access student MVP version")
