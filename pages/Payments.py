import streamlit as st

st.set_page_config(page_title="Payment", layout="centered")

st.title("💳 Scan2Crack Premium Access")
st.caption("Simple • Affordable • Student-friendly")

st.markdown("---")

# =========================
# PRICING CARDS
# =========================

st.subheader("📄 Resume Builder")
st.write("✔ Industry-ready resume PDF")
st.markdown("### 💰 ₹39")

st.markdown("---")

st.subheader("📘 Interview Question Pack")
st.write("✔ 500+ ECE Interview Questions (PDF + Website)")
st.markdown("### 💰 ₹99")

st.markdown("---")

st.subheader("🤖 AI Interview Assistant")
st.write("✔ Ask unlimited ECE interview questions")
st.markdown("### 💰 ₹149")

st.markdown("---")

# =========================
# PAYMENT SECTION
# =========================
st.subheader("📲 Scan & Pay (UPI)")

st.image(
    "assets/payment/upi_qr.png",
    caption="Scan the QR to make payment",
    use_container_width=True
)

st.info("""
📌 After payment:
• Take a screenshot  
• Send it to **scan2crack.support@gmail.com**  
• Access will be enabled manually  

🚀 Automated payments coming soon.
""")

st.markdown("---")
st.caption("⚠️ This is an early-access student MVP version")
