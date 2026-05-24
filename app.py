import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TwinAI",
    page_icon="🧠",
    layout="wide"
)

# --------------------
# STYLE
# --------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.big-title {
    font-size: 55px;
    font-weight: bold;
}

.subtitle {
    font-size:18px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# --------------------
# DATA
# --------------------

df = pd.read_csv("data.csv")

# --------------------
# SIDEBAR
# --------------------

st.sidebar.title("🧠 TwinAI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "My Twin",
        "Future Simulator"
    ]
)

# --------------------
# HERO
# --------------------

st.image("assets/banner.jpg", use_container_width=True)

st.markdown(
    '<div class="big-title">TwinAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Build your digital twin and predict your future performance.</div>',
    unsafe_allow_html=True
)

st.write("")

# --------------------
# DASHBOARD
# --------------------

if page == "Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Productivity", "88%")
    col2.metric("Focus", "91%")
    col3.metric("Energy", "85%")
    col4.metric("Burnout Risk", "12%")

    st.divider()

    st.subheader("Weekly Data")

    st.dataframe(df, use_container_width=True)

# --------------------
# MY TWIN
# --------------------

elif page == "My Twin":

    st.header("Create Your Digital Twin")

    name = st.text_input("Your Name")

    study = st.slider("Study Hours", 0, 12, 6)

    sleep = st.slider("Sleep Hours", 0, 12, 8)

    exercise = st.slider("Exercise Hours", 0, 5, 1)

    mood = st.slider("Mood", 1, 10, 8)

    screen = st.slider("Screen Time", 0, 15, 5)

    twin_score = (
        study * 4
        + sleep * 4
        + exercise * 8
        + mood * 2
        - screen
    )

    twin_score = max(0, min(100, twin_score))

    st.progress(twin_score / 100)

    st.success(f"{name}'s Twin Score: {twin_score}/100")

    if twin_score >= 80:
        st.info("Status: Elite Performer 🚀")
    elif twin_score >= 60:
        st.info("Status: Strong Growth 📈")
    else:
        st.info("Status: Needs Improvement ⚠️")

# --------------------
# FUTURE SIMULATOR
# --------------------

elif page == "Future Simulator":

    st.header("Future Prediction")

    current = st.slider(
        "Current Productivity",
        0,
        100,
        75
    )

    improvement = st.slider(
        "Expected Improvement %",
        0,
        50,
        15
    )

    future = min(100, current + improvement)

    st.metric(
        "Predicted Future Productivity",
        f"{future}%"
    )

    st.progress(future / 100)

    if future >= 90:
        st.success(
            "Your twin predicts exceptional performance."
        )
    elif future >= 75:
        st.info(
            "Your twin predicts strong future growth."
        )
    else:
        st.warning(
            "Your twin recommends improving daily habits."
        )
