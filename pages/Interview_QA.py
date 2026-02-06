import streamlit as st
from pathlib import Path

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Interview Q&A", layout="wide")

# ---------- ACCESS CHECK (ADMIN UNLOCK CONNECTS HERE) ----------
interview_unlocked = st.session_state.user_data.get("interview", False)

# ---------- PROJECT ROOT & PDF PATH (FIXED) ----------
# Interview_QA.py is inside /pages
# parent -> project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

PDF_PATH = PROJECT_ROOT / "assets" / "interview_packs" / "Scan2Crack_All_Domains_Interview_QA.pdf"

# ---------- HEADER ----------
st.title("🎯 Interview Questions – ECE Edition")
st.caption("500+ curated interview questions across Core, Embedded, VLSI & HR")

st.markdown("---")

tabs = st.tabs([
    "🔹 Core ECE",
    "🔹 Embedded Systems",
    "🔹 VLSI / Digital",
    "🔹 HR & Projects"
])

# ===============================
# CORE ECE (FREE PREVIEW)
# ===============================
with tabs[0]:
    st.subheader("Core ECE Fundamentals – Free Preview")

    st.markdown("""
**Q1. What is Power Electronics?**  
Power electronics deals with conversion and control of electrical power using semiconductor devices.

**Q2. What is SMPS?**  
SMPS uses high-frequency switching to efficiently convert electrical power.

**Q3. What is PWM?**  
PWM controls power delivered to a load by varying the duty cycle.

**Q4. What is a rectifier?**  
A rectifier converts AC to DC.

**Q5. What is an inverter?**  
An inverter converts DC to AC.
""")

    st.info("📘 Full PDF includes **120+ Core ECE questions**")

# ===============================
# EMBEDDED SYSTEMS (FREE PREVIEW)
# ===============================
with tabs[1]:
    st.subheader("Embedded Systems – Free Preview")

    st.markdown("""
**Q1. What is an Embedded System?**  
An embedded system performs a specific function using hardware and software.

**Q2. What is ESP32?**  
ESP32 is a low-power microcontroller with Wi-Fi and Bluetooth.

**Q3. Arduino vs ESP32?**  
ESP32 supports wireless and higher processing power.

**Q4. Communication protocols used?**  
UART, I2C, SPI.

**Q5. What is IoT?**  
IoT connects devices to the internet for automation.
""")

    st.info("📘 Full PDF includes **150+ Embedded Systems questions**")

# ===============================
# VLSI / DIGITAL (FREE PREVIEW)
# ===============================
with tabs[2]:
    st.subheader("VLSI / Digital – Free Preview")

    st.markdown("""
**Q1. What is VLSI?**  
Very Large Scale Integration integrates millions of transistors on a chip.

**Q2. What is CMOS?**  
CMOS uses complementary NMOS and PMOS.

**Q3. What is setup time?**  
Minimum time data must be stable before clock edge.

**Q4. What is hold time?**  
Minimum time data must remain stable after clock edge.

**Q5. What is metastability?**  
Unstable output due to timing violations.
""")

    st.info("📘 Full PDF includes **120+ VLSI questions**")

# ===============================
# HR & PROJECT (FREE PREVIEW)
# ===============================
with tabs[3]:
    st.subheader("HR & Project – Free Preview")

    st.markdown("""
**Q1. Tell me about yourself.**  
Brief academic and technical introduction.

**Q2. Explain your project.**  
Explain problem, solution, tools, and result.

**Q3. Why should we hire you?**  
Mention skills, projects, and learning attitude.

**Q4. Challenges faced?**  
Explain technical or team challenges.

**Q5. Strengths?**  
Mention technical and personal strengths.
""")

    st.info("📘 Full PDF includes **100+ HR & Project questions**")

# ===============================
# PREMIUM DOWNLOAD SECTION
# ===============================
st.markdown("---")
st.subheader("📄 Download Complete Interview Pack")

if interview_unlocked:
    if PDF_PATH.exists():
        with open(PDF_PATH, "rb") as file:
            st.download_button(
                label="⬇️ Download All Domains Interview PDF",
                data=file,
                file_name="Scan2Crack_All_Domains_Interview_QA.pdf",
                mime="application/pdf"
            )
        st.success("✅ Premium access unlocked")
    else:
        st.error("❌ Interview PDF not found.")
        st.code(str(PDF_PATH))  # shows resolved path for debugging
else:
    st.warning("🔒 Interview Pack Locked – ₹99")
    st.caption("""
Includes:
• 120+ Core ECE Questions  
• 150+ Embedded Systems Questions  
• 120+ VLSI Questions  
• 100+ HR & Project Questions  
""")

    if st.button("Go to Payment"):
        st.session_state.page = "payment"
        st.rerun()

# ---------- BACK ----------
if st.button("⬅ Back to Dashboard"):
    st.session_state.page = "home"
    st.rerun()
