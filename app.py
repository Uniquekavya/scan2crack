import streamlit as st
from auth import register_user, login_user, admin_login
from database import load_users, save_users

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
    if st.button("Create new account"):
        st.session_state.page = "register"
        st.rerun()

    if st.button("Login as Admin"):
        st.session_state.page = "admin_login"
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
# USER DASHBOARD
# =================================================
elif st.session_state.page == "home":

    st.success(f"Welcome, {st.session_state.user_data.get('name','User')} 👋")
    st.markdown("### 🎓 Your Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📄 Resume Builder")
        if st.session_state.user_data["resume"]:
            st.success("Unlocked")
        else:
            st.warning("Locked – ₹5")
            if st.button("Unlock Resume"):
                st.session_state.page = "payment"
                st.rerun()

    with col2:
        st.subheader("🎯 Interview Q&A")
        if st.session_state.user_data["interview"]:
            st.success("Unlocked")
        else:
            st.warning("Locked – ₹10")
            if st.button("Unlock Interview"):
                st.session_state.page = "payment"
                st.rerun()

    with col3:
        st.subheader("🤖 AI Assistant")
        if st.session_state.user_data["ai"]:
            st.success("Unlocked")
        else:
            st.warning("Locked – ₹20")
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
    • Send screenshot + registered email  
    • Admin will unlock manually  

    🚀 Automated payment coming soon
    """)

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "home"
        st.rerun()

# =================================================
# ADMIN LOGIN
# =================================================
elif st.session_state.page == "admin_login":

    st.header("🔐 Admin Login")

    email = st.text_input("Admin Email")
    password = st.text_input("Admin Password", type="password")

    if st.button("Login"):
        if admin_login(email, password):
            st.session_state.page = "admin_panel"
            st.rerun()
        else:
            st.error("Invalid admin credentials")

    if st.button("Back"):
        st.session_state.page = "login"
        st.rerun()

# =================================================
# ADMIN PANEL
# =================================================
elif st.session_state.page == "admin_panel":

    st.header("🛠️ Admin Panel – Unlock Users")

    users = load_users()

    if not users:
        st.info("No registered users.")
    else:
        selected_email = st.selectbox("Select User", list(users.keys()))
        user = users[selected_email]

        resume = st.checkbox("Resume Access", value=user["resume"])
        interview = st.checkbox("Interview Access", value=user["interview"])
        ai = st.checkbox("AI Access", value=user["ai"])

        if st.button("Save Access"):
            users[selected_email]["resume"] = resume
            users[selected_email]["interview"] = interview
            users[selected_email]["ai"] = ai
            save_users(users)
            st.success("Access updated successfully!")

    if st.button("Logout Admin"):
        st.session_state.page = "login"
        st.rerun()

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>MVP v1 • Built with ❤️ by Kav • Scan2Crack</div>",
    unsafe_allow_html=True
)
