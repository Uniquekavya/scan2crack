import streamlit as st
from auth import register_user, login_user

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Scan2Crack – ECE Edition",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------------------------
# SESSION STATE INIT
# -------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "login"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# -------------------------------------------------
# TOP NAV BAR
# -------------------------------------------------
nav1, nav2, nav3 = st.columns([2, 6, 2])

with nav1:
    st.markdown("## 🚀 Scan2Crack")

with nav3:
    if st.session_state.logged_in:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.rerun()

st.markdown("---")

# =================================================
# LOGIN PAGE
# =================================================
if st.session_state.page == "login":

    st.header("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        ok, user = login_user(email, password)
        if ok:
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.session_state.user_data = user
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Invalid email or password")

    st.markdown("---")
    st.write("Don't have an account?")
    if st.button("Create new account"):
        st.session_state.page = "register"
        st.rerun()

# =================================================
# REGISTER PAGE
# =================================================
elif st.session_state.page == "register":

    st.header("📝 Register")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        ok, msg = register_user(name, email, password)
        if ok:
            st.success("Account created successfully. Please login.")
            st.session_state.page = "login"
            st.rerun()
        else:
            st.error(msg)

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()

# =================================================
# HOME / DASHBOARD
# =================================================
elif st.session_state.page == "home":

    st.success(f"Welcome, {st.session_state.user_data.get('name','User')} 👋")
    st.markdown("### 🎓 Your Dashboard")

    col1, col2, col3 = st.columns(3)

    # ---------------- RESUME ----------------
    with col1:
        st.subheader("📄 Resume Builder")
        if st.session_state.user_data.get("resume"):
            st.success("Unlocked")
        else:
            st.warning("Locked – ₹39")
            if st.button("Unlock Resume"):
                st.session_state.page = "payment"
                st.rerun()

    # ---------------- INTERVIEW ----------------
    with col2:
        st.subheader("🎯 Interview Q&A")
        if st.session_state.user_data.get("interview"):
            st.success("Unlocked")
        else:
            st.warning("Locked – ₹99")
            if st.button("Unlock Interview"):
                st.session_state.page = "payment"
                st.rerun()

    # ---------------- AI ----------------
    with col3:
        st.subheader("🤖 AI Assistant")
        if st.session_state.user_data.get("ai"):
            st.success("Unlocked")
        else:
            st.warning("Locked – ₹149")
            if st.button("Unlock AI"):
                st.session_state.page = "payment"
                st.rerun()

# =================================================
# PAYMENT PAGE
# =================================================
elif st.session_state.page == "payment":

    st.header("💳 Payment")

    st.info("""
    🔹 Early-access MVP  

    • Pay via UPI / QR  
    • Send payment screenshot + registered email  
    • Admin will unlock access manually  

    🚀 Automated payment coming soon
    """)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "home"
        st.rerun()

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>MVP v1 • Built with ❤️ by Kav • Scan2Crack</div>",
    unsafe_allow_html=True
)
