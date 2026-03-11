import streamlit as st

def set_page_config():
    """Sets initial config and custom dark theme."""
    st.set_page_config(
        page_title="Ad Click Prediction Dashboard",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown("""
    <style>
        /* ── Base ── */
        .stApp { background: #0f1117; color: #e0e0e0; }

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background: linear-gradient(160deg, #1a1d2e 0%, #12141f 100%);
            border-right: 1px solid #2a2d3e;
        }

        /* ── Tabs ── */
        .stTabs [data-baseweb="tab-list"] {
            background: #1a1d2e;
            border-radius: 12px;
            padding: 4px;
            gap: 4px;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px;
            color: #9da3b4;
            font-weight: 600;
            font-size: 0.9rem;
            padding: 8px 20px;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #6c63ff, #a855f7) !important;
            color: white !important;
        }

        /* ── Metric cards ── */
        [data-testid="metric-container"] {
            background: #1a1d2e;
            border: 1px solid #2a2d3e;
            border-radius: 12px;
            padding: 16px;
        }

        /* ── Buttons ── */
        .stButton > button {
            background: linear-gradient(135deg, #6c63ff, #a855f7);
            color: white;
            border: none;
            border-radius: 10px;
            font-weight: 700;
            font-size: 1rem;
            padding: 10px 30px;
            transition: all 0.3s ease;
            width: 100%;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(108, 99, 255, 0.4);
        }

        /* ── Result cards ── */
        .result-card-click {
            background: linear-gradient(135deg, #0d3d2e, #0f5c40);
            border: 1px solid #1db87a;
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            margin-top: 10px;
        }
        .result-card-noclick {
            background: linear-gradient(135deg, #3d0d0d, #5c1010);
            border: 1px solid #e74c3c;
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            margin-top: 10px;
        }
        .result-title { font-size: 2rem; font-weight: 800; margin: 0; }
        .result-sub   { font-size: 1rem; color: #b0b8c1; margin-top: 6px; }

        /* ── Section header ── */
        .section-header {
            font-size: 1.4rem;
            font-weight: 700;
            color: #a78bfa;
            border-left: 4px solid #6c63ff;
            padding-left: 12px;
            margin: 24px 0 12px;
        }

        /* ── Divider ── */
        hr { border-color: #2a2d3e; }

        /* ── Upload box ── */
        [data-testid="stFileUploader"] {
            background: #1a1d2e;
            border: 2px dashed #3a3d4e;
            border-radius: 12px;
        }
    </style>
    """, unsafe_allow_html=True)
