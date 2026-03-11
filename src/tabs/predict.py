import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from src.utils import predict

def render_predict_tab(model, scaler, daily_time, age, area_income, daily_internet, male, hour, day):
    st.markdown("## 🏠 Ad Click Predictor")
    st.markdown("Adjust the user profile in the **sidebar**, then click **Predict**.")

    col_btn, _ = st.columns([1, 2])
    with col_btn:
        predict_btn = st.button("🔍 Predict Ad Click", use_container_width=True)

    if predict_btn:
        pred, proba = predict(
            model, scaler, daily_time, age, area_income, daily_internet, male, hour, day
        )

        # ── Result card ──
        if pred == 1:
            st.markdown(
                f'<div class="result-card-click">'
                f'<p class="result-title">✅ Will Click!</p>'
                f'<p class="result-sub">This user is <b>likely to click</b> the advertisement.</p>'
                f'</div>', unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="result-card-noclick">'
                f'<p class="result-title">❌ Won\'t Click</p>'
                f'<p class="result-sub">This user is <b>unlikely to click</b> the advertisement.</p>'
                f'</div>', unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Gauges ──
        c1, c2 = st.columns(2)
        with c1:
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=round(proba * 100, 1),
                title={"text": "Click Probability (%)", "font": {"color": "#a78bfa"}},
                gauge={
                    "axis": {"range": [0, 100], "tickcolor": "#555"},
                    "bar":  {"color": "#6c63ff"},
                    "steps": [
                        {"range": [0, 40], "color": "#2d1f3d"},
                        {"range": [40, 70], "color": "#3b3070"},
                        {"range": [70, 100], "color": "#4a3f8a"},
                    ],
                    "threshold": {
                        "line": {"color": "#a855f7", "width": 3},
                        "thickness": 0.75,
                        "value": 50,
                    },
                },
                number={"suffix": "%", "font": {"color": "#e0e0e0"}},
            ))
            fig_gauge.update_layout(
                paper_bgcolor="#1a1d2e", font_color="#e0e0e0",
                height=280, margin=dict(t=40, b=10, l=20, r=20)
            )
            st.plotly_chart(fig_gauge, use_container_width=True)

        with c2:
            # Probability bar chart (click vs no-click)
            fig_bar = go.Figure(go.Bar(
                x=["Won't Click", "Will Click"],
                y=[round((1 - proba) * 100, 1), round(proba * 100, 1)],
                marker_color=["#e74c3c", "#1db87a"],
                text=[f"{(1-proba)*100:.1f}%", f"{proba*100:.1f}%"],
                textposition="outside",
            ))
            fig_bar.update_layout(
                title="Probability Breakdown",
                paper_bgcolor="#1a1d2e", plot_bgcolor="#1a1d2e",
                font_color="#e0e0e0",
                yaxis=dict(range=[0, 110], title="Probability (%)", gridcolor="#2a2d3e"),
                xaxis=dict(color="#e0e0e0"),
                height=280, margin=dict(t=50, b=10, l=10, r=10),
                showlegend=False,
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        # ── Save to history ──
        gender = "Male" if male == 1 else "Female"
        st.session_state.history.append({
            "Time on Site": daily_time,
            "Age": age,
            "Income ($)": area_income,
            "Internet Usage": daily_internet,
            "Gender": gender,
            "Hour": hour,
            "Day": day,
            "Click Prob (%)": f"{proba*100:.1f}%",
            "Prediction": "✅ Click" if pred == 1 else "❌ No Click",
        })

    # ── Prediction History ──
    if st.session_state.history:
        st.markdown('<div class="section-header">📋 Session Prediction History</div>', unsafe_allow_html=True)
        hist_df = pd.DataFrame(st.session_state.history)
        st.dataframe(hist_df, use_container_width=True, hide_index=True)
        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.rerun()
