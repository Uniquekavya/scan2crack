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
# GLOBAL CSS (UI MAGIC)
# -------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #F8FAFC;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.hero {
    background: linear-gradient(90deg, #4F46E5, #6366F1);
    padding: 30px;
    border-radius: 18px;
    color: white;
}
.hero h1 {
    margin-bottom: 5px;
}
.center {
    text-align: center;
}
.stButton>button {
    background-color: #4F46E5;
    color: white;
    border-radius: 10px;
    padding: 0.6em 1.2em;
}
.stButton>button:hover {
    background-color: #4338CA;
}
</style>
""", unsafe_allow_html=True)

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
# TOP HERO BAR
# -------------------------------------------------
st.markdown("""
<div class="hero center">
    <h1>🚀 Scan2Crack – ECE Edition</h1>
    <p>Crack Core ECE Interviews with Confidence</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =================================================
# LOGIN PAGE
# =================================================
if st.session_state.page == "login":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
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
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Create new account"):
            st.session_state.page = "register"
            st.rerun()
    with col2:
        if st.button("Login as Admin"):
            st.session_state.page = "admin_login"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# =================================================
# REGISTER PAGE
# =================================================
elif st.session_state.page == "register":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("📝 Create Account")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        ok, msg = register_user(name, email, password)
        if ok:
            st.success("Account created successfully!")
            st.session_state.page = "login"
            st.rerun()
        else:
            st.error(msg)

    if st.button("⬅ Back to Login"):
        st.session_state.page = "login"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# =================================================
# USER DASHBOARD
# =================================================
elif st.session_state.page == "home":

    st.success(f"Welcome, {st.session_state.user_data.get('name','User')} 👋")
    st.markdown("### 🎓 Your Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📄 Resume Builder")
        st.write("ATS-friendly resume + scoring")
        if st.session_state.user_data["resume"]:
            st.success("Unlocked")
        else:
            st.warning("Locked – ₹39")
            if st.button("Unlock Resume"):
                st.session_state.page = "payment"
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🎯 Interview Q&A")
        st.write("500+ Core ECE questions")
        if st.session_state.user_data["interview"]:
            st.success("Unlocked")
        else:
            st.warning("Locked – ₹99")
            if st.button("Unlock Interview"):
                st.session_state.page = "payment"
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🤖 AI Assistant")
        st.write("Smart interview helper")
        if st.session_state.user_data["ai"]:
            st.success("Unlocked")
        else:
            st.warning("Locked – ₹149")
            if st.button("Unlock AI"):
                st.session_state.page = "payment"
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.rerun()

# =================================================
# PAYMENT PAGE
# =================================================
elif st.session_state.page == "payment":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
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
    st.markdown("</div>", unsafe_allow_html=True)

# =================================================
# ADMIN LOGIN
# =================================================
elif st.session_state.page == "admin_login":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🔐 Admin Login")

    email = st.text_input("Admin Email")
    password = st.text_input("Admin Password", type="password")

    if st.button("Login"):
        if admin_login(email, password):
            st.session_state.page = "admin_panel"
            st.rerun()
        else:
            st.error("Invalid admin credentials")

    if st.button("⬅ Back"):
        st.session_state.page = "login"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# =================================================
# ADMIN PANEL
# =================================================
elif st.session_state.page == "admin_panel":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🛠️ Admin Panel")

    users = load_users()
    if users:
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
    else:
        st.info("No registered users yet.")

    if st.button("Logout Admin"):
        st.session_state.page = "login"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("""
<div class="center" style="color:gray; margin-top:30px;">
    MVP v1 • Built with ❤️ by Kav • Scan2Crack
</div>
""", unsafe_allow_html=True)
