"""
Compilation script for Phase 2 Academic Data Report.
Generates a publication-quality PDF document summarizing synthetic data generation,
data dictionary schema, and quality assurance audit results.
"""

import os
import json
import pymupdf

def build_pdf():
    pdf_path = os.path.join("phase_2", "Phase_2_Data_Report.pdf")
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
        page.insert_text(pymupdf.Point(435, 36), "Phase 2: Data Engineering Report", fontsize=8, fontname="helv", color=SLATE)
        
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
    page1.insert_text(pymupdf.Point(65, 72), "SMART INDIA HACKATHON 2026  |  CAPSTONE DATA ENGINEERING REPORT", fontsize=10, fontname="helv", color=ACCENT_BLUE)
    page1.insert_text(pymupdf.Point(65, 88), "PROBLEM ID: SIH26184  |  PHASE 2: DATASET GENERATION, SCHEMA & VALIDATION", fontsize=9, fontname="helv", color=SLATE)
    
    title_rect = pymupdf.Rect(50, 120, 545, 270)
    page1.insert_textbox(title_rect, 
        "CYBERCRIME CASH-WITHDRAWAL BENCHMARK DATASET\n\n"
        "Synthetic Data Engineering, Stochastic Process Calibration (NCRB/RBI), "
        "Standardized Data Dictionary, and Quality Assurance Audit",
        fontsize=18, fontname="helv", color=NAVY, align=pymupdf.TEXT_ALIGN_LEFT)
    
    page1.draw_rect(pymupdf.Rect(50, 280, 545, 320), color=NAVY, fill=NAVY)
    page1.insert_text(pymupdf.Point(65, 305), "PHASE 2 DELIVERABLES: DATA ENGINE & SCHEMA SPECIFICATION (PASSED)", fontsize=11, fontname="helv", color=WHITE)
    
    meta_rect = pymupdf.Rect(50, 345, 545, 480)
    page1.draw_rect(meta_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    meta_text = (
        "DATASET AUDIT SPECIFICATION\n\n"
        "• Simulated Geography: Delhi NCR Metropolitan Sector (20km x 20km Bounding Box)\n"
        "• Spatial Partitioning: M = 400 Planar Grid Cells (1km x 1km resolution)\n"
        "• Temporal Coverage: 181 Operational Days (January 1, 2026 to June 30, 2026)\n"
        "• Total Complaints Generated: 27,291 Incident Records\n"
        "• Total Verified Cash Extractions: 18,527 ATM Dispensation Events (67.9% Cash-Out Rate)\n"
        "• Macro Calibration Reference: NCRB 'Crime in India 2022' & RBI Fraud Reports 2023-24\n"
        "• Legal Governance Standard: Digital Personal Data Protection (DPDP) Act 2023 (India)"
    )
    page1.insert_textbox(meta_rect, meta_text, fontsize=9.2, fontname="helv", color=DARK_TEXT)
    
    abs_rect = pymupdf.Rect(50, 500, 545, 730)
    page1.draw_rect(abs_rect, color=BORDER_COLOR, fill=WHITE)
    page1.draw_rect(pymupdf.Rect(50, 500, 545, 525), color=SLATE, fill=SLATE)
    page1.insert_text(pymupdf.Point(65, 518), "EXECUTIVE SUMMARY & STATUTORY COMPLIANCE", fontsize=10, fontname="helv", color=WHITE)
    summary_text = (
        "Phase 2 delivers a privacy-compliant, statistically calibrated synthetic benchmark dataset for training "
        "and evaluating supervised cash-withdrawal forecasting algorithms. Due to statutory privacy quarantines under "
        "the DPDP Act 2023 and Banking Regulation Act 1949, real ATM transaction logs and police investigation dockets "
        "cannot be distributed openly. Phase 2 solves this barrier by implementing a stochastic simulation engine based on "
        "spatiotemporal point processes and random utility destination choice.\n\n"
        "The generator accurately reproduces key empirical properties of Indian financial cybercrime: overdispersed Negative Binomial "
        "daily complaint arrivals, Log-Normal fraud amounts matching RBI loss distributions (median INR 30,960), Gamma-distributed "
        "muling layering delays (mean 14.65 hours), and multinomial logit destination choice governed by cell ATM density and transit corridors. "
        "An automated test suite verified 100% causal temporal ordering, 100% bounding box geofencing, zero nulls in essential fields, "
        "and complete spatial decoupling between victim complaint locations and physical cash-out terminals."
    )
    page1.insert_textbox(pymupdf.Rect(60, 535, 535, 725), summary_text, fontsize=8.8, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)
    
    page1.insert_text(pymupdf.Point(50, 785), "AUDIT VERDICT: 7 OF 7 QUALITY ASSURANCE TESTS PASSED. READY FOR PHASE 3 FEATURE PIPELINE.", fontsize=8, fontname="helv", color=ACCENT_BLUE)

    # ==================== PAGE 2: SCHEMA & VALIDATION MATRIX ====================
    page2 = add_page(2)
    y = draw_header(page2, 55, "Section 1: Data Dictionary & Quality Assurance Audit")
    
    sec1_text = (
        "1.1 Automated Quality Assurance Audit Scorecard\n"
        "The validation suite (phase_2/validate_data.py) executed seven structural assertions:\n\n"
        "• Test 1 (Spatial Grid Integrity): PASSED. 400 cells created across [28.50, 28.70]N x [77.10, 77.30]E. All cells contain ATMs (2-50).\n"
        "• Test 2 (Schema Field Completeness): PASSED. All 18 essential and withdrawal fields verified.\n"
        "• Test 3 (Null Rate Integrity): PASSED. Exactly 0 nulls detected in verified cash-out records.\n"
        "• Test 4 (Temporal Causal Ordering): PASSED. 100% causal sequence valid (Incident < Complaint, Incident < Withdrawal). Mean delay: 14.65 hrs.\n"
        "• Test 5 (Withdrawal Geofence): PASSED. 100% of 18,527 withdrawals lie strictly inside defined metropolitan bounds.\n"
        "• Test 6 (Spatial Decoupling): PASSED. 100.0% of events maintain physical decoupling between victim complaint geo and cash-out ATM.\n"
        "• Test 7 (Statistical Calibration): PASSED. Median amount INR 30,960.21, mean INR 48,677.25. Cash-out conversion: 67.9% (target: 68%).\n\n"
        "1.2 Standardized Field-Level Data Dictionary\n"
        "1. record_id: Unique complaint identifier (e.g., 'CR-2026-0008412')\n"
        "2. complaint_timestamp: ISO-8601 filing time via 1930 helpline / portal\n"
        "3. incident_timestamp: ISO-8601 fraudulent digital transfer occurrence time\n"
        "4. defrauded_amount: Total financial loss in INR (Log-Normal distribution)\n"
        "5. fraud_category: Scam classification (Investment, Task/Job, UPI Phishing, Digital Arrest, Loan App)\n"
        "6. victim_bank_code: Originating bank identifier (SBIN, HDFC, ICIC, PUNB, UTIB, CBIN)\n"
        "7. victim_lat / victim_lon: Victim geographic coordinates (strictly decoupled from ATM location)\n"
        "8. reporting_delay_hours: Time elapsed between unauthorized transfer and complaint filing\n"
        "9. is_cash_out: Binary indicator whether illicit funds reached physical cash liquidation stage\n"
        "10. withdrawal_timestamp: Exact physical ATM dispensation timestamp (Ground-Truth Target Anchor)\n"
        "11. withdrawal_amount: Physical currency dispensed at ATM terminal (INR)\n"
        "12. grid_cell_id: Spatial grid unit identifier ('CELL_00_00' to 'CELL_19_19')\n"
        "13. latitude / longitude: Exact terrestrial coordinates of verified cash extraction\n"
        "14. atm_terminal_id: Unique hardware identifier of dispensing ATM kiosk\n"
        "15. cell_atm_count: Total registered ATMs inside grid cell (Static Infrastructure Feature)\n"
        "16. transit_score: Inverted distance to commercial/highway transit hubs in [0, 1]\n"
        "17. mule_hub_score: Proximity indicator to known criminal cash runner corridors\n"
        "18. mule_layer_depth: Number of intermediate mule digital accounts crossed (1 to 4)\n"
        "19. layering_delay_hours: Duration elapsed between incident and cash withdrawal"
    )
    page2.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec1_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)
    
    doc.save(pdf_path)
    doc.close()
    print(f"Phase 2 PDF Report compiled successfully: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
