import streamlit as st
from auth import login_user, register_user, admin_login
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
# SESSION INIT
# -------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

# -------------------------------------------------
# TOP BAR
# -------------------------------------------------
l, m, r = st.columns([3, 6, 3])

with l:
    st.markdown("## 🚀 Scan2Crack")

with r:
    if st.session_state.logged_in:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_data = {}
            st.session_state.is_admin = False
            st.rerun()

st.markdown("---")

# =================================================
# LANDING PAGE (NOT LOGGED IN)
# =================================================
if not st.session_state.logged_in:

    # ---------------- STYLES ----------------
    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(135deg, #7C3AED, #6366F1, #EC4899);
        padding: 80px 40px;
        border-radius: 22px;
        text-align: center;
        color: white;
    }
    .hero h1 { font-size: 52px; }
    .hero-btn {
        background-color: #FACC15;
        color: black;
        padding: 12px 26px;
        border-radius: 12px;
        font-weight: bold;
        margin: 10px;
        display: inline-block;
    }
    .card {
        background: white;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }
    .center { text-align:center; }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- HERO ----------------
    st.markdown("""
    <div class="hero">
        <p style="background:#ffffff22; display:inline-block; padding:6px 14px; border-radius:999px;">
            Your Ultimate ECE Interview Companion
        </p>
        <h1>Scan2Crack – <span style="color:#FACC15;">ECE Edition</span></h1>
        <p>
            One scan. One payment. All ECE interview essentials.<br>
            Resume • Core • Embedded • VLSI • AI Help
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- CTA BUTTONS ----------------
    cta1, cta2 = st.columns(2)

    with cta1:
        if st.button("🚀 Unlock for ₹99"):
            st.session_state.show_login = True

    with cta2:
        if st.button("👀 View Free Preview"):
            st.switch_page("pages/Interview_QA.py")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ---------------- LOGIN & REGISTER ----------------
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
                st.rerun()
            else:
                st.error("Invalid credentials")

    with col2:
        st.subheader("Register")
        name = st.text_input("Full Name")
        reg_email = st.text_input("Register Email")
        reg_password = st.text_input("Register Password", type="password")

        if st.button("Create Account"):
            ok, msg = register_user(name, reg_email, reg_password)
            if ok:
                st.success("Account created. Please login.")
            else:
                st.error(msg)

    st.markdown("---")

    # ---------------- ADMIN LOGIN ----------------
    st.subheader("🛠️ Admin Login")

    admin_email = st.text_input("Admin Email")
    admin_pass = st.text_input("Admin Password", type="password")

    if st.button("Login as Admin"):
        if admin_login(admin_email, admin_pass):
            st.session_state.logged_in = True
            st.session_state.is_admin = True
            st.rerun()
        else:
            st.error("Invalid admin credentials")

    st.stop()
# =================================================
# ADMIN PANEL (INSIDE app.py)
# =================================================
elif st.session_state.logged_in and st.session_state.is_admin:

    st.header("🛠️ Admin Panel – Unlock User Access")
    st.markdown("---")

    users = load_users()

    if not users:
        st.info("No registered users yet.")
    else:
        selected_email = st.selectbox("Select User Email", list(users.keys()))
        user = users[selected_email]

        st.markdown("### 👤 User Details")
        st.write(f"**Name:** {user.get('name')}")
        st.write(f"**Email:** {selected_email}")

        st.markdown("---")
        st.markdown("### 🔓 Unlock Products")

        resume = st.checkbox("📄 Resume Builder", value=user.get("resume", False))
        interview = st.checkbox("🎯 Interview Q&A", value=user.get("interview", False))
        ai = st.checkbox("🤖 AI Assistant", value=user.get("ai", False))

        if st.button("💾 Save Access"):
            users[selected_email]["resume"] = resume
            users[selected_email]["interview"] = interview
            users[selected_email]["ai"] = ai

            save_users(users)
            st.success("✅ Access updated successfully!")

    st.markdown("---")
    if st.button("⬅ Back to Dashboard"):
        st.session_state.is_admin = False
        st.rerun()


# =================================================
# DASHBOARD (LOGGED IN)
# =================================================
st.success(f"Welcome {st.session_state.user_data.get('name','User')} 👋")
st.markdown("## 🎓 Dashboard")

c1, c2, c3 = st.columns(3)

with c1:
    st.image("assets/resume.jpg", use_container_width=True)
    if st.button("📄 Resume Builder"):
        st.switch_page("pages/Resume.py")

with c2:
    st.image("assets/interview.jpg", use_container_width=True)
    if st.button("🎯 Interview Q&A"):
        st.switch_page("pages/Interview_QA.py")

with c3:
    st.image("assets/ai.jpg", use_container_width=True)
    if st.button("🤖 AI Assistant"):
        st.switch_page("pages/AI_Assistant.py")

st.markdown("---")
if st.button("💳 Payment / Unlock"):
    st.switch_page("pages/Payments.py")

st.markdown(
    "<div style='text-align:center; color:gray;'>MVP v1 • Built with ❤️ by Kav • Scan2Crack</div>",
    unsafe_allow_html=True
)
