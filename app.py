import streamlit as st

# ---------------- HERO SECTION ----------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #7C3AED, #6366F1, #EC4899);
    padding: 80px 40px;
    border-radius: 22px;
    text-align: center;
    color: white;
}
.hero h1 {
    font-size: 52px;
    margin-bottom: 10px;
}
.hero p {
    font-size: 18px;
    opacity: 0.95;
}
.hero-btn {
    background-color: #FACC15;
    color: black;
    padding: 12px 26px;
    border-radius: 12px;
    font-weight: bold;
    display: inline-block;
    margin: 15px;
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
    <br>
    <a class="hero-btn">Unlock for ₹99</a>
    <a class="hero-btn" style="background:#ffffff33; color:white;">View Free Preview</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- WHY CHOOSE ----------------
st.markdown("<h2 class='center'>Why Choose Scan2Crack?</h2>", unsafe_allow_html=True)
st.markdown("<p class='center'>Designed by ECE students, for ECE students</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card center">
        ⚡<h4>Quick Access</h4>
        <p>Instant access to interview prep. No confusion. No overload.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card center">
        🧠<h4>Smart Content</h4>
        <p>Curated questions, answers, and resume formats that actually work.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card center">
        📈<h4>Proven Results</h4>
        <p>Core ECE, Embedded, VLSI & HR — all covered.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- WHAT YOU GET ----------------
st.markdown("<h2 class='center'>Everything You Need</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

features = [
    "📄 ECE Fresher Resume Template",
    "🎯 500+ Interview Questions",
    "🤖 AI Interview Assistant",
    "🧩 Domain-wise Preparation",
    "⚡ Last-minute Revision Planner",
    "🧠 Ready-made HR Answers"
]

for i in range(0, len(features), 2):
    col1, col2 = st.columns(2)
    col1.markdown(f"<div class='card'>{features[i]}</div>", unsafe_allow_html=True)
    if i+1 < len(features):
        col2.markdown(f"<div class='card'>{features[i+1]}</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
