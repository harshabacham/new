# Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
## Smart India Hackathon 2026 (SIH 2026) | Problem ID: SIH26184
### Undergraduate B.Tech AI/ML Capstone Project | Academic Track

---

## 1. Project Overview

* **Problem ID**: SIH26184
* **Title**: Cybercrime Cash-Withdrawal Location Forecasting
* **Domain**: Supervised Machine Learning, Geospatial Analytics, Spatiotemporal Point Processes, Financial Cybercrime Intelligence
* **Evaluation Framework**: B.Tech AI/ML Academic Capstone / Smart India Hackathon 2026
* **Status**: **ALL FIVE PHASES FULLY IMPLEMENTED AND EMPIRICALLY VERIFIED [COMPLETED]**

### Official Problem Statement
> *"Estimate likely geographic withdrawal clusters from cybercrime complaint metadata such as time, amount, bank and geography. Classification/regression prototype; geographic feature engineering; evaluation of cluster prediction; actionable-intelligence report."*

### Core Scientific Objective & Breakthrough
To investigate whether supervised machine learning algorithms, trained on spatiotemporally aggregated cybercrime complaint metadata, financial indicators, and built-environment features under strict chronological walk-forward evaluation, can forecast discrete spatial grid cells with an elevated likelihood or count of cybercrime cash-withdrawal activity over future operational time windows.

**Key Experimental Findings**:
* **Champion Multi-Model Stacking Classifier**: Blending Gradient Boosted Trees and Random Forest via Logistic Meta-Learner achieves **ROC-AUC = 0.9348** and **PAI@10 = 8.54** under strict chronological holdout evaluation.
* **Isotonic Probability Calibration**: Resolves severe class imbalance (5.07% prevalence) by reducing **Brier calibration score from 0.1040 down to 0.0370 (-64.4% error reduction)**.
* **Spatial Concentration Power**: Our tree ensemble achieves a **Prediction Accuracy Index (PAI@10) of 8.81**, outperforming the random spatial baseline by **9.1x** and capturing **65.6% of theoretical maximum efficiency (PEI@10 = 0.656)** with **55.9% Precision@10**.
* **Cost-Sensitive Threshold Tuning**: Shifting the decision threshold to $\tau^* = 0.05$ (accounting for $C_{\text{FN}} = 35\text{k}$ vs $C_{\text{FP}} = 3\text{k}$) yields **INR 29.21 Million** in net operational utility.
* **Real-World Dataset Ingestion**: Successfully validated across 2,500 real-world geocoded crimes via Chicago Open Data SODA API and PaySim mobile financial records.

---

## 2. Five-Phase Completed Project Roadmap

```
+----------------------------------------------------------------------------------------------------+
|                                    FIVE-PHASE PROJECT ROADMAP                                      |
+----------------------------------------------------------------------------------------------------+
|  PHASE 1: Problem Definition & Literature Review                                      [COMPLETED]  |
|           16 peer-reviewed studies across 8 pillars, 5 research gaps, spatial entity decoupling.   |
|           Artifact: phase_1/Phase_1_Research_Report.pdf                                            |
|                                                                                                    |
|  PHASE 2: Dataset Collection, Generation & Quality Assurance Audit                    [COMPLETED]  |
|           DPDP Act 2023-compliant synthetic engine, 27,291 complaints, 18,527 withdrawals, 100% QA.|
|           Artifact: phase_2/Phase_2_Data_Report.pdf                                                |
|                                                                                                    |
|  PHASE 3: Exploratory Spatial Data Analysis (ESDA) & Feature Pipeline                 [COMPLETED]  |
|           Moran's I (+0.6018), DBSCAN point clustering, 74,400-unit spatiotemporal panel.          |
|           Artifact: phase_3/Phase_3_Feature_Report.pdf                                             |
|                                                                                                    |
|  PHASE 4: Supervised Model Training & Chronological Walk-Forward Backtesting          [COMPLETED]  |
|           9 models (Baselines, Logistic, Poisson, RF, GBDT), PAI/PEI benchmarks, model artifacts.  |
|           Artifact: phase_4/Phase_4_Modeling_Report.pdf                                            |
|                                                                                                    |
|  PHASE 5: Geospatial Visualization & Actionable Intelligence Reporting                [COMPLETED]  |
|           Folium GIS choropleth, Streamlit app (app.py), local SHAP XAI, tactical incident dossier.|
|           Artifact: phase_5/Phase_5_Tactical_Briefing.pdf & Phase_5_Intelligence_Report.pdf        |
+----------------------------------------------------------------------------------------------------+
|  MASTER CAPSTONE THESIS: Cybercrime_Withdrawal_Forecasting_Final_Report.pdf           [COMPLETED]  |
+----------------------------------------------------------------------------------------------------+
```

---

## 3. Repository Architecture & File Navigation

```
supervised/
├── README.md                                           # Master Overview, Results Matrix & Usage Guide
├── run_all_phases.py                                   # Master End-to-End Orchestrator (Executes Phases 1 to 5)
├── app.py                                              # Interactive Streamlit Tactical Command Dashboard
├── compile_full_capstone_report.py                     # Compiles Master Capstone Thesis (14 Pages)
├── compile_report.py                                   # Compiles Phase 1 Research Report
├── Cybercrime_Withdrawal_Forecasting_Final_Report.pdf # Final Master Capstone Thesis & Evaluation Dossier
│
├── phase_1/                                            # PHASE 1: RESEARCH FOUNDATIONS
│   ├── 01_problem_definition.md                        # Problem Definition, Aim, Objectives & Entity Decoupling
│   ├── 02_literature_review.md                         # Exhaustive Review of 16 Studies across 8 Pillars
│   ├── 03_research_gap_analysis.md                     # Comparative 16-Study Matrix & 5 Foundational Gaps
│   ├── 04_dataset_feasibility.md                       # Feasibility Audit (DPDP Act 2023) & Synthetic Specs
│   ├── 05_proposed_methodology.md                      # Options A vs. B, Candidate Models & 9-Stage Pipeline
│   ├── 06_evaluation_and_ethics.md                     # 4-Tier Evaluation Metrics (PAI, PEI) & 5 Ethics Pillars
│   ├── 07_references.bib                               # Complete Verified BibTeX Bibliography (19 DOIs)
│   ├── 08_phase_1_summary.md                           # Answers to 9 Foundational Questions
│   └── Phase_1_Research_Report.pdf                     # Compiled Phase 1 Academic PDF Report
│
├── phase_2/                                            # PHASE 2: DATASET ENGINEERING & VALIDATION
│   ├── config.py                                       # Simulation Hyperparameters & Distribution Configs
│   ├── generate_synthetic_data.py                      # Stochastic Generator (Complaints + Gamma Delayed Cash-Out)
│   ├── validate_data.py                                # Automated 7-Test Schema & Quality Assurance Audit
│   ├── 01_synthetic_engine_architecture.md             # Mathematical Architecture of Generation Engine
│   ├── 02_data_dictionary_and_schema.md               # Standardized 19-Field Data Dictionary
│   ├── 03_validation_and_quality_report.md             # Quality Assurance Scorecard (100% Pass)
│   └── Phase_2_Data_Report.pdf                         # Compiled Phase 2 Data Engineering PDF Report
│
├── phase_3/                                            # PHASE 3: ESDA & FEATURE ENGINEERING
│   ├── spatial_clustering_esda.py                      # Global Moran's I & DBSCAN Spatial Clustering
│   ├── spatiotemporal_feature_pipeline.py              # Leak-Free Panel Discretization (74,400 Observations)
│   ├── esda_spatial_clusters.png                       # ESDA Spatial Distribution & Clustering Map
│   ├── 01_esda_and_clustering_findings.md              # Moran's I Autocorrelation & DBSCAN Synthesis
│   ├── 02_feature_engineering_methodology.md           # 29-Feature Spatiotemporal Taxonomy
│   ├── 03_leak_free_pipeline_verification.md           # Proof of Zero Temporal Leakage
│   └── Phase_3_Feature_Report.pdf                      # Compiled Phase 3 Feature PDF Report
│
├── phase_4/                                            # PHASE 4: SUPERVISED TRAINING & EVALUATION
│   ├── train_and_evaluate.py                           # Walk-Forward Training & Evaluation (9 Models)
│   ├── model_performance_charts.png                    # Comparative PAI@10 and PR-AUC Performance Charts
│   ├── benchmark_comparison.csv                        # Master Quantitative Evaluation CSV Matrix
│   ├── benchmark_results.json                          # Structured JSON Evaluation Artifact
│   ├── 01_model_architectures_and_baselines.md         # 9-Model Candidate Suite & Baselines
│   ├── 02_walk_forward_evaluation_results.md           # Empirical Benchmark Matrix & RQ Resolutions
│   ├── 03_error_analysis_and_ablation.md               # Feature Importance (Recency: 26.8%, 7d: 18.4%)
│   └── Phase_4_Modeling_Report.pdf                     # Compiled Phase 4 Modeling PDF Report
│
├── phase_5/                                            # PHASE 5: VISUALIZATION & ACTIONABLE INTELLIGENCE
│   ├── explainability_engine.py                        # Local Additive Feature Attributions & Conformal Intervals
│   ├── generate_interactive_map.py                     # Interactive Folium GIS Map Generator
│   ├── generate_tactical_briefing.py                   # Automated Tactical Briefing (Markdown + PDF)
│   ├── interactive_hotspot_forecast_map.html           # Standalone Folium GIS Map with Layer Control
│   ├── tactical_intelligence_briefing.md               # Incident Commander Operational Directive
│   ├── latest_operational_forecasts.csv                # 400-Cell Tactical Predictions with XAI Drivers
│   ├── 01_explainability_and_attribution.md            # XAI Formulation & Conformal Coverage Theory
│   ├── 02_geospatial_interface_guide.md                # GIS Layer Guide & Streamlit User Manual
│   ├── Phase_5_Tactical_Briefing.pdf                   # Compiled Tactical Intelligence Incident Dossier
│   └── Phase_5_Intelligence_Report.pdf                 # Compiled Phase 5 Intelligence PDF Report
│
├── models/                                             # TRAINED MODEL SERIALIZATION ARTIFACTS
│   ├── best_classifier_hgb.joblib                      # Top Classifier (HistGradientBoosting / LightGBM)
│   ├── best_classifier_rf.joblib                       # Random Forest Classifier Artifact
│   ├── best_regressor_hgb.joblib                       # Top Poisson Regressor (HistGradientBoosting Poisson)
│   ├── best_regressor_rf.joblib                        # Random Forest Regressor Artifact
│   └── preprocessor.joblib                             # Standard Scaler & Feature Columns Mapping
│
└── data/                                               # GENERATED DATASET ARTIFACTS
    ├── grid_cells.csv                                  # 400 Planar Cells with Centroids & ATM Counts
    ├── cybercrime_complaints.csv                       # 27,291 Complaint Records
    ├── verified_withdrawals.csv                        # 18,527 Verified Cash-Out Records
    ├── cybercrime_paired_events.csv                    # Coupled Paired Event Master Dataset
    ├── cybercrime_paired_events.parquet                # High-Performance Parquet Storage
    ├── spatiotemporal_feature_matrix.parquet           # 74,400 x 29 Spatiotemporal Feature Matrix
    ├── spatiotemporal_feature_matrix.csv               # CSV Feature Matrix Export
    └── validation_summary.json                         # Automated Quality Assurance Audit Summary
```

---

## 4. Master Comparative Benchmark Results (Phase 4)

All models were evaluated on the **18,400-observation chronological holdout partition** (46 continuous operational test days) under strict walk-forward backtesting with **zero data leakage**:

### Master Benchmark Scorecard

| Model / Baseline | Paradigm | PR-AUC | ROC-AUC | F1-Score | PAI@10 | PEI@10 | Precision@10 | Recall@10 | MAE | Poisson Deviance |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Uniform Random** | Baseline | 0.0500 | 0.5000 | 0.0927 | 0.97 | 0.070 | 0.039 | 0.024 | — | — |
| **2. Persistent Lag (Yesterday)** | Baseline | 0.2334 | 0.7712 | 0.3353 | 6.52 | 0.488 | 0.383 | 0.163 | 0.449 | 0.985 |
| **3. Flag + Boost MA** [10] | Baseline | 0.4597 | 0.8845 | 0.4356 | 8.78 | 0.653 | 0.550 | 0.220 | 0.395 | 0.742 |
| **4. Logistic Regression (L2)** | Option A | 0.4821 | 0.8860 | 0.3640 | 8.65 | 0.645 | 0.552 | 0.216 | — | — |
| **5. Poisson GLM Regressor** | Option B | **0.4837** | 0.8864 | **0.4482** | 8.62 | 0.641 | 0.554 | 0.215 | 0.367 | **0.672** |
| **6. Random Forest Classifier** | Option A | 0.4211 | 0.8752 | 0.4458 | 8.04 | 0.601 | 0.511 | 0.201 | — | — |
| **7. Random Forest Regressor** | Option B | 0.4471 | 0.8801 | 0.4341 | 8.64 | 0.643 | 0.541 | 0.216 | 0.365 | 0.698 |
| **8. Gradient Boosted Trees (HGB)**| Option A | 0.4692 | **0.8878** | 0.3678 | **8.81** | **0.656** | **0.559** | **0.220** | — | — |
| **9. Gradient Boosted Poisson** | Option B | 0.4593 | 0.8839 | 0.4320 | 8.71 | 0.648 | 0.548 | 0.218 | **0.364** | 0.684 |

### Direct Scientific Answers to Research Questions:
1. **RQ1 (Spatiotemporal Predictability)**: Confirmed. Moran's $I = +0.6018$ ($p < 0.0001$) and $\text{PAI@10} = 8.81$ demonstrate that physical cash-out activity is intensely clustered and highly predictable compared to uniform random allocation ($\text{PAI} = 0.97$).
2. **RQ2 (Option A vs. Option B)**: Option A (Classification) delivers superior spatial priority ranking ($\text{PAI} = 8.81$, $\text{Precision@10} = 55.9\%$), while Option B (Poisson GLM / GBDT) delivers calibrated continuous incident counts ($\text{MAE} = 0.364$, $\text{Poisson Deviance} = 0.672$).
3. **RQ3 (Feature Importance)**: Historical recency decay (`decay_intensity_30d`: 26.8%) and 7-day momentum (`lag_count_7d`: 18.4%) account for $>45\%$ of predictive power, while spatial Queen diffusion (`spatial_lag_neighbor_7d`: 11.5%) captures near-repeat contagion.
4. **RQ4 (Evaluation Metric Alignment)**: Global ROC-AUC (0.88) obscures localized spatial concentration. Resource-bounded indices (PAI, PEI, Precision@K) faithfully reflect tactical operational utility.
5. **RQ5 (Fairness & Bias)**: Runaway feedback loops are mitigated via an **80/20 exploitation-exploration patrol split** and localized additive SHAP explanations.

---

## 5. How to Run and Verify the Project

### 5.0 One-Click Windows Launchers (Double-Click Execution)
* **`launch_dashboard.bat`**: Launches the 7-tab Streamlit Tactical Command Dashboard with live 1930 burst simulator.
* **`run_api.bat`**: Starts the high-performance Starlette/Uvicorn REST API microservice on port 8000.
* **`run_pipeline.bat`**: Executes the master orchestrator running all 5 phases, external imports, modeling, and compilation.
* **`run_tests.bat`**: Runs the complete 13-test automated unit and integration test suite.
* **`simulate_burst.bat`**: Injects a live burst batch of Helpline 1930 cybercrime reports.

### 5.1 Execute Full End-to-End Pipeline
Run the master orchestrator to sequentially execute data generation, QA tests, ESDA, feature engineering, model training, report compilation, and the automated test suite:
```bash
python run_all_phases.py
```

### 5.2 Run Automated Unit & Integration Test Suite
Execute the 13-test automated verification suite:
```bash
python run_tests.py
```
* Status: **13 of 13 tests passing (100% success rate)** verifying schemas, causality, zero-leakage, inference, REST endpoints, external data adapters, stacking/calibration, and GeoJSON tactical packages.

### 5.3 Launch the Interactive Streamlit Tactical Dashboard
Launch the interactive 7-tab web application for live scenario analysis, parameter tuning, GIS map exploration, and live burst simulation:
```bash
streamlit run app.py
```
* Dashboard features (7 Comprehensive Tabs):
  * **Tab 1: Interactive GIS Map**: Risk choropleth, Top-10 prioritized targets, and 80/20 exploration patrol zones.
  * **Tab 2: Prioritized Hotspot Matrix**: Probability ranking, expected incident counts, and 90% conformal intervals.
  * **Tab 3: Advanced ML Diagnostics**: PR curves, ROC curves, reliability diagrams, and cost-utility curves.
  * **Tab 4: Explainable AI (XAI)**: Local additive waterfall attributions per grid cell.
  * **Tab 5: External Dataset Ingestion**: Universal drag-and-drop CSV/Excel auto-mapper and Chicago/PaySim benchmarks.
  * **Tab 6: Multi-Agency Directives**: LEA & Bank SOPs with one-click downloads for GeoJSON, Police CSV & Bank Directives.
  * **Tab 7: Live 1930 Incident Simulator**: Interactive incident surge injector with Gamma-delay interdiction windows.

### 5.4 Interactive Capstone Jupyter Notebook
Explore the interactive code cells, mathematical formulations, and visual displays in the master evaluation notebook:
* [`capstone_interactive_walkthrough.ipynb`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/capstone_interactive_walkthrough.ipynb)

### 5.5 Docker Containerization & Microservice Orchestration
Start both the Streamlit Dashboard (Port 8501) and the REST API (Port 8000) using Docker Compose:
```bash
docker-compose up --build
```

### 5.6 Launch REST API Microservice
Start the high-performance Starlette/Uvicorn REST microservice directly:
```bash
python api.py
```
* Endpoints:
  * `GET /health` — Service health & evaluation scorecard
  * `GET /api/v1/forecasts?limit=10&min_prob=0.30` — Top-K tactical cell forecasts
  * `GET /api/v1/forecasts/{cell_id}` — Detailed cell forensics & conformal bounds
  * `GET /api/v1/benchmarks` — Walk-forward model performance matrix
  * `POST /api/v1/simulate/burst` — Ingest complaint burst and return priority ATM corridors

### 5.7 Simulate Real-Time Streaming Incident Bursts
Simulate real-time complaint arrivals from Helpline `1930` and observe dynamic ATM priority alerts:
```bash
python simulate_realtime_feed.py
```

### 5.8 View Presentation Pitch Deck & Live Demo Script
* **SIH 2026 Jury Pitch Deck (Landscape PDF)**: [`presentation/SIH26184_Jury_Pitch_Deck.pdf`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/presentation/SIH26184_Jury_Pitch_Deck.pdf)
* **Slide-by-Slide Markdown Notes**: [`presentation/sih_pitch_deck.md`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/presentation/sih_pitch_deck.md)
* **5-Minute Live Jury Demo Script**: [`presentation/hackathon_demo_script.md`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/presentation/hackathon_demo_script.md)

### 5.9 Compile All PDF Reports
* Master Capstone Thesis (14 pages): `python compile_full_capstone_report.py` -> [`Cybercrime_Withdrawal_Forecasting_Final_Report.pdf`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/Cybercrime_Withdrawal_Forecasting_Final_Report.pdf)
* Jury Presentation Slides: `python presentation/compile_pitch_deck.py` -> [`presentation/SIH26184_Jury_Pitch_Deck.pdf`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/presentation/SIH26184_Jury_Pitch_Deck.pdf)
* Phase 1 Research Report: `python compile_report.py` -> [`phase_1/Phase_1_Research_Report.pdf`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/phase_1/Phase_1_Research_Report.pdf)
* Phase 2 Data Engineering Report: `python phase_2/compile_phase_2_report.py` -> [`phase_2/Phase_2_Data_Report.pdf`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/phase_2/Phase_2_Data_Report.pdf)
* Phase 3 Feature Pipeline Report: `python phase_3/compile_phase_3_report.py` -> [`phase_3/Phase_3_Feature_Report.pdf`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/phase_3/Phase_3_Feature_Report.pdf)
* Phase 4 Supervised Modeling Report: `python phase_4/compile_phase_4_report.py` -> [`phase_4/Phase_4_Modeling_Report.pdf`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/phase_4/Phase_4_Modeling_Report.pdf)
* Phase 5 Tactical Briefing: `python phase_5/generate_tactical_briefing.py` -> [`phase_5/Phase_5_Tactical_Briefing.pdf`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/phase_5/Phase_5_Tactical_Briefing.pdf)
* Phase 5 Intelligence Systems Report: `python phase_5/compile_phase_5_report.py` -> [`phase_5/Phase_5_Intelligence_Report.pdf`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/phase_5/Phase_5_Intelligence_Report.pdf)

---

## 6. Fundamental Ethical Principles & Responsible AI Non-Goals

1. **Decision Support, Not Automated Enforcement**: The platform is strictly an investigative and tactical prioritization tool for authorized human officers. It technically cannot trigger automated police actions, bank account freezing, or citizen surveillance.
2. **Epistemic Distinction (Association $\ne$ Prediction $\ne$ Guilt)**: A forecasted hotspot is a statistical probability, **NOT legal evidence or proof of wrongdoing**. Any citizen withdrawing funds within a forecasted cell is presumed entirely innocent under the Indian Evidence Act / Bharatiya Sakshya Adhiniyam 2023.
3. **Privacy Compliance (DPDP Act 2023)**: Operates in strict accordance with the Digital Personal Data Protection (DPDP) Act 2023 (India). Real-world PII is systematically excluded, identifiers are SHA-256 hashed, and all demonstrations utilize synthetic benchmark data.
4. **Mitigating Algorithmic Feedback Loops**: Enforces an **80/20 exploration-exploitation patrol split**, allocating 20% of monitoring capacity to random cells to prevent self-reinforcing surveillance bias.

---
*Prepared for Smart India Hackathon 2026 Evaluation | Undergraduate B.Tech in Artificial Intelligence & Machine Learning*
