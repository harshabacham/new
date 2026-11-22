"""
Phase 2: Synthetic Data Generation Engine.
Simulates coupled cybercrime complaints and physical ATM cash withdrawals
across a 20x20 urban spatial grid using stochastic point processes and multinomial logit destination choice.
"""

import sys
import os
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Add parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase_2.config import GRID_CONFIG, SIM_CONFIG

def generate_spatial_grid(config=GRID_CONFIG, seed=42):
    """
    Generates a 20x20 planar grid (400 cells) over the metropolitan bounding box
    with realistic infrastructure features: ATM counts, transit accessibility, and mule ring affinity.
    """
    np.random.seed(seed)
    n_rows = config.n_rows
    n_cols = config.n_cols
    
    lat_step = (config.max_lat - config.min_lat) / n_rows
    lon_step = (config.max_lon - config.min_lon) / n_cols
    
    # Hub locations (representing major commercial/transit centers, e.g., Central Delhi, South Hub, West Hub, Airport corridor)
    hubs = [
        {"lat": 28.6300, "lon": 77.2200, "weight": 2.5, "name": "Central_Business_District"},
        {"lat": 28.5500, "lon": 77.2500, "weight": 2.0, "name": "South_Commercial_Hub"},
        {"lat": 28.6500, "lon": 77.1500, "weight": 1.8, "name": "West_Market_Corridor"},
        {"lat": 28.5600, "lon": 77.1200, "weight": 1.6, "name": "Airport_Transit_Corridor"},
    ]
    
    # Known mule withdrawal syndicates operate near transit corridors with quick highway exit routes
    mule_hotspots = [
        {"lat": 28.6450, "lon": 77.2150, "radius": 0.035, "intensity": 2.2},
        {"lat": 28.5350, "lon": 77.2600, "radius": 0.040, "intensity": 2.5},
        {"lat": 28.6700, "lon": 77.1300, "radius": 0.030, "intensity": 2.0},
    ]

    cells = []
    for r in range(n_rows):
        for c in range(n_cols):
            cell_id = f"CELL_{r:02d}_{c:02d}"
            c_lat = config.min_lat + (r + 0.5) * lat_step
            c_lon = config.min_lon + (c + 0.5) * lon_step
            
            # Min/max bounds for the cell
            lat_min = config.min_lat + r * lat_step
            lat_max = lat_min + lat_step
            lon_min = config.min_lon + c * lon_step
            lon_max = lon_min + lon_step
            
            # Transit accessibility: inverted distance to closest hub
            min_hub_dist = min(np.sqrt((c_lat - h["lat"])**2 + (c_lon - h["lon"])**2) for h in hubs)
            transit_score = float(np.exp(-min_hub_dist / 0.06))
            
            # Mule ring affinity: localized Gaussian peaks around mule hubs
            mule_score = 0.2
            for mh in mule_hotspots:
                d = np.sqrt((c_lat - mh["lat"])**2 + (c_lon - mh["lon"])**2)
                mule_score += mh["intensity"] * np.exp(-0.5 * (d / mh["radius"])**2)
            
            # ATM count: Poisson with lambda driven by transit score and commercial density
            lambda_atm = max(2.0, 5.0 + 22.0 * transit_score + np.random.normal(0, 1.5))
            cell_atm_count = int(np.random.poisson(lambda_atm))
            cell_atm_count = max(2, min(50, cell_atm_count))
            
            cells.append({
                "grid_cell_id": cell_id,
                "row_idx": r,
                "col_idx": c,
                "centroid_lat": round(c_lat, 6),
                "centroid_lon": round(c_lon, 6),
                "lat_min": round(lat_min, 6),
                "lat_max": round(lat_max, 6),
                "lon_min": round(lon_min, 6),
                "lon_max": round(lon_max, 6),
                "cell_atm_count": cell_atm_count,
                "transit_score": round(transit_score, 4),
                "mule_hub_score": round(mule_score, 4)
            })
            
    df_grid = pd.DataFrame(cells)
    
    # Calculate multinomial logit base destination utility for each cell:
    # U(c) = beta1 * log(ATM) + beta2 * Transit + beta3 * MuleHub + noise
    utility = (
        1.25 * np.log(df_grid["cell_atm_count"]) +
        1.40 * df_grid["transit_score"] +
        1.80 * df_grid["mule_hub_score"] +
        np.random.normal(0, 0.25, len(df_grid))
    )
    df_grid["destination_probability"] = np.exp(utility) / np.sum(np.exp(utility))
    return df_grid

def generate_events(df_grid, sim_config=SIM_CONFIG):
    """
    Generates synthetic complaints and verified withdrawal events across the simulation window.
    """
    np.random.seed(sim_config.random_seed)
    
    start_dt = datetime.fromisoformat(sim_config.start_date)
    end_dt = datetime.fromisoformat(sim_config.end_date)
    total_days = (end_dt - start_dt).days + 1
    
    complaint_list = []
    withdrawal_list = []
    paired_list = []
    
    categories = list(sim_config.fraud_categories.keys())
    cat_weights = list(sim_config.fraud_categories.values())
    
    banks = list(sim_config.bank_market_share.keys())
    bank_weights = list(sim_config.bank_market_share.values())
    
    cell_ids = df_grid["grid_cell_id"].values
    cell_probs = df_grid["destination_probability"].values
    cell_dict = df_grid.set_index("grid_cell_id").to_dict(orient="index")
    
    record_counter = 1
    
    for day_idx in range(total_days):
        current_date = start_dt + timedelta(days=day_idx)
        
        # Day of week seasonality (higher complaint filing on Mondays, weekend dip)
        dow = current_date.weekday()
        dow_factor = 1.15 if dow == 0 else (0.90 if dow in [5, 6] else 1.0)
        
        # Monthly salary cycle surge (days 1-4 and 28-31)
        dom = current_date.day
        salary_factor = 1.20 if (dom <= 4 or dom >= 28) else 1.0
        
        day_mean = sim_config.daily_complaints_mean * dow_factor * salary_factor
        
        # Draw daily complaints from Negative Binomial
        # NB parameterization: mean = day_mean, var = day_mean + alpha * day_mean^2
        variance = day_mean + sim_config.daily_complaints_dispersion * (day_mean ** 1.5)
        p = day_mean / variance
        n = (day_mean ** 2) / (variance - day_mean)
        n_complaints = int(np.random.negative_binomial(max(1, n), max(0.01, min(0.99, p))))
        
        hour_probs = np.array([
            0.01, 0.01, 0.01, 0.01, 0.01, 0.02, # 00-05
            0.03, 0.04, 0.06, 0.08, 0.09, 0.09, # 06-11
            0.08, 0.08, 0.08, 0.07, 0.07, 0.06, # 12-17
            0.05, 0.04, 0.03, 0.02, 0.01, 0.01  # 18-23
        ])
        hour_probs = hour_probs / hour_probs.sum()
        
        # Generate complaint events throughout the 24-hour day
        for _ in range(n_complaints):
            rec_id = f"CR-2026-{record_counter:07d}"
            record_counter += 1
            
            hour = int(np.random.choice(24, p=hour_probs))
            minute = np.random.randint(0, 60)
            second = np.random.randint(0, 60)
            
            complaint_time = current_date + timedelta(hours=hour, minutes=minute, seconds=second)
            
            # Incident occurred before complaint: reporting latency Delta_rep ~ Exponential(mean=18 hours)
            reporting_latency_hours = float(np.random.exponential(scale=18.0) + 0.5)
            incident_time = complaint_time - timedelta(hours=reporting_latency_hours)
            
            # Defrauded amount (INR)
            amount_log = np.random.normal(sim_config.amount_log_mean, sim_config.amount_log_sigma)
            defrauded_amount = float(np.exp(amount_log))
            defrauded_amount = max(sim_config.min_amount, min(sim_config.max_amount, defrauded_amount))
            defrauded_amount = round(defrauded_amount, 2)
            
            fraud_cat = np.random.choice(categories, p=cat_weights)
            victim_bank = np.random.choice(banks, p=bank_weights)
            
            # Victim location (geographically decoupled from withdrawal location)
            # Simulated within metropolitan or adjoining regions
            victim_lat = round(float(np.random.uniform(28.45, 28.75)), 6)
            victim_lon = round(float(np.random.uniform(77.05, 77.35)), 6)
            
            complaint_record = {
                "record_id": rec_id,
                "complaint_timestamp": complaint_time.isoformat(),
                "incident_timestamp": incident_time.isoformat(),
                "defrauded_amount": defrauded_amount,
                "fraud_category": fraud_cat,
                "victim_bank_code": victim_bank,
                "victim_lat": victim_lat,
                "victim_lon": victim_lon,
                "reporting_delay_hours": round(reporting_latency_hours, 2)
            }
            complaint_list.append(complaint_record)
            
            # Does this complaint lead to a physical cash withdrawal?
            leads_to_cashout = np.random.rand() < sim_config.cash_out_conversion_rate
            
            if leads_to_cashout:
                # Layering delay between incident and withdrawal: Gamma distributed
                layering_delay_hours = float(np.random.gamma(
                    shape=sim_config.delay_gamma_shape,
                    scale=sim_config.delay_gamma_scale_hours
                ) + 0.25)
                
                withdrawal_time = incident_time + timedelta(hours=layering_delay_hours)
                
                # Spatial destination choice: select grid cell
                selected_cell_id = np.random.choice(cell_ids, p=cell_probs)
                c_meta = cell_dict[selected_cell_id]
                
                # Perturb coordinate within the cell boundary
                w_lat = round(float(np.random.uniform(c_meta["lat_min"], c_meta["lat_max"])), 6)
                w_lon = round(float(np.random.uniform(c_meta["lon_min"], c_meta["lon_max"])), 6)
                
                # Mule withdrawal amount (often multiple ATM swipes; realistic single sweep INR 10,000 - 50,000)
                withdrawal_amount = min(defrauded_amount, float(np.random.choice([10000, 20000, 25000, 40000, 50000])))
                if defrauded_amount < 10000:
                    withdrawal_amount = defrauded_amount
                
                mule_layer_depth = int(np.random.choice([1, 2, 3, 4], p=[0.25, 0.45, 0.20, 0.10]))
                terminal_id = f"ATM-{selected_cell_id}-{np.random.randint(1, c_meta['cell_atm_count'] + 1):03d}"
                
                withdrawal_record = {
                    "record_id": rec_id,
                    "withdrawal_timestamp": withdrawal_time.isoformat(),
                    "withdrawal_amount": round(withdrawal_amount, 2),
                    "grid_cell_id": selected_cell_id,
                    "latitude": w_lat,
                    "longitude": w_lon,
                    "atm_terminal_id": terminal_id,
                    "cell_atm_count": c_meta["cell_atm_count"],
                    "transit_score": c_meta["transit_score"],
                    "mule_hub_score": c_meta["mule_hub_score"],
                    "mule_layer_depth": mule_layer_depth
                }
                withdrawal_list.append(withdrawal_record)
                
                # Combined paired record
                paired_record = {
                    **complaint_record,
                    **withdrawal_record,
                    "layering_delay_hours": round(layering_delay_hours, 2),
                    "is_cash_out": 1
                }
                paired_list.append(paired_record)
            else:
                paired_record = {
                    **complaint_record,
                    "withdrawal_timestamp": None,
                    "withdrawal_amount": 0.0,
                    "grid_cell_id": None,
                    "latitude": None,
                    "longitude": None,
                    "atm_terminal_id": None,
                    "cell_atm_count": None,
                    "transit_score": None,
                    "mule_hub_score": None,
                    "mule_layer_depth": 0,
                    "layering_delay_hours": None,
                    "is_cash_out": 0
                }
                paired_list.append(paired_record)

    df_complaints = pd.DataFrame(complaint_list)
    df_withdrawals = pd.DataFrame(withdrawal_list)
    df_paired = pd.DataFrame(paired_list)
    
    return df_complaints, df_withdrawals, df_paired

def main():
    print("=" * 70)
    print("PHASE 2: SYNTHETIC DATA ENGINE GENERATION")
    print("=" * 70)
    
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
    os.makedirs(data_dir, exist_ok=True)
    
    print("[1/3] Generating 20x20 Urban Spatial Grid (400 cells)...")
    df_grid = generate_spatial_grid()
    grid_path = os.path.join(data_dir, "grid_cells.csv")
    df_grid.to_csv(grid_path, index=False)
    print(f" -> Saved grid cells: {grid_path} ({len(df_grid)} cells)")
    
    print("[2/3] Simulating Coupled Complaints & Physical Cash-Out Events (181 days)...")
    df_complaints, df_withdrawals, df_paired = generate_events(df_grid)
    
    comp_path = os.path.join(data_dir, "cybercrime_complaints.csv")
    with_path = os.path.join(data_dir, "verified_withdrawals.csv")
    pair_csv_path = os.path.join(data_dir, "cybercrime_paired_events.csv")
    pair_pq_path = os.path.join(data_dir, "cybercrime_paired_events.parquet")
    
    df_complaints.to_csv(comp_path, index=False)
    df_withdrawals.to_csv(with_path, index=False)
    df_paired.to_csv(pair_csv_path, index=False)
    df_paired.to_parquet(pair_pq_path, index=False)
    
    print(f" -> Total Cybercrime Complaints Generated: {len(df_complaints):,}")
    print(f" -> Total Verified ATM Withdrawals:       {len(df_withdrawals):,}")
    print(f" -> Paired Event Dataset:                  {len(df_paired):,} rows")
    print(f" -> Exported files in '{data_dir}':")
    print(f"    - {comp_path}")
    print(f"    - {with_path}")
    print(f"    - {pair_csv_path}")
    print(f"    - {pair_pq_path}")
    print("=" * 70)
    print("Synthetic data generation completed successfully.")

if __name__ == "__main__":
    main()
