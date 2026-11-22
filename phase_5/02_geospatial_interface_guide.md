# Phase 5: Geospatial Visualization & Tactical Interface Guide
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. GIS Interface Architecture

Phase 5 delivers a dual-modality visualization and command suite:
1. **Standalone Interactive GIS Choropleth (`interactive_hotspot_forecast_map.html`)**: Lightweight, self-contained Folium HTML map suitable for deployment in dispatch rooms, mobile command units, or offline forensic laptops.
2. **Interactive Streamlit Command Dashboard (`app.py`)**: Full-featured web interface featuring real-time risk filtering, KPI metric scorecards, localized SHAP driver exploration, and CSV intelligence exports.

---

## 2. Interactive Map Layer Breakdown

The interactive map is partitioned into three functional operational layers controlled via the top-right Layer Control:

```
+----------------------------------------------------------------------------------------------------+
|                                    INTERACTIVE MAP LAYER ARCHITECTURE                              |
+----------------------------------------------------------------------------------------------------+
|  Layer 1: Probability Choropleth  --> All 400 planar cells shaded from gray (low) to crimson (high)|
|  Layer 2: Top-10 Tactical Targets --> Red warning markers with popups detailing XAI drivers & TTPs |
|  Layer 3: Unbiased Audit Zones    --> Blue circle markers designating 20% exploration patrol zones |
+----------------------------------------------------------------------------------------------------+
```

### Table 1: Color Risk Scale & Operational Protocol

| Risk Level | Color Code | Forecasted Probability | Recommended Multi-Agency Operational Response |
| :--- | :---: | :---: | :--- |
| **CRITICAL** | `#990000` (Crimson) | $P \ge 70\%$ | Deploy plainclothes LEA interception units (11:00–16:00 IST); enforce bank step-up biometric verification and INR 10,000 cash limits. |
| **HIGH** | `#e6550d` (Orange-Red) | $50\% \le P < 70\%$ | Periodic marked mobile patrols; issue preemptive CCTV preservation requests to branch managers. |
| **ELEVATED** | `#fdae6b` (Light Orange) | $30\% \le P < 50\%$ | Routine beat patrol vigilance; automated bank ATM fraud monitoring. |
| **LOW / ROUTINE** | `#f7f7f7` (Neutral Gray) | $P < 30\%$ | Standard background operations; 20% allocated for random exploration audits. |

---

## 3. Launching the Interactive Web Dashboard

To run the full Streamlit dashboard locally:
```bash
streamlit run app.py
```
* Access URL: `http://localhost:8501`
* Features: Real-time slider for patrol budget $K$, risk threshold $\tau$, bank circle filters, embedded Folium map, and localized SHAP waterfall breakdowns.

---
*Document Version: 2.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
