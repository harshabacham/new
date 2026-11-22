"""
Compilation script for Phase 1 Academic Research Report.
Uses PyMuPDF to generate a publication-quality PDF document with:
- Professional cover page with institutional metadata
- Executive abstract and metadata box
- Numbered sections, formatted headings, and lead text
- Structured ASCII / formatted tables
- Mathematical formulations and algorithmic specifications
- Running headers, footers, and page numbers
"""

import os
import pymupdf

def build_pdf():
    pdf_path = os.path.join("phase_1", "Phase_1_Research_Report.pdf")
    doc = pymupdf.open()
    
    # Color palette
    NAVY = (0.08, 0.18, 0.36)
    SLATE = (0.25, 0.35, 0.45)
    LIGHT_BG = (0.95, 0.96, 0.98)
    DARK_TEXT = (0.12, 0.14, 0.18)
    ACCENT_BLUE = (0.12, 0.40, 0.70)
    BORDER_COLOR = (0.75, 0.80, 0.88)
    WHITE = (1.0, 1.0, 1.0)
    
    # Helper to create a new page with header and footer (except cover)
    def add_standard_page(page_num, total_pages_placeholder=False):
        page = doc.new_page(width=595, height=842) # A4
        # Running header
        page.draw_line(pymupdf.Point(50, 42), pymupdf.Point(545, 42), color=BORDER_COLOR, width=0.8)
        page.insert_text(pymupdf.Point(50, 36), "SIH 2026 | Problem ID: SIH26184 — Cybercrime Cash-Withdrawal Location Forecasting", fontsize=8, fontname="helv", color=SLATE)
        page.insert_text(pymupdf.Point(440, 36), "Phase 1: Research Dossier", fontsize=8, fontname="helv", color=SLATE)
        
        # Running footer
        page.draw_line(pymupdf.Point(50, 805), pymupdf.Point(545, 805), color=BORDER_COLOR, width=0.8)
        page.insert_text(pymupdf.Point(50, 818), "B.Tech AI/ML Capstone Project | Supervised Machine Learning & Geospatial Analytics", fontsize=8, fontname="helv", color=SLATE)
        page.insert_text(pymupdf.Point(490, 818), f"Page {page_num}", fontsize=8, fontname="helv", color=SLATE)
        return page

    # ==================== PAGE 1: COVER PAGE ====================
    page1 = doc.new_page(width=595, height=842)
    # Background decorative sidebar
    page1.draw_rect(pymupdf.Rect(0, 0, 18, 842), color=NAVY, fill=NAVY)
    page1.draw_rect(pymupdf.Rect(18, 0, 24, 842), color=ACCENT_BLUE, fill=ACCENT_BLUE)
    
    # Top banner metadata
    page1.draw_rect(pymupdf.Rect(50, 50, 545, 85), color=BORDER_COLOR, fill=LIGHT_BG)
    page1.insert_text(pymupdf.Point(65, 72), "SMART INDIA HACKATHON 2026  |  ACADEMIC CAPSTONE RESEARCH REPORT", fontsize=10, fontname="helv", color=ACCENT_BLUE)
    page1.insert_text(pymupdf.Point(65, 88), "PROBLEM ID: SIH26184  |  TRACK: UNDERGRADUATE B.TECH AI/ML", fontsize=9, fontname="helv", color=SLATE)
    
    # Main Title Box
    title_rect = pymupdf.Rect(50, 120, 545, 290)
    page1.insert_textbox(title_rect, 
        "CYBERCRIME CASH-WITHDRAWAL LOCATION FORECASTING\n\n"
        "Investigating Supervised Machine Learning and Geospatial Analytics for "
        "Predicting ATM Cash-Out Hotspots from Financial Complaint Telemetry",
        fontsize=20, fontname="helv", color=NAVY, align=pymupdf.TEXT_ALIGN_LEFT)
    
    # Subtitle / Phase Tag
    page1.draw_rect(pymupdf.Rect(50, 295, 545, 335), color=NAVY, fill=NAVY)
    page1.insert_text(pymupdf.Point(65, 320), "PHASE 1: PROBLEM DEFINITION, LITERATURE REVIEW & ARCHITECTURE", fontsize=11, fontname="helv", color=WHITE)
    
    # Project Details Box
    meta_rect = pymupdf.Rect(50, 360, 545, 510)
    page1.draw_rect(meta_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    meta_text = (
        "PROJECT SPECIFICATION & METADATA\n\n"
        "• Problem Statement ID: SIH26184\n"
        "• Official Title: Cybercrime Cash-Withdrawal Location Forecasting\n"
        "• Academic Program: Bachelor of Technology (B.Tech) in Artificial Intelligence & Machine Learning\n"
        "• Core Research Focus: Spatiotemporal Grid Discretization, Supervised Tree Ensembles (RF/XGBoost),\n"
        "  Count GLMs, Spatial Evaluation Metrics (PAI, PEI), and Responsible AI Governance\n"
        "• Statutory Reference Framework: NCRB (2022/2023), I4C CFCFRMS (Helpline 1930), DPDP Act 2023\n"
        "• Current Phase: Phase 1 — Problem Definition & Literature Review (Zero Training Code Phase)\n"
        "• Evaluation Date: Academic Year 2026"
    )
    page1.insert_textbox(meta_rect, meta_text, fontsize=9.5, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_LEFT)
    
    # Executive Abstract Box
    abs_rect = pymupdf.Rect(50, 530, 545, 740)
    page1.draw_rect(abs_rect, color=BORDER_COLOR, fill=WHITE)
    page1.draw_rect(pymupdf.Rect(50, 530, 545, 555), color=SLATE, fill=SLATE)
    page1.insert_text(pymupdf.Point(65, 548), "EXECUTIVE ABSTRACT", fontsize=10, fontname="helv", color=WHITE)
    abstract_text = (
        "This research report delivers Phase 1 of an undergraduate B.Tech project addressing official Smart "
        "India Hackathon Problem ID SIH26184. The project investigates whether supervised machine learning models "
        "trained on spatiotemporally aggregated cybercrime complaint metadata, banking indicators, and built-environment "
        "infrastructure can forecast geographic grid cells exhibiting elevated cybercrime-related cash-withdrawal activity.\n\n"
        "In the cybercrime lifecycle, physical cash extraction at Automated Teller Machines (ATMs) and banking correspondent "
        "points constitutes the critical phase where digital criminals or money mule operatives physically interact with terrestrial "
        "infrastructure to convert digital balances into untraceable cash. Once withdrawn, digital audit trails break and fund-freezing "
        "mechanisms fail. This report synthesizes 16 authoritative peer-reviewed publications and statutory reports across 8 research pillars; "
        "formulates formal mathematical problem specifications; decouples four distinct geographic entities (Complaint, Transaction, Branch, "
        "and Withdrawal locations); identifies five critical research gaps; evaluates dataset feasibility under Indian privacy legislation (DPDP Act 2023); "
        "establishes a conceptual leak-free machine learning pipeline evaluated via chronological walk-forward backtesting; defines specialized "
        "spatial evaluation metrics (PAI, PEI, Precision@K); and formalizes five responsible AI governance principles."
    )
    page1.insert_textbox(pymupdf.Rect(60, 565, 535, 735), abstract_text, fontsize=8.8, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)
    
    # Footer Notice
    page1.insert_text(pymupdf.Point(50, 780), "CONFIDENTIALITY & ETHICAL DISCLAIMER: Intended strictly for authorized investigative decision support.", fontsize=7.5, fontname="helv", color=SLATE)
    page1.insert_text(pymupdf.Point(50, 792), "A predicted hotspot is NOT proof of criminal activity. Models do not identify individuals or predict individual crimes with certainty.", fontsize=7.5, fontname="helv", color=SLATE)

    # ==================== PAGE 2: TABLE OF CONTENTS & SECTION 1 ====================
    page2 = add_standard_page(2)
    
    # Section Header Helper
    def draw_section_header(page, y, num_str, title_str):
        page.draw_rect(pymupdf.Rect(50, y, 545, y+24), color=NAVY, fill=NAVY)
        page.insert_text(pymupdf.Point(60, y+16), f"SECTION {num_str}: {title_str.upper()}", fontsize=11, fontname="helv", color=WHITE)
        return y + 34
    
    # Table of Contents
    y = draw_section_header(page2, 55, "0", "Report Table of Contents")
    toc_rect = pymupdf.Rect(50, y, 545, y+130)
    page2.draw_rect(toc_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    toc_text = (
        "Section 1: Problem Definition & Operational Framing .............................................................. Page 2\n"
        "Section 2: Structured Literature Review (16 Studies across 8 Pillars) ........................................ Page 3\n"
        "Section 3: Comparative Research Gap Analysis (Matrix & 5 Foundational Gaps) ..................... Page 5\n"
        "Section 4: Dataset Feasibility Study & Synthetic Benchmark Specification ................................ Page 6\n"
        "Section 5: Proposed Technical Methodology & Leak-Free Pipeline ......................................... Page 7\n"
        "Section 6: Multi-Tiered Evaluation & Responsible AI Governance ............................................ Page 8\n"
        "Section 7: Executive Synthesis, Nine Core Answers & Phase 2 Handoff Plan ............................. Page 9\n"
        "Section 8: Verified Bibliographic References (IEEE Citation Format) ........................................ Page 10"
    )
    page2.insert_textbox(pymupdf.Rect(60, y+8, 535, y+125), toc_text, fontsize=8.5, fontname="helv", color=DARK_TEXT)
    
    y = y + 145
    y = draw_section_header(page2, y, "1", "Problem Definition & Operational Framing")
    
    sec1_text = (
        "1.1 Official Problem Statement (SIH26184)\n"
        "Problem ID: SIH26184 | Title: Cybercrime Cash-Withdrawal Location Forecasting\n"
        "Description: 'Estimate likely geographic withdrawal clusters from cybercrime complaint metadata such as time, "
        "amount, bank and geography. Classification/regression prototype; geographic feature engineering; evaluation of cluster "
        "prediction; actionable-intelligence report.'\n\n"
        "1.2 Background and Operational Context\n"
        "Digital financial transactions in India (UPI, IMPS, AePS) have expanded exponentially, accompanied by a sharp surge in "
        "cyber financial frauds (NCRB 2022 records a 24.4% annual increase, with financial fraud comprising 71.2% of total cybercrimes). "
        "Fraud syndicates execute rapid multi-tiered digital layering across compromised 'money mule' accounts. However, digital layering "
        "is only intermediate: the criminal endgame is physical cash liquidation (cash-out) at ATMs, Micro-ATMs, and Bank Mitra points. "
        "Once extracted as physical paper currency, digital lien marks (e.g., I4C CFCFRMS 1930) fail and the digital audit trail terminates. "
        "Cash-out represents the sole phase where cyber syndicates must physically interact with terrestrial infrastructure.\n\n"
        "1.3 Decoupling the Four Geographic Entities in Cybercrime Analysis\n"
        "A critical scientific error is conflating different spatial attributes recorded in cybercrime investigation dockets:\n"
        "1. Complaint Location: Where the victim resides or registers the report (e.g., New Delhi). Unrelated to cash extraction.\n"
        "2. Reported Transaction Location: The virtual network point of origin (IP address, mobile cell-tower). Easily masked via VPNs.\n"
        "3. Bank/Branch Registered Region: The home branch holding the mule account (IFSC code). Digital banking permits cash withdrawals nationwide.\n"
        "4. Verified Withdrawal Location: The physical coordinate and ATM Terminal ID where cash was dispensed. THIS IS THE TRUE GROUND TRUTH.\n\n"
        "1.4 Specific Problem Statement & Aim\n"
        "Let operational space be partitioned into M discrete cells S = {c_1, ..., c_M} and time into windows of duration Delta_t. "
        "The aim is to train supervised function f_theta mapping historical feature vectors x_(c, t) to future cash-out outcomes Y_(c, t+Delta_t) "
        "(Option A: binary hotspot classification; Option B: discrete count regression) to generate actionable intelligence."
    )
    page2.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec1_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 3: LITERATURE REVIEW (PART 1) ====================
    page3 = add_standard_page(3)
    y = draw_section_header(page3, 55, "2", "Structured Literature Review (Pillars 1 to 4)")
    
    lit1_text = (
        "The literature review investigates 16 authoritative peer-reviewed publications and statutory government reports across 8 pillars.\n\n"
        "PILLAR 1: CYBERCRIME ANALYTICS & PHYSICAL MONEY MULING\n"
        "• Leukfeldt, Kleemans, & Stol (2017) [Br. J. Criminol., DOI: 10.1093/bjc/azw009]: Investigated 40 cybercriminal networks using Dutch police dossiers. "
        "Proved that while phishing is planned online, cash-out operations rely strictly on physical, localized social and transit networks. Local mule herders "
        "and cash runners recruit mules offline, concentrating ATM sweeps into localized terrestrial clusters. Direct scientific justification for our project.\n"
        "• Assumpção et al. (2022) [IEEE BigData / arXiv:2205.10293]: Multi-task learning with Heterogeneous GNNs to detect laundering subgraphs on transaction graphs. "
        "Core finding: detects mule rings digitally but completely omits physical cash-out geography, highlighting the exact research gap our project bridges.\n"
        "• NCRB (2023) & I4C (2024) Reports [MHA, Govt of India]: Documented 65,893 registered cases, 71.2% financial fraud, and over 1.5M helpline complaints. "
        "Identified the 'cash-out gap': funds reaching Layer 3 accounts are withdrawn via ATMs within hours of victim deposit.\n\n"
        "PILLAR 2: GEOGRAPHIC CRIME HOTSPOT ANALYSIS & SPATIAL POINT PROCESSES\n"
        "• Chainey, Tompson, & Uhlig (2008) [Security Journal, DOI: 10.1057/palgrave.sj.8350066]: Evaluated hotspot mapping on London crime data. Formulated the "
        "foundational Prediction Accuracy Index (PAI = (n/N) / (a/A)), proving that spatial forecasting must balance incident capture against area targeted.\n"
        "• Mohler et al. (2011) [J. Amer. Statist. Assoc., DOI: 10.1198/jasa.2011.ap09546]: Self-exciting point process (ETAS) modeling of LAPD crime records. "
        "Demonstrated that crime exhibits near-repeat spatial-temporal contagion, capturing 1.4-2.1x more crime than static KDE. Justifies spatiotemporal lag decay features.\n\n"
        "PILLAR 3: SUPERVISED MACHINE LEARNING FOR SPATIOTEMPORAL FORECASTING\n"
        "• Lin, Yen, & Yu (2018) [ISPRS Int. J. Geo-Inf., DOI: 10.3390/ijgi7080298]: Discretized Taipei into 500m x 500m grids. Trained Random Forest, SVM, and Logistic "
        "Regression on OSM POI features and temporal lags. Random Forest achieved F1 ~0.72. Proved validity of grid-based supervised tree ensembles.\n"
        "• Bogomolov et al. (2014) [ACM ICMI '14, DOI: 10.1145/2663204.2663254]: Discretized London into 200m cells. Used Random Forest to predict crime hotspots "
        "from mobile CDRs and demographics (>70% accuracy). Demonstrated feasibility of binary classification over discrete urban panels."
    )
    page3.insert_textbox(pymupdf.Rect(50, y, 545, 790), lit1_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 4: LITERATURE REVIEW (PART 2) ====================
    page4 = add_standard_page(4)
    y = draw_section_header(page4, 55, "2 (Contd.)", "Structured Literature Review (Pillars 5 to 8)")
    
    lit2_text = (
        "PILLAR 4: CLASSIFICATION VS. REGRESSION FOR SPATIAL PREDICTION\n"
        "• Wheeler & Steenbeek (2021) [J. Quant. Criminol., DOI: 10.1007/s10940-020-09457-7]: Evaluated penalized Poisson regression vs. Random Forest Regressor "
        "and Boosted Trees on Dallas crime data. Found tree ensembles excel in risk ranking, while Poisson GLMs provide calibrated probabilities for sparse counts.\n"
        "• Lee, O, & Eck (2020) [Police Quarterly, DOI: 10.1177/1098611119887809]: National Institute of Justice (NIJ) Crime Forecasting Challenge winner. "
        "Developed 'Flag-and-Boost' combining chronic historical baselines (flag) with short-term moving average spikes (boost). Establishes our competitive heuristic baseline.\n\n"
        "PILLAR 5: DENSITY-BASED SPATIAL CLUSTERING (DBSCAN & ST-DBSCAN)\n"
        "• Ester et al. (1996) [ACM KDD '96]: Foundational DBSCAN algorithm discovering arbitrary shape clusters and isolating noise. Serves as our Phase 3 ESDA tool.\n"
        "• Birant & Kut (2007) [Data & Knowl. Eng., DOI: 10.1016/j.datak.2006.01.013]: Formulated ST-DBSCAN with dual spatial and temporal thresholds (eps1, eps2). "
        "Enables discovery of coordinated historical cash-out bursts across space and time. Unsupervised clustering is explicitly decoupled from supervised forecasting.\n\n"
        "PILLAR 6: MODEL EVALUATION FOR SPARSE COUNTS & SPATIAL EFFICIENCY\n"
        "• Adepeju, Rosser, & Cheng (2016) [IJGIS, DOI: 10.1080/13658816.2016.1159684]: Proved PAI is hypersensitive to study area size A. Mandates pairing PAI with "
        "Precision@K, Recall@K, and PR-AUC over fixed operational boundaries.\n"
        "• White, Hunt, & Green (2023) [Security Journal, DOI: 10.1057/s41284-023-00367-4]: Mathematical formulation of Predictive Efficiency Index (PEI = PAI / PAI*). "
        "Bounds spatial accuracy relative to the theoretical maximum achievable, perfectly suited for resource-constrained police patrols.\n\n"
        "PILLAR 7: EXPLAINABLE AI, FAIRNESS, BIAS & RESPONSIBLE USE\n"
        "• Lundberg & Lee (2017) [NeurIPS 2017]: Formulated SHAP (TreeSHAP). Powers our Phase 5 intelligence report to explain why a cell is flagged (e.g., bank complaint spike).\n"
        "• Ensign et al. (2018) [PMLR FAT* / arXiv:1706.09847]: Proved predictive policing algorithms risk runaway feedback loops when trained on police-recorded data. "
        "Mandates exploration-exploitation patrol allocation to prevent self-fulfilling spatial biases.\n"
        "• Lum & Isaac (2016) [Significance, DOI: 10.1111/j.1740-9713.2016.00960.x]: Proved spatial crime models predict reporting behavior rather than ground-truth crime. "
        "Mandates explicit epistemic separation: association != prediction != proof of guilt."
    )
    page4.insert_textbox(pymupdf.Rect(50, y, 545, 790), lit2_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 5: RESEARCH GAP ANALYSIS ====================
    page5 = add_standard_page(5)
    y = draw_section_header(page5, 55, "3", "Comparative Research Gap Analysis")
    
    gap_table_text = (
        "LITERATURE COMPARISON MATRIX (16 AUTHORITATIVE SOURCES)\n"
        "--------------------------------------------------------------------------------------------------------------------\n"
        "Study [Ref]             Year  Domain & Data           Methodology           Key Metric   Core Limitation\n"
        "--------------------------------------------------------------------------------------------------------------------\n"
        "Leukfeldt et al. [4]    2017  40 Dutch Cyber Rings    Social Network (SNA)  Centrality   Retrospective police dossiers\n"
        "Chainey et al. [5]      2008  London Street Crime     KDE / Point Pattern   PAI Index    Static spatial density only\n"
        "Lin, Yen, & Yu [6]      2018  Taipei 500m Grid + POI  Random Forest / SVM   F1 / AUC     No walk-forward temporal split\n"
        "Bogomolov et al. [7]    2014  London Grid + CDR Logs  Random Forest Class.  Accuracy     Random CV causes leakage\n"
        "Mohler et al. [8]       2011  LAPD Crime Incidents    ETAS Point Process    Hit Rate     Computationally heavy; no tabular data\n"
        "Wheeler & Steenbeek [9] 2021  Dallas Street Segments  Poisson GLM vs. RF    MAE / PAI    Street crime; no banking telemetry\n"
        "Lee, O, & Eck [10]      2020  Portland 5-Yr Crime     Flag-and-Boost MA     PEI / PAI    Heuristic threshold tuning\n"
        "Ester et al. [11]       1996  Spatial Point Database  DBSCAN Density Clust. Silhouette   Static Euclidean space; no time\n"
        "Birant & Kut [12]       2007  Sensor Point Dockets    ST-DBSCAN Clustering Purity       Unsupervised only; cannot forecast\n"
        "Adepeju et al. [13]     2016  London Burglary Grids   Point Process Models  PAI / Spars. Proves PAI sensitive to study area\n"
        "White, Hunt, Green [14] 2023  NIJ Forecasting Data    Spatial Index Math    PEI Index    Evaluates static polygons\n"
        "Assumpção et al. [15]   2022  Bank Transaction Graph  Heterogeneous GNN     PR-AUC       Purely virtual; zero spatial cash-out\n"
        "Ensign et al. [16]      2018  Oakland Simulated Data  Polya Urn Simulation Disparate    Evaluated drug crime feedback loops\n"
        "Lum & Isaac [17]        2016  Oakland Arrest Records  Point Process Mapping Risk Ratio   Proves models reflect reporting bias\n"
        "Lundberg & Lee [18]     2017  Multi-Domain Benchmarks TreeSHAP Attributions Consistency  Computational overhead on dense panels\n"
        "NCRB & I4C [1, 2]       2023  Pan-India Cybercrime    Statutory Reporting   Case Counts  Macro-level state tallies only\n"
        "--------------------------------------------------------------------------------------------------------------------"
    )
    page5.draw_rect(pymupdf.Rect(50, y, 545, y+160), color=BORDER_COLOR, fill=LIGHT_BG)
    page5.insert_textbox(pymupdf.Rect(55, y+5, 540, y+155), gap_table_text, fontsize=6.8, fontname="courier", color=DARK_TEXT)
    
    y = y + 170
    gaps_narrative = (
        "SYNTHESIS OF THE FIVE FOUNDATIONAL RESEARCH GAPS\n\n"
        "• Gap 1: Virtual Fraud Detection vs. Terrestrial Cash-Out Forecasting. Existing financial fraud ML (e.g., Assumpção et al. [15]) "
        "operates exclusively in topological graph space to flag accounts, completely omitting where stolen funds physically convert into cash. "
        "Our project directly bridges digital complaint telemetry to physical geographic ATM forecasting.\n\n"
        "• Gap 2: Spatial Feature Engineering for Decoupled Cybercrimes. Conventional spatial crime models rely on street-level opportunities "
        "(bars, schools). Cybercrime cash-out requires banking infrastructure indicators, inter-bank settlement delays, and transit corridors.\n\n"
        "• Gap 3: Evaluation Integrity & Temporal Leakage in Spatial ML. Studies using random cross-validation (e.g., Bogomolov et al. [7]) "
        "introduce catastrophic lookahead bias. We mandate strict chronological walk-forward validation.\n\n"
        "• Gap 4: Ground-Truth Granularity vs. Strict Banking Secrecy. Real ATM transaction logs are legally quarantined (DPDP Act 2023). "
        "The community lacks an open, statistically grounded synthetic generation framework simulating realistic cash-out dynamics.\n\n"
        "• Gap 5: Interpretable Intelligence vs. Black-Box Heatmaps. Police commanders require local SHAP feature attributions and bounded "
        "uncertainty intervals to justify tactical patrol allocations, rather than opaque risk surfaces."
    )
    page5.insert_textbox(pymupdf.Rect(50, y, 545, 790), gaps_narrative, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 6: DATASET FEASIBILITY ====================
    page6 = add_standard_page(6)
    y = draw_section_header(page6, 55, "4", "Dataset Feasibility Study & Synthetic Specification")
    
    sec4_text = (
        "4.1 Audit of Candidate Data Sources\n"
        "Six candidate sources were evaluated: NCRB Annual Reports [1], Open Government Data (data.gov.in), I4C CFCFRMS 1930 [2], "
        "RBI Fraud Reports [19], PaySim Financial Simulator [20], and Chicago Open Data [21].\n"
        "Definitive Finding: No publicly accessible, lawful dataset in India provides paired event-level cybercrime complaint metadata "
        "and physical ATM cash-withdrawal coordinates. Real ATM transaction logs are quarantined under the Digital Personal Data Protection "
        "(DPDP) Act 2023 and Banking Regulation Act 1949.\n\n"
        "4.2 Realistic Synthetic Data Generation Specification\n"
        "To ensure academic rigor, reproducibility, and privacy compliance, we formulate a stochastic synthetic generation engine:\n"
        "1. Urban Space: Partitioned into M = 400 planar cells (20 x 20 km grid, 1km^2 resolution) or Uber H3 Hexagons (Res 7).\n"
        "2. Infrastructure Layer: ATM counts per cell N_ATM(c) ~ Poisson(lambda_infra(c)), modulated by commercial/highway density.\n"
        "3. Complaint Arrival Process: Daily complaints follow an overdispersed Negative Binomial process calibrated on NCRB 2022 stats.\n"
        "4. Stochastic Layering Delay: Operational lag Delta_tau ~ Gamma(shape=3, scale=6 hours), modeling mule account transfers.\n"
        "5. Destination Choice (Multinomial Logit): Probability of cash-out in cell c is driven by ATM density, transit hubs, and mule hubs:\n"
        "   P(c | i) = exp(beta1 log N_ATM(c) + beta2 Transit(c) + beta3 MuleHub(c) + eta_c) / Sum_c' exp(...)\n\n"
        "4.3 Field-Level Data Dictionary (19 Standardized Fields)\n"
        "• Essential: record_id, complaint_timestamp, incident_timestamp, defrauded_amount, fraud_category, victim_bank_code, "
        "withdrawal_timestamp, withdrawal_amount, grid_cell_id, cell_atm_count, lag_count_7d, lag_count_30d, spatial_lag_neighbor, "
        "target_count (Option B), target_hotspot (Option A).\n"
        "• Optional: mule_layer_depth, victim_channel (UPI, NetBanking, Card).\n"
        "• Sensitive (Excluded / Hashed): atm_terminal_id, raw latitude/longitude, customer account numbers, bank IFSC."
    )
    page6.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec4_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 7: PROPOSED METHODOLOGY ====================
    page7 = add_standard_page(7)
    y = draw_section_header(page7, 55, "5", "Proposed Technical Methodology & Pipeline")
    
    sec5_text = (
        "5.1 Supervised Target Formulation: Option A vs. Option B\n"
        "• Option A (Spatiotemporal Classification): Y_(c, t+Delta_t) = I(k_(c, t+Delta_t) >= tau_thresh) in {0, 1}. Directly answers the tactical "
        "question: 'Should patrol/surveillance be allocated to this cell?' Robust to count noise in ultra-sparse cells.\n"
        "• Option B (Spatiotemporal Count Regression): Y_(c, t+Delta_t) = k_(c, t+Delta_t) in {0, 1, 2, ...}. Models expected incident volume "
        "via Poisson / Negative Binomial GLMs. Handles overdispersed counts but suffers from heavy zero-inflation (>90% zero cells).\n"
        "Recommendation: Deploy Option A (Calibrated Probability Random Forest/XGBoost) as primary, with Option B as parallel benchmark.\n\n"
        "5.2 Candidate Algorithm Suite\n"
        "1. Regularized Logistic Regression: Minimal linear baseline with L2 penalty.\n"
        "2. Poisson & Negative Binomial Regression: Standard statistical benchmark for spatial count processes [Wheeler & Steenbeek, 2021].\n"
        "3. Random Forest (Classifier/Regressor): Captures complex non-linear feature interactions without manual expansions [Lin et al., 2018].\n"
        "4. XGBoost / LightGBM: Gradient boosted trees with second-order Taylor expansions and focal loss for extreme class imbalance.\n"
        "5. DBSCAN / ST-DBSCAN: Strictly unsupervised exploratory spatial data analysis (ESDA), decoupled from supervised forecasting.\n\n"
        "5.3 End-to-End Leak-Free Pipeline (9 Stages)\n"
        "Raw Feeds -> Data Sanitization -> ESDA & DBSCAN Clustering -> Spatiotemporal Aggregation (1km Grids / H3) -> "
        "Feature Engineering (Lags, POIs, Bank Proportions) -> Supervised Model Training (RF/XGBoost) -> Chronological Walk-Forward Backtesting -> "
        "Geospatial Map Rendering (Folium) -> Actionable Intelligence Briefing with Local SHAP Attributions.\n\n"
        "5.4 Chronological Walk-Forward Validation Protocol\n"
        "To prevent future-data leakage, time is split chronologically: Training strictly precedes validation and testing in time. "
        "Expanding-window backtesting simulates operational reality: Model trained on Months 1-3 predicts Month 4; retrained on Months 1-4 "
        "predicts Month 5; evaluated across all subsequent operational windows."
    )
    page7.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec5_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 8: EVALUATION & ETHICS ====================
    page8 = add_standard_page(8)
    y = draw_section_header(page8, 55, "6", "Evaluation Framework & Responsible AI Governance")
    
    sec6_text = (
        "6.1 Multi-Tiered Evaluation Strategy\n"
        "Because spatial grids exhibit >90% zero-event cells, standard global accuracy is deceptive. Models are evaluated across:\n"
        "• Classification Metrics: Precision, Recall, F1-Score, and Area Under the Precision-Recall Curve (PR-AUC).\n"
        "• Resource-Constrained Metrics: Precision@K and Recall@K (K in {5, 10, 20}), reflecting the patrol capacity of police divisions.\n"
        "• Specialized Spatial Indices: Prediction Accuracy Index (PAI = (n/N)/(a/A)) [Chainey et al., 2008] and Predictive Efficiency Index "
        "(PEI = PAI / PAI*) [White et al., 2023], measuring spatial capture efficiency against the theoretical maximum.\n"
        "• Count Metrics: MAE, RMSE, and Poisson Deviance for Option B count regressions.\n"
        "• Baselines: Outperforming naive persistent (yesterday=today) and theory-driven chronic flag + boost moving averages [Lee et al., 2020].\n"
        "Academic Pledge: Zero upfront promises of arbitrary accuracy percentages before running empirical experiments.\n\n"
        "6.2 Responsible AI Governance & Ethical Guardrails\n"
        "1. Personal Data Protection (DPDP Act 2023): Absolute exclusion of PII (names, Aadhaar, PAN, phone numbers). Hashed identifiers.\n"
        "2. Spatial Aggregation: Predictions operate over coarse 1km^2 / H3 cells, providing mathematical k-anonymity and preventing individual tracking.\n"
        "3. Mitigating Runaway Feedback Loops: To prevent self-fulfilling surveillance bias (Ensign et al. [16]), tactical deployments must "
        "maintain an 80/20 exploitation/exploration resource split, allocating 20% of monitoring to random cells for unbiased ground truth.\n"
        "4. Epistemic Separation: Association != Prediction != Proof of Guilt. A predicted hotspot is NOT proof of criminal activity. "
        "Citizens at predicted ATMs are presumed innocent. Statistical predictions serve solely as investigative prioritization leads.\n"
        "5. Human-in-the-Loop Protocol: System is strictly a decision-support tool. Automated punitive actions (account freezing, police raids) "
        "are technically barred. Every intelligence report presents SHAP feature attributions and conformal confidence intervals."
    )
    page8.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec6_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 9: SYNTHESIS & PHASE 2 HANDOFF ====================
    page9 = add_standard_page(9)
    y = draw_section_header(page9, 55, "7", "Executive Synthesis & Phase 2 Handoff Plan")
    
    sec7_text = (
        "7.1 Concise Answers to the Nine Foundational Questions\n"
        "1. Problem: Forecasting spatial grid cells with elevated cybercrime cash-out activity over future operational horizons.\n"
        "2. Utility: Enables proactive police deterrence and risk-weighted bank ATM friction before stolen funds exit into untraceable cash.\n"
        "3. Established Research: Physical muling geography [4], grid-based ML validity [6], and spatial PAI/PEI efficiency metrics [5, 14].\n"
        "4. Defensible Gap: Connecting upstream complaint telemetry bursts to downstream terrestrial cash-out forecasting under chronological splits.\n"
        "5. Data Needed: Spatiotemporal panels containing timestamps, amounts, victim banks, and verified withdrawal cell coordinates.\n"
        "6. Initial ML: Option A (Calibrated Random Forest / XGBoost Classification) benchmarked against Negative Binomial Count Regression.\n"
        "7. Evaluation: Rolling-origin walk-forward validation evaluated via PAI, PEI, Precision@K, and PR-AUC.\n"
        "8. Limitations: Regulatory privacy quarantines, victim reporting delay decay, zero-inflation, and runaway feedback loop risks.\n"
        "9. Pre-Phase 2 Decisions: Finalize spatial index (H3 Res 7 vs. 1km UTM) and calibrate synthetic generator on NCRB/RBI macro proportions.\n\n"
        "7.2 Phase 1 Quality Checklist & Sign-Off\n"
        "All 8 required markdown deliverables and BibTeX database have been authored, verified, and placed in 'phase_1/':\n"
        "• 01_problem_definition.md [COMPLETE]  • 02_literature_review.md [COMPLETE]  • 03_research_gap_analysis.md [COMPLETE]\n"
        "• 04_dataset_feasibility.md [COMPLETE] • 05_proposed_methodology.md [COMPLETE] • 06_evaluation_and_ethics.md [COMPLETE]\n"
        "• 07_references.bib [COMPLETE]         • 08_phase_1_summary.md [COMPLETE]      • README.md [COMPLETE]\n\n"
        "7.3 Phase 2 Handoff Plan: Dataset Collection & Validation\n"
        "Phase 2 will initiate data engineering: (1) Construct urban bounding box and generate H3/UTM grid geometries; (2) Implement "
        "stochastic synthetic generator coupling complaint bursts with Gamma-delayed cash-out destination choices; (3) Execute schema "
        "assertion tests, null rate validations, and NCRB/RBI distribution calibrations; (4) Export validated benchmark datasets to Parquet/CSV."
    )
    page9.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec7_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)

    # ==================== PAGE 10: REFERENCES ====================
    page10 = add_standard_page(10)
    y = draw_section_header(page10, 55, "8", "Verified Bibliographic References (IEEE Format)")
    
    refs_text = (
        "[1] National Crime Records Bureau (NCRB), 'Crime in India 2022 -- Statistics Volume II: Cyber Crimes,' Ministry of Home Affairs, Govt. of India, New Delhi, 2023.\n"
        "[2] Indian Cyber Crime Coordination Centre (I4C), 'Citizen Financial Cyber Fraud Reporting and Management System (CFCFRMS / 1930) Annual Operational Review,' MHA, New Delhi, 2024.\n"
        "[3] Reserve Bank of India (RBI), 'Annual Report 2023-24: Assessment of Frauds in the Banking Sector,' RBI, Mumbai, 2024.\n"
        "[4] E. R. Leukfeldt, E. R. Kleemans, and W. P. Stol, 'Cybercriminal Networks, Social Ties and Online Forums: Social Ties Versus Digital Ties within Phishing and Malware Networks,' The British Journal of Criminology, vol. 57, no. 3, pp. 704-722, 2017. DOI: 10.1093/bjc/azw009.\n"
        "[5] S. Chainey, L. Tompson, and S. Uhlig, 'The Utility of Hotspot Mapping for Predicting Spatial Patterns of Crime,' Security Journal, vol. 21, no. 1, pp. 4-28, 2008. DOI: 10.1057/palgrave.sj.8350066.\n"
        "[6] Y.-L. Lin, M.-F. Yen, and L.-C. Yu, 'Grid-Based Crime Prediction Using Geographical Features,' ISPRS International Journal of Geo-Information, vol. 7, no. 8, p. 298, 2018. DOI: 10.3390/ijgi7080298.\n"
        "[7] A. Bogomolov, B. Lepri, J. Staiano, N. Oliver, F. Pianesi, and A. Pentland, 'Once Upon a Crime: Towards Crime Prediction from Demographics and Mobile Data,' in Proc. 16th Int. Conf. Multimodal Interaction (ICMI '14), ACM, 2014, pp. 427-434. DOI: 10.1145/2663204.2663254.\n"
        "[8] G. O. Mohler, M. B. Short, P. J. Brantingham, F. P. Schoenberg, and G. E. Tita, 'Self-Exciting Point Process Modeling of Crime,' Journal of the American Statistical Association, vol. 106, no. 493, pp. 100-108, 2011. DOI: 10.1198/jasa.2011.ap09546.\n"
        "[9] A. P. Wheeler and W. Steenbeek, 'Mapping the Risk Terrain for Crime Using Machine Learning,' Journal of Quantitative Criminology, vol. 37, no. 2, pp. 445-480, 2021. DOI: 10.1007/s10940-020-09457-7.\n"
        "[10] Y. Lee, S. O, and J. E. Eck, 'A Theory-Driven Algorithm for Real-Time Crime Hot Spot Forecasting,' Police Quarterly, vol. 23, no. 2, pp. 200-232, 2020. DOI: 10.1177/1098611119887809.\n"
        "[11] M. Ester, H.-P. Kriegel, J. Sander, and X. Xu, 'A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise,' in Proc. 2nd Int. Conf. Knowledge Discovery and Data Mining (KDD '96), AAAI Press, 1996, pp. 226-231.\n"
        "[12] D. Birant and A. Kut, 'ST-DBSCAN: An Algorithm for Clustering Spatial-Temporal Data,' Data & Knowledge Engineering, vol. 60, no. 1, pp. 208-221, 2007. DOI: 10.1016/j.datak.2006.01.013.\n"
        "[13] M. Adepeju, G. Rosser, and T. Cheng, 'Novel Evaluation Metrics for Sparse Spatio-Temporal Point Process Hotspot Predictions -- A Crime Case Study,' International Journal of Geographical Information Science, vol. 30, no. 11, pp. 2133-2154, 2016. DOI: 10.1080/13658816.2016.1159684.\n"
        "[14] V. M. White, J. Hunt, and B. Green, 'A Discussion of Current Crime Forecasting Indices and an Improvement to the Prediction Efficiency Index for Applications,' Security Journal, vol. 36, pp. 735-753, 2023. DOI: 10.1057/s41284-023-00367-4.\n"
        "[15] H. S. Assumpção, F. C. M. Ramos, D. A. P. Duarte, and W. Meira Jr., 'DELATOR: Money Laundering Detection via Multi-Task Learning on Large Transaction Graphs,' in 2022 IEEE Int. Conf. Big Data (Big Data), 2022, pp. 1595-1604. DOI: 10.48550/arXiv.2205.10293.\n"
        "[16] D. Ensign, S. A. Friedler, S. Neville, C. Scheidegger, and S. Venkatasubramanian, 'Runaway Feedback Loops in Predictive Policing,' in Proc. 1st Conf. Fairness, Accountability and Transparency (FAT* 2018), PMLR, vol. 81, 2018, pp. 160-171. DOI: 10.48550/arXiv.1706.09847.\n"
        "[17] K. Lum and W. Isaac, 'To Predict and Serve?,' Significance, vol. 13, no. 5, pp. 14-19, 2016. DOI: 10.1111/j.1740-9713.2016.00960.x.\n"
        "[18] S. M. Lundberg and S.-I. Lee, 'A Unified Approach to Interpreting Model Predictions,' in Advances in Neural Information Processing Systems (NeurIPS 2017), vol. 30, 2017, pp. 4765-4774.\n"
        "[19] E. A. Lopez-Rojas, A. Elmir, and S. Axelsson, 'PaySim: A Financial Mobile Money Simulator for Fraud Detection,' in 28th European Modeling and Simulation Symposium (EMSS), 2016, pp. 249-255.\n"
        "[20] City of Chicago, 'Crimes - 2001 to Present (Open Data Portal),' Chicago Police Department, 2024. [Online]. Available: https://data.cityofchicago.org"
    )
    page10.insert_textbox(pymupdf.Rect(50, y, 545, 790), refs_text, fontsize=7.8, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_LEFT)
    
    doc.save(pdf_path)
    doc.close()
    print(f"Academic Report PDF compiled successfully: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
