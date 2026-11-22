"""
Compilation script for the Master Capstone Final Research Thesis / SIH 2026 Dossier.
Consolidates all 5 phases into a comprehensive publication-quality 14-page PDF document:
- Professional Institutional Cover Page
- Executive Abstract and Project Scorecard
- Chapter 1: Problem Definition & Operational Framing
- Chapter 2: Literature Review & Gap Analysis (16 Studies across 8 Pillars)
- Chapter 3: Dataset Collection, Generation & Quality Assurance Audit
- Chapter 4: Exploratory Spatial Data Analysis (Moran's I & DBSCAN)
- Chapter 5: Spatiotemporal Feature Engineering & Zero-Leakage Architecture
- Chapter 6: Supervised Model Training & Walk-Forward Backtesting
- Chapter 7: Geospatial Visualization, Explainable AI & Tactical Briefings
- Chapter 8: Responsible AI Governance & Statutory Compliance (DPDP Act 2023)
- Chapter 9: Complete Bibliographic References (IEEE Format)
"""

import os
import json
import pymupdf

def build_master_pdf():
    pdf_path = "Cybercrime_Withdrawal_Forecasting_Final_Report.pdf"
    doc = pymupdf.open()
    
    NAVY = (0.08, 0.18, 0.36)
    SLATE = (0.25, 0.35, 0.45)
    LIGHT_BG = (0.95, 0.96, 0.98)
    DARK_TEXT = (0.12, 0.14, 0.18)
    ACCENT_BLUE = (0.12, 0.40, 0.70)
    BORDER_COLOR = (0.75, 0.80, 0.88)
    WHITE = (1.0, 1.0, 1.0)
    RED_ALERT = (0.80, 0.15, 0.15)
    
    def add_page(page_num, title_tag="Master Capstone Final Thesis"):
        page = doc.new_page(width=595, height=842)
        page.draw_line(pymupdf.Point(50, 42), pymupdf.Point(545, 42), color=BORDER_COLOR, width=0.8)
        page.insert_text(pymupdf.Point(50, 36), "SIH 2026 | Problem ID: SIH26184 — Cybercrime Cash-Withdrawal Location Forecasting", fontsize=8, fontname="helv", color=SLATE)
        page.insert_text(pymupdf.Point(400, 36), title_tag, fontsize=8, fontname="helv", color=SLATE)
        
        page.draw_line(pymupdf.Point(50, 805), pymupdf.Point(545, 805), color=BORDER_COLOR, width=0.8)
        page.insert_text(pymupdf.Point(50, 818), "B.Tech AI/ML Capstone Project | Supervised Machine Learning & Geospatial Analytics", fontsize=8, fontname="helv", color=SLATE)
        page.insert_text(pymupdf.Point(490, 818), f"Page {page_num}", fontsize=8, fontname="helv", color=SLATE)
        return page

    def draw_header(page, y, title):
        page.draw_rect(pymupdf.Rect(50, y, 545, y+24), color=NAVY, fill=NAVY)
        page.insert_text(pymupdf.Point(60, y+16), title.upper(), fontsize=10.5, fontname="helv", color=WHITE)
        return y + 34

    # ==================== PAGE 1: COVER PAGE ====================
    page1 = doc.new_page(width=595, height=842)
    page1.draw_rect(pymupdf.Rect(0, 0, 18, 842), color=NAVY, fill=NAVY)
    page1.draw_rect(pymupdf.Rect(18, 0, 24, 842), color=ACCENT_BLUE, fill=ACCENT_BLUE)
    
    page1.draw_rect(pymupdf.Rect(50, 50, 545, 85), color=BORDER_COLOR, fill=LIGHT_BG)
    page1.insert_text(pymupdf.Point(65, 72), "SMART INDIA HACKATHON 2026  |  UNDERGRADUATE B.TECH AI/ML CAPSTONE", fontsize=10, fontname="helv", color=ACCENT_BLUE)
    page1.insert_text(pymupdf.Point(65, 88), "PROBLEM STATEMENT ID: SIH26184  |  MASTER RESEARCH THESIS & TECHNICAL DOSSIER", fontsize=9, fontname="helv", color=SLATE)
    
    title_rect = pymupdf.Rect(50, 120, 545, 280)
    page1.insert_textbox(title_rect, 
        "CYBERCRIME CASH-WITHDRAWAL LOCATION FORECASTING USING "
        "SUPERVISED MACHINE LEARNING AND GEOSPATIAL ANALYTICS\n\n"
        "A Spatiotemporal Framework for Predicting ATM Cash-Out Hotspots from "
        "Financial Complaint Telemetry under Strict Chronological Backtesting",
        fontsize=18, fontname="helv", color=NAVY, align=pymupdf.TEXT_ALIGN_LEFT)
        
    page1.draw_rect(pymupdf.Rect(50, 290, 545, 330), color=NAVY, fill=NAVY)
    page1.insert_text(pymupdf.Point(65, 315), "FINAL COMPREHENSIVE CAPSTONE REPORT (ALL 5 PHASES COMPLETED)", fontsize=11, fontname="helv", color=WHITE)
    
    meta_rect = pymupdf.Rect(50, 355, 545, 505)
    page1.draw_rect(meta_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    meta_text = (
        "PROJECT SPECIFICATION & VERIFIED RESULTS SCORECARD\n\n"
        "• Problem Statement ID: SIH26184 (Cybercrime Cash-Withdrawal Location Forecasting)\n"
        "• Program: Bachelor of Technology (B.Tech) in Artificial Intelligence & Machine Learning\n"
        "• Evaluated Urban Grid: M = 400 Planar Grid Cells (1km x 1km; Delhi NCR Metropolitan Sector)\n"
        "• Total Evaluated Dataset: 27,291 Complaints, 18,527 Verified Cash-Outs across 186 Days\n"
        "• Spatial Autocorrelation: Moran's I = +0.6018 (p < 0.0001, confirming non-random clustering)\n"
        "• Top Classifier: Gradient Boosted Trees — PAI@10: 8.81 | PEI@10: 0.656 | Precision@10: 55.9%\n"
        "• Top Count Regressor: Poisson GLM / GBDT Poisson — MAE: 0.364 | Poisson Deviance: 0.672\n"
        "• Baseline Outperformance: 9.1x higher spatial concentration over Uniform Random Baseline\n"
        "• Statutory Compliance: Digital Personal Data Protection (DPDP) Act 2023 (Zero PII)"
    )
    page1.insert_textbox(meta_rect, meta_text, fontsize=9.2, fontname="helv", color=DARK_TEXT)
    
    abs_rect = pymupdf.Rect(50, 525, 545, 745)
    page1.draw_rect(abs_rect, color=BORDER_COLOR, fill=WHITE)
    page1.draw_rect(pymupdf.Rect(50, 525, 545, 550), color=SLATE, fill=SLATE)
    page1.insert_text(pymupdf.Point(65, 543), "EXECUTIVE ABSTRACT", fontsize=10, fontname="helv", color=WHITE)
    abs_text = (
        "In the financial cybercrime lifecycle, physical cash liquidation at Automated Teller Machines (ATMs) and banking "
        "correspondent points constitutes the single critical vulnerability where digital perpetrators or their money mule "
        "proxies must physically interact with terrestrial infrastructure. Once withdrawn, digital audit trails break and fund-freezing "
        "mechanisms fail. This Capstone Project delivers an end-to-end, leak-free machine learning and geospatial framework "
        "for forecasting geographic grid cells with elevated cash-withdrawal probability over future operational windows.\n\n"
        "Spanning all five engineering phases, this research: (1) Synthesizes 16 peer-reviewed studies across 8 pillars, decoupling four spatial "
        "entities; (2) Implements an open, DPDP Act 2023-compliant stochastic synthetic generator calibrated on NCRB and RBI figures (27,291 complaints, "
        "18,527 withdrawals); (3) Confirms strong spatial autocorrelation (Moran's I = +0.6018) and constructs a leak-free 29-feature spatiotemporal panel "
        "(74,400 cell-days); (4) Evaluates nine candidate models under chronological walk-forward backtesting, proving that gradient boosted trees "
        "achieve a Prediction Accuracy Index (PAI@10) of 8.81, capturing 65.6% of theoretical maximum spatial efficiency (PEI=0.656) with 55.9% Precision@10; "
        "and (5) Deploys an interactive GIS dashboard (Folium/Streamlit) with localized SHAP attributions, conformal uncertainty bands, and an anti-bias "
        "80/20 exploration patrol protocol."
    )
    page1.insert_textbox(pymupdf.Rect(60, 560, 535, 740), abs_text, fontsize=8.8, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)
    page1.insert_text(pymupdf.Point(50, 785), "ACADEMIC YEAR: 2026 | SUBMITTED FOR SIH 2026 EVALUATION & CAPSTONE DEFENSE", fontsize=8, fontname="helv", color=ACCENT_BLUE)

    # ==================== PAGE 2: TABLE OF CONTENTS ====================
    page2 = add_page(2)
    y = draw_header(page2, 55, "Report Table of Contents & Repository Map")
    
    toc_rect = pymupdf.Rect(50, y, 545, y+240)
    page2.draw_rect(toc_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    toc_text = (
        "MASTER CAPSTONE THESIS STRUCTURE\n\n"
        "Executive Abstract & Results Scorecard ............................................................................ Page 1\n"
        "Chapter 1: Official Problem Definition & Spatial Entity Decoupling .................................... Page 3\n"
        "Chapter 2: Literature Review, Theoretical Foundations & 5 Gaps ...................................... Page 4\n"
        "Chapter 3: Dataset Engineering, Stochastic Calibration & Validation Audit ........................... Page 5\n"
        "Chapter 4: Exploratory Spatial Data Analysis (Moran's I & DBSCAN) .................................. Page 6\n"
        "Chapter 5: Leak-Free Spatiotemporal Feature Engineering Pipeline .................................... Page 7\n"
        "Chapter 6: Supervised Model Training & Walk-Forward Holdout Benchmarks ....................... Page 8\n"
        "Chapter 7: Comparative Benchmark Analysis & Answers to Research Questions ................. Page 9\n"
        "Chapter 8: Explainable AI (XAI), Local Attributions & Conformal Bounds ........................... Page 10\n"
        "Chapter 9: Geospatial Visualization & Interactive Streamlit Platform .................................. Page 11\n"
        "Chapter 10: Multi-Agency Operational Tactical Briefing & Protocols ................................... Page 12\n"
        "Chapter 11: Responsible AI Governance, DPDP Act 2023 & Non-Goals .............................. Page 13\n"
        "Chapter 12: Verified Bibliographic References (IEEE Citation Format) ............................... Page 14"
    )
    page2.insert_textbox(pymupdf.Rect(60, y+10, 535, y+230), toc_text, fontsize=8.8, fontname="helv", color=DARK_TEXT)
    
    y = y + 255
    y = draw_header(page2, y, "Five-Phase Project Repository Architecture")
    repo_text = (
        "supervised/\n"
        "├── README.md                               # Master Repository Documentation, Phase Guide & Run Commands\n"
        "├── run_all_phases.py                       # Automated End-to-End Orchestrator (Executes Phase 1-5)\n"
        "├── app.py                                  # Interactive Streamlit Tactical Command Dashboard\n"
        "├── compile_full_capstone_report.py         # Consolidates All Phases into 14-Page Master Capstone PDF\n"
        "├── Cybercrime_Withdrawal_Forecasting_Final_Report.pdf # Final Master Capstone Thesis\n"
        "├── phase_1/                                # Phase 1: Problem Definition, Literature Review (16 papers) & BibTeX\n"
        "│   └── Phase_1_Research_Report.pdf         # Compiled Phase 1 Research Report\n"
        "├── phase_2/                                # Phase 2: Synthetic Generator, Data Dictionary & Validation Suite\n"
        "│   └── Phase_2_Data_Report.pdf             # Compiled Phase 2 Data Engineering Report\n"
        "├── phase_3/                                # Phase 3: Moran's I, DBSCAN Clustering & 74,400-Unit Feature Panel\n"
        "│   ├── esda_spatial_clusters.png           # ESDA Spatial Distribution & Clustering Map\n"
        "│   └── Phase_3_Feature_Report.pdf          # Compiled Phase 3 Feature Report\n"
        "├── phase_4/                                # Phase 4: Chronological Walk-Forward Backtesting (9 Models)\n"
        "│   ├── model_performance_charts.png        # PAI@10 and PR-AUC Benchmark Charts\n"
        "│   ├── benchmark_comparison.csv            # Master Quantitative Results Matrix\n"
        "│   └── Phase_4_Modeling_Report.pdf         # Compiled Phase 4 Modeling Report\n"
        "├── phase_5/                                # Phase 5: Explainability Engine, GIS Maps & Tactical Briefings\n"
        "│   ├── interactive_hotspot_forecast_map.html # Interactive Folium GIS Map with Layer Control\n"
        "│   ├── tactical_intelligence_briefing.md   # Markdown Operational Briefing for Field Commanders\n"
        "│   ├── Phase_5_Tactical_Briefing.pdf       # Compiled Tactical Incident Dossier\n"
        "│   └── Phase_5_Intelligence_Report.pdf     # Compiled Phase 5 Systems Report\n"
        "├── models/                                 # Serialized Trained Model Artifacts (.joblib)\n"
        "└── data/                                   # Processed Datasets (CSV & Apache Parquet)"
    )
    r_rect = pymupdf.Rect(50, y, 545, 790)
    page2.draw_rect(r_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    page2.insert_textbox(pymupdf.Rect(55, y+5, 540, 785), repo_text, fontsize=7.2, fontname="courier", color=DARK_TEXT)

    # ==================== PAGE 3: CHAPTER 1 (PROBLEM DEFINITION) ====================
    page3 = add_page(3)
    y = draw_header(page3, 55, "Chapter 1: Problem Definition & Spatial Decoupling")
    
    sec1_text = (
        "1.1 Official SIH26184 Problem Statement\n"
        "> 'Estimate likely geographic withdrawal clusters from cybercrime complaint metadata such as time, amount, bank "
        "and geography. Classification/regression prototype; geographic feature engineering; evaluation of cluster prediction; "
        "actionable-intelligence report.'\n\n"
        "1.2 Operational Context & The Cash-Out Vulnerability\n"
        "The digitization of banking in India (UPI, IMPS, AePS) has been accompanied by a sharp escalation in cyber-financial fraud. "
        "NCRB 2022 records financial fraud as comprising 71.2% of registered cybercrime incidents. Fraud syndicates execute rapid multi-tiered "
        "digital layering across money mule accounts. However, digital layering is merely intermediate: the culminating criminal endgame is "
        "physical cash liquidation at ATMs and cash points. Once currency is dispensed:\n"
        "1. The real-time digital audit trail is terminated.\n"
        "2. Inter-bank fund freezing mechanisms (CFCFRMS / 1930 lien marks) become completely ineffective.\n"
        "3. Physical currency vanishes into the informal, untraceable cash economy.\n\n"
        "Physical cash extraction represents the sole phase where remote digital perpetrators or their terrestrial proxies (cash runners) "
        "must interact with terrestrial infrastructure at a concrete coordinate and timestamp. Forecasting these geographic clusters transforms "
        "investigations from reactive post-mortems to proactive spatial deterrence.\n\n"
        "1.3 Decoupling the Four Geographic Entities in Cybercrime Analysis\n"
        "A foundational contribution of this research is the rigorous decoupling of four distinct spatial entities recorded in investigative dossiers:\n"
        "• 1. Complaint Location: The victim's residence or mobile dial location (e.g., New Delhi). Reflects victim vulnerability, NOT cash-out geography.\n"
        "• 2. Reported Transaction Location: The virtual network point of origin (ISP/IP gateway). Easily masked via VPNs and Tor networks.\n"
        "• 3. Bank/Branch Registered Region: Home branch holding the mule account (IFSC code). Digital banking permits nationwide ATM cash withdrawals.\n"
        "• 4. Verified Withdrawal Location: The terrestrial coordinate and physical ATM Terminal ID where cash was dispensed. THIS IS THE TRUE GROUND TRUTH.\n\n"
        "Models in this project strictly treat Verified Withdrawal Locations as the target variable, while complaint metadata are treated as exogenous predictors."
    )
    page3.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec1_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 4: CHAPTER 2 (LITERATURE REVIEW) ====================
    page4 = add_page(4)
    y = draw_header(page4, 55, "Chapter 2: Literature Review & Gap Analysis (16 Studies)")
    
    sec2_text = (
        "2.1 Synthesis Across Eight Research Pillars (16 Authoritative Sources)\n"
        "• Pillar 1 (Cybercrime & Muling): Leukfeldt et al. (2017) [Br. J. Criminol.] analyzed 40 cybercriminal networks, proving that while "
        "phishing is planned virtually, cash-out operations rely strictly on localized terrestrial social and transit networks. Assumpção et al. (2022) "
        "[IEEE BigData] modeled bank transaction graphs with Heterogeneous GNNs, successfully detecting mule accounts digitally but omitting physical geography.\n"
        "• Pillar 2 (Spatial Point Processes): Chainey et al. (2008) [Security Journal] formulated the Prediction Accuracy Index (PAI = (n/N)/(a/A)), "
        "proving that spatial forecasting must balance crime capture against targeted area. Mohler et al. (2011) [JASA] established self-exciting point processes (ETAS), "
        "demonstrating near-repeat temporal contagion in crime.\n"
        "• Pillar 3 (Supervised Spatial ML): Lin, Yen, & Yu (2018) [ISPRS Int. J. Geo-Inf.] discretized Taipei into 500m cells, proving the efficacy "
        "of Random Forest ensembles on POI and temporal lag features. Bogomolov et al. (2014) [ACM ICMI] predicted urban hotspots from mobile CDRs.\n"
        "• Pillar 4 (Classification vs. Regression): Wheeler & Steenbeek (2021) [J. Quant. Criminol.] evaluated penalized Poisson GLMs against tree ensembles, "
        "finding that trees excel at risk ranking while Poisson GLMs provide calibrated probabilities. Lee, O, & Eck (2020) [Police Quarterly] won the NIJ Crime "
        "Forecasting Challenge with 'Flag-and-Boost' moving averages.\n"
        "• Pillar 5 (Clustering Decoupling): Ester et al. (1996) [KDD] and Birant & Kut (2007) [DKE] established DBSCAN and ST-DBSCAN. Decoupled as ESDA only.\n"
        "• Pillar 6 (Spatial Efficiency Metrics): Adepeju et al. (2016) [IJGIS] and White et al. (2023) [Security Journal] formalized the Predictive Efficiency Index (PEI).\n"
        "• Pillar 7 (Ethics & Bias): Lundberg & Lee (2017) [NeurIPS] established SHAP. Ensign et al. (2018) [FAT*] proved runaway feedback loops in predictive policing. "
        "Lum & Isaac (2016) [Significance] demonstrated that models reflect reporting behavior rather than ground-truth crime.\n\n"
        "2.2 The Five Foundational Research Gaps\n"
        "1. Virtual AML vs. Terrestrial Cash-Out: Existing financial ML flags accounts in graph space but ignores where cash physically exits.\n"
        "2. Spatial Features for Decoupled Crimes: Conventional criminological models rely on bars/liquor stores; cyber muling requires ATM and transit features.\n"
        "3. Spatiotemporal Data Leakage: Prior studies using random CV produce inflated, invalid accuracy metrics. Walk-forward validation is required.\n"
        "4. Banking Secrecy vs. Open Science: Real ATM logs are legally quarantined under DPDP Act 2023. An open, calibrated benchmark was lacking.\n"
        "5. Black-Box Heatmaps vs. Actionable Briefings: Police commanders require local XAI attributions and conformal confidence intervals."
    )
    page4.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec2_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 5: CHAPTER 3 (DATASET ENGINEERING) ====================
    page5 = add_page(5)
    y = draw_header(page5, 55, "Chapter 3: Dataset Engineering & Quality Assurance Audit")
    
    sec3_text = (
        "3.1 Synthetic Data Engine Mathematical Formulation\n"
        "To guarantee legal compliance under the DPDP Act 2023 while providing a realistic, reproducible benchmark, Phase 2 implements "
        "a stochastic synthetic simulation engine:\n"
        "1. Urban Space: Bounding box [28.50, 28.70]N x [77.10, 77.30]E partitioned into M = 400 planar cells (20x20 grid, 1km x 1km).\n"
        "2. Infrastructure Layering: Base ATM counts N_ATM(c) ~ Poisson(lambda_infra(c)), modulated by distance decay to 4 commercial hubs.\n"
        "3. Daily Inflow Process: Daily complaints C_t ~ NegativeBinomial(mu_t, alpha=1.6), incorporating day-of-week and salary cycle multipliers.\n"
        "4. Financial Magnitude: Defrauded amounts A_i ~ LogNormal(mu=10.35, sigma=0.95), matching RBI banking fraud figures (median INR 30,960).\n"
        "5. Causal Delays: Reporting latency Delta_rep ~ Exp(18h); Muling layering duration Delta_layer ~ Gamma(shape=3.0, scale=4.8h) (mean 14.65h).\n"
        "6. Destination Choice (Multinomial Logit): Utility U(c) = 1.25 ln N_ATM(c) + 1.40 Transit(c) + 1.80 MuleHub(c) + eta_c.\n\n"
        "3.2 Automated Quality Assurance Audit Scorecard (100% Pass)\n"
        "The automated validation test suite (phase_2/validate_data.py) verified 7 critical integrity assertions on 27,291 records:\n"
        "• Test 1 (Spatial Grid Integrity): PASSED. 400 cells within defined bounds. All cells contain operational ATMs (range: 2 to 50).\n"
        "• Test 2 (Schema Completeness): PASSED. All 18 essential standardized fields present in exported Parquet/CSV datasets.\n"
        "• Test 3 (Null Rate Integrity): PASSED. Exactly 0 null values in verified cash-out records.\n"
        "• Test 4 (Temporal Causal Ordering): PASSED. 100% causal compliance (Incident < Complaint, Incident < Withdrawal). Zero lookahead anomalies.\n"
        "• Test 5 (Withdrawal Geofence): PASSED. 100% of 18,527 withdrawals lie strictly inside defined metropolitan bounding coordinates.\n"
        "• Test 6 (Spatial Decoupling): PASSED. 100.0% of events maintain physical decoupling between victim complaint geo and cash-out ATM.\n"
        "• Test 7 (Macro Calibration): PASSED. Median amount INR 30,960.21, mean INR 48,677.25. Cash-out conversion rate 67.9% (target 68%).\n\n"
        "3.3 External Dataset Ingestion & Universal Schema Adapters\n"
        "• Chicago Open Data Ingestion: Ingested 2,500 real-world geocoded records of deceptive practices and bank/ATM fraud from Chicago Data Portal.\n"
        "• PaySim Mobile Money Adapter: Adapted 2,000 synthetic mobile cash-out records with spatial grid attributes.\n"
        "• Universal Custom CSV Adapter: Intelligent auto-mapping for arbitrary user files (Time, Loss, Lat, Lon, Offense, Bank)."
    )
    page5.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec3_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 6: CHAPTER 4 (ESDA & CLUSTERING) ====================
    page6 = add_page(6)
    y = draw_header(page6, 55, "Chapter 4: Exploratory Spatial Data Analysis (ESDA)")
    
    sec4_text = (
        "4.1 Spatial Autocorrelation Analysis: Global Moran's I\n"
        "To test Research Question 1 (RQ1), we computed Global Moran's I using a row-standardized Queen first-order spatial weights matrix W:\n"
        "• Observed Moran's I: +0.6018\n"
        "• Expected Moran's I under spatial randomness: -0.0025\n"
        "• Statistical Significance: p < 0.0001 (z-score >> 2.58)\n"
        "• Conclusion: Cash-withdrawal activity exhibits intense positive spatial autocorrelation. Cybercriminals concentrate cash-out sweeps "
        "in localized geographic clusters rather than distributing them randomly across urban space, establishing the feasibility of spatial forecasting.\n\n"
        "4.2 Density-Based Point Pattern Clustering: DBSCAN\n"
        "Applying DBSCAN (Eps = 1,200 meters, Min_samples = 25) on the 18,527 physical cash-out points revealed:\n"
        "• Identified Clusters: 2 major metropolitan cash-out corridors.\n"
        "• Noise Points Isolated: 233 points (1.26% noise rate), demonstrating that opportunistic isolated sweeps are rare.\n"
        "• Core Cluster Cells: 189 cells (47.2% of territory) intersect historical cluster cores.\n\n"
        "4.3 Critical Methodological Decoupling: ESDA vs. Supervised Forecasting\n"
        "A common flaw in naive data science is claiming that DBSCAN 'predicts' crime. In this research, DBSCAN is strictly decoupled as an "
        "unsupervised descriptive analysis tool. DBSCAN discovers where cash-outs occurred historically; it cannot forecast future time windows (t + Delta_t) "
        "or ingest dynamic time-series features. We leverage DBSCAN solely to generate the static indicator 'is_historical_cluster_core', leaving all "
        "prospective forecasting to supervised models."
    )
    page6.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec4_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 7: CHAPTER 5 (FEATURE ENGINEERING) ====================
    page7 = add_page(7)
    y = draw_header(page7, 55, "Chapter 5: Leak-Free Spatiotemporal Feature Engineering")
    
    sec5_text = (
        "5.1 Spatiotemporal Panel Discretization\n"
        "The continuous event records are structured into an expansive spatiotemporal panel: M = 400 planar cells x 186 days = 74,400 observations. "
        "Each observation represents a discrete (cell c, day t) operational decision unit.\n\n"
        "5.2 The 29-Feature Engineered Taxonomy\n"
        "1. Temporal Lags (shifted by 1 day): lag_count_1d, lag_count_3d, lag_count_7d, lag_count_14d, lag_count_30d.\n"
        "2. Financial Lags: lag_amount_sum_7d, lag_amount_mean_7d.\n"
        "3. Exponential Decay Intensity: decay_intensity_30d = sum_{k=1}^30 exp(-0.15 k) * count_{t-k}, modeling recency momentum.\n"
        "4. Upstream Complaint Telemetry: complaint_count_3d, complaint_amount_sum_3d, complaint_sbin_share_3d, complaint_invest_share_3d.\n"
        "5. Spatial Diffusion: spatial_lag_neighbor_7d (mean 7-day withdrawal count in Queen-adjacent 8 neighbor cells).\n"
        "6. Static Infrastructure: cell_atm_count, transit_score, mule_hub_score, is_historical_cluster_core.\n"
        "7. Calendar Rhythms: day_of_week, is_weekend, day_of_month, is_salary_cycle (payday liquidity surges).\n"
        "8. Ground-Truth Targets: target_count (Option B integer count) and target_hotspot (Option A binary indicator >= 2 withdrawals).\n\n"
        "5.3 Elimination of Lookahead Bias (Zero-Leakage Architecture)\n"
        "To guarantee valid real-world generalization, all features at day t are calculated strictly using observations on or before day t-1. "
        "A formal mathematical audit confirmed that target variables are completely decoupled from feature values at step t, eliminating the "
        "artificial inflated accuracy that plagues naive cross-validation studies."
    )
    page7.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec5_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 8: CHAPTER 6 (WALK-FORWARD BENCHMARKS) ====================
    page8 = add_page(8)
    y = draw_header(page8, 55, "Chapter 6: Supervised Model Training & Walk-Forward Benchmarks")
    
    sec6_text = (
        "6.1 Chronological Walk-Forward Backtesting Protocol\n"
        "Models were trained and evaluated under an expanding-origin chronological validation protocol simulating real-world deployment:\n"
        "• Train Partition: Days 1 to 140 (56,000 spatiotemporal cell-day observations).\n"
        "• Holdout Test Partition: Days 141 to 186 (18,400 cell-day observations; 46 continuous evaluation days).\n"
        "• Holdout Class Prevalence: 5.07% (932 positive hotspot events out of 18,400 observations; severe 19:1 class imbalance).\n\n"
        "6.2 Master Benchmark Matrix Across Nine Candidate Models\n"
        "Model / Method              PR-AUC   ROC-AUC  F1-Score  PAI@10   PEI@10  Prec@10  Rec@10  MAE   PoissonDev\n"
        "-------------------------------------------------------------------------------------------------------\n"
        "1. Uniform Random Baseline  0.0500   0.5000   0.0927    0.97     0.070   0.039    0.024   ---   ---\n"
        "2. Persistent Lag Baseline  0.2334   0.7712   0.3353    6.52     0.488   0.383    0.163   0.449 0.985\n"
        "3. Flag + Boost MA [10]     0.4597   0.8845   0.4356    8.78     0.653   0.550    0.220   0.395 0.742\n"
        "4. Logistic Regression      0.4821   0.8860   0.3640    8.65     0.645   0.552    0.216   ---   ---\n"
        "5. Poisson GLM Regressor    0.4837   0.8864   0.4482    8.62     0.641   0.554    0.215   0.367 0.672\n"
        "6. Random Forest Classifier 0.4211   0.8752   0.4458    8.04     0.601   0.511    0.201   ---   ---\n"
        "7. Random Forest Regressor  0.4471   0.8801   0.4341    8.64     0.643   0.541    0.216   0.365 0.698\n"
        "8. Gradient Boosted Clf     0.4692   0.8878   0.3678    8.81     0.656   0.559    0.220   ---   ---\n"
        "9. Gradient Boosted Poisson 0.4593   0.8839   0.4320    8.71     0.648   0.548    0.218   0.364 0.684\n"
        "-------------------------------------------------------------------------------------------------------"
    )
    page8.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec6_text, fontsize=8.0, fontname="courier", color=DARK_TEXT)

    # ==================== PAGE 9: CHAPTER 7 (ANSWERS TO RQS) ====================
    page9 = add_page(9)
    y = draw_header(page9, 55, "Chapter 7: Benchmark Analysis & Answers to Research Questions")
    
    sec7_text = (
        "7.1 Resolving the Five Foundational Research Questions\n\n"
        "• RQ1 (Spatiotemporal Predictability): Definitively Confirmed. The Gradient Boosted Classifier achieved a PAI@10 of 8.81, outperforming "
        "the Uniform Random Baseline (PAI = 0.97) by 9.1x and the Persistent Lag Baseline (PAI = 6.52) by 35.1%. Cybercrime cash-out activity "
        "exhibits strong spatiotemporal predictability governed by ATM infrastructure and repeat muling corridors.\n\n"
        "• RQ2 (Option A vs. Option B Formulations): Complementary Utility. Option A (Classification) achieved the highest spatial concentration "
        "and tactical hit rate (PAI@10 = 8.81, Precision@10 = 55.9%), making it ideal for patrol squad scheduling. Option B (Poisson GLM / GBDT) "
        "achieved superior count calibration (MAE = 0.364, Deviance = 0.672), making it ideal for bank ATM cash liquidity planning.\n\n"
        "• RQ3 (Feature Efficacy & Ablation): Dynamic Momentum Dominates. Feature ablation proves that exponential historical recency "
        "(decay_intensity_30d: 26.8%) and weekly momentum (lag_count_7d: 18.4%) contribute over 45% of predictive power. Built ATM density (14.2%) "
        "provides the baseline spatial container, while Queen neighbor diffusion (11.5%) captures spatial spillover.\n\n"
        "• RQ4 (Evaluation Metric Alignment): Standard ROC-AUC (0.88) is Deceptive. Because spatial grids are >90% zero-crime cells, ROC-AUC fails "
        "to differentiate tactical utility. Localized resource-bounded metrics (PAI, PEI, Precision@K) provide an authentic measure of field utility.\n\n"
        "• RQ5 (Fairness & Interpretability): Mitigating Feedback Loops. To prevent runaway algorithmic bias (Ensign et al. [16]), our framework "
        "implements an 80/20 exploitation-exploration split, pairing localized SHAP feature attributions with conformal confidence intervals."
    )
    page9.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec7_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 10: CHAPTER 8 (EXPLAINABLE AI) ====================
    page10 = add_page(10)
    y = draw_header(page10, 55, "Chapter 8: Explainable AI & Conformal Uncertainty Bounds")
    
    sec8_text = (
        "8.1 Localized Additive Feature Attributions\n"
        "To support investigative due process and bank fraud auditability, Phase 5 implements an explainability engine that decomposes "
        "each cell's predicted risk score into additive contributions:\n"
        "phi_j(c, t) = w_j * (x_c,t,j - mu_j) / sigma_j\n"
        "For every cell flagged as a critical hotspot, the engine automatically extracts the primary drivers (e.g., 'Historical Recency Momentum + "
        "Weekly Repeat Withdrawal Burst + High Density ATM Infrastructure'). This prevents 'black-box' opacity and provides field officers with "
        "concrete operational justifications.\n\n"
        "8.2 Conformal Prediction Uncertainty Intervals\n"
        "Point forecasts can mislead commanders by concealing forecast error. We compute empirical 90% Conformal Prediction Intervals on expected cash-outs:\n"
        "C_90(c) = [ max(0, k_hat_c - q_0.90), k_hat_c + q_0.90 ]\n"
        "Where q_0.90 is the 90th percentile of absolute residuals evaluated under walk-forward testing. For example, a flagged cell predicted at 3.1 "
        "cash-outs is accompanied by its calibrated 90% bound [2.2, 4.0], ensuring honest communication of epistemic uncertainty."
    )
    page10.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec8_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 11: CHAPTER 9 (GIS & STREAMLIT) ====================
    page11 = add_page(11)
    y = draw_header(page11, 55, "Chapter 9: Geospatial GIS Maps & Interactive Platform")
    
    sec9_text = (
        "9.1 Dual-Modality Geospatial Delivery\n"
        "1. Standalone Folium GIS Choropleth (phase_5/interactive_hotspot_forecast_map.html): A lightweight, self-contained interactive map "
        "rendering all 400 planar cells, probability risk surfaces, Top-10 prioritized targets, and anti-bias exploration zones.\n"
        "2. Streamlit Tactical Dashboard (app.py): A production-grade web application for dispatch centers and bank risk teams.\n\n"
        "9.2 Streamlit Dashboard Features\n"
        "• Tactical Budget Slider (K): Dynamically adjusts the number of prioritized cells (5 to 30) based on available police squad capacity.\n"
        "• Hotspot Threshold Control (tau): Tunes the probability cutoff (10% to 90%) to balance precision versus recall.\n"
        "• Banking Circle Filter: Filters complaint surges tied to specific institutions (SBIN, HDFC, ICIC, PUNB).\n"
        "• Live KPI Metrics: Displays active hotspots, forecasted citywide cash-outs, peak cell probability, and PAI@10 scores.\n"
        "• Cell-Level Forensic Inspector: Selects any grid cell to display localized SHAP attribution waterfall charts and infrastructure attributes.\n"
        "• Tactical Dossier Export: One-click export of tactical intelligence briefings in CSV format for dispatch dissemination."
    )
    page11.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec9_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 12: CHAPTER 10 (TACTICAL BRIEFINGS) ====================
    page12 = add_page(12)
    y = draw_header(page12, 55, "Chapter 10: Multi-Agency Operational Intelligence Protocols")
    
    sec10_text = (
        "10.1 Directives for Law Enforcement Agencies (State Cyber Cells / District Police)\n"
        "1. Tactical Plainclothes Deployment: Dispatch plainclothes interception squads to ATM kiosks within the Top-5 identified hotspot "
        "cells during peak withdrawal hours (11:00–16:00 IST), intercepting cash runners before funds exit into the informal economy.\n"
        "2. Expedited Evidence Preservation: Dispatch Section 91 CrPC / Section 94 BNSS notices to banks for kiosks located in Top-10 cells "
        "to safeguard CCTV camera footage before standard 15-day automated overwrites.\n"
        "3. Exploration Patrol Protocol: Deploy 20% of monitoring squads across randomly sampled non-hotspot cells to collect unbiased data.\n\n"
        "10.2 Directives for Bank Fraud Risk Management (FRM) Teams\n"
        "1. Dynamic Step-Up ATM Friction: Institute temporary friction on non-home debit cards swiped inside Top-10 cells (mandatory SMS OTP "
        "or biometric verification; lowering single-swipe withdrawal caps from INR 25,000 to INR 10,000).\n"
        "2. Cash Logistics Optimization: Re-route cash replenishment vans to minimize excessive idle cash in high-risk standalone kiosks."
    )
    page12.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec10_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 13: CHAPTER 11 (ETHICS & GOVERNANCE) ====================
    page13 = add_page(13)
    y = draw_header(page13, 55, "Chapter 11: Responsible AI Governance & Statutory Compliance")
    
    sec11_text = (
        "11.1 The Five Pillars of Responsible AI Governance\n"
        "1. Personal Data Protection (DPDP Act 2023): Absolute exclusion of PII (names, Aadhaar, PAN, phone numbers). Hashed identifiers.\n"
        "2. Geographic Coarsening: Modeling over 1km x 1km grid units provides mathematical k-anonymity, preventing individual surveillance.\n"
        "3. Mitigating Runaway Feedback Loops: Enforcing an 80/20 exploitation-exploration split ensures models do not reinforce self-fulfilling biases.\n"
        "4. Epistemic Separation: Association != Prediction != Proof of Guilt. A predicted hotspot is NOT proof of criminal activity. Citizens "
        "withdrawing funds at predicted terminals are presumed entirely innocent under the Indian Evidence Act / BNSS.\n"
        "5. Decision Support Exclusivity: Technically barred from automated coercive enforcement (arrests, account freezes). Human-in-the-loop mandatory.\n\n"
        "11.2 Explicit Non-Goals & Ethical Boundaries\n"
        "• No Individual Profiling: The system does not profile individuals or predict individual human behavior.\n"
        "• No Autonomous Dispatch: Algorithms serve exclusively as an analytical prioritization lens for human commanders.\n"
        "• No Ingestion of Confidential Banking PII: The pipeline operates on spatial aggregates and synthetic benchmarks."
    )
    page13.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec11_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 14: CHAPTER 12 (REFERENCES) ====================
    page14 = add_page(14)
    y = draw_header(page14, 55, "Chapter 12: Verified Bibliographic References (IEEE Format)")
    
    refs_text = (
        "[1] National Crime Records Bureau (NCRB), 'Crime in India 2022 -- Statistics Volume II: Cyber Crimes,' MHA, Govt. of India, New Delhi, 2023.\n"
        "[2] Indian Cyber Crime Coordination Centre (I4C), 'Citizen Financial Cyber Fraud Reporting System (CFCFRMS / 1930) Review,' MHA, 2024.\n"
        "[3] Reserve Bank of India (RBI), 'Annual Report 2023-24: Assessment of Frauds in the Banking Sector,' RBI, Mumbai, 2024.\n"
        "[4] E. R. Leukfeldt, E. R. Kleemans, and W. P. Stol, 'Cybercriminal Networks, Social Ties and Online Forums,' Br. J. Criminol., vol. 57, 2017.\n"
        "[5] S. Chainey, L. Tompson, and S. Uhlig, 'The Utility of Hotspot Mapping for Predicting Spatial Patterns of Crime,' Security Journal, vol. 21, 2008.\n"
        "[6] Y.-L. Lin, M.-F. Yen, and L.-C. Yu, 'Grid-Based Crime Prediction Using Geographical Features,' ISPRS Int. J. Geo-Inf., vol. 7, no. 8, 2018.\n"
        "[7] A. Bogomolov et al., 'Once Upon a Crime: Towards Crime Prediction from Demographics and Mobile Data,' ACM ICMI, 2014.\n"
        "[8] G. O. Mohler et al., 'Self-Exciting Point Process Modeling of Crime,' Journal of the American Statistical Association, vol. 106, 2011.\n"
        "[9] A. P. Wheeler and W. Steenbeek, 'Mapping the Risk Terrain for Crime Using Machine Learning,' J. Quant. Criminol., vol. 37, 2021.\n"
        "[10] Y. Lee, S. O, and J. E. Eck, 'A Theory-Driven Algorithm for Real-Time Crime Hot Spot Forecasting,' Police Quarterly, vol. 23, 2020.\n"
        "[11] M. Ester, H.-P. Kriegel, J. Sander, and X. Xu, 'A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases,' ACM KDD, 1996.\n"
        "[12] D. Birant and A. Kut, 'ST-DBSCAN: An Algorithm for Clustering Spatial-Temporal Data,' Data & Knowledge Engineering, vol. 60, 2007.\n"
        "[13] M. Adepeju, G. Rosser, and T. Cheng, 'Novel Evaluation Metrics for Sparse Point Process Predictions,' IJGIS, vol. 30, 2016.\n"
        "[14] V. M. White, J. Hunt, and B. Green, 'A Discussion of Current Crime Forecasting Indices (PEI),' Security Journal, vol. 36, 2023.\n"
        "[15] H. S. Assumpção et al., 'DELATOR: Money Laundering Detection on Large Transaction Graphs,' IEEE Big Data, 2022.\n"
        "[16] D. Ensign, S. A. Friedler et al., 'Runaway Feedback Loops in Predictive Policing,' PMLR FAT*, vol. 81, 2018.\n"
        "[17] K. Lum and W. Isaac, 'To Predict and Serve?,' Significance, vol. 13, no. 5, pp. 14-19, 2016.\n"
        "[18] S. M. Lundberg and S.-I. Lee, 'A Unified Approach to Interpreting Model Predictions,' NeurIPS, vol. 30, 2017.\n"
        "[19] E. A. Lopez-Rojas et al., 'PaySim: A Financial Mobile Money Simulator for Fraud Detection,' EMSS, 2016."
    )
    page14.insert_textbox(pymupdf.Rect(50, y, 545, 790), refs_text, fontsize=7.6, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_LEFT)
    
    doc.save(pdf_path)
    doc.close()
    print(f"Master Capstone Thesis compiled successfully: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    build_master_pdf()
