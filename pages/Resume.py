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
# STEP 2: RESUME – JD MATCHING
# =================================================
st.subheader("🔍 Resume–JD Match Analysis")

if jd_text:

    # -------- Combine Resume Content --------
    resume_text = (
        profile + " " +
        skills_col1 + " " +
        skills_col2 + " " +
        skills_col3 + " " +
        experience
    ).lower()

    jd_lower = jd_text.lower()

    # -------- Core ECE Keyword Bank --------
    keyword_bank = [
        "embedded", "esp32", "arduino", "microcontroller",
        "uart", "spi", "i2c", "rtos",
        "c", "embedded c",
        "digital electronics", "verilog", "vlsi",
        "cmos", "asic", "fpga",
        "iot", "sensors",
        "debugging", "testing", "pcb"
    ]

    # -------- Extract JD Keywords --------
    jd_keywords = [k for k in keyword_bank if k in jd_lower]

    # -------- Match Analysis --------
    matched = [k for k in jd_keywords if k in resume_text]
    missing = [k for k in jd_keywords if k not in resume_text]

    if jd_keywords:
        match_percent = int((len(matched) / len(jd_keywords)) * 100)
    else:
        match_percent = 0

    # -------- Display Results --------
    st.metric("Resume–JD Match", f"{match_percent}%")

    if match_percent >= 80:
        st.success("Excellent match with job description.")
    elif match_percent >= 60:
        st.info("Good match, but resume can be improved.")
    else:
        st.warning("Low match. Resume needs customization.")

    # -------- Matched Keywords --------
    if matched:
        st.markdown("### ✅ Matching Skills")
        st.write(", ".join(matched))

    # -------- Missing Keywords --------
    if missing:
        st.markdown("### ❌ Missing Skills")
        for m in missing:
            st.write(f"• {m}")

        st.markdown("### 💡 Suggestions to Improve Resume")
        for m in missing:
            st.write(f"• Add a project or experience related to **{m}**")

else:
    st.info("Paste a Job Description above to see matching analysis.")

# =================================================
# STEP 3: ROLE-BASED PREPARATION GUIDE
# =================================================
st.markdown("---")
st.subheader("🧠 Preparation Guide")

if jd_text:
    jd_lower = jd_text.lower()

    # -------- Role Detection --------
    if any(k in jd_lower for k in ["embedded", "esp32", "microcontroller", "rtos"]):
        role = "Embedded Engineer"

        prepare_list = [
            "Embedded C (pointers, memory, interrupts)",
            "ESP32 architecture & peripherals",
            "UART, SPI, I2C protocols",
            "RTOS basics (tasks, scheduling)",
            "Timers, ADC, GPIO",
            "Debugging techniques"
        ]

        resources = {
            "YouTube – Embedded C (Gate Smashers)": "https://www.youtube.com/watch?v=KJgsSFOSQv0",
            "YouTube – ESP32 Tutorials (Random Nerd)": "https://www.youtube.com/@RandomNerdTutorials",
            "Website – GeeksforGeeks Embedded": "https://www.geeksforgeeks.org/embedded-systems/"
        }

    elif any(k in jd_lower for k in ["vlsi", "cmos", "rtl", "verilog", "asic"]):
        role = "VLSI / Digital Engineer"

        prepare_list = [
            "Digital Logic & FSMs",
            "CMOS fundamentals",
            "Verilog HDL",
            "Timing analysis (setup/hold)",
            "ASIC vs FPGA",
            "Low power design basics"
        ]

        resources = {
            "YouTube – Digital Electronics (Neso Academy)": "https://www.youtube.com/@NesoAcademy",
            "YouTube – Verilog HDL": "https://www.youtube.com/watch?v=YCM2sG8c1nE",
            "Website – VLSI Basics": "https://www.vlsiguru.com/"
        }

    else:
        role = "Core ECE Engineer"

        prepare_list = [
            "Analog & Digital Electronics",
            "Signals & Systems basics",
            "Control Systems",
            "Communication fundamentals",
            "Power Electronics",
            "Basic semiconductor devices"
        ]

        resources = {
            "YouTube – Analog Electronics (Gate Smashers)": "https://www.youtube.com/@GateSmashers",
            "YouTube – Communication Systems": "https://www.youtube.com/@nptelhrd",
            "Website – Electronics Tutorials": "https://www.electronics-tutorials.ws/"
        }

    # -------- Display --------
    st.success(f"Detected Role: **{role}**")

    st.markdown("### ✅ What to Prepare")
    for item in prepare_list:
        st.write(f"• {item}")

    st.markdown("### 📚 Recommended Resources")
    for name, link in resources.items():
        st.markdown(f"- [{name}]({link})")

else:
    st.info("Paste a Job Description above to see preparation guidance.")
# =================================================
# ATS READINESS INDICATOR (TUNED VERSION)
# =================================================
st.markdown("---")
st.subheader("📄 ATS Readiness Indicator")

def ats_score_checker(resume_text, experience_text, jd_text):
    score = 0
    remarks = []

    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    # -------- Strong Action Verbs --------
    action_verbs = [
        "designed", "developed", "implemented",
        "integrated", "optimized", "analyzed"
    ]
    verb_hits = sum(1 for v in action_verbs if v in experience_text.lower())

    if verb_hits >= 3:
        score += 18
    elif verb_hits == 2:
        score += 12
        remarks.append("Use more strong action verbs (designed, implemented, etc.).")
    else:
        remarks.append("Experience section lacks strong action verbs.")

    # -------- JD-Specific Keyword Matching --------
    role_keywords = [
        "embedded", "esp32", "microcontroller",
        "uart", "spi", "i2c", "rtos",
        "verilog", "cmos", "vlsi", "asic",
        "iot", "sensors"
    ]

    jd_relevant = [k for k in role_keywords if k in jd_lower]
    matched = [k for k in jd_relevant if k in resume_lower]

    if jd_relevant:
        match_ratio = len(matched) / len(jd_relevant)
    else:
        match_ratio = 0

    if match_ratio >= 0.7:
        score += 25
    elif match_ratio >= 0.5:
        score += 18
        remarks.append("Resume partially matches job description keywords.")
    else:
        remarks.append("Resume lacks important job-specific keywords.")

    # -------- Bullet Structure --------
    bullet_lines = [l for l in experience_text.split("\n") if l.strip()]
    if len(bullet_lines) >= 3:
        score += 15
    else:
        remarks.append("Add more bullet points in experience section.")

    # -------- Section Completeness --------
    sections_ok = all(len(s.strip()) > 20 for s in [profile, experience, education])
    if sections_ok:
        score += 15
    else:
        remarks.append("One or more resume sections are incomplete.")

    # -------- Sentence Length Control --------
    long_lines = [l for l in experience_text.split("\n") if len(l) > 120]
    if not long_lines:
        score += 15
    else:
        remarks.append("Avoid long sentences; keep points concise.")

    # -------- Generic Keyword Penalty --------
    generic_words = ["engineering", "technology", "system", "project"]
    generic_hits = sum(1 for g in generic_words if g in resume_lower)

    if generic_hits > 5:
        score -= 5
        remarks.append("Reduce generic terms; add more role-specific details.")

    # -------- Cap Score (REALISTIC ATS) --------
    return min(score, 88), remarks


# -------- RUN ATS CHECK --------
if jd_text:
    resume_text_full = (
        profile + " " +
        skills_col1 + " " +
        skills_col2 + " " +
        skills_col3 + " " +
        experience + " " +
        education
    )

    ats_score, ats_remarks = ats_score_checker(
        resume_text_full,
        experience,
        jd_text
    )

    st.metric("ATS Compatibility Score", f"{ats_score} / 100")

    if ats_score >= 80:
        st.success("✅ High ATS Readiness")
    elif ats_score >= 60:
        st.info("⚠️ Medium ATS Readiness")
    else:
        st.warning("❌ Low ATS Readiness")

    if ats_remarks:
        st.markdown("### 🔧 ATS Improvement Suggestions")
        for r in ats_remarks:
            st.write(f"• {r}")
else:
    st.info("Paste a Job Description to evaluate ATS readiness.")


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
