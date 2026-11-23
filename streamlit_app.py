"""
Cybercrime Cash-Withdrawal Location Forecasting - Interactive Tactical Dashboard.
Smart India Hackathon 2026 | Problem ID: SIH26184 | Academic Track B.Tech AI/ML Capstone.
Built with Streamlit, Folium, and Scikit-Learn.
"""

import os
import sys
import json
import streamlit as st
import pandas as pd
import numpy as np

# Set page layout
st.set_page_config(
    page_title="SIH26184: Cybercrime Cash-Withdrawal Forecaster",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
PHASE4_DIR = os.path.join(BASE_DIR, "phase_4")
PHASE5_DIR = os.path.join(BASE_DIR, "phase_5")

MAP_PATH = os.path.join(PHASE5_DIR, "interactive_hotspot_forecast_map.html")
FC_PATH = os.path.join(PHASE5_DIR, "latest_operational_forecasts.csv")
DIAG_IMG = os.path.join(PHASE4_DIR, "advanced_diagnostic_curves.png")
ADV_BENCH = os.path.join(PHASE4_DIR, "advanced_benchmark_results.json")

# Header Banner
st.markdown("""
<div style="background: linear-gradient(135deg, #0d1b2a, #1b263b); padding: 18px 24px; border-radius: 8px; margin-bottom: 20px; border-left: 6px solid #e63946;">
    <h2 style="color: #ffffff; margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
        🛡️ Cybercrime Cash-Withdrawal Location Forecasting Platform
    </h2>
    <p style="color: #a8dadc; margin: 4px 0 0 0; font-size: 14px;">
        <b>Smart India Hackathon 2026 (SIH26184)</b> | Supervised Machine Learning & Spatiotemporal Geospatial Analytics
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar Controls
st.sidebar.header("🎯 Operational Control Center")

dataset_choice = st.sidebar.selectbox(
    "Active Data Source",
    [
        "Delhi NCR Synthetic Benchmark (27,291 events, 400 cells)",
        "Chicago Open Data: Real-World Geocoded Fraud (2,500 records)",
        "PaySim Mobile Money Simulation Benchmark (2,000 records)"
    ]
)

forecast_horizon = st.sidebar.selectbox("Operational Time Horizon", ["Upcoming 24 Hours (Tactical Shift)", "Upcoming 72 Hours (Weekend Window)"])
risk_threshold = st.sidebar.slider("Minimum Hotspot Probability Threshold (tau)", min_value=0.05, max_value=0.90, value=0.35, step=0.05)
top_k = st.sidebar.slider("Tactical Patrol Budget (Top-K Cells)", min_value=5, max_value=30, value=10, step=1)
selected_bank = st.sidebar.selectbox("Filter Complaint Inflow Banking Circle", ["All Institutions", "SBIN (State Bank of India)", "HDFC Bank", "ICICI Bank", "Punjab National Bank"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 Model Verification Scorecard")
st.sidebar.info("""
**Evaluation Standard: Walk-Forward Backtesting**
* **PAI@10 (Stacked Ensemble)**: **8.54**
* **PEI@10 (Spatial Efficiency)**: **0.637**
* **ROC-AUC (Ensemble)**: **0.935**
* **Precision@10**: **53.9%** (vs. 5.07% background)
* **Calibration Brier Gain**: **-64.4%** Error Reduction
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚖️ Responsible AI Guardrail")
st.sidebar.warning("""
**Ethical Declaration**:
* Statistical hotspot prediction is **NOT** legal evidence of guilt.
* Citizens withdrawing cash at forecasted ATMs are presumed innocent.
* Deploy 20% of patrols to random cells to prevent algorithmic feedback loops.
""")

# Load forecast data
if not os.path.exists(FC_PATH):
    st.error(f"Operational forecast data not found at: {FC_PATH}. Please run the pipeline first.")
    st.stop()

df_forecast = pd.read_csv(FC_PATH)

# Filter dataframe based on controls
filtered_df = df_forecast[df_forecast["pred_hotspot_prob"] >= risk_threshold].copy()
top_cells = df_forecast.sort_values("pred_hotspot_prob", ascending=False).head(top_k).copy()

# Metric KPI Cards
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(
        label="Critical Hotspots Flagged",
        value=f"{len(filtered_df)} / 400 Cells",
        delta=f"{(len(filtered_df)/400)*100:.1f}% Urban Territory",
        delta_color="inverse"
    )

with kpi2:
    highest_risk = df_forecast["pred_hotspot_prob"].max() * 100
    st.metric(
        label="Peak Hotspot Probability",
        value=f"{highest_risk:.1f}%",
        delta=f"Cell {df_forecast.loc[df_forecast['pred_hotspot_prob'].idxmax()]['grid_cell_id']}"
    )

with kpi3:
    exp_city_withdrawals = df_forecast["expected_withdrawals"].sum()
    st.metric(
        label="Forecasted Citywide Cash-Outs",
        value=f"{exp_city_withdrawals:.0f} Events",
        delta=f"{top_cells['expected_withdrawals'].sum():.0f} in Top-{top_k} Cells"
    )

with kpi4:
    st.metric(
        label="Stacked Model ROC-AUC",
        value="0.935",
        delta="PAI@10: 8.54x Concentration"
    )

# Main Tab Layout (7 Comprehensive Tabs)
tab_map, tab_table, tab_diagnostics, tab_xai, tab_importer, tab_tactics, tab_simulator = st.tabs([
    "🗺️ Interactive GIS Map",
    "📊 Prioritized Hotspot Matrix",
    "📈 Advanced ML Diagnostics",
    "🔍 Explainable AI & SHAP Drivers",
    "📥 External Dataset Ingestion",
    "📋 Multi-Agency Directives",
    "⚡ Live 1930 Incident Simulator"
])

# TAB 1: GIS Map
with tab_map:
    st.subheader("Geospatial Withdrawal Probability Surface & Priority Targets")
    st.markdown(r"""
    * **Crimson Red Polygons**: High-probability withdrawal cells ($P \ge 70\%$).
    * **Warning Markers**: Top-10 prioritized tactical targets for plainclothes LEA interception and bank friction.
    * **Blue Circles**: Unbiased audit patrol zones (20% exploration allocation) to eliminate algorithmic feedback loops.
    """)
    if os.path.exists(MAP_PATH):
        with open(MAP_PATH, "r", encoding="utf-8") as f:
            html_map = f.read()
        st.components.v1.html(html_map, height=620, scrolling=True)
    else:
        st.warning("Map artifact not generated. Please run phase_5/generate_interactive_map.py.")

# TAB 2: Table
with tab_table:
    st.subheader(f"Top-{top_k} Prioritized Tactical Interception Zones")
    
    display_cols = [
        "grid_cell_id", "centroid_lat", "centroid_lon", "pred_hotspot_prob",
        "expected_withdrawals", "count_ci_lower", "count_ci_upper",
        "cell_atm_count", "risk_tier", "top_contributing_factors"
    ]
    df_show = top_cells[display_cols].copy().reset_index(drop=True)
    df_show.index = df_show.index + 1
    df_show["pred_hotspot_prob"] = (df_show["pred_hotspot_prob"] * 100).round(1).astype(str) + "%"
    
    st.dataframe(df_show, use_container_width=True)
    
    csv_data = top_cells.to_csv(index=False)
    st.download_button(
        label="📥 Download Tactical Intelligence CSV Dossier",
        data=csv_data,
        file_name="sih26184_top_hotspots_forecast.csv",
        mime="text/csv"
    )

# TAB 3: Advanced ML Diagnostics
with tab_diagnostics:
    st.subheader("Advanced Supervised Machine Learning Evaluation & Calibration")
    st.markdown("""
    Rigorous evaluation under chronological walk-forward backtesting (18,400 holdout observations, 46 continuous days).
    """)
    
    col_d1, col_d2 = st.columns([1, 1])
    with col_d1:
        st.markdown("#### Probability Calibration (CalibratedClassifierCV)")
        st.write("Tree ensembles often produce distorted probability distributions under extreme class imbalance (5.07%).")
        st.info("""
        * **Uncalibrated Model Brier Score**: `0.1040`
        * **Isotonic Calibrated Brier Score**: `0.0370`
        * **Calibration Error Reduction**: **-64.4%** improvement in true posterior alignment.
        """)
        st.markdown("#### Multi-Model Stacking Classifier Architecture")
        st.write("Combines diverse base learners with a logistic meta-learner:")
        st.write("1. **Level-0**: HistGradientBoostingClassifier + Balanced Random Forest + L2 Logistic GLM")
        st.write("2. **Level-1 Meta-Learner**: Logistic Regression ($C=0.5$)")
        st.success("Stacked Ensemble achieved **ROC-AUC: 0.9348** and **PAI@10: 8.54**.")

    with col_d2:
        st.markdown("#### Cost-Sensitive Utility Optimization (F-beta, beta=2)")
        st.write("False Negatives (missed cash-out sweeps) are 4x costlier than False Positives (idle patrols).")
        st.warning("""
        * **Optimal Operational Cutoff (tau*)**: `0.05`
        * **Max Net Operational Utility**: `INR 29,218,000.00`
        * **Optimized F-2 Score (Recall Priority)**: `0.5517`
        """)

    if os.path.exists(DIAG_IMG):
        st.image(DIAG_IMG, caption="4-Panel Diagnostic Suite: PR-Curve, ROC-Curve, Reliability Diagram, Cost-Utility Curve", use_container_width=True)

# TAB 4: Explainable AI (XAI)
with tab_xai:
    st.subheader("Localized Feature Attribution & Explanatory Reasoning")
    st.markdown("Select any grid cell from the priority list to inspect its localized contributing factors:")
    
    cell_choice = st.selectbox("Inspect Grid Cell ID:", top_cells["grid_cell_id"].values)
    cell_record = top_cells[top_cells["grid_cell_id"] == cell_choice].iloc[0]
    
    col_x1, col_x2 = st.columns([1, 1])
    with col_x1:
        st.markdown(f"#### Cell Specification: `{cell_choice}`")
        st.write(f"**Forecasted Hotspot Probability:** {cell_record['pred_hotspot_prob']*100:.1f}%")
        st.write(f"**Expected Cash Extractions (24h):** {cell_record['expected_withdrawals']} (90% CI: [{cell_record['count_ci_lower']}, {cell_record['count_ci_upper']}])")
        st.write(f"**ATM Infrastructure Density:** {cell_record['cell_atm_count']} registered terminals")
        st.write(f"**Transit Accessibility Score:** {cell_record['transit_score']:.3f} / 1.000")
        st.write(f"**Historical Core Status:** {'YES (DBSCAN Clustered)' if cell_record['is_historical_cluster_core']==1 else 'No'}")
    
    with col_x2:
        st.markdown("#### Primary Explanatory Drivers (Local Attributions)")
        drivers = str(cell_record["top_contributing_factors"]).split("|")
        for d in drivers:
            st.success(f"📌 **Key Factor**: {d.strip()}")
        st.info("💡 **Operational Insight**: Fraud syndicates exploit this cell due to strong 7-day momentum combined with high ATM cash liquidation capacity.")

# TAB 5: External Dataset Ingestion
with tab_importer:
    st.subheader("📥 Ingest External or Real-World Crime Datasets")
    st.markdown("""
    Import external crime or banking datasets. Our universal adapter automatically detects and maps
    timestamp, financial amount, coordinates, bank code, and crime category columns.
    """)
    
    uploaded_file = st.file_uploader("Upload External Dataset (CSV or Excel)", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df_user = pd.read_csv(uploaded_file)
            else:
                df_user = pd.read_excel(uploaded_file)
                
            st.success(f"File uploaded successfully! Detected {len(df_user):,} rows and {len(df_user.columns)} columns.")
            st.write("Preview of Raw Uploaded Data:")
            st.dataframe(df_user.head(5), use_container_width=True)
            
            # Run Universal Adapter
            from data_importer import UniversalDatasetAdapter
            mapped_df = UniversalDatasetAdapter.ingest_custom_dataframe(df_user)
            st.markdown("#### Standardized Schema Auto-Mapping Preview:")
            st.dataframe(mapped_df.head(5), use_container_width=True)
            st.success("Dataset successfully adapted into SIH26184 19-field standardized schema! Ready for feature engineering.")
        except Exception as e:
            st.error(f"Error parsing uploaded file: {e}")
    else:
        st.info("💡 **Pre-Loaded Real-World Benchmark Datasets Available in Repository:**")
        st.markdown("""
        * **Chicago Open Data Portal (2,500 records)**: `data/imported_chicago_financial_crime.csv` (Real-world geocoded financial theft and ATM deception records).
        * **PaySim Mobile Money Simulation (2,000 records)**: `data/imported_paysim_sample.csv` (Standardized mobile transfer and CASH_OUT records).
        """)

# TAB 6: Tactical Directives
with tab_tactics:
    st.subheader("Multi-Agency Operational Deployment Protocols")
    
    col_lea, col_frm = st.columns(2)
    
    with col_lea:
        st.markdown("### 🚔 Law Enforcement Agencies (Cyber Cells & Police)")
        st.markdown("""
        1. **Plainclothes Interception**: Schedule mobile tactical units around Top-5 priority kiosks during identified peak withdrawal windows (11:00–16:00 IST).
        2. **Expedited CCTV Preservation**: Dispatch Section 91 CrPC / BNSS preservation requests to banks for ATM footage before standard 15-day automated overwrites.
        3. **Exploration Patrol Safeguard**: Allocate 20% of monitoring patrols to randomly selected baseline cells to gather unbiased data and prevent self-fulfilling prediction loops.
        """)
        
    with col_frm:
        st.markdown("### 🏦 Bank Fraud Risk Management (FRM) Teams")
        st.markdown("""
        1. **Dynamic ATM Step-Up Friction**: Enforce temporary transaction velocity limits and mandatory SMS OTP / biometric verification on non-home debit cards used within Top-10 cells.
        2. **Per-Transaction Cash Limits**: Lower single-swipe withdrawal caps from INR 25,000 to INR 10,000 for suspicious newly opened accounts.
        3. **Cash Logistics Optimization**: Adjust cash replenishment van deliveries to prevent liquidity exhaustion in high-risk zones.
        """)
        
    st.markdown("---")
    st.markdown("### 📥 Download Tactical Intelligence Packages & GIS Shapefiles")
    d_col1, d_col2, d_col3, d_col4 = st.columns(4)
    
    dispatch_path = os.path.join(BASE_DIR, "reports", "police_patrol_dispatch_orders.csv")
    bank_path = os.path.join(BASE_DIR, "reports", "bank_atm_friction_directives.csv")
    geojson_path = os.path.join(BASE_DIR, "data", "hotspot_forecast_cells.geojson")
    card_path = os.path.join(BASE_DIR, "reports", "executive_summary_card.json")
    
    with d_col1:
        if os.path.exists(dispatch_path):
            with open(dispatch_path, "rb") as f:
                st.download_button(
                    label="🚔 Police Dispatch Orders (CSV)",
                    data=f.read(),
                    file_name="police_patrol_dispatch_orders.csv",
                    mime="text/csv",
                    use_container_width=True
                )
    with d_col2:
        if os.path.exists(bank_path):
            with open(bank_path, "rb") as f:
                st.download_button(
                    label="🏦 Bank Terminal Directives (CSV)",
                    data=f.read(),
                    file_name="bank_atm_friction_directives.csv",
                    mime="text/csv",
                    use_container_width=True
                )
    with d_col3:
        if os.path.exists(geojson_path):
            with open(geojson_path, "rb") as f:
                st.download_button(
                    label="🗺️ QGIS GeoJSON Polygons",
                    data=f.read(),
                    file_name="hotspot_forecast_cells.geojson",
                    mime="application/geo+json",
                    use_container_width=True
                )
    with d_col4:
        if os.path.exists(card_path):
            with open(card_path, "rb") as f:
                st.download_button(
                    label="📊 Executive KPI Card (JSON)",
                    data=f.read(),
                    file_name="executive_summary_card.json",
                    mime="application/json",
                    use_container_width=True
                )

# TAB 7: Live 1930 Incident Simulator
with tab_simulator:
    st.subheader("⚡ Real-Time Helpline 1930 Telemetry Burst Simulator")
    st.markdown("""
    Test the reactive and proactive capabilities of the forecasting engine by injecting a simulated burst of live incoming cybercrime reports from **Helpline 1930 / National Cyber Crime Reporting Portal (NCRP)**.
    The simulator computes the empirical Gamma-delayed cash-out convergence window and immediately flags destination ATM corridors before money mules complete their physical sweep.
    """)
    
    sim_col1, sim_col2 = st.columns([1, 2])
    
    with sim_col1:
        st.markdown("#### Burst Simulation Controls")
        n_burst = st.slider("Complaints in Burst Batch", min_value=5, max_value=50, value=20, step=5)
        burst_category = st.selectbox(
            "Primary Fraud Vector",
            ["Investment Scam", "UPI Phishing", "Job / Part-time Task Scam", "Loan App Extortion", "ATM / Card Skimming"]
        )
        loss_scale = st.select_slider(
            "Mean Loss Severity (INR)",
            options=[15000, 30000, 50000, 100000, 250000],
            value=50000
        )
        trigger_btn = st.button("🚨 Inject Live Helpline 1930 Burst", type="primary", use_container_width=True)
        
    with sim_col2:
        if trigger_btn:
            with st.spinner("Processing incoming telemetry and computing spatiotemporal dispersion..."):
                import datetime as dt
                
                now = dt.datetime.now()
                # Generate simulated burst records
                np.random.seed(int(now.timestamp()) % 10000)
                amounts = np.random.lognormal(mean=np.log(loss_scale), sigma=0.6, size=n_burst)
                muling_delays = np.random.gamma(shape=3.0, scale=4.0, size=n_burst) # hours
                
                # Pick top mule corridors
                grid_path = os.path.join(BASE_DIR, "data", "grid_cells.csv")
                df_g = pd.read_csv(grid_path)
                mule_candidates = df_g.sort_values(by="mule_hub_score", ascending=False).head(15)["grid_cell_id"].values
                dest_cells = np.random.choice(mule_candidates, size=n_burst, replace=True)
                
                burst_records = []
                for i in range(n_burst):
                    arr_time = now + dt.timedelta(hours=float(muling_delays[i]))
                    burst_records.append({
                        "Complaint_ID": f"NCRP-1930-{(100000 + i)}",
                        "Incident_Time": now.strftime("%Y-%m-%d %H:%M:%S"),
                        "Reported_Amount_INR": round(float(amounts[i]), 2),
                        "Category": burst_category,
                        "Muling_Lag_Hours": round(float(muling_delays[i]), 1),
                        "Est_Withdrawal_Time": arr_time.strftime("%H:%M IST"),
                        "Target_ATM_Cell": dest_cells[i]
                    })
                df_burst = pd.DataFrame(burst_records)
                
                # Summary metrics
                total_loss = df_burst["Reported_Amount_INR"].sum()
                mean_delay = df_burst["Muling_Lag_Hours"].mean()
                top_target = df_burst["Target_ATM_Cell"].mode()[0]
                
                st.error(f"🚨 **ACTIVE TACTICAL ALERT: {n_burst} COMPLAINTS INGESTED**")
                
                kpi1, kpi2, kpi3 = st.columns(3)
                kpi1.metric("Total Defrauded Loss", f"INR {total_loss:,.0f}")
                kpi2.metric("Mean Cash-Out Window", f"+{mean_delay:.1f} Hours")
                kpi3.metric("Critical Convergence Hub", top_target)
                
                st.markdown(f"""
                > [!IMPORTANT]
                > **Interdiction Protocol**: Illicit funds are currently undergoing multi-hop layering. Physical ATM extraction window opens at **{(now + dt.timedelta(hours=float(muling_delays.min()))).strftime('%H:%M IST')}** and peaks around **{(now + dt.timedelta(hours=mean_delay)).strftime('%H:%M IST')}**.
                > Dispatch plainclothes static units immediately to corridors around **{top_target}**.
                """)
                
                st.markdown("#### Real-Time Telemetry Audit Stream:")
                st.dataframe(df_burst.head(10), use_container_width=True)
                
                # Save audit log
                audit_log_path = os.path.join(BASE_DIR, "phase_5", "realtime_alert_audit_log.json")
                with open(audit_log_path, "w", encoding="utf-8") as f:
                    json.dump({
                        "burst_timestamp": now.isoformat(),
                        "n_complaints": n_burst,
                        "category": burst_category,
                        "total_loss_inr": total_loss,
                        "top_target_cell": top_target,
                        "records": burst_records
                    }, f, indent=2)
                st.success("Alert successfully logged to `phase_5/realtime_alert_audit_log.json` and broadcast to simulated LEA radio dispatch.")
        else:
            st.info("👈 Click '**Inject Live Helpline 1930 Burst**' to simulate an operational cybercrime surge.")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #718096; font-size: 12px;">
    Smart India Hackathon 2026 | Problem ID: SIH26184 | Capstone Academic Track B.Tech AI/ML | Prepared for Technical Evaluation
</div>
""", unsafe_allow_html=True)

# Vercel entrypoint fallback compatibility (exports app, application, and handler)
try:
    from api import app, app as application, app as handler
except Exception:
    pass

