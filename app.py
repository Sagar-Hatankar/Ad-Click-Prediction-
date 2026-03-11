import streamlit as st
from src.ui import set_page_config
from src.utils import load_artifacts

# Import Tab Modules
from src.tabs.predict import render_predict_tab
from src.tabs.eda import render_eda_tab
from src.tabs.performance import render_performance_tab
from src.tabs.bulk_predict import render_bulk_predict_tab

# ──────────────────────────────────────────────
#  INITIALIZATION
# ──────────────────────────────────────────────
set_page_config()

# Load Model & Scaler
model, scaler = load_artifacts()

# Session State for prediction history
if "history" not in st.session_state:
    st.session_state.history = []

# ──────────────────────────────────────────────
#  SIDEBAR — Shared Inputs
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎯 Ad Click Predictor")
    st.markdown("*Logistic Regression · 95.5% Accuracy*")
    st.divider()
    st.markdown("### 👤 User Profile")

    daily_time = st.slider(
        "Daily Time on Site (min)", 0.0, 300.0, 65.0, step=0.5,
        help="Average minutes user spends on the website per day"
    )
    age = st.slider("Age", 10, 80, 32)
    area_income = st.slider(
        "Area Income ($)", 10_000, 100_000, 52_000, step=500
    )
    daily_internet = st.slider(
        "Daily Internet Usage (min)", 0.0, 500.0, 180.0, step=0.5
    )
    gender = st.radio("Gender", ["Female", "Male"], horizontal=True)
    male = 1 if gender == "Male" else 0

    st.divider()
    st.markdown("### 🕐 Timing")
    hour = st.slider("Hour of Day", 0, 23, 14)
    day  = st.slider("Day of Month", 1, 31, 15)

    st.divider()
    st.markdown(
        "<div style='text-align:center; color:#6b7280; font-size:0.8rem'>"
        "Built with ❤️ using Streamlit</div>",
        unsafe_allow_html=True,
    )

# ──────────────────────────────────────────────
#  MAIN TABS RENDERING
# ──────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "🏠  Predict",
    "📊  EDA Dashboard",
    "🎯  Model Performance",
    "📁  Bulk Predict",
])

with tab1:
    render_predict_tab(
        model, scaler,
        daily_time, age, area_income, daily_internet, male, hour, day
    )

with tab2:
    render_eda_tab()

with tab3:
    render_performance_tab()

with tab4:
    render_bulk_predict_tab(model, scaler)
