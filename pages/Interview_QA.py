
import streamlit as st

# 🔐 Payment flag (temporary MVP logic)
interview_paid = False   # change to True to unlock
import os

st.set_page_config(page_title="Interview Q&A", layout="wide")

# ===============================
# CONFIG
# ===============================
PDF_PATH = "assets/interview_packs/Scan2Crack_All_Domains_Interview_QA.pdf"
paid_user = False   # 🔴 change to True after payment integration

# ===============================
# HEADER
# ===============================
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
PWM controls power delivered to a load by varying the duty cycle of a digital signal.

**Q4. What is a rectifier?**  
A rectifier converts AC to DC.

**Q5. What is an inverter?**  
An inverter converts DC power into AC power.
""")

    st.info("📘 Full PDF includes **120+ Core ECE questions**")

# ===============================
# EMBEDDED SYSTEMS (FREE PREVIEW)
# ===============================
with tabs[1]:
    st.subheader("Embedded Systems – Free Preview")

    st.markdown("""
**Q1. What is an Embedded System?**  
An embedded system is designed to perform a specific task using hardware and software.

**Q2. What is ESP32?**  
ESP32 is a low-power microcontroller with built-in Wi-Fi and Bluetooth.

**Q3. Difference between Arduino and ESP32?**  
ESP32 supports wireless communication and higher processing power.

**Q4. What protocols have you used?**  
UART, I2C, and SPI.

**Q5. What is IoT?**  
IoT connects devices to the internet for monitoring and automation.
""")

    st.info("📘 Full PDF includes **150+ Embedded Systems questions**")

# ===============================
# VLSI / DIGITAL (FREE PREVIEW)
# ===============================
with tabs[2]:
    st.subheader("VLSI / Digital – Free Preview")

    st.markdown("""
**Q1. What is VLSI?**  
VLSI integrates millions of transistors onto a single chip.

**Q2. What is CMOS?**  
CMOS uses complementary NMOS and PMOS transistors.

**Q3. What is setup time?**  
Minimum time data must be stable before the clock edge.

**Q4. What is hold time?**  
Minimum time data must remain stable after the clock edge.

**Q5. What is metastability?**  
Unstable output due to timing violations.
""")

    st.info("📘 Full PDF includes **120+ VLSI questions**")

# ===============================
# HR & PROJECT (FREE PREVIEW)
# ===============================
with tabs[3]:
    st.subheader("HR & Project Questions – Free Preview")

    st.markdown("""
**Q1. Tell me about yourself.**  
Give a brief academic and technical introduction.

**Q2. Explain your final year project.**  
Focus on problem, solution, tools, and results.

**Q3. Why should we hire you?**  
Highlight your skills, projects, and learning attitude.

**Q4. What challenges did you face?**  
Explain technical or team challenges and solutions.

**Q5. What are your strengths?**  
Mention technical strengths and consistency.
""")

    st.info("📘 Full PDF includes **100+ HR & Project questions**")

# ===============================
# PREMIUM DOWNLOAD SECTION
# ===============================
st.markdown("---")
st.subheader("📄 Download Complete Interview Pack")

if paid_user:
    if os.path.exists(PDF_PATH):
        with open(PDF_PATH, "rb") as file:
            st.download_button(
                label="⬇️ Download All Domains Interview PDF",
                data=file,
                file_name="Scan2Crack_All_Domains_Interview_QA.pdf",
                mime="application/pdf"
            )
        st.success("✅ Premium access unlocked")
    else:
        st.error("❌ Interview PDF not found. Please check file path.")
else:
    st.warning("🔒 Unlock Full Interview Pack – ₹99")
    st.caption("""
Includes:
• 120+ Core ECE Questions  
• 150+ Embedded Systems Questions  
• 120+ VLSI Questions  
• 100+ HR & Project Questions  
""")
    
if not interview_paid:
    st.warning("🔒 Unlock Interview Pack – ₹99")
    if st.button("Go to Payment"):
        st.switch_page("pages/4_Payment.py")
