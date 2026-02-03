import streamlit as st
try:
    from reportlab.lib.pagesizes import A4
except ImportError:
    A4 = None

from reportlab.pdfgen import canvas
import io

st.set_page_config(page_title="Resume Builder", layout="wide")

st.title("📄 Resume Builder – Tech Fresher Format")
st.caption("Industry-standard resume used by real recruiters")

st.markdown("---")

# =========================
# INPUT SECTION
# =========================

st.subheader("🔹 Basic Details")

name = st.text_input("Full Name", "YOUR NAME")
phone = st.text_input("Phone", "+91XXXXXXXXXX")
email = st.text_input("Email", "name@gmail.com")
linkedin = st.text_input("LinkedIn Profile", "linkedin.com/in/yourprofile")

st.subheader("🔹 Profile Summary (3 bullet points)")

profile = st.text_area(
    "Profile",
    """Final-year Electronics and Communication Engineering student with strong foundation in embedded systems and digital electronics.
Hands-on experience in ESP32, IoT-based automation projects, and sensor interfacing.
Eager to apply technical skills in a core engineering or embedded systems role.""",
    height=120
)

st.subheader("🔹 Skills (comma separated)")

skills = st.text_area(
    "Skills",
    "Embedded C, ESP32, Arduino, Digital Electronics, Verilog HDL, IoT, MATLAB, Sensors, UART, I2C, SPI",
    height=80
)

st.subheader("🔹 Experience / Projects")

exp_org = st.text_input("Organization / Project Title", "IoT-Enabled Smart Trash Compactor")
exp_role = st.text_input("Role", "Embedded Systems Developer")
exp_date = st.text_input("Duration", "Feb 202X – Present")

experience = st.text_area(
    "Experience Description",
    """Designed and developed an ESP32-based smart trash compactor using ultrasonic and moisture sensors.
Implemented real-time cloud monitoring and automated alerts for waste level detection.
Integrated relay-controlled actuator system for compaction, improving waste handling efficiency.""",
    height=140
)

st.subheader("🔹 Education")

education = st.text_area(
    "Education",
    """Bachelor of Engineering – Electronics & Communication, XYZ College, 2021–2025
PUC / 12th Standard, ABC College, 2019–2021""",
    height=80
)

st.subheader("🔹 Volunteering / Extracurricular")

volunteer = st.text_area(
    "Volunteering",
    """Active member of IEEE Student Branch, participated in technical workshops and outreach programs.
Contributed to organizing technical events and peer learning sessions.""",
    height=80
)

st.markdown("---")

# =========================
# PDF GENERATION
# =========================

def generate_resume_pdf():
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 40

    # NAME
    c.setFont("Helvetica-Bold", 18)
    c.drawString(40, y, name)

    # CONTACT
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"{phone} | {email} | {linkedin}")

    # PROFILE
    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "PROFILE")

    y -= 15
    c.setFont("Helvetica", 10)
    for line in profile.split("\n"):
        c.drawString(50, y, f"- {line}")
        y -= 14

    # SKILLS
    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "SKILLS")

    y -= 15
    c.setFont("Helvetica", 10)
    skill_list = skills.split(",")
    x_positions = [40, 200, 360]
    col = 0
    for skill in skill_list:
        c.drawString(x_positions[col], y, f"- {skill.strip()}")
        col += 1
        if col == 3:
            col = 0
            y -= 14

    # EXPERIENCE
    y -= 25
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

    # EDUCATION
    y -= 15
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "EDUCATION")

    y -= 15
    c.setFont("Helvetica", 10)
    for line in education.split("\n"):
        c.drawString(50, y, f"- {line}")
        y -= 14

    # VOLUNTEERING
    y -= 15
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "VOLUNTEERING / EXTRACURRICULAR")

    y -= 15
    c.setFont("Helvetica", 10)
    for line in volunteer.split("\n"):
        c.drawString(50, y, f"- {line}")
        y -= 14

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer


# =========================
# DOWNLOAD
# =========================

paid_user = False  # later this becomes True after payment

st.subheader("⬇️ Download Resume")

if paid_user:
    pdf = generate_resume_pdf()
    st.download_button(
        "📄 Download Resume (PDF)",
        data=pdf,
        file_name="Scan2Crack_Resume.pdf",
        mime="application/pdf"
    )
else:
    st.warning("🔒 Unlock Resume Pack – ₹39 to download")
    st.caption("Payment integration coming soon")


if st.button("Go to Payment"):
    st.switch_page("pages/4_Payment.py")
