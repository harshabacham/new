"""
Compilation script for Phase 3 Academic Feature Engineering & ESDA Report.
Generates a publication-quality PDF document summarizing spatial clustering findings,
Moran's I autocorrelation, 29-feature taxonomy, and leak-free verification.
"""

import os
import pymupdf

def build_pdf():
    pdf_path = os.path.join("phase_3", "Phase_3_Feature_Report.pdf")
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
        page.insert_text(pymupdf.Point(425, 36), "Phase 3: ESDA & Feature Pipeline", fontsize=8, fontname="helv", color=SLATE)
        
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
    page1.insert_text(pymupdf.Point(65, 72), "SMART INDIA HACKATHON 2026  |  CAPSTONE RESEARCH & FEATURE REPORT", fontsize=10, fontname="helv", color=ACCENT_BLUE)
    page1.insert_text(pymupdf.Point(65, 88), "PROBLEM ID: SIH26184  |  PHASE 3: ESDA, DBSCAN & SPATIOTEMPORAL FEATURE ENGINEERING", fontsize=9, fontname="helv", color=SLATE)
    
    title_rect = pymupdf.Rect(50, 120, 545, 270)
    page1.insert_textbox(title_rect, 
        "EXPLORATORY SPATIAL DATA ANALYSIS (ESDA) &\n"
        "SPATIOTEMPORAL FEATURE ENGINEERING\n\n"
        "Global Moran's I Autocorrelation, DBSCAN Cluster Decoupling, "
        "29-Feature Spatiotemporal Panel, and Zero-Leakage Pipeline Architecture",
        fontsize=17, fontname="helv", color=NAVY, align=pymupdf.TEXT_ALIGN_LEFT)
    
    page1.draw_rect(pymupdf.Rect(50, 280, 545, 320), color=NAVY, fill=NAVY)
    page1.insert_text(pymupdf.Point(65, 305), "PHASE 3 DELIVERABLES: ESDA DISCOVERY & 74,400-UNIT FEATURE PANEL (COMPLETE)", fontsize=11, fontname="helv", color=WHITE)
    
    meta_rect = pymupdf.Rect(50, 345, 545, 480)
    page1.draw_rect(meta_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    meta_text = (
        "ESDA & FEATURE PIPELINE SPECIFICATION\n\n"
        "• Global Moran's I Autocorrelation: +0.6018 (p < 0.0001, confirming intense spatial clustering)\n"
        "• DBSCAN Parameters: Eps = 1,200m, Min_samples = 25 (2 clusters identified; 1.26% noise points)\n"
        "• Spatiotemporal Panel Size: 400 Cells x 186 Days = 74,400 Observation Rows\n"
        "• Total Engineered Columns: 29 Features spanning Lags, Decays, Diffusion, Upstream Telemetry\n"
        "• Option A Hotspot Prevalence: 5.07% Positive Class (3,775 / 74,400; severe 19:1 class imbalance)\n"
        "• Zero-Leakage Guarantee: Strict 1-day temporal buffer on all rolling series (shift=1)"
    )
    page1.insert_textbox(meta_rect, meta_text, fontsize=9.2, fontname="helv", color=DARK_TEXT)
    
    abs_rect = pymupdf.Rect(50, 500, 545, 730)
    page1.draw_rect(abs_rect, color=BORDER_COLOR, fill=WHITE)
    page1.draw_rect(pymupdf.Rect(50, 500, 545, 525), color=SLATE, fill=SLATE)
    page1.insert_text(pymupdf.Point(65, 518), "EXECUTIVE ABSTRACT", fontsize=10, fontname="helv", color=WHITE)
    abs_text = (
        "Phase 3 bridges the synthetic benchmark dataset into a production-grade machine learning feature matrix. "
        "First, exploratory spatial data analysis confirms strong positive spatial autocorrelation (Moran's I = +0.6018), "
        "statistically rejecting spatial randomness and establishing the empirical feasibility of spatial forecasting (RQ1). "
        "DBSCAN clustering isolates physical cash-out hubs from noise, and is strictly decoupled from future forecasting.\n\n"
        "Second, we engineer a leak-free 29-feature spatiotemporal panel across 74,400 cell-day units. The feature suite incorporates "
        "historical withdrawal lags (1d, 3d, 7d, 14d, 30d), exponential temporal decay, citywide upstream complaint telemetry (complaints, "
        "defrauded sums, SBI bank share), spatial Queen-adjacency diffusion terms, and built-environment infrastructure. "
        "All features enforce strict causal directionality via 1-day shift buffers, eliminating lookahead bias and setting the stage "
        "for rigorous walk-forward backtesting in Phase 4."
    )
    page1.insert_textbox(pymupdf.Rect(60, 535, 535, 725), abs_text, fontsize=8.8, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)
    page1.insert_text(pymupdf.Point(50, 785), "STATUS: FEATURE MATRIX EXPORTED (PARQUET/CSV). READY FOR PHASE 4 MODEL TRAINING.", fontsize=8, fontname="helv", color=ACCENT_BLUE)

    # ==================== PAGE 2: ESDA FINDINGS & FEATURE TAXONOMY ====================
    page2 = add_page(2)
    y = draw_header(page2, 55, "Section 1: ESDA Findings & Spatiotemporal Feature Architecture")
    
    sec1_text = (
        "1.1 Spatial Autocorrelation & DBSCAN Clustering Findings\n"
        "• Global Moran's I: +0.6018 (Expected: -0.0025, p < 0.0001). Confirms strong spatial dependency.\n"
        "• DBSCAN Analysis: Grouped 18,527 physical cash-out points into 2 primary spatial corridors with 233 noise points (1.26%).\n"
        "• Critical Guardrail: DBSCAN is strictly used for ESDA and static feature creation ('is_historical_cluster_core'), NOT forecasting.\n\n"
        "1.2 Feature Taxonomy (29 Standardized Columns)\n"
        "1. Spatial Anchors: grid_cell_id, row_idx, col_idx, centroid_lat, centroid_lon\n"
        "2. Temporal Lags: lag_count_1d, lag_count_3d, lag_count_7d, lag_count_14d, lag_count_30d\n"
        "3. Financial Lags: lag_amount_sum_7d, lag_amount_mean_7d\n"
        "4. Temporal Decay: decay_intensity_30d (exponentially weighted moving average with lambda=0.15)\n"
        "5. Upstream Telemetry: complaint_count_3d, complaint_amount_sum_3d, complaint_sbin_share_3d, complaint_invest_share_3d\n"
        "6. Spatial Diffusion: spatial_lag_neighbor_7d (mean 7-day withdrawal count in Queen adjacent 8 neighbors)\n"
        "7. Built Environment: cell_atm_count, transit_score, mule_hub_score, is_historical_cluster_core\n"
        "8. Calendar Rhythms: day_of_week, is_weekend, day_of_month, is_salary_cycle\n"
        "9. Ground-Truth Targets: target_count (Option B count), target_hotspot (Option A binary indicator >= 2 withdrawals)\n\n"
        "1.3 Strict Zero-Leakage Causal Guarantee\n"
        "To eliminate lookahead bias, all temporal and spatial features for day t are calculated using observations strictly on or before day t-1. "
        "Target values on day t are decoupled from input features, preventing synthetic correlation artifacts."
    )
    page2.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec1_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)
    
    doc.save(pdf_path)
    doc.close()
    print(f"Phase 3 PDF Report compiled successfully: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
