import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def load_artifacts():
    model  = joblib.load("models/pred_ad_click.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler

def predict(model, scaler, d_time, d_age, d_income, d_net, d_male, d_hour, d_day):
    arr = np.array([[d_time, d_age, d_income, d_net, d_male, d_hour, d_day]])
    scaled = scaler.transform(arr)
    pred   = model.predict(scaled)[0]
    proba  = model.predict_proba(scaled)[0][1]
    return int(pred), float(proba)
