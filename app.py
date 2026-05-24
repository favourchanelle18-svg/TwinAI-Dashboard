import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="TwinAI",
    page_icon="🧠",
    layout="wide"
)

# --------------------
# CUSTOM STYLING
# --------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.metric-card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

.big-title {
    font-size: 50px;
    font-weight: bold;
}

.subtitle {
    color: grey;
    font-size:18px;
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
        "Digital Twin",
        "Predictions"
    ]
)

# --------------------
# HERO IMAGE
# --------------------

st.image("assets/banner.jpg", use_container_width=True)

st.markdown(
    '<div class="big-title">TwinAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your Personal Digital Twin Dashboard</div>',
    unsafe_allow_html=True
)

st.write("")

# --------------------
# DASHBOARD
# --------------------

if page == "Dashboard":

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Productivity", "88%")
    c2.metric("Focus", "91%")
    c3.metric("Wellness", "85%")
    c4.metric("Burnout Risk", "12%")

    st.divider()

    fig = px.line(
        df,
        x="Date",
        y=["Study", "Sleep", "Mood"],
        title="Life Performance Trends"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:
        fig2 = px.bar(
            df,
            x="Date",
            y="Study",
            title="Study Hours"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    with col2:
        fig3 = px.bar(
            df,
            x="Date",
            y="Sleep",
            title="Sleep Hours"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

# --------------------
# DIGITAL TWIN
# --------------------

elif page == "Digital Twin":

    st.header("Build Your Twin")

    study = st.slider(
        "Study Hours",
        0,
        12,
        6
    )

    sleep = st.slider(
        "Sleep Hours",
        0,
        12,
        8
    )

    exercise = st.slider(
        "Exercise Hours",
        0,
        5,
        1
    )

    mood = st.slider(
        "Mood",
        1,
        10,
        8
    )

    twin_score = (
        study*4 +
        sleep*4 +
        exercise*8 +
        mood*2
    )

    if twin_score > 80:
        status = "Elite"
    elif twin_score > 60:
        status = "Strong"
    else:
        status = "Needs Improvement"

    st.subheader("Twin Score")

    st.progress(twin_score/100)

    st.success(
        f"Score: {twin_score}/100"
    )

    st.info(
        f"Digital Twin Status: {status}"
    )

# --------------------
# PREDICTIONS
# --------------------

elif page == "Predictions":

    st.header("Future Forecast")

    st.success(
        """
        Based on current habits,
        TwinAI predicts a 14% increase
        in productivity over the next week.
        """
    )

    future = pd.DataFrame({
        "Week":[
            "Current",
            "Next"
        ],
        "Productivity":[
            88,
            100
        ]
    })

    fig = px.bar(
        future,
        x="Week",
        y="Productivity"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
