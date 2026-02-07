import streamlit as st

# ---------- SAFE SESSION INIT ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Interview Assistant", layout="wide")

st.title("🤖 Scan2Crack Smart Interview Bot")
st.caption("ECE interview answers • Offline • Student-friendly")

st.markdown("---")

# ---------- LOGIN PROTECTION ----------
if not st.session_state.logged_in:
    st.error("❌ Please login to access the AI Assistant.")
    if st.button("⬅ Go to Login"):
        st.session_state.page = "login"
        st.rerun()
    st.stop()

# ---------- ACCESS CHECK (ADMIN UNLOCK CONNECTS HERE) ----------
ai_unlocked = st.session_state.user_data.get("ai", False)

# ---------- LOCKED STATE ----------
if not ai_unlocked:
    st.warning("🔒 AI Assistant Locked – ₹20")
    st.caption("""
Unlock benefits:
• Ask unlimited ECE interview questions  
• Core, Embedded, VLSI & HR coverage  
• Offline, zero API cost  
""")

    if st.button("Go to Payment"):
        st.session_state.page = "payment"
        st.rerun()

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "home"
        st.rerun()

    st.stop()

# ===============================
# AI KNOWLEDGE BASE (UNLOCKED)
# ===============================

knowledge_base = {
    "pwm": "PWM controls power delivered to a load by varying duty cycle.",
    "smps": "SMPS is a switch-mode power supply using high-frequency switching.",
    "power electronics": "Power electronics deals with conversion and control of electrical power.",
    "embedded system": "An embedded system performs a specific task using hardware and software.",
    "esp32": "ESP32 is a low-power MCU with Wi-Fi and Bluetooth.",
    "uart": "UART is a serial communication protocol.",
    "i2c": "I2C is a two-wire serial communication protocol.",
    "spi": "SPI is a high-speed serial communication protocol.",
    "cmos": "CMOS uses complementary NMOS and PMOS transistors.",
    "setup time": "Minimum time data must be stable before clock edge.",
    "hold time": "Minimum time data must remain stable after clock edge.",
    "metastability": "Unstable output caused by timing violations.",
    "asic": "ASIC is an application-specific integrated circuit.",
    "tell me about yourself": "I am an ECE student with strong fundamentals and hands-on project experience.",
    "final year project": "Explain the problem, solution, tools used, and results.",
    "why should we hire you": "Highlight skills, projects, and learning attitude."
}

# ===============================
# USER INTERACTION
# ===============================

st.subheader("💬 Ask an Interview Question")

user_question = st.text_input(
    "Type your question",
    placeholder="Example: What is PWM?"
)

if st.button("Ask"):
    if not user_question.strip():
        st.warning("Please enter a question.")
    else:
        question_lower = user_question.lower()
        found = False

        for key in knowledge_base:
            if key in question_lower:
                st.success("🧠 Interview Answer")
                st.write(knowledge_base[key])
                found = True
                break

        if not found:
            st.info("""
🤖 I couldn’t find an exact match.

Try keywords like:
PWM, ESP32, Embedded System, CMOS, Setup Time, Project
""")

# ---------- BACK ----------
if st.button("⬅ Back to Dashboard"):
    st.session_state.page = "home"
    st.rerun()
