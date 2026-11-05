
import os
import joblib
import pandas as pd
import streamlit as st

FEATURES = ["pclass", "sex", "age", "fare"]

st.set_page_config(
    page_title="Titanic AI | Survival Predictor",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --navy: #071827;
    --teal: #18b6a4;
    --gold: #e6bd70;
    --muted: #9fb1c4;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 5%, rgba(20,126,145,.20), transparent 38%),
        radial-gradient(ellipse at 95% 25%, rgba(230,189,112,.10), transparent 32%),
        linear-gradient(135deg, #071827 0%, #0b2032 55%, #102d40 100%);
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"],
#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 34px 36px;
    margin-bottom: 25px;
    border: 1px solid rgba(255,255,255,.13);
    border-radius: 25px;
    background: linear-gradient(115deg,
        rgba(17,64,83,.92), rgba(11,35,55,.96) 58%,
        rgba(20,79,83,.85));
    box-shadow: 0 18px 55px rgba(0,0,0,.20);
}

.hero:after {
    content: "🚢";
    position: absolute;
    right: 38px;
    top: 20px;
    font-size: 95px;
    opacity: .17;
    transform: rotate(-8deg);
}

.eyebrow {
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 11px;
    font-weight: 700;
    margin-bottom: 12px;
}

.hero h1 {
    color: #f5f8fb;
    font-family: 'Playfair Display', serif;
    font-size: clamp(30px, 4vw, 47px);
    line-height: 1.15;
    margin: 0 0 12px 0;
}

.hero p {
    color: #bdcedb;
    font-size: 15px;
    max-width: 620px;
    line-height: 1.8;
    margin: 0;
}

.pill {
    display: inline-block;
    margin-top: 20px;
    padding: 7px 13px;
    border-radius: 30px;
    background: rgba(24,182,164,.12);
    border: 1px solid rgba(24,182,164,.35);
    color: #73e4d4;
    font-size: 12px;
    font-weight: 600;
}

.section-heading {
    color: #f1f6fb;
    font-size: 22px;
    font-weight: 700;
    margin: 8px 0 4px 0;
}

.section-sub {
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 20px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(14,38,56,.78);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 20px;
    box-shadow: 0 12px 35px rgba(0,0,0,.12);
}

div[data-testid="stWidgetLabel"] p,
.stSelectbox label, .stSlider label, .stRadio label {
    color: #d8e5ee !important;
    font-weight: 600 !important;
}

div[data-baseweb="select"] > div {
    background: #102b40;
    border: 1px solid #345165;
    border-radius: 10px;
    color: white;
}

div[role="radiogroup"] label {
    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.11);
    border-radius: 10px;
    padding: 9px 13px;
    margin-right: 8px;
}

.stSlider [data-baseweb="slider"] {
    padding-top: 8px;
}

.stButton > button {
    width: 100%;
    min-height: 49px;
    border: none;
    border-radius: 12px;
    background: linear-gradient(100deg, #16b8a4, #168d9d);
    color: #061b28;
    font-size: 15px;
    font-weight: 800;
    box-shadow: 0 7px 22px rgba(22,184,164,.20);
    transition: all .2s ease;
}

.stButton > button:hover {
    color: #061b28;
    border: none;
    transform: translateY(-2px);
    box-shadow: 0 11px 28px rgba(22,184,164,.34);
}

.result-card {
    padding: 27px;
    border: 1px solid rgba(230,189,112,.28);
    border-radius: 19px;
    background: linear-gradient(145deg,
        rgba(27,67,79,.92), rgba(14,39,57,.96));
    margin-top: 14px;
}

.result-label {
    color: #a9c0ce;
    text-transform: uppercase;
    letter-spacing: 1.7px;
    font-size: 11px;
    font-weight: 700;
}

.result-number {
    color: #f2d28f;
    font-size: clamp(37px, 4vw, 54px);
    font-weight: 800;
    line-height: 1.3;
    margin: 8px 0;
}

.result-note {
    color: #c5d5df;
    font-size: 13px;
    line-height: 1.7;
}

.info-card {
    padding: 16px;
    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.09);
    border-radius: 14px;
    margin-top: 12px;
}

.info-label {
    color: #9fb5c5;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.info-value {
    color: #f2f7fa;
    font-size: 21px;
    font-weight: 700;
    margin-top: 5px;
}

.footer-note {
    text-align: center;
    color: #8ca3b5;
    font-size: 12px;
    padding: 24px 0 5px;
    line-height: 1.8;
}

hr {
    border-color: rgba(255,255,255,.10);
}

@media (max-width: 700px) {
    .block-container {
        padding: 1rem .8rem 2rem;
    }
    .hero {
        padding: 25px 21px;
    }
    .hero:after {
        right: 12px;
        top: 15px;
        font-size: 55px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">Machine Learning · Interactive Demo</div>
    <h1>Titanic Survival<br>Predictor</h1>
    <p>
        A journey into the past, powered by machine learning.
        Explore how passenger characteristics influence a model's
        estimated survival probability.
    </p>
    <div class="pill">✦ DECISION TREE CLASSIFIER &nbsp; · &nbsp; LIVE PREDICTION</div>
</div>
""", unsafe_allow_html=True)


# ---------------- MAIN LAYOUT ----------------
left, right = st.columns([1.08, 0.92], gap="large")

with left:
    st.markdown('<div class="section-heading">⚓ Passenger Profile</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Customize the passenger details below.</div>',
                unsafe_allow_html=True)

    with st.container(border=True):
        pclass = st.selectbox(
            "🎟️ Ticket class",
            [1, 2, 3],
            format_func=lambda x: {
                1: "1st Class — Premium",
                2: "2nd Class — Standard",
                3: "3rd Class — Economy"
            }[x]
        )

        sex = st.radio(
            "👤 Passenger sex",
            ["Female", "Male"],
            horizontal=True
        )

        age = st.slider("🎂 Passenger age", 1, 80, 30)
        fare = st.slider("💳 Ticket fare (£)", 0, 500, 30)

        st.markdown("---")
        predict_clicked = st.button(
            "✦  ANALYZE SURVIVAL PROBABILITY",
            type="primary",
            use_container_width=True
        )

with right:
    st.markdown('<div class="section-heading">📊 Prediction Insights</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Your model-generated estimate.</div>',
                unsafe_allow_html=True)

    if predict_clicked:
        if not os.path.exists("model.joblib"):
            st.error(
                "Model file not found. Place model.joblib beside app.py."
            )
        else:
            try:
                @st.cache_resource
                def load_model():
                    return joblib.load("model.joblib")

                model = load_model()

                passenger = pd.DataFrame(
                    [[pclass, 1 if sex == "Female" else 0, age, fare]],
                    columns=FEATURES
                )

                probabilities = model.predict_proba(passenger)[0]
                classes = list(model.classes_)
                chance = float(probabilities[classes.index(1)])

                st.markdown(f"""
                <div class="result-card">
                    <div class="result-label">Estimated survival probability</div>
                    <div class="result-number">{chance:.1%}</div>
                    <div class="result-note">
                        Based on the passenger details and patterns learned
                        from the historical Titanic dataset.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.progress(chance, text="Survival probability")

                if chance >= 0.5:
                    st.success("The model estimates survival is more likely.")
                else:
                    st.warning("The model estimates survival is less likely.")

                st.markdown(f"""
                <div class="info-card">
                    <div class="info-label">Passenger summary</div>
                    <div class="info-value">
                        {"Female" if sex == "Female" else "Male"} · Age {age}
                    </div>
                    <div class="result-note">
                        Ticket class: {pclass} &nbsp; | &nbsp;
                        Fare: £{fare}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            except Exception:
                st.error(
                    "We couldn't generate a prediction. "
                    "Please check that model.joblib is valid."
                )
    else:
        st.markdown("""
        <div class="result-card">
            <div class="result-label">Ready for analysis</div>
            <div style="font-size:46px;margin:12px 0;">🌊</div>
            <div style="color:#f2f7fa;font-size:21px;font-weight:700;">
                Your journey starts here
            </div>
            <p class="result-note">
                Select passenger details and press the analyze button
                to reveal the model's estimated survival probability.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
            <div class="info-label">Model information</div>
            <div class="info-value">Decision Tree</div>
            <div class="result-note">
                Four input features · Historical passenger data
            </div>
        </div>
        """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer-note">
    🚢 TITANIC AI LAB<br>
    An educational machine learning project by Shreya Kumari<br>
    Predictions are estimates from historical data, not guarantees
    or real-world advice.
</div>
""", unsafe_allow_html=True)
