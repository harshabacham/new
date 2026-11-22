"""
Real-Time Telemetry Streaming & Incident Burst Simulation Engine.
Demonstrates how real-time complaint ingestion from I4C CFCFRMS (Helpline 1930)
updates rolling spatiotemporal feature buffers and triggers proactive ATM intervention alerts.
"""

import os
import sys
import json
import time
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PHASE5_DIR = os.path.join(BASE_DIR, "phase_5")
DATA_DIR = os.path.join(BASE_DIR, "data")

def run_simulation(burst_complaints=35, scam_type="INVESTMENT_SCAM", originating_bank="SBIN"):
    print("=" * 75)
    print("REAL-TIME STREAMING COMPLAINT BURST SIMULATION & TACTICAL ALERT DISPATCH")
    print("Smart India Hackathon 2026 | Problem Statement ID: SIH26184")
    print("=" * 75)
    
    fc_path = os.path.join(PHASE5_DIR, "latest_operational_forecasts.csv")
    assert os.path.exists(fc_path), "Operational forecast data missing"
    
    df_fc = pd.read_csv(fc_path)
    
    print(f"\n[EVENT 10:14:00 IST] INGESTING REAL-TIME COMPLAINT STREAM FROM HELPLINE 1930...")
    print(f" -> Batch Size: {burst_complaints} newly registered cyber financial fraud complaints")
    print(f" -> Dominant Scam Typology: {scam_type} (High-yield deceptive return scheme)")
    print(f" -> Originating Bank Victim Accounts: {originating_bank} (State Bank of India)")
    print(f" -> Estimated Total Defrauded Amount: INR {burst_complaints * 45000:,.2f}")
    
    # Simulate processing delay
    time.sleep(0.8)
    
    print("\n[EVENT 10:14:02 IST] STOCHASTIC LAYERING & CASH-OUT CONVERSION MODELING...")
    conversion_rate = 0.68
    expected_cashouts = int(burst_complaints * conversion_rate)
    mean_layering_delay = 14.65 # hours
    
    convergence_start = datetime.now() + timedelta(hours=8)
    convergence_peak = datetime.now() + timedelta(hours=mean_layering_delay)
    
    print(f" -> Cash-Out Conversion Rate: {conversion_rate*100:.1f}%")
    print(f" -> Expected Physical Cash Dispensation Events: ~{expected_cashouts} ATM sweeps")
    print(f" -> Projected Muling Hop Duration: Gamma(3.0, 4.8h) -> Mean {mean_layering_delay:.1f} hours")
    print(f" -> Physical Withdrawal Convergence Window:")
    print(f"    - Interception Window Opens: {convergence_start.strftime('%Y-%m-%d %H:%M:%S IST')} (+8 hours)")
    print(f"    - Peak Terrestrial Cash Extraction: {convergence_peak.strftime('%Y-%m-%d %H:%M:%S IST')} (+14.6 hours)")
    
    time.sleep(0.8)
    
    print("\n[EVENT 10:14:04 IST] RUNNING SPATIOTEMPORAL MULTINOMIAL LOGIT ROUTING...")
    # Top cells prioritized
    top_targets = df_fc.sort_values("pred_hotspot_prob", ascending=False).head(5)
    
    print("\n" + "-" * 75)
    print("CRITICAL ALERT: TOP-5 TARGETED ATM CELLS FOR PROACTIVE INTERDICTION")
    print("-" * 75)
    
    alert_payload = []
    for rank, (_, row) in enumerate(top_targets.iterrows(), 1):
        cid = row["grid_cell_id"]
        prob = row["pred_hotspot_prob"] * 100
        lat, lon = row["centroid_lat"], row["centroid_lon"]
        atms = int(row["cell_atm_count"])
        exp_sweeps = round(row["expected_withdrawals"] * 1.35, 1) # Surge-adjusted
        xai = row["top_contributing_factors"].split("|")[0].strip()
        
        print(f"PRIORITY #{rank} | Cell: {cid} | Coordinates: ({lat:.4f}, {lon:.4f})")
        print(f"  • Hotspot Probability: {prob:.1f}% [CRITICAL RISK]")
        print(f"  • Surge-Adjusted Expected Cash-Outs: {exp_sweeps} sweeps (ATMs: {atms})")
        print(f"  • Primary Causal Driver: {xai}")
        print(f"  • Tactical Action: Dispatch plainclothes patrol; issue Section 91 CCTV hold.")
        print("-" * 75)
        
        alert_payload.append({
            "rank": rank,
            "cell_id": cid,
            "lat": lat,
            "lon": lon,
            "probability": prob,
            "surge_expected_sweeps": exp_sweeps,
            "cell_atm_count": atms
        })
        
    # Serialize audit alert log
    log_path = os.path.join(PHASE5_DIR, "realtime_alert_audit_log.json")
    audit_data = {
        "timestamp": datetime.now().isoformat(),
        "burst_id": f"ALERT-BURST-{int(time.time())}",
        "ingested_complaints": burst_complaints,
        "scam_type": scam_type,
        "originating_bank": originating_bank,
        "convergence_window": {
            "start": convergence_start.isoformat(),
            "peak": convergence_peak.isoformat()
        },
        "prioritized_interception_cells": alert_payload,
        "responsible_ai_notice": "Decisions must be validated by human investigators. Presumption of innocence applies."
    }
    
    with open(log_path, "w") as f:
        json.dump(audit_data, f, indent=2)
        
    print(f"\n[OK] Real-time tactical alert logged to: {log_path}")
    print("=" * 75)
    return audit_data

if __name__ == "__main__":
    run_simulation()
