"""
Compilation script for Phase 5 Academic Geospatial Visualization & Intelligence Report.
Generates a publication-quality PDF document summarizing explainability algorithms,
tactical briefing structure, GIS mapping layers, and human-in-the-loop protocols.
"""

import os
import pymupdf

def build_pdf():
    pdf_path = os.path.join("phase_5", "Phase_5_Intelligence_Report.pdf")
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
        page.insert_text(pymupdf.Point(420, 36), "Phase 5: Intelligence & GIS Report", fontsize=8, fontname="helv", color=SLATE)
        
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
    page1.insert_text(pymupdf.Point(65, 88), "PROBLEM ID: SIH26184  |  PHASE 5: GEOSPATIAL VISUALIZATION & ACTIONABLE REPORTING", fontsize=9, fontname="helv", color=SLATE)
    
    title_rect = pymupdf.Rect(50, 120, 545, 270)
    page1.insert_textbox(title_rect, 
        "GEOSPATIAL VISUALIZATION, EXPLAINABLE AI (XAI) &\n"
        "ACTIONABLE INTELLIGENCE DOSSIER GENERATION\n\n"
        "Interactive Folium GIS Choropleths, Localized Feature Attributions, "
        "Streamlit Command Platform, and Responsible Multi-Agency Governance",
        fontsize=16.5, fontname="helv", color=NAVY, align=pymupdf.TEXT_ALIGN_LEFT)
    
    page1.draw_rect(pymupdf.Rect(50, 280, 545, 320), color=NAVY, fill=NAVY)
    page1.insert_text(pymupdf.Point(65, 305), "PHASE 5 DELIVERABLES: GIS ENGINE, TACTICAL BRIEFINGS & DASHBOARD (COMPLETE)", fontsize=11, fontname="helv", color=WHITE)
    
    meta_rect = pymupdf.Rect(50, 345, 545, 480)
    page1.draw_rect(meta_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    meta_text = (
        "PHASE 5 OPERATIONAL DELIVERABLES & ARTIFACTS\n\n"
        "• Interactive GIS Web Map: interactive_hotspot_forecast_map.html (Folium layer control, choropleths)\n"
        "• Tactical Intelligence Dossier: Phase_5_Tactical_Briefing.pdf & tactical_intelligence_briefing.md\n"
        "• Interactive Command Dashboard: app.py (Streamlit full-featured multi-tab application)\n"
        "• Explainability Engine: explainability_engine.py (Localized SHAP-proxy attributions & conformal intervals)\n"
        "• Ethical Guardrail Implementation: 80/20 Exploitation-Exploration split (Anti-bias audit patrol)\n"
        "• Target Audience: State Cyber Cells (LEAs), District Police, and Bank Fraud Risk Management (FRM)"
    )
    page1.insert_textbox(meta_rect, meta_text, fontsize=9.2, fontname="helv", color=DARK_TEXT)
    
    abs_rect = pymupdf.Rect(50, 500, 545, 730)
    page1.draw_rect(abs_rect, color=BORDER_COLOR, fill=WHITE)
    page1.draw_rect(pymupdf.Rect(50, 500, 545, 525), color=SLATE, fill=SLATE)
    page1.insert_text(pymupdf.Point(65, 518), "EXECUTIVE ABSTRACT", fontsize=10, fontname="helv", color=WHITE)
    abs_text = (
        "Phase 5 bridges technical supervised machine learning into operational field intelligence. To support "
        "police commanders and banking risk officers, we developed an integrated suite of explainability, visualization, "
        "and decision-support tools. The explainability engine decomposes individual cell predictions into additive "
        "feature contributions, providing clear plain-language justifications (e.g., 'Weekly Repeat Withdrawal Burst + "
        "ATM Infrastructure Density') and 90% conformal prediction intervals.\n\n"
        "Geospatial visualization is delivered via an interactive Folium GIS choropleth mapping all 400 grid cells, "
        "highlighting Top-10 prioritized tactical targets and embedding an 80/20 exploitation-exploration patrol protocol "
        "to prevent self-fulfilling algorithmic feedback loops. A standardized Actionable Intelligence Tactical Dossier "
        "compiles concrete directives for LEA plainclothes deployments and bank ATM step-up friction. Finally, an interactive "
        "Streamlit web platform (app.py) provides live scenario filtering, parameter tuning, and forensic audit capabilities."
    )
    page1.insert_textbox(pymupdf.Rect(60, 535, 535, 725), abs_text, fontsize=8.8, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)
    page1.insert_text(pymupdf.Point(50, 785), "STATUS: ALL 5 PHASES COMPLETED. CAPSTONE DOSSIER & REPOSITORY READY FOR EVALUATION.", fontsize=8, fontname="helv", color=ACCENT_BLUE)

    # ==================== PAGE 2: ARCHITECTURE & ETHICS ====================
    page2 = add_page(2)
    y = draw_header(page2, 55, "Section 1: Operational Architecture & Responsible Governance")
    
    sec1_text = (
        "1.1 Explainable AI & Conformal Uncertainty Formulation\n"
        "• Localized Attributions: Decomposes predicted probabilities into additive feature contributions relative to urban baseline means.\n"
        "• Conformal Uncertainty Intervals: Computes empirical 90% prediction intervals [lower, upper] on expected withdrawal counts, "
        "communicating honest statistical error bounds to field commanders.\n\n"
        "1.2 Multi-Agency Operational Protocols\n"
        "• Police Tactical Deployment: Directs specialized plainclothes patrol units to Top-5 priority kiosks during peak extraction hours "
        "(11:00-16:00 IST), enabling timely interdiction before funds disperse into the informal cash economy.\n"
        "• Preemptive Evidence Preservation: Triggers Section 91 CrPC / Section 94 BNSS notices to banks for ATM CCTV footage preservation.\n"
        "• Bank Fraud Risk Friction: Enables dynamic ATM limits (capping withdrawals to INR 10,000) and step-up 2FA/biometric friction on high-risk card sweeps.\n\n"
        "1.3 Statutory Ethical Guardrails (DPDP Act 2023 & ACM/IEEE Standards)\n"
        "1. Epistemic Principle: Spatial Association != Probabilistic Prediction != Proof of Guilt. Citizens withdrawing cash in forecasted "
        "cells are presumed innocent. Predictions constitute investigative prioritization leads, NOT legal proof.\n"
        "2. Decision Support Exclusivity: Technically bars automated coercive actions (account freezing, arrests). Requires human-in-the-loop review.\n"
        "3. Mitigating Runaway Feedback Loops: Enforces an 80/20 exploration-exploitation split, deploying 20% of monitoring capacity to random cells "
        "to continuously collect unbiased ground-truth observations [Ensign et al., 2018]."
    )
    page2.insert_textbox(pymupdf.Rect(50, y, 545, 790), sec1_text, fontsize=8.4, fontname="helv", color=DARK_TEXT, align=pymupdf.TEXT_ALIGN_JUSTIFY)
    
    doc.save(pdf_path)
    doc.close()
    print(f"Phase 5 PDF Report compiled successfully: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
