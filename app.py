import streamlit as st
from auth import login_user, register_user, admin_login
from database import load_users, save_users

# =================================================
# PAGE CONFIG
# =================================================
st.set_page_config(
    page_title="Scan2Crack – ECE Edition",
    page_icon="🚀",
    layout="wide"
)

# =================================================
# GLOBAL STYLES (VERY IMPORTANT)
# =================================================
st.markdown("""
<style>
/* Hide sidebar completely */
[data-testid="stSidebar"] { display: none; }

/* Fonts */
html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #7C3AED, #6366F1, #EC4899);
    padding: 80px 40px;
    border-radius: 26px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}
.hero h1 {
    font-size: 52px;
    margin-bottom: 10px;
}
.hero p {
    font-size: 18px;
    opacity: 0.95;
}

/* Buttons */
.primary-btn {
    background: #FACC15;
    color: black;
    padding: 12px 26px;
    border-radius: 14px;
    font-weight: 600;
    border: none;
}
.secondary-btn {
    background: #ffffff30;
    color: white;
    padding: 12px 26px;
    border-radius: 14px;
    font-weight: 600;
}

/* Cards */
.card {
    background: white;
    padding: 26px;
    border-radius: 18px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    text-align: center;
}

/* Dashboard cards */
.dash-card {
    background: linear-gradient(135deg,#EEF2FF,#FDF2F8);
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    text-align: center;
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    padding: 20px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# =================================================
# SESSION STATE
# =================================================
if "page" not in st.session_state:
    st.session_state.page = "landing"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

# =================================================
# TOP BAR
# =================================================
l, m, r = st.columns([3, 6, 3])
with l:
    st.markdown("## 🚀 Scan2Crack")
with r:
    if st.session_state.logged_in:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_data = {}
            st.session_state.is_admin = False
            st.session_state.page = "landing"
            st.rerun()

st.markdown("---")

# =================================================
# LANDING PAGE
# =================================================
if st.session_state.page == "landing" and not st.session_state.logged_in:

    st.markdown("""
    <div class="hero">
        <p style="background:#ffffff22; display:inline-block; padding:6px 16px; border-radius:999px;">
            Your Ultimate ECE Interview Companion
        </p>
        <h1>Scan2Crack – <span style="color:#FACC15;">ECE Edition</span></h1>
        <p>
            Resume • Core • Embedded • VLSI • AI Assistant<br>
            Everything you need to crack ECE interviews
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'>📄 ATS-friendly Resume Builder</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'>🎯 500+ Interview Questions</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'>🤖 Smart Interview Assistant</div>", unsafe_allow_html=True)

    st.markdown("## 🔐 Login / Register")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            ok, user = login_user(email, password)
            if ok:
                st.session_state.logged_in = True
                st.session_state.user_data = user
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("Invalid credentials")

    with col2:
        st.subheader("Register")
        name = st.text_input("Name")
        reg_email = st.text_input("Register Email")
        reg_pass = st.text_input("Register Password", type="password")
        if st.button("Create Account"):
            ok, msg = register_user(name, reg_email, reg_pass)
            if ok:
                st.success("Account created. Please login.")
            else:
                st.error(msg)

    st.markdown("### 🛠️ Admin Login")
    admin_email = st.text_input("Admin Email")
    admin_pass = st.text_input("Admin Password", type="password")
    if st.button("Login as Admin"):
        if admin_login(admin_email, admin_pass):
            st.session_state.logged_in = True
            st.session_state.is_admin = True
            st.session_state.page = "admin"
            st.rerun()
        else:
            st.error("Invalid admin credentials")

    st.stop()

# =================================================
# DASHBOARD
# =================================================
if st.session_state.page == "dashboard" and st.session_state.logged_in:

    st.markdown(f"## 👋 Welcome, {st.session_state.user_data.get('name','User')}")

    d1, d2, d3 = st.columns(3)

    with d1:
        st.markdown("<div class='dash-card'>📄 Resume Builder</div>", unsafe_allow_html=True)
        if st.button("Open Resume"):
            st.switch_page("pages/Resume.py")

    with d2:
        st.markdown("<div class='dash-card'>🎯 Interview Q&A</div>", unsafe_allow_html=True)
        if st.button("Open Interview"):
            st.switch_page("pages/Interview_QA.py")

    with d3:
        st.markdown("<div class='dash-card'>🤖 AI Assistant</div>", unsafe_allow_html=True)
        if st.button("Open AI"):
            st.switch_page("pages/AI_Assistant.py")

    if st.button("💳 Payment / Unlock"):
        st.switch_page("pages/Payments.py")

# =================================================
# ADMIN PANEL (IN SAME FILE)
# =================================================
elif st.session_state.page == "admin" and st.session_state.is_admin:

    st.markdown("## 🛠️ Admin Panel – Unlock Users")

    users = load_users()
    if not users:
        st.info("No users registered yet.")
    else:
        selected_email = st.selectbox("Select User", list(users.keys()))
        user = users[selected_email]

        resume = st.checkbox("Resume", value=user.get("resume", False))
        interview = st.checkbox("Interview", value=user.get("interview", False))
        ai = st.checkbox("AI", value=user.get("ai", False))

        if st.button("Save Access"):
            users[selected_email]["resume"] = resume
            users[selected_email]["interview"] = interview
            users[selected_email]["ai"] = ai
            save_users(users)
            st.success("Access updated. User must re-login.")

    if st.button("⬅ Back"):
        st.session_state.page = "landing"
        st.session_state.logged_in = False
        st.session_state.is_admin = False
        st.rerun()

# =================================================
# FOOTER
# =================================================
st.markdown("<div class='footer'>MVP v1 • Built with ❤️ by Kav • Scan2Crack</div>", unsafe_allow_html=True)
