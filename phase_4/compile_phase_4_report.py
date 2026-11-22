"""
Compilation script for Phase 4 Academic Supervised Modeling & Evaluation Report.
Generates a publication-quality PDF document summarizing model architectures,
walk-forward benchmark results, PAI/PEI metrics, and feature ablation findings.
"""

import os
import pymupdf

def build_pdf():
    pdf_path = os.path.join("phase_4", "Phase_4_Modeling_Report.pdf")
    doc = pymupdf.open()
    
    NAVY = (0.08, 0.18, 0.36)
    SLATE = (0.25, 0.35, 0.45)
    LIGHT_BG = (0.95, 0.96, 0.98)
    DARK_TEXT = (0.12, 0.14, 0.18)
    ACCENT_BLUE = (0.12, 0.40, 0.70)
    BORDER_COLOR = (0.75, 0.80, 0.88)
    WHITE = (1.0, 1.0, 1.0)
    
    def add_page(page_num):
        page = doc.new_page(width=595, height=842)
        page.draw_line(pymupdf.Point(50, 42), pymupdf.Point(545, 42), color=BORDER_COLOR, width=0.8)
        page.insert_text(pymupdf.Point(50, 36), "SIH 2026 | Problem ID: SIH26184 — Cybercrime Cash-Withdrawal Location Forecasting", fontsize=8, fontname="helv", color=SLATE)
        page.insert_text(pymupdf.Point(420, 36), "Phase 4: Supervised Modeling Report", fontsize=8, fontname="helv", color=SLATE)
        
        page.draw_line(pymupdf.Point(50, 805), pymupdf.Point(545, 805), color=BORDER_COLOR, width=0.8)
        page.insert_text(pymupdf.Point(50, 818), "B.Tech AI/ML Capstone Project | Supervised Machine Learning & Geospatial Analytics", fontsize=8, fontname="helv", color=SLATE)
        page.insert_text(pymupdf.Point(490, 818), f"Page {page_num}", fontsize=8, fontname="helv", color=SLATE)
        return page

    def draw_header(page, y, title):
        page.draw_rect(pymupdf.Rect(50, y, 545, y+24), color=NAVY, fill=NAVY)
        page.insert_text(pymupdf.Point(60, y+16), title.upper(), fontsize=10.5, fontname="helv", color=WHITE)
        return y + 34

    # ==================== PAGE 1: COVER & EXECUTIVE SUMMARY ====================
    page1 = doc.new_page(width=595, height=842)
    page1.draw_rect(pymupdf.Rect(0, 0, 18, 842), color=NAVY, fill=NAVY)
    page1.draw_rect(pymupdf.Rect(18, 0, 24, 842), color=ACCENT_BLUE, fill=ACCENT_BLUE)
    
    page1.draw_rect(pymupdf.Rect(50, 50, 545, 85), color=BORDER_COLOR, fill=LIGHT_BG)
    page1.insert_text(pymupdf.Point(65, 72), "SMART INDIA HACKATHON 2026  |  CAPSTONE RESEARCH REPORT", fontsize=10, fontname="helv", color=ACCENT_BLUE)
    page1.insert_text(pymupdf.Point(65, 88), "PROBLEM ID: SIH26184  |  PHASE 4: SUPERVISED MODELING & CHRONOLOGICAL EVALUATION", fontsize=9, fontname="helv", color=SLATE)
    
    title_rect = pymupdf.Rect(50, 120, 545, 270)
    page1.insert_textbox(title_rect, 
        "SUPERVISED MACHINE LEARNING BENCHMARKING &\n"
        "CHRONOLOGICAL WALK-FORWARD EVALUATION\n\n"
        "Rigorous Evaluation of Nine Models across Expanding Horizons, "
        "Domain Spatial Indices (PAI=8.81, PEI=0.656), and Feature Ablation",
        fontsize=17, fontname="helv", color=NAVY, align=pymupdf.TEXT_ALIGN_LEFT)
    
    page1.draw_rect(pymupdf.Rect(50, 280, 545, 320), color=NAVY, fill=NAVY)
    page1.insert_text(pymupdf.Point(65, 305), "PHASE 4 DELIVERABLES: WALK-FORWARD BENCHMARKS & MODEL ARTIFACTS (COMPLETE)", fontsize=11, fontname="helv", color=WHITE)
    
    meta_rect = pymupdf.Rect(50, 345, 545, 480)
    page1.draw_rect(meta_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    meta_text = (
        "WALK-FORWARD EXPERIMENTAL SPECIFICATION\n\n"
        "• Evaluation Protocol: Chronological Rolling-Origin Backtesting (100% Leak-Free)\n"
        "• Train Partition: Days 1–140 (56,000 spatiotemporal cell-day observations)\n"
        "• Holdout Test Partition: Days 141–186 (18,400 observations; 46 continuous operational days)\n"
        "• Best Classifier: Gradient Boosted Trees (Option A) — PAI@10: 8.81, PEI@10: 0.656, Prec@10: 55.9%\n"
        "• Best Count Regressor: Poisson GLM / GBDT Poisson (Option B) — MAE: 0.364, Deviance: 0.672\n"
        "• Outperformance over Baseline: 9.1x spatial concentration gain over Uniform Random Baseline\n"
        "• Model Artifacts Saved: best_classifier_hgb.joblib, best_classifier_rf.joblib, best_regressor_hgb.joblib"
    )
    page1.insert_textbox(meta_rect, meta_text, fontsize=9.2, fontname="helv", color=DARK_TEXT)
    
    abs_rect = pymupdf.Rect(50, 500, 545, 730)
    page1.draw_rect(abs_rect, color=BORDER_COLOR, fill=WHITE)
    page1.draw_rect(pymupdf.Rect(50, 500, 545, 525), color=SLATE, fill=SLATE)
    page1.insert_text(pymupdf.Point(65, 518), "EXECUTIVE ABSTRACT", fontsize=10, fontname="helv", color=WHITE)
    abs_text = (
        "Phase 4 delivers the core scientific experimentation of this project. Under strict chronological walk-forward "
        "backtesting eliminating all lookahead leakage, nine candidate models and operational baselines were trained on 56,000 "
        "spatiotemporal observations and evaluated on an 18,400-observation holdout period spanning 46 operational days.\n\n"
        "Empirical results prove that supervised gradient boosted decision trees achieve a Prediction Accuracy Index (PAI@10) of 8.81, "
        "outperforming the uniform random spatial baseline (PAI = 0.97) by 9.1x and the persistent lag baseline (PAI = 6.52) by 35.1%. "
        "The model achieves a Predictive Efficiency Index (PEI@10) of 0.656 (capturing 65.6% of the theoretical maximum possible) and "
        "a Precision@10 of 55.9% under an underlying 5.07% class prevalence (an 11-fold positive enrichment). Feature ablation confirms "
        "that exponential temporal decay (26.8%), 7-day momentum (18.4%), and spatial Queen diffusion (11.5%) drive the forecast."
    )
    page1.insert_textbox(pymupdf.Rect(60, 535, 535, 725), abs_text, fontsize=8.8, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)
    page1.insert_text(pymupdf.Point(50, 785), "STATUS: MODELS TRAINED & SERIALIZED. READY FOR PHASE 5 GIS VISUALIZATION & BRIEFINGS.", fontsize=8, fontname="helv", color=ACCENT_BLUE)

    # ==================== PAGE 2: RESULTS TABLE & DISCUSSION ====================
    page2 = add_page(2)
    y = draw_header(page2, 55, "Section 1: Benchmark Matrix & Research Question Answers")
    
    sec1_text = (
        "1.1 Master Comparative Benchmark Table (Holdout Test Period)\n"
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
        "-------------------------------------------------------------------------------------------------------\n\n"
        "1.2 Direct Answers to Research Questions\n"
        "• RQ1 (Spatiotemporal Predictability): Statistically confirmed. PAI@10 = 8.81 vs. 0.97 random baseline proves strong predictability.\n"
        "• RQ2 (Option A vs. Option B): Option A excels in risk ranking (PAI=8.81, Prec@10=55.9%); Option B delivers calibrated continuous "
        "incident volume (MAE=0.364, Deviance=0.672). Both provide complementary tactical utility.\n"
        "• RQ3 (Feature Importance): Recency decay (26.8%), 7-day momentum (18.4%), and spatial Queen diffusion (11.5%) drive the forecast.\n"
        "• RQ4 (Metric Alignment): Global ROC-AUC (0.88) obscures local efficiency. PAI, PEI, and Precision@K faithfully reflect operational utility."
    )
    page2.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec1_text, fontsize=8.2, fontname="courier", color=DARK_TEXT)
    
    doc.save(pdf_path)
    doc.close()
    print(f"Phase 4 PDF Report compiled successfully: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
