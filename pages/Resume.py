import streamlit as st
import io

# =================================================
# SAFE SESSION INIT
# =================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# =================================================
# PDF IMPORT
# =================================================
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
except ImportError:
    A4 = None
    canvas = None

# =================================================
# PAGE CONFIG
# =================================================
st.set_page_config(page_title="Resume Builder", layout="wide")

# =================================================
# LOGIN PROTECTION
# =================================================
if not st.session_state.logged_in:
    st.error("❌ Please login to access Resume Builder.")
    if st.button("⬅ Go to Login"):
        st.session_state.page = "login"
        st.rerun()
    st.stop()

# =================================================
# ACCESS CHECK (ADMIN UNLOCK)
# =================================================
resume_unlocked = st.session_state.user_data.get("resume", False)

# =================================================
# UI HEADER
# =================================================
st.title("📄 Resume Builder – Tech Fresher")
st.caption("ATS-friendly • Recruiter-approved • ECE focused")
st.markdown("---")

# =================================================
# INPUT SECTION
# =================================================
st.subheader("🔹 Header Details")
name = st.text_input("Full Name", "YOUR NAME")
phone = st.text_input("Phone", "+91XXXXXXXXXX")
email = st.text_input("Email", "name@gmail.com")
linkedin = st.text_input("LinkedIn", "linkedin.com/in/yourprofile")

st.subheader("🔹 Profile Summary (3 bullets)")
profile = st.text_area(
    "Profile",
    """Final-year Electronics and Communication Engineering student with strong fundamentals in Embedded Systems and Digital Electronics.
Hands-on experience in ESP32, IoT-based automation, and sensor interfacing.
Seeking entry-level opportunities in Embedded Systems / Core ECE roles.""",
    height=120
)

st.subheader("🔹 Skills (3-column format)")
skills_col1 = st.text_area("Technical Skills", "Embedded C\nDigital Electronics\nVerilog HDL\nMicrocontrollers", height=90)
skills_col2 = st.text_area("Tools & Platforms", "ESP32\nArduino IDE\nMATLAB\nThingSpeak", height=90)
skills_col3 = st.text_area("Professional Skills", "Problem Solving\nTeam Collaboration\nDocumentation\nPresentation", height=90)

st.subheader("🔹 Experience / Projects")
org = st.text_input("Project / Organization", "IoT-Enabled Smart Trash Compactor")
role = st.text_input("Role", "Embedded Systems Developer")
duration = st.text_input("Duration", "Feb 2024 – Present")
experience = st.text_area(
    "Experience Description",
    """Designed and developed an ESP32-based smart trash compactor using ultrasonic and moisture sensors.
Implemented real-time cloud monitoring and alert system.
Integrated relay-controlled actuator system for automated compaction.
Improved waste management efficiency through automation.""",
    height=140
)

st.subheader("🔹 Education")
education = st.text_area(
    "Education",
    """Bachelor of Engineering – Electronics & Communication, XYZ College (2021–2025)
PUC / Class XII – ABC College (2019–2021)""",
    height=90
)

st.subheader("🔹 Volunteering / Extracurriculars")
volunteer = st.text_area(
    "Volunteering",
    """Active member of IEEE Student Branch.
Participated in technical workshops and outreach programs.
Assisted in organizing college-level technical events.""",
    height=90
)

st.markdown("---")

# =================================================
# RESUME SCORE CHECKER (NEW)
# =================================================
def calculate_resume_score(profile, skills, experience, education, volunteer):
    score = 0
    feedback = []

    # Profile
    if len(profile.split("\n")) >= 2:
        score += 15
    else:
        feedback.append("Improve profile summary (add 2–3 strong bullets).")

    # Skills
    skill_count = len([s for s in skills.split("\n") if s.strip()])
    if skill_count >= 8:
        score += 25
    elif skill_count >= 5:
        score += 18
        feedback.append("Add more relevant technical skills.")
    else:
        feedback.append("Skills section is weak.")

    # Experience
    exp_lines = [l for l in experience.split("\n") if l.strip()]
    if len(exp_lines) >= 3:
        score += 25
    else:
        feedback.append("Add more impact-based project points.")

    # Education
    if len(education.strip()) > 10:
        score += 10
    else:
        feedback.append("Education details missing.")

    # Keywords
    keywords = ["designed", "developed", "implemented", "integrated", "analyzed"]
    keyword_hits = sum(1 for k in keywords if k in experience.lower())
    score += min(keyword_hits * 2, 10)

    # Volunteering
    if len(volunteer.strip()) > 10:
        score += 10
    else:
        feedback.append("Add volunteering or extracurricular activities.")

    # Formatting (fixed)
    score += 5

    return min(score, 100), feedback

# =================================================
# SCORE UI
# =================================================
st.subheader("📊 Resume Score Checker")

if st.button("Check Resume Score"):
    score, feedback = calculate_resume_score(
        profile,
        skills_col1 + "\n" + skills_col2 + "\n" + skills_col3,
        experience,
        education,
        volunteer
    )

    st.metric("Resume Score", f"{score} / 100")

    if score >= 85:
        st.success("Excellent resume – recruiter ready!")
    elif score >= 70:
        st.info("Good resume – minor improvements needed.")
    else:
        st.warning("Resume needs improvement.")

    if feedback:
        st.markdown("### 🔍 Suggestions to Improve")
        for f in feedback:
            st.write(f"• {f}")

st.markdown("---")
# =================================================
# STEP 1: JOB DESCRIPTION INPUT
# =================================================
st.markdown("---")
st.subheader("📄 Job Description (JD) Analysis")

jd_text = st.text_area(
    "Paste the Job Description here",
    placeholder="Paste job description from company career page...",
    height=200
)

if jd_text:
    st.success("JD received successfully.")


# =================================================
# PDF GENERATION
# =================================================
def generate_resume_pdf():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 40

    c.setFont("Helvetica-Bold", 20)
    c.drawString(40, y, name)

    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"{phone} | {email} | {linkedin}")
    y -= 10
    c.line(40, y, width - 40, y)

    y -= 25
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "PROFILE")
    y -= 15
    c.setFont("Helvetica", 10)
    for line in profile.split("\n"):
        c.drawString(50, y, f"• {line}")
        y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "SKILLS")
    y -= 15

    col_x = [40, 200, 360]
    cols = [skills_col1.split("\n"), skills_col2.split("\n"), skills_col3.split("\n")]
    max_len = max(len(c) for c in cols)

    c.setFont("Helvetica", 10)
    for i in range(max_len):
        for col in range(3):
            if i < len(cols[col]):
                c.drawString(col_x[col], y, f"• {cols[col][i]}")
        y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "EXPERIENCE")
    y -= 15
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, y, f"{org} | {role}")
    c.drawRightString(width - 40, y, duration)

    y -= 15
    c.setFont("Helvetica", 10)
    for line in experience.split("\n"):
        c.drawString(50, y, f"• {line}")
        y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "EDUCATION")
    y -= 15
    c.setFont("Helvetica", 10)
    for line in education.split("\n"):
        c.drawString(50, y, f"• {line}")
        y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "VOLUNTEERING / EXTRACURRICULARS")
    y -= 15
    c.setFont("Helvetica", 10)
    for line in volunteer.split("\n"):
        c.drawString(50, y, f"• {line}")
        y -= 14

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# =================================================
# DOWNLOAD SECTION
# =================================================
st.subheader("⬇️ Download Resume")

if resume_unlocked:
    if A4 is None:
        st.error("PDF library missing.")
    else:
        pdf = generate_resume_pdf()
        st.download_button(
            "📄 Download Resume (PDF)",
            data=pdf,
            file_name="Scan2Crack_Resume.pdf",
            mime="application/pdf"
        )
else:
    st.warning("🔒 Resume Pack Locked – ₹39")
    st.caption("Complete payment. Admin will unlock access.")

    if st.button("Go to Payment"):
        st.session_state.page = "payment"
        st.rerun()

# =================================================
# BACK
# =================================================
if st.button("⬅ Back to Dashboard"):
    st.session_state.page = "home"
    st.rerun()
