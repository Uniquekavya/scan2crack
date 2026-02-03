import streamlit as st

st.set_page_config(page_title="AI Interview Assistant", layout="wide")

st.title("🤖 Scan2Crack Smart Interview Bot")
st.caption("ECE interview answers • Offline • Free")

st.markdown("---")

paid_user = True  # later used for premium unlock

# -------------------------
# KNOWLEDGE BASE (FREE AI)
# -------------------------
knowledge_base = {
    "pwm": "PWM is a technique used to control power delivered to a load by varying the duty cycle of a digital signal.",
    "smps": "SMPS is a switch-mode power supply that uses high-frequency switching for high efficiency.",
    "power electronics": "Power electronics deals with conversion and control of electrical power using semiconductor devices.",
    "embedded system": "An embedded system is a dedicated system designed to perform a specific task using hardware and software.",
    "esp32": "ESP32 is a low-power microcontroller with built-in Wi-Fi and Bluetooth, widely used in IoT applications.",
    "uart": "UART is a serial communication protocol used for short-distance communication.",
    "i2c": "I2C is a two-wire communication protocol supporting multiple slave devices.",
    "spi": "SPI is a high-speed serial communication protocol using master-slave architecture.",
    "cmos": "CMOS uses complementary NMOS and PMOS transistors for low power consumption.",
    "setup time": "Setup time is the minimum time data must be stable before the clock edge.",
    "hold time": "Hold time is the minimum time data must remain stable after the clock edge.",
    "metastability": "Metastability occurs when a flip-flop output becomes unstable due to timing violations.",
    "asic": "ASIC is an application-specific integrated circuit designed for a particular use.",
    "tell me about yourself": "I am an ECE student with strong interest in embedded systems and core electronics, with hands-on project experience.",
    "final year project": "Explain the problem statement, your solution, tools used, and results clearly.",
    "why should we hire you": "Mention your technical skills, project experience, and willingness to learn."
}

# -------------------------
# USER INPUT
# -------------------------
st.subheader("💬 Ask an Interview Question")

user_question = st.text_input(
    "Type your question",
    placeholder="Example: What is PWM?"
)

# -------------------------
# RESPONSE LOGIC
# -------------------------
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
            st.info(
                "🤖 I couldn't find an exact match.\n\n"
                "Try using keywords like:\n"
                "PWM, ESP32, Embedded System, CMOS, Setup Time, Project"
            )
if not ai_paid:
    st.warning("🔒 Unlock AI Assistant – ₹149")
    if st.button("Go to Payment"):
        st.switch_page("pages/4_Payment.py")
    st.stop()
