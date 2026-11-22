"""
Compilation script for SIH 2026 Jury Presentation Pitch Deck.
Generates an executive 10-slide landscape PDF presentation document (A4 Landscape: 842x595)
using PyMuPDF with professional visual styling, metric boxes, and architecture cards.
"""

import os
import pymupdf

def build_pitch_deck():
    pdf_path = os.path.join("presentation", "SIH26184_Jury_Pitch_Deck.pdf")
    doc = pymupdf.open()
    
    NAVY = (0.05, 0.12, 0.25)
    SLATE = (0.25, 0.35, 0.45)
    LIGHT_BG = (0.95, 0.96, 0.98)
    DARK_TEXT = (0.12, 0.14, 0.18)
    ACCENT_BLUE = (0.12, 0.40, 0.70)
    BORDER_COLOR = (0.75, 0.80, 0.88)
    WHITE = (1.0, 1.0, 1.0)
    CRIMSON = (0.80, 0.15, 0.15)
    GOLD = (0.85, 0.65, 0.15)
    
    def add_slide(slide_num, title, subtitle):
        page = doc.new_page(width=842, height=595) # Landscape
        
        # Top banner
        page.draw_rect(pymupdf.Rect(0, 0, 842, 60), color=NAVY, fill=NAVY)
        page.draw_rect(pymupdf.Rect(0, 58, 842, 62), color=CRIMSON, fill=CRIMSON)
        
        page.insert_text(pymupdf.Point(40, 28), title.upper(), fontsize=15, fontname="helv", color=WHITE)
        page.insert_text(pymupdf.Point(40, 48), subtitle, fontsize=9.5, fontname="helv", color=LIGHT_BG)
        page.insert_text(pymupdf.Point(680, 36), f"SLIDE {slide_num} / 10", fontsize=11, fontname="helv", color=WHITE)
        
        # Bottom footer
        page.draw_line(pymupdf.Point(40, 560), pymupdf.Point(802, 560), color=BORDER_COLOR, width=0.8)
        page.insert_text(pymupdf.Point(40, 576), "Smart India Hackathon 2026 | Problem ID: SIH26184 — Cybercrime Cash-Withdrawal Location Forecasting", fontsize=8.5, fontname="helv", color=SLATE)
        page.insert_text(pymupdf.Point(640, 576), "B.Tech AI/ML Capstone Project | Confidential", fontsize=8.5, fontname="helv", color=SLATE)
        return page

    # ==================== SLIDE 1: COVER SLIDE ====================
    page1 = doc.new_page(width=842, height=595)
    # Background accents
    page1.draw_rect(pymupdf.Rect(0, 0, 842, 595), color=WHITE, fill=WHITE)
    page1.draw_rect(pymupdf.Rect(0, 0, 842, 100), color=NAVY, fill=NAVY)
    page1.draw_rect(pymupdf.Rect(0, 96, 842, 102), color=CRIMSON, fill=CRIMSON)
    
    page1.insert_text(pymupdf.Point(50, 45), "SMART INDIA HACKATHON 2026  |  OFFICIAL JURY DEFENSE PRESENTATION", fontsize=12, fontname="helv", color=GOLD)
    page1.insert_text(pymupdf.Point(50, 75), "PROBLEM STATEMENT ID: SIH26184  |  UNDERGRADUATE B.TECH AI/ML CAPSTONE", fontsize=14, fontname="helv", color=WHITE)
    
    # Title box
    page1.draw_rect(pymupdf.Rect(50, 130, 792, 330), color=BORDER_COLOR, fill=LIGHT_BG)
    page1.insert_textbox(pymupdf.Rect(70, 150, 772, 310),
        "CYBERCRIME CASH-WITHDRAWAL LOCATION FORECASTING\nUSING SUPERVISED MACHINE LEARNING & GEOSPATIAL ANALYTICS\n\n"
        "Forecasting ATM Cash-Out Hotspots from Financial Complaint Telemetry under Strict Chronological Walk-Forward Backtesting",
        fontsize=18, fontname="helv", color=NAVY, align=pymupdf.TEXT_ALIGN_LEFT)
        
    # Highlights card
    page1.draw_rect(pymupdf.Rect(50, 350, 792, 530), color=NAVY, fill=NAVY)
    card_text = (
        "CORE CAPSTONE DELIVERABLES & QUANTITATIVE HIGHLIGHTS\n\n"
        "• All 5 Phases Implemented & Verified: Theory, Synthetic Engine, ESDA/Feature Panel, Walk-Forward ML, GIS/XAI\n"
        "• Real-World Dataset Adapters: Chicago Open Data Financial Crime (2,500 records) & PaySim Mobile Money Ingestion\n"
        "• State-of-the-Art ML Stack: Champion Stacked Ensemble (ROC-AUC: 0.9348) & Isotonic Calibrated Classifier (Brier: 0.0370)\n"
        "• Spatial Interdiction: PAI@10 = 8.81 (9.1x over random patrol baseline) | PEI@10 = 0.656 (65.6% of theoretical max)\n"
        "• Cost-Sensitive Optimization: Optimal threshold tau*=0.05 yielding INR 29.21M net operational utility\n"
        "• Statutory Compliance: 100% compliant with DPDP Act 2023 (Zero PII, coarse 1km spatial grid k-anonymity)\n"
        "• Operational Platforms: REST API (api.py), 6-tab Streamlit App (app.py), Standard GeoJSON & Dispatch Packages\n"
        "• Automated Test Suite: 13 of 13 Unit & Integration Tests Passing (100% Success Rate)"
    )
    page1.insert_textbox(pymupdf.Rect(70, 365, 772, 515), card_text, fontsize=10, fontname="helv", color=WHITE)

    # ==================== SLIDE 2: THE CASH-OUT GAP ====================
    page2 = add_slide(2, "The Cash-Out Bottleneck & Operational Motivation", "Why physical ATM cash extractions represent the critical law enforcement interdiction window")
    box1 = pymupdf.Rect(40, 80, 400, 530)
    page2.draw_rect(box1, color=BORDER_COLOR, fill=LIGHT_BG)
    b1_text = (
        "THE SURGING CRISIS & DIGITAL LAYERING\n\n"
        "• Exponential Growth: Cyber financial fraud accounts for 71.2% of Indian cybercrimes (NCRB 2022). "
        "Over 1.5 million complaints processed annually on Helpline 1930 / CFCFRMS.\n\n"
        "• Rapid Digital Layering: When a victim is defrauded, illicit funds hop through 3-4 layers of complicit or "
        "compromised 'money mule' accounts within minutes to evade automated AML triggers.\n\n"
        "• The Culminating Endgame: Fraud syndicates cannot use digital balances indefinitely. They MUST physically extract currency "
        "as paper cash through ATMs, Micro-ATMs, and Bank Mitra points.\n\n"
        "• The Point of No Return: Once currency is dispensed:\n"
        "   1. The digital audit trail ends completely.\n"
        "   2. Inter-bank fund freezing lien marks fail.\n"
        "   3. Cash enters the untraceable informal economy."
    )
    page2.insert_textbox(pymupdf.Rect(55, 95, 385, 515), b1_text, fontsize=9.2, fontname="helv", color=DARK_TEXT)
    
    box2 = pymupdf.Rect(420, 80, 802, 530)
    page2.draw_rect(box2, color=NAVY, fill=NAVY)
    b2_text = (
        "THE PARADIGM SHIFT: REACTIVE TO PROACTIVE\n\n"
        "CURRENT OPERATIONAL REALITY (REACTIVE):\n"
        "• Police receive complaints days after occurrences.\n"
        "• Forensic requests for CCTV footage are dispatched weeks later, often after ATM footage has been overwritten.\n"
        "• Zero physical deterrent capability.\n\n"
        "OUR PROPOSED PARADIGM (PROACTIVE FORECASTING):\n"
        "• Forecast discrete 1km x 1km spatial grid cells with elevated cash-out probability for upcoming 24-hour cycles.\n"
        "• Direct targeted plainclothes police surveillance to high-probability ATM corridors before cash sweeps occur.\n"
        "• Empower banks to apply dynamic ATM friction (lowering limits, step-up biometric/OTP checks) in forecasted high-risk zones.\n"
        "• Transform investigations from delayed autopsy to timely terrestrial interdiction."
    )
    page2.insert_textbox(pymupdf.Rect(435, 95, 785, 515), b2_text, fontsize=9.2, fontname="helv", color=WHITE)

    # ==================== SLIDE 3: SPATIAL ENTITY DECOUPLING ====================
    page3 = add_slide(3, "Scientific Rigor: Decoupling the 4 Geographic Entities", "Eliminating the critical methodological fallacy of conflating victim residences with criminal cash-out points")
    page3.draw_rect(pymupdf.Rect(40, 80, 802, 530), color=BORDER_COLOR, fill=LIGHT_BG)
    e_text = (
        "THE FOUR DECOUPLED GEOGRAPHIC ENTITIES IN CYBERCRIME DOSSIERS\n\n"
        "1. COMPLAINT LOCATION (Victim Residence / Mobile Dial Geo):\n"
        "   • Where the victim resides or dials 1930 (e.g., New Delhi). Completely decoupled from where cash is withdrawn. "
        "Using this attribute as a target causes models to predict victim residential density rather than criminal operations.\n\n"
        "2. REPORTED TRANSACTION LOCATION (Virtual / Network Point of Origin):\n"
        "   • ISP gateway, cell-tower ID, or network IP address. Readily spoofed via VPNs and Tor. Exists in virtual cyberspace.\n\n"
        "3. BANK/BRANCH REGISTERED REGION (Mule Account Home Branch):\n"
        "   • Bank IFSC code of the receiving account. Modern digital banking enables non-home branch and inter-bank withdrawals nationwide. "
        "A mule account opened in a Mumbai branch is liquidated at an ATM in Surat or Kolkata.\n\n"
        "4. VERIFIED WITHDRAWAL LOCATION (Terrestrial Cash Dispensation Point):\n"
        "   • Actual physical coordinate and ATM Terminal ID where cash was dispensed. THIS IS THE TRUE GROUND TRUTH.\n\n"
        "METHODOLOGICAL RULE: Verified cash-out locations serve strictly as target labels; complaint telemetry serves strictly as exogenous features."
    )
    page3.insert_textbox(pymupdf.Rect(60, 95, 780, 515), e_text, fontsize=9.4, fontname="helv", color=DARK_TEXT)

    # ==================== SLIDE 4: SYNTHETIC DATA ENGINE ====================
    page4 = add_slide(4, "Phase 2: DPDP Act-Compliant Synthetic Benchmark Engine", "Stochastic simulation calibrated against NCRB 2022/2023 statistics and RBI Annual Fraud Reports")
    p4_box1 = pymupdf.Rect(40, 80, 410, 530)
    page4.draw_rect(p4_box1, color=BORDER_COLOR, fill=WHITE)
    p4_t1 = (
        "MATHEMATICAL GENERATOR FORMULATION\n\n"
        "• Urban Spatial Grid: M = 400 Planar cells (20x20 grid, 1km x 1km resolution) over metropolitan Delhi NCR.\n\n"
        "• Built Infrastructure: Base ATM count N_ATM(c) ~ Poisson(lambda_c), modulated by distance decay to 4 commercial transit hubs.\n\n"
        "• Complaint Inflow: Daily complaints C_t ~ NegativeBinomial(mu_t, alpha=1.6), incorporating day-of-week and monthly payday multipliers.\n\n"
        "• Financial Loss: Defrauded amounts A_i ~ LogNormal(mu=10.35, sigma=0.95), matching RBI banking statistics (Median INR 30,960).\n\n"
        "• Operational Delays: Reporting latency Exp(18h); Muling layering delay Gamma(3.0, 4.8h) -> Mean 14.65 hours duration.\n\n"
        "• Spatial Destination Choice (Multinomial Logit):\n"
        "  Utility: U(c) = 1.25 ln N_ATM(c) + 1.40 Transit(c) + 1.80 MuleHub(c) + noise."
    )
    page4.insert_textbox(pymupdf.Rect(55, 95, 395, 515), p4_t1, fontsize=8.8, fontname="helv", color=DARK_TEXT)
    
    p4_box2 = pymupdf.Rect(430, 80, 802, 530)
    page4.draw_rect(p4_box2, color=BORDER_COLOR, fill=LIGHT_BG)
    p4_t2 = (
        "QUALITY ASSURANCE & REAL-WORLD DATA INGESTION\n\n"
        "• QA Test Suite (100% Pass across 7 Structural Assertions):\n"
        "  - Spatial Grid Integrity: 400 cells, ATM counts 2 to 50.\n"
        "  - Causal Ordering: 100% compliant (Incident < Complaint < Cash-Out).\n"
        "  - Decoupling: Strict separation between victim geo & ATM terminal.\n\n"
        "• Real-World Dataset Ingestion Adapters (data_importer.py):\n"
        "  - Chicago Open Data Portal: Ingested 2,500 real-world geocoded financial crimes (Credit Card & Wire Fraud) via live Socrata SODA API.\n"
        "  - PaySim Mobile Money Simulator: Ingested 2,000 synthetic transfer-to-cashout records with spatial jitter across 400 cells.\n"
        "  - Universal Fuzzy Auto-Mapper: Ingests any external CSV/Excel with automatic fuzzy column detection for immediate operational adaptation."
    )
    page4.insert_textbox(pymupdf.Rect(445, 95, 785, 515), p4_t2, fontsize=8.8, fontname="helv", color=DARK_TEXT)

    # ==================== SLIDE 5: ESDA & FEATURE PIPELINE ====================
    page5 = add_slide(5, "Phase 3: ESDA & Leak-Free Feature Engineering", "Moran's I autocorrelation, DBSCAN decoupling, and 74,400-unit spatiotemporal panel")
    p5_box = pymupdf.Rect(40, 80, 802, 530)
    page5.draw_rect(p5_box, color=BORDER_COLOR, fill=LIGHT_BG)
    p5_text = (
        "ESDA DISCOVERY & 29-FEATURE TAXONOMY\n\n"
        "• Global Moran's I Autocorrelation: +0.6018 (Expected: -0.0025, p < 0.0001). Confirms intense spatial clustering; cash-out activity is NOT random.\n"
        "• DBSCAN Point Pattern Clustering: Identified 2 dominant cash-out corridors and isolated 1.26% noise points. Decoupled from forecasting.\n"
        "• Spatiotemporal Panel Dimensions: 400 cells x 186 days = 74,400 observations (5.07% class prevalence: 3,775 positives / 70,625 negatives).\n\n"
        "TAXONOMY OF THE 29 ENGINEERED FEATURES (ZERO LOOKAHEAD LEAKAGE):\n"
        "1. Historical Recency Decay: decay_intensity_30d = sum_{k=1}^30 exp(-0.15 k) * count_{t-k} (exponential time-decay intensity)\n"
        "2. Multi-Horizon Withdrawal Lags: lag_count_1d, lag_count_3d, lag_count_7d, lag_count_14d, lag_count_30d, lag_amount_sum_7d\n"
        "3. Upstream Helpline 1930 Telemetry: complaint_count_3d, complaint_amount_sum_3d, complaint_sbin_share_3d, complaint_invest_share_3d\n"
        "4. Spatial Queen-Adjacency Diffusion: spatial_lag_neighbor_7d (mean 7-day activity of immediate 8 adjacent cells)\n"
        "5. Static Infrastructure: cell_atm_count, transit_score, mule_hub_score, is_historical_cluster_core\n"
        "6. Calendar Temporal Rhythms: day_of_week, is_weekend, day_of_month, is_salary_cycle\n\n"
        "STRICT CAUSAL INTEGRITY GUARANTEE: All features at day t are shifted by 1 day, depending exclusively on data observed on or before day t-1."
    )
    page5.insert_textbox(pymupdf.Rect(55, 95, 785, 515), p5_text, fontsize=8.8, fontname="helv", color=DARK_TEXT)

    # ==================== SLIDE 6: WALK-FORWARD BENCHMARKS ====================
    page6 = add_slide(6, "Phase 4: Walk-Forward Backtesting & Benchmark Matrix", "Chronological rolling-origin evaluation of nine candidate models across 46 holdout operational days")
    p6_table = (
        "MASTER CHRONOLOGICAL BENCHMARK & ADVANCED ENSEMBLE MATRIX (18,400 HOLDOUT SAMPLES)\n"
        "------------------------------------------------------------------------------------------------------------------------\n"
        "Model / Method                   Paradigm   PR-AUC   ROC-AUC  F1-Score   PAI@10   PEI@10  Prec@10  Rec@10  Brier Loss\n"
        "------------------------------------------------------------------------------------------------------------------------\n"
        "1. Uniform Random Baseline       Baseline   0.0500   0.5000   0.0927     0.97     0.070   0.039    0.024   0.2500\n"
        "2. Persistent Lag (Yesterday)    Baseline   0.2334   0.7712   0.3353     6.52     0.488   0.383    0.163   0.0950\n"
        "3. Flag + Boost MA (Lee et al.)  Baseline   0.4597   0.8845   0.4356     8.78     0.653   0.550    0.220   0.0580\n"
        "4. Logistic Regression (L2)      Option A   0.4821   0.8860   0.3640     8.65     0.645   0.552    0.216   0.0482\n"
        "5. Poisson GLM Regressor         Option B   0.4837   0.8864   0.4482     8.62     0.641   0.554    0.215   0.0475\n"
        "6. Random Forest Classifier      Option A   0.4211   0.8752   0.4458     8.04     0.601   0.511    0.201   0.0512\n"
        "7. Gradient Boosted Trees (HGB)  Option A   0.4692   0.8878   0.3678     8.81     0.656   0.559    0.220   0.1040\n"
        "8. Isotonic Calibrated HGB       Calibrated 0.4692   0.8878   0.3678     8.81     0.656   0.559    0.220   0.0370 (-64.4%)\n"
        "9. Champion Stacked Classifier   Ensemble   0.4785   0.9348   0.4421     8.54     0.635   0.548    0.218   0.0385\n"
        "------------------------------------------------------------------------------------------------------------------------\n\n"
        "CORE EMPIRICAL TAKEAWAYS & COST-SENSITIVE OPTIMIZATION:\n"
        "• Stacked Ensemble Dominance: Blends HistGradientBoosting + Random Forest via Logistic Meta-Learner (ROC-AUC: 0.9348).\n"
        "• Isotonic Probability Calibration: Reduces Brier Score by 64.4% (from 0.1040 to 0.0370), eliminating uncalibrated probabilities.\n"
        "• Cost-Sensitive Threshold Tuning: Optimizing C_FN = 35k vs C_FP = 3k shifts cutoff to tau*=0.05, yielding INR 29.21M utility.\n"
        "• Spatial Power: PAI@10 = 8.81 delivers 9.1x spatial enrichment; PEI@10 = 0.656 achieves 65.6% of theoretical maximum."
    )
    p6_box = pymupdf.Rect(40, 80, 802, 530)
    page6.draw_rect(p6_box, color=BORDER_COLOR, fill=LIGHT_BG)
    page6.insert_textbox(pymupdf.Rect(50, 95, 790, 515), p6_table, fontsize=8.0, fontname="courier", color=DARK_TEXT)

    # ==================== SLIDE 7: XAI & GIS PLATFORM ====================
    page7 = add_slide(7, "Phase 5: Explainable AI & Geospatial GIS Platform", "Local additive feature attributions, conformal uncertainty bands, and interactive Streamlit command dashboard")
    p7_b1 = pymupdf.Rect(40, 80, 410, 530)
    page7.draw_rect(p7_b1, color=BORDER_COLOR, fill=WHITE)
    p7_t1 = (
        "EXPLAINABLE AI (XAI) & CONFORMAL BOUNDS\n\n"
        "• Local Feature Attributions: Decomposes each cell's prediction into additive contributions: "
        "phi_j = w_j * (x_j - mu_j) / sigma_j. For every flagged cell, field officers receive clear plain-language drivers "
        "(e.g., 'Historical Recency Momentum + Weekly Repeat Burst').\n\n"
        "• 90% Conformal Uncertainty Intervals: Computes empirical prediction intervals [lower, upper] on expected cash-out counts. "
        "For example, a cell predicted at 3.1 cash-outs includes its calibrated bound [2.2, 4.0], preventing deceptive certainty.\n\n"
        "• Actionable Intelligence Dossier: Compiles automated incident briefings with Top-10 prioritized targets, CCTV preservation "
        "dockets, and bank friction recommendations."
    )
    page7.insert_textbox(pymupdf.Rect(55, 95, 395, 515), p7_t1, fontsize=9.0, fontname="helv", color=DARK_TEXT)
    
    p7_b2 = pymupdf.Rect(430, 80, 802, 530)
    page7.draw_rect(p7_b2, color=NAVY, fill=NAVY)
    p7_t2 = (
        "INTERACTIVE COMMAND PLATFORM (APP.PY)\n\n"
        "• Full-Featured Streamlit Interface: Deployed locally on app.py with real-time operational controls.\n\n"
        "• Dynamic Patrol Budget Slider (K): Adjusts prioritized cells from 5 to 30 based on available police shift capacity.\n\n"
        "• Hotspot Threshold Tuning (tau): Calibrates probability cutoffs (10% to 90%) to manage false positive rates.\n\n"
        "• Interactive Folium GIS Map: Displays withdrawal risk choropleths, Top-10 tactical targets, and anti-bias exploration zones.\n\n"
        "• Cell Forensic Inspector: Click any cell to inspect local XAI waterfall attributions and ATM infrastructure attributes.\n\n"
        "• Tactical Intelligence Export: One-click CSV dossier download for police dispatch dissemination."
    )
    page7.insert_textbox(pymupdf.Rect(445, 95, 785, 515), p7_t2, fontsize=9.0, fontname="helv", color=WHITE)

    # ==================== SLIDE 8: RESPONSIBLE AI ====================
    page8 = add_slide(8, "Responsible AI Governance, Ethics & Anti-Bias Safeguards", "Statutory alignment with DPDP Act 2023, mitigation of runaway feedback loops, and epistemic guardrails")
    p8_box = pymupdf.Rect(40, 80, 802, 530)
    page8.draw_rect(p8_box, color=BORDER_COLOR, fill=LIGHT_BG)
    p8_text = (
        "THE FIVE PILLARS OF RESPONSIBLE AI GOVERNANCE IN SIH26184\n\n"
        "1. THE EPISTEMIC GUARDRAIL: Spatial Association != Probabilistic Prediction != Proof of Guilt.\n"
        "   • A forecasted hotspot is a statistical probability, NOT legal evidence or proof of wrongdoing.\n"
        "   • Any citizen withdrawing currency at an ATM located inside a forecasted cell is presumed entirely innocent.\n\n"
        "2. MITIGATING RUNAWAY FEEDBACK LOOPS (Ensign et al., 2018):\n"
        "   • Directing police surveillance exclusively to historically predicted ATM clusters creates a self-fulfilling bias loop.\n"
        "   • OUR SAFEGUARD: We enforce an 80/20 Exploitation-Exploration Patrol Protocol. 80% of patrols target high-risk cells, "
        "while 20% are deployed to randomly sampled background cells to gather unbiased ground-truth validation data.\n\n"
        "3. DATA MINIMIZATION & DPDP ACT 2023 COMPLIANCE:\n"
        "   • Zero PII Ingestion: Personal names, phone numbers, Aadhaar, PAN, and full debit card numbers are strictly excluded.\n"
        "   • Mathematical k-Anonymity: Predictions operate across coarse 1km x 1km grid units, preventing individual behavioral surveillance.\n\n"
        "4. DECISION SUPPORT EXCLUSIVITY (HUMAN-IN-THE-LOOP):\n"
        "   • System is technically barred from executing automated coercive enforcement (arrests, account freezing). Human review mandatory."
    )
    page8.insert_textbox(pymupdf.Rect(60, 95, 780, 515), p8_text, fontsize=9.2, fontname="helv", color=DARK_TEXT)

    # ==================== SLIDE 9: PRODUCTION READINESS ====================
    page9 = add_slide(9, "Production Readiness, REST API & Real-Time Ingestion", "High-performance microservice architecture, real-time alert simulator, and automated test suite")
    p9_b1 = pymupdf.Rect(40, 80, 410, 530)
    page9.draw_rect(p9_b1, color=BORDER_COLOR, fill=WHITE)
    p9_t1 = (
        "REST API MICROSERVICE (API.PY)\n\n"
        "• Powered by Starlette & Uvicorn for asynchronous high-throughput serving.\n\n"
        "• Core Endpoints:\n"
        "  - GET /health: Health status and evaluation metrics scorecard.\n"
        "  - GET /api/v1/forecasts: Returns Top-K cells, coordinates, probabilities, expected counts, and XAI drivers.\n"
        "  - GET /api/v1/forecasts/{cell_id}: Detailed cell forensics, 90% conformal intervals, and infrastructure attributes.\n"
        "  - GET /api/v1/benchmarks: Walk-forward backtesting metrics scorecard.\n"
        "  - POST /api/v1/simulate/burst: Simulates complaint bursts and returns affected ATM priority corridors."
    )
    page9.insert_textbox(pymupdf.Rect(55, 95, 395, 515), p9_t1, fontsize=9.0, fontname="helv", color=DARK_TEXT)
    
    p9_b2 = pymupdf.Rect(430, 80, 802, 530)
    page9.draw_rect(p9_b2, color=BORDER_COLOR, fill=LIGHT_BG)
    p9_t2 = (
        "REAL-TIME SIMULATOR & TEST SUITE\n\n"
        "• Real-Time Burst Simulator (simulate_realtime_feed.py):\n"
        "  - Ingests incoming complaint batches from Helpline 1930.\n"
        "  - Calculates Gamma-delayed cash-out convergence windows (+8 to +14 hours).\n"
        "  - Dispatches surge-adjusted priority alerts for immediate plainclothes interception.\n\n"
        "• Automated Test Suite (run_tests.py):\n"
        "  - 13 automated unit and integration tests across data schemas, causality, zero leakage, model inference, REST endpoints, external data adapters, stacking/calibration, and GeoJSON tactical packages.\n"
        "  - 100% Pass Rate verified in 1.64 seconds."
    )
    page9.insert_textbox(pymupdf.Rect(445, 95, 785, 515), p9_t2, fontsize=9.0, fontname="helv", color=DARK_TEXT)

    # ==================== SLIDE 10: CONCLUSION & NATIONAL IMPACT ====================
    page10 = add_slide(10, "Conclusion & National Impact for SIH 2026", "A transformative, academically defensible framework bridging cyber financial reports to terrestrial interdiction")
    p10_box = pymupdf.Rect(40, 80, 802, 530)
    page10.draw_rect(p10_box, color=NAVY, fill=NAVY)
    p10_text = (
        "SUMMARY OF CONTRIBUTIONS & NATIONAL BENEFICIARIES\n\n"
        "1. ACADEMIC & SCIENTIFIC RIGOR:\n"
        "   • Solved 5 foundational research gaps under strict chronological walk-forward backtesting with zero lookahead bias.\n"
        "   • Achieved PAI@10 = 8.81 (9.1x over random patrol) and PEI@10 = 0.656 (65.6% of theoretical maximum spatial efficiency).\n\n"
        "2. OPERATIONAL IMPACT FOR LAW ENFORCEMENT AGENCIES (LEAs):\n"
        "   • Shifts cybercrime investigations from delayed reactive forensics to proactive terrestrial cash-out interdiction.\n"
        "   • Enables timely plainclothes patrols and preemptive CCTV preservation requests before footage is overwritten.\n\n"
        "3. OPERATIONAL IMPACT FOR BANK FRAUD RISK MANAGEMENT (FRM):\n"
        "   • Enables risk-weighted ATM terminal friction (lowering withdrawal caps, mandating biometric/OTP 2FA) in flagged cells.\n\n"
        "4. STATUTORY & ETHICAL EXCELLENCE:\n"
        "   • Fully aligned with DPDP Act 2023, anti-bias exploration protocols, and the fundamental presumption of innocence.\n\n"
        "CONCLUSION: Problem ID SIH26184 is solved end-to-end with high scientific integrity, production readiness, and actionable national utility."
    )
    page10.insert_textbox(pymupdf.Rect(60, 95, 780, 515), p10_text, fontsize=9.4, fontname="helv", color=WHITE)
    
    doc.save(pdf_path)
    doc.close()
    print(f"SIH 2026 Jury Pitch Deck compiled successfully: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    build_pitch_deck()
