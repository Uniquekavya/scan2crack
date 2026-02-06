import streamlit as st
import io

# ---------- SAFE IMPORT FOR STREAMLIT CLOUD ----------
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
except ImportError:
    A4 = None
    canvas = None

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Resume Builder", layout="wide")

st.title("📄 Resume Builder – Tech Fresher Format")
st.caption("Industry-standard resume used by real recruiters")

st.markdown("---")

# ---------- ACCESS CHECK ----------
# This is the IMPORTANT LINE (ADMIN UNLOCK CONNECTS HERE)
resume_unlocked = st.session_state.user_data.get("resume", False)

# ---------- INPUT SECTION ----------
st.subheader("🔹 Basic Details")

name = st.text_input("Full Name", "YOUR NAME")
phone = st.text_input("Phone", "+91XXXXXXXXXX")
email = st.text_input("Email", "name@gmail.com")
linkedin = st.text_input("LinkedIn Profile", "linkedin.com/in/yourprofile")

st.subheader("🔹 Profile Summary (3 bullet points)")
profile = st.text_area(
    "Profile",
    """Final-year Electronics and Communication Engineering student with strong foundation in embedded systems.
Hands-on experience in ESP32 and IoT projects.
Seeking entry-level embedded systems role.""",
    height=120
)

st.subheader("🔹 Skills")
skills = st.text_area(
    "Skills",
    "Embedded C, ESP32, Arduino, Digital Electronics, Verilog, IoT, MATLAB",
    height=80
)

st.subheader("🔹 Projects / Experience")
exp_org = st.text_input("Project / Organization", "IoT Smart Trash Compactor")
exp_role = st.text_input("Role", "Embedded Developer")
exp_date = st.text_input("Duration", "Feb 2024 – Present")

experience = st.text_area(
    "Description",
    """Designed ESP32-based smart trash compactor.
Integrated sensors and cloud alerts.
Implemented relay-based actuator control.""",
    height=120
)

st.subheader("🔹 Education")
education = st.text_area(
    "Education",
    """B.E. Electronics & Communication – XYZ College (2021–2025)
PUC – ABC College (2019–2021)""",
    height=80
)

st.markdown("---")

# ---------- PDF GENERATION ----------
def generate_resume_pdf():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 40

    c.setFont("Helvetica-Bold", 18)
    c.drawString(40, y, name)

    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"{phone} | {email} | {linkedin}")

    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "PROFILE")

    y -= 15
    c.setFont("Helvetica", 10)
    for line in profile.split("\n"):
        c.drawString(50, y, f"- {line}")
        y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "SKILLS")

    y -= 15
    c.setFont("Helvetica", 10)
    for skill in skills.split(","):
        c.drawString(50, y, f"- {skill.strip()}")
        y -= 14

    y -= 15
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "EXPERIENCE")

    y -= 15
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, y, f"{exp_org} | {exp_role}")
    c.drawRightString(width - 40, y, exp_date)

    y -= 15
    c.setFont("Helvetica", 10)
    for line in experience.split("\n"):
        c.drawString(50, y, f"- {line}")
        y -= 14

    y -= 15
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "EDUCATION")

    y -= 15
    c.setFont("Helvetica", 10)
    for line in education.split("\n"):
        c.drawString(50, y, f"- {line}")
        y -= 14

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# ---------- DOWNLOAD SECTION ----------
st.subheader("⬇️ Download Resume")

if resume_unlocked:
    if A4 is None:
        st.error("PDF library missing. Please contact admin.")
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

# ---------- BACK ----------
if st.button("⬅ Back to Dashboard"):
    st.session_state.page = "home"
    st.rerun()
