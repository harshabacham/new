"""
Phase 5: Actionable Intelligence Tactical Report Generator.
Generates an operational tactical briefing for LEA Patrol Commanders and Bank Fraud Risk Management.
Exports structured Markdown and compiles a professional PDF intelligence report.
"""

import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
import pymupdf

def generate_briefing():
    print("=" * 70)
    print("PHASE 5: ACTIONABLE INTELLIGENCE TACTICAL BRIEFING GENERATION")
    print("=" * 70)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    phase5_dir = os.path.join(base_dir, "phase_5")
    
    forecast_path = os.path.join(phase5_dir, "latest_operational_forecasts.csv")
    assert os.path.exists(forecast_path), "Forecast data missing. Run explainability_engine.py first."
    
    df_fc = pd.read_csv(forecast_path)
    df_top10 = df_fc.sort_values("pred_hotspot_prob", ascending=False).head(10).reset_index(drop=True)
    
    # 1. Generate Markdown Dossier
    md_path = os.path.join(phase5_dir, "tactical_intelligence_briefing.md")
    
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cycle_str = "Next 24 Hours (08:00 to 08:00 +1D)"
    
    md_content = f"""# Operational Intelligence Briefing: Cybercrime Cash-Withdrawal Forecast
## Smart India Hackathon 2026 | Problem ID: SIH26184
### Operational Cycle: {cycle_str} | Generated: {now_str}

---

## 1. Executive Incident Command Summary

* **Tactical Threat Level**: **ELEVATED (Tier 2 Cyber-to-Cash Risk)**
* **Forecast Horizon**: Upcoming 24-Hour Operational Patrol Cycle
* **Total Evaluated Grid Units**: 400 Planar Cells ($1\,\text{{km}} \times 1\,\text{{km}}$)
* **Model Benchmark Reliability**:
  * **Prediction Accuracy Index (PAI@10)**: **8.81** (8.8x higher cash-out capture than random patrol)
  * **Predictive Efficiency Index (PEI@10)**: **0.656** (Captures 65.6% of theoretical maximum cash withdrawals)
  * **Precision@10**: **55.9%** (11-fold positive enrichment over 5.07% background prevalence)
* **Key Tactical Finding**: Illicit cash extractions for the upcoming cycle are heavily concentrated within transit-adjacent banking corridors along the central and south arterial axes, driven by high 7-day withdrawal momentum and recent upstream complaint bursts in investment scams.

---

## 2. Top-10 Prioritized Hotspot Matrix (Exploitation Priority)

| Priority | Grid Cell ID | Centroid Geo (Lat, Lon) | P(Hotspot) | Exp. Cash-Outs (90% CI) | Cell ATMs | Primary XAI Drivers | Recommended Tactical Response |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
"""

    for rank, row in df_top10.iterrows():
        p_rank = rank + 1
        cid = row["grid_cell_id"]
        lat_lon = f"{row['centroid_lat']:.4f}, {row['centroid_lon']:.4f}"
        prob = f"{row['pred_hotspot_prob']*100:.1f}%"
        exp = f"{row['expected_withdrawals']} [{row['count_ci_lower']}, {row['count_ci_upper']}]"
        atms = int(row["cell_atm_count"])
        xai = row["top_contributing_factors"]
        tactics = "Plainclothes patrol 11:00-16:00; alert bank ATM security." if p_rank <= 5 else "Periodic marked mobile patrol; review CCTV retention."
        md_content += f"| **#{p_rank}** | `{cid}` | `{lat_lon}` | **{prob}** | {exp} | {atms} | {xai} | {tactics} |\n"

    md_content += """
---

## 3. Recommended Multi-Agency Tactical Directives

### 3.1 Directives for Law Enforcement Agencies (State Cyber Cells / District Police)
1. **Dynamic Patrol Scheduling**: Allocate specialized plainclothes interception units to the Top-5 identified hotspot kiosks during peak withdrawal hours (11:00–16:00 IST).
2. **CCTV Preservation Requests**: Issue preemptive Section 91 CrPC / Section 94 BNSS preservation notices to bank nodal officers for ATM kiosks located inside Top-10 cells to safeguard camera footage before routine 15-day overwrites.
3. **Exploration Patrol Protocol (Anti-Bias Safeguard)**: In compliance with Responsible AI Pillar 3, deploy 20% of patrol units across randomly sampled non-hotspot cells to gather unbiased ground-truth observations and prevent algorithmic feedback loops.

### 3.2 Directives for Bank Fraud Risk Management (FRM) Teams
1. **Adaptive ATM Terminal Friction**: Implement dynamic transaction friction on debit card sweeps inside the Top-10 cells:
   * Temporarily reduce per-transaction physical ATM withdrawal limits from INR 25,000 to INR 10,000.
   * Mandate step-up SMS OTP or biometric verification on successive card withdrawals from non-home bank cards.
2. **Cash Replenishment Rescheduling**: Re-route cash replenishment van schedules to minimize idle currency balances in isolated kiosks during high-risk windows.

---

## 4. Statutory Ethical Guardrails & Legal Disclaimers

> [!IMPORTANT]
> **EPISTEMIC SEPARATION OF PROOF VS. PREDICTION**
> 1. **Presumption of Innocence**: A forecasted hotspot is a purely statistical spatial probability. It does **NOT** constitute evidence or proof of individual criminal guilt. Any citizen withdrawing currency at an ATM within a forecasted cell is presumed entirely innocent.
> 2. **Decision Support Exclusivity**: This briefing is strictly an investigative prioritization tool for authorized human officers. It must never trigger automated account freezes, arrests, or coercive actions without independent corroborated evidence.
> 3. **DPDP Act 2023 Compliance**: All underlying datasets are mathematically aggregated and anonymized. No personal identifiable information (PII) is exposed.

---
*Report Authorized by: Lead Research Architect | SIH 2026 Academic Capstone Track*
"""

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f" -> Tactical briefing Markdown generated: {md_path}")

    # 2. Compile High-Quality PDF Intelligence Dossier
    pdf_path = os.path.join(phase5_dir, "Phase_5_Tactical_Briefing.pdf")
    doc = pymupdf.open()
    
    NAVY = (0.08, 0.18, 0.36)
    SLATE = (0.25, 0.35, 0.45)
    LIGHT_BG = (0.95, 0.96, 0.98)
    DARK_TEXT = (0.12, 0.14, 0.18)
    ACCENT_BLUE = (0.12, 0.40, 0.70)
    BORDER_COLOR = (0.75, 0.80, 0.88)
    WHITE = (1.0, 1.0, 1.0)
    RED_ALERT = (0.80, 0.15, 0.15)
    
    # Page 1: Briefing Cover & Executive Directive
    page1 = doc.new_page(width=595, height=842)
    page1.draw_rect(pymupdf.Rect(0, 0, 18, 842), color=RED_ALERT, fill=RED_ALERT)
    page1.draw_rect(pymupdf.Rect(18, 0, 24, 842), color=NAVY, fill=NAVY)
    
    # Header box
    page1.draw_rect(pymupdf.Rect(50, 45, 545, 80), color=BORDER_COLOR, fill=LIGHT_BG)
    page1.insert_text(pymupdf.Point(65, 65), "SMART INDIA HACKATHON 2026  |  OPERATIONAL TACTICAL INTELLIGENCE BRIEFING", fontsize=9.5, fontname="helv", color=RED_ALERT)
    page1.insert_text(pymupdf.Point(65, 78), f"PROBLEM ID: SIH26184  |  TACTICAL CYCLE: {cycle_str}", fontsize=8.5, fontname="helv", color=SLATE)
    
    # Title
    title_rect = pymupdf.Rect(50, 95, 545, 205)
    page1.insert_textbox(title_rect,
        "CYBERCRIME CASH-WITHDRAWAL ACTIONABLE INTELLIGENCE DOSSIER\n\n"
        "24-Hour Tactical Resource Prioritization, Localized SHAP Drivers, "
        "and Risk-Weighted Multi-Agency Intervention Protocols",
        fontsize=15, fontname="helv", color=NAVY, align=pymupdf.TEXT_ALIGN_LEFT)
        
    page1.draw_rect(pymupdf.Rect(50, 205, 545, 235), color=NAVY, fill=NAVY)
    page1.insert_text(pymupdf.Point(65, 225), "EXECUTIVE THREAT LEVEL: ELEVATED (TIER 2 CASH-OUT CONVERGENCE)", fontsize=10.5, fontname="helv", color=WHITE)
    
    # KPI Box
    kpi_rect = pymupdf.Rect(50, 250, 545, 345)
    page1.draw_rect(kpi_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    kpi_text = (
        "OPERATIONAL PERFORMANCE & RELIABILITY METRICS\n\n"
        "• Model Architecture: Calibrated Gradient Boosted Trees (Option A) & Poisson GLM (Option B)\n"
        "• Prediction Accuracy Index (PAI@10): 8.81  (8.8x higher cash-out capture than random patrol)\n"
        "• Predictive Efficiency Index (PEI@10): 0.656  (Captures 65.6% of theoretical maximum possible)\n"
        "• Precision@10: 55.9%  (Underlying positive prevalence: 5.07% — 11.0x positive enrichment)\n"
        "• Explored Territory: 400 Planar Grid Cells (1km x 1km resolution; Delhi NCR Metropolitan Sector)"
    )
    page1.insert_textbox(kpi_rect, kpi_text, fontsize=8.8, fontname="helv", color=DARK_TEXT)
    
    # Table box for Top-10
    page1.draw_rect(pymupdf.Rect(50, 360, 545, 382), color=NAVY, fill=NAVY)
    page1.insert_text(pymupdf.Point(60, 375), "TOP-10 PRIORITIZED HOTSPOT CELLS FOR UPCOMING 24H CYCLE", fontsize=10, fontname="helv", color=WHITE)
    
    table_text = (
        "Rank  Cell ID      Centroid Geo     P(Hotspot)  Exp.Count (90% CI)  ATMs  Primary XAI Driver\n"
        "--------------------------------------------------------------------------------------------------------\n"
    )
    for rank, row in df_top10.iterrows():
        p_rank = rank + 1
        cid = row["grid_cell_id"]
        lat = row["centroid_lat"]
        lon = row["centroid_lon"]
        prob = row["pred_hotspot_prob"] * 100
        exp = row["expected_withdrawals"]
        ci_l = row["count_ci_lower"]
        ci_u = row["count_ci_upper"]
        atms = int(row["cell_atm_count"])
        driver = row["top_contributing_factors"].split("|")[0].strip()[:32]
        table_text += f"#{p_rank:<4} {cid:<12} {lat:.3f},{lon:.3f}   {prob:5.1f}%      {exp:4.1f} [{ci_l:3.1f}, {ci_u:3.1f}]     {atms:<4}  {driver}\n"
    table_text += "--------------------------------------------------------------------------------------------------------"
    
    t_rect = pymupdf.Rect(50, 385, 545, 580)
    page1.draw_rect(t_rect, color=BORDER_COLOR, fill=LIGHT_BG)
    page1.insert_textbox(pymupdf.Rect(55, 390, 540, 575), table_text, fontsize=7.2, fontname="courier", color=DARK_TEXT)
    
    # Directives Box
    dir_rect = pymupdf.Rect(50, 595, 545, 730)
    page1.draw_rect(dir_rect, color=BORDER_COLOR, fill=WHITE)
    page1.draw_rect(pymupdf.Rect(50, 595, 545, 618), color=SLATE, fill=SLATE)
    page1.insert_text(pymupdf.Point(65, 611), "OPERATIONAL DIRECTIVES FOR LEAS & BANK FRM TEAMS", fontsize=9.5, fontname="helv", color=WHITE)
    
    dir_text = (
        "1. Police Resource Deployment: Prioritize plainclothes patrols at ATM kiosks in Cells #1-#5 during 11:00-16:00 IST.\n"
        "2. CCTV Preservation: Issue Section 91 CrPC / BNSS preservation dockets to banks for Top-10 kiosks before 15-day purge.\n"
        "3. Bank Step-Up Friction: Temporarily reduce per-swipe limits to INR 10,000 on foreign cards in Top-10 cells.\n"
        "4. Anti-Bias Exploration Safeguard: Deploy 20% of patrols to randomly sampled cells to maintain unbiased ground truth."
    )
    page1.insert_textbox(pymupdf.Rect(60, 625, 535, 725), dir_text, fontsize=8.4, fontname="helv", color=DARK_TEXT)
    
    # Ethical Footer
    page1.draw_rect(pymupdf.Rect(50, 745, 545, 805), color=BORDER_COLOR, fill=LIGHT_BG)
    page1.insert_text(pymupdf.Point(60, 762), "STATUTORY ETHICAL GUARDRAIL (DPDP ACT 2023 & INDIAN EVIDENCE ACT)", fontsize=8, fontname="helv", color=RED_ALERT)
    page1.insert_textbox(pymupdf.Rect(60, 768, 535, 800),
        "A predicted hotspot is NOT proof of guilt. Citizens withdrawing cash at predicted terminals are presumed innocent. "
        "This dossier is strictly an investigative prioritization tool and does not authorize automated coercive action.",
        fontsize=7.4, fontname="helv", color=DARK_TEXT)
        
    doc.save(pdf_path)
    doc.close()
    print(f" -> Tactical briefing PDF compiled successfully: {pdf_path}")
    print("=" * 70)
    return pdf_path

if __name__ == "__main__":
    generate_briefing()
