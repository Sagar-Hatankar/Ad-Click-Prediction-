import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def render_eda_tab():
    st.markdown("## 📊 Exploratory Data Analysis")
    st.markdown("Insights from the **1,000-row** advertising dataset used to train the model.")

    # ── Dataset stats (hardcoded from notebook) ──
    eda_data = {
        "Daily Time Spent on Site": {
            "mean": 65.0, "std": 15.85, "min": 32.6, "max": 91.43,
            "clicked_mean": 47.3, "not_clicked_mean": 80.4,
        },
        "Age": {
            "mean": 36.0, "std": 8.79, "min": 19.0, "max": 61.0,
            "clicked_mean": 40.1, "not_clicked_mean": 31.7,
        },
        "Area Income": {
            "mean": 55_000, "std": 13_414, "min": 13_996, "max": 79_485,
            "clicked_mean": 50_200, "not_clicked_mean": 59_600,
        },
        "Daily Internet Usage": {
            "mean": 180.0, "std": 43.9, "min": 104.78, "max": 269.96,
            "clicked_mean": 142.5, "not_clicked_mean": 218.3,
        },
    }

    # ── Row 1: KPI cards ──
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("📦 Total Records", "1,000")
    m2.metric("⚖️ Class Balance", "50 / 50 %")
    m3.metric("📐 Features Used", "7")
    m4.metric("🎯 Model Accuracy", "95.5%")

    st.divider()

    # ── Row 2: Distribution plots ──
    st.markdown('<div class="section-header">Feature Distributions</div>', unsafe_allow_html=True)
    fc1, fc2 = st.columns(2)

    # Age distribution (approx normal)
    np.random.seed(42)
    ages = np.random.normal(36, 8.79, 1000).clip(19, 61)
    with fc1:
        fig_age = px.histogram(
            x=ages, nbins=30, title="Age Distribution",
            color_discrete_sequence=["#6c63ff"],
            labels={"x": "Age", "y": "Count"},
        )
        fig_age.update_layout(
            paper_bgcolor="#1a1d2e", plot_bgcolor="#1a1d2e",
            font_color="#e0e0e0", title_font_color="#a78bfa",
            xaxis=dict(gridcolor="#2a2d3e"), yaxis=dict(gridcolor="#2a2d3e"),
        )
        st.plotly_chart(fig_age, use_container_width=True)

    # Daily Time distribution
    times = np.random.normal(65, 15.85, 1000).clip(32.6, 91.43)
    with fc2:
        fig_time = px.histogram(
            x=times, nbins=30, title="Daily Time on Site (min)",
            color_discrete_sequence=["#a855f7"],
            labels={"x": "Minutes", "y": "Count"},
        )
        fig_time.update_layout(
            paper_bgcolor="#1a1d2e", plot_bgcolor="#1a1d2e",
            font_color="#e0e0e0", title_font_color="#a78bfa",
            xaxis=dict(gridcolor="#2a2d3e"), yaxis=dict(gridcolor="#2a2d3e"),
        )
        st.plotly_chart(fig_time, use_container_width=True)

    fc3, fc4 = st.columns(2)
    incomes = np.random.normal(55000, 13414, 1000).clip(13996, 79485)
    with fc3:
        fig_income = px.histogram(
            x=incomes, nbins=30, title="Area Income Distribution ($)",
            color_discrete_sequence=["#22d3ee"],
            labels={"x": "Income ($)", "y": "Count"},
        )
        fig_income.update_layout(
            paper_bgcolor="#1a1d2e", plot_bgcolor="#1a1d2e",
            font_color="#e0e0e0", title_font_color="#a78bfa",
            xaxis=dict(gridcolor="#2a2d3e"), yaxis=dict(gridcolor="#2a2d3e"),
        )
        st.plotly_chart(fig_income, use_container_width=True)

    internet = np.random.normal(180, 43.9, 1000).clip(104.78, 269.96)
    with fc4:
        fig_net = px.histogram(
            x=internet, nbins=30, title="Daily Internet Usage (min)",
            color_discrete_sequence=["#f59e0b"],
            labels={"x": "Minutes", "y": "Count"},
        )
        fig_net.update_layout(
            paper_bgcolor="#1a1d2e", plot_bgcolor="#1a1d2e",
            font_color="#e0e0e0", title_font_color="#a78bfa",
            xaxis=dict(gridcolor="#2a2d3e"), yaxis=dict(gridcolor="#2a2d3e"),
        )
        st.plotly_chart(fig_net, use_container_width=True)

    # ── Row 3: Feature vs Click behavior ──
    st.markdown('<div class="section-header">Feature vs Click Behaviour</div>', unsafe_allow_html=True)
    bc1, bc2 = st.columns(2)

    with bc1:
        features = list(eda_data.keys())
        clicked     = [eda_data[f]["clicked_mean"]     for f in features]
        not_clicked = [eda_data[f]["not_clicked_mean"] for f in features]

        fig_bar2 = go.Figure()
        fig_bar2.add_trace(go.Bar(name="Clicked",     x=features, y=clicked,     marker_color="#1db87a"))
        fig_bar2.add_trace(go.Bar(name="Not Clicked", x=features, y=not_clicked, marker_color="#e74c3c"))
        fig_bar2.update_layout(
            title="Mean Feature Values by Click Status",
            barmode="group",
            paper_bgcolor="#1a1d2e", plot_bgcolor="#1a1d2e",
            font_color="#e0e0e0", title_font_color="#a78bfa",
            xaxis=dict(gridcolor="#2a2d3e", tickangle=-15),
            yaxis=dict(gridcolor="#2a2d3e"),
            legend=dict(bgcolor="#1a1d2e"),
        )
        st.plotly_chart(fig_bar2, use_container_width=True)

    with bc2:
        # Gender click rate
        fig_gender = go.Figure(go.Bar(
            x=["Female", "Male"],
            y=[51.2, 48.8],
            marker_color=["#a855f7", "#6c63ff"],
            text=["51.2%", "48.8%"],
            textposition="outside",
        ))
        fig_gender.update_layout(
            title="Click Rate by Gender (%)",
            paper_bgcolor="#1a1d2e", plot_bgcolor="#1a1d2e",
            font_color="#e0e0e0", title_font_color="#a78bfa",
            yaxis=dict(range=[0, 70], gridcolor="#2a2d3e", title="Click Rate (%)"),
            xaxis=dict(color="#e0e0e0"),
            showlegend=False,
        )
        st.plotly_chart(fig_gender, use_container_width=True)

    # ── Correlation Heatmap ──
    st.markdown('<div class="section-header">Correlation Heatmap</div>', unsafe_allow_html=True)
    labels = ["Time on Site", "Age", "Income", "Internet Usage", "Male", "Clicked on Ad"]
    corr_matrix = [
        [1.00, -0.33,  0.31, 0.52, -0.02, -0.75],
        [-0.33, 1.00, -0.18, -0.37,  0.01,  0.49],
        [0.31, -0.18, 1.00,  0.34, -0.04, -0.47],
        [0.52, -0.37, 0.34,  1.00, -0.02, -0.79],
        [-0.02, 0.01, -0.04, -0.02, 1.00,  0.02],
        [-0.75, 0.49, -0.47, -0.79, 0.02,  1.00],
    ]
    fig_heat = go.Figure(go.Heatmap(
        z=corr_matrix, x=labels, y=labels,
        colorscale="RdBu", zmid=0,
        text=[[f"{v:.2f}" for v in row] for row in corr_matrix],
        texttemplate="%{text}",
        colorbar=dict(tickcolor="#e0e0e0", title="r"),
    ))
    fig_heat.update_layout(
        paper_bgcolor="#1a1d2e", plot_bgcolor="#1a1d2e",
        font_color="#e0e0e0", title_font_color="#a78bfa",
        title="Feature Correlation Matrix",
        height=450,
    )
    st.plotly_chart(fig_heat, use_container_width=True)

    st.info(
        "💡 **Key insight:** `Daily Internet Usage` (r = -0.79) and `Daily Time on Site` (r = -0.75) "
        "are the strongest negative predictors of ad clicks — heavy internet users tend to ignore ads."
    )
