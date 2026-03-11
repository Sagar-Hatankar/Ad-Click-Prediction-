import streamlit as st
import pandas as pd
import plotly.express as px

def render_bulk_predict_tab(model, scaler):
    st.markdown("## 📁 Bulk Prediction")
    st.markdown("Upload a **CSV file** with user data and get click predictions for all rows at once.")

    with st.expander("📋 Required CSV Format", expanded=False):
        sample = pd.DataFrame({
            "Daily Time Spent on Site": [68.95, 45.0],
            "Age": [35, 42],
            "Area Income": [61833.90, 50000.0],
            "Daily Internet Usage": [256.09, 140.0],
            "Male": [0, 1],
            "Hour": [10, 14],
            "Day": [3, 15],
        })
        st.dataframe(sample, hide_index=True)
        # Download sample CSV
        csv_sample = sample.to_csv(index=False).encode()
        st.download_button(
            "⬇️ Download Sample CSV",
            csv_sample,
            "sample_input.csv",
            "text/csv",
        )

    uploaded = st.file_uploader(
        "Drop your CSV here", type=["csv"], label_visibility="collapsed"
    )

    if uploaded is not None:
        try:
            df_up = pd.read_csv(uploaded)
            required_cols = [
                "Daily Time Spent on Site", "Age", "Area Income",
                "Daily Internet Usage", "Male", "Hour", "Day"
            ]
            missing = [c for c in required_cols if c not in df_up.columns]
            if missing:
                st.error(f"❌ Missing columns: {', '.join(missing)}")
            else:
                X_up = df_up[required_cols].values
                X_scaled = scaler.transform(X_up)
                preds  = model.predict(X_scaled)
                probas = model.predict_proba(X_scaled)[:, 1]

                df_up["Click Probability (%)"] = (probas * 100).round(1)
                df_up["Prediction"] = ["✅ Click" if p == 1 else "❌ No Click" for p in preds]

                st.markdown('<div class="section-header">Prediction Results</div>', unsafe_allow_html=True)

                # Summary metrics
                n_click = int(preds.sum())
                n_total = len(preds)
                r1, r2, r3 = st.columns(3)
                r1.metric("Total Records", n_total)
                r2.metric("Predicted Clicks",    n_click,          f"{n_click/n_total*100:.1f}%")
                r3.metric("Predicted No-Clicks", n_total - n_click, f"{(n_total-n_click)/n_total*100:.1f}%")

                st.dataframe(df_up, use_container_width=True, hide_index=True)

                # Download results
                out_csv = df_up.to_csv(index=False).encode()
                st.download_button(
                    "⬇️ Download Results CSV",
                    out_csv,
                    "predictions.csv",
                    "text/csv",
                    use_container_width=True,
                )

                # Distribution pie chart
                fig_pie = px.pie(
                    names=["Will Click", "Won't Click"],
                    values=[n_click, n_total - n_click],
                    color_discrete_sequence=["#1db87a", "#e74c3c"],
                    title="Predicted Click Distribution",
                )
                fig_pie.update_layout(
                    paper_bgcolor="#1a1d2e",
                    font_color="#e0e0e0",
                    title_font_color="#a78bfa",
                )
                st.plotly_chart(fig_pie, use_container_width=True)

        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.info("👆 Upload a CSV to get started. Use the **sample CSV** above as a template.")
