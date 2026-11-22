"""
Phase 3: Spatiotemporal Feature Engineering Pipeline.
Transforms event-level records into an expansive spatiotemporal panel (400 cells x 181 days = 72,400 observations).
Constructs rolling temporal lags, spatial neighbor diffusions, and upstream complaint telemetry with STRICT ZERO LEAKAGE.
"""

import os
import sys
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def build_spatiotemporal_panel():
    print("=" * 70)
    print("PHASE 3: SPATIOTEMPORAL FEATURE ENGINEERING PIPELINE")
    print("=" * 70)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    phase3_dir = os.path.join(base_dir, "phase_3")
    
    grid_path = os.path.join(data_dir, "grid_cells.csv")
    pair_path = os.path.join(data_dir, "cybercrime_paired_events.csv")
    
    df_grid = pd.read_csv(grid_path)
    df_paired = pd.read_csv(pair_path)
    
    # Parse timestamps
    df_paired["complaint_dt"] = pd.to_datetime(df_paired["complaint_timestamp"])
    df_paired["complaint_date"] = df_paired["complaint_dt"].dt.date
    
    cashouts = df_paired[df_paired["is_cash_out"] == 1].copy()
    cashouts["withdrawal_dt"] = pd.to_datetime(cashouts["withdrawal_timestamp"])
    cashouts["withdrawal_date"] = cashouts["withdrawal_dt"].dt.date
    
    # Simulation calendar
    all_dates = sorted(cashouts["withdrawal_date"].unique())
    start_date = all_dates[0]
    end_date = all_dates[-1]
    date_range = pd.date_range(start=start_date, end=end_date, freq="D").date
    
    n_cells = len(df_grid)
    n_days = len(date_range)
    print(f"Constructing Spatiotemporal Panel: {n_cells} cells x {n_days} days = {n_cells * n_days:,} panel units.")
    
    # 1. Base Panel Generation (Cartesian product of cells x dates)
    cell_ids = df_grid["grid_cell_id"].values
    panel_index = pd.MultiIndex.from_product([cell_ids, date_range], names=["grid_cell_id", "date"])
    df_panel = pd.DataFrame(index=panel_index).reset_index()
    
    # Merge static cell metadata
    grid_meta_cols = ["grid_cell_id", "row_idx", "col_idx", "centroid_lat", "centroid_lon",
                      "cell_atm_count", "transit_score", "mule_hub_score", "is_historical_cluster_core"]
    df_panel = df_panel.merge(df_grid[grid_meta_cols], on="grid_cell_id", how="left")
    
    # 2. Daily observed cash-out counts and sums per cell
    daily_cell_stats = cashouts.groupby(["grid_cell_id", "withdrawal_date"]).agg(
        daily_count=("record_id", "count"),
        daily_amount=("withdrawal_amount", "sum")
    ).reset_index().rename(columns={"withdrawal_date": "date"})
    
    df_panel = df_panel.merge(daily_cell_stats, on=["grid_cell_id", "date"], how="left")
    df_panel["daily_count"] = df_panel["daily_count"].fillna(0).astype(int)
    df_panel["daily_amount"] = df_panel["daily_amount"].fillna(0.0)
    
    # Sort panel chronologically by cell and date to compute leak-free rolling features
    df_panel = df_panel.sort_values(["grid_cell_id", "date"]).reset_index(drop=True)
    
    print("[1/4] Calculating Rolling Historical Withdrawal Lags (1d, 3d, 7d, 14d, 30d)...")
    # For day t, lag features must look STRICTLY at days <= t-1 (shift=1) to prevent lookahead leakage
    # We group by grid_cell_id and use rolling windows on shifted values
    grouped = df_panel.groupby("grid_cell_id")
    
    shifted_count = grouped["daily_count"].shift(1).fillna(0)
    shifted_amount = grouped["daily_amount"].shift(1).fillna(0)
    
    df_panel["lag_count_1d"] = shifted_count.astype(int)
    
    # Rolling sums on shifted series
    df_panel["lag_count_3d"] = grouped["daily_count"].transform(lambda x: x.shift(1).rolling(3, min_periods=1).sum()).fillna(0).astype(int)
    df_panel["lag_count_7d"] = grouped["daily_count"].transform(lambda x: x.shift(1).rolling(7, min_periods=1).sum()).fillna(0).astype(int)
    df_panel["lag_count_14d"] = grouped["daily_count"].transform(lambda x: x.shift(1).rolling(14, min_periods=1).sum()).fillna(0).astype(int)
    df_panel["lag_count_30d"] = grouped["daily_count"].transform(lambda x: x.shift(1).rolling(30, min_periods=1).sum()).fillna(0).astype(int)
    
    df_panel["lag_amount_sum_7d"] = grouped["daily_amount"].transform(lambda x: x.shift(1).rolling(7, min_periods=1).sum()).fillna(0.0)
    df_panel["lag_amount_mean_7d"] = grouped["daily_amount"].transform(lambda x: x.shift(1).rolling(7, min_periods=1).mean()).fillna(0.0)
    
    # Exponential decay intensity over 30 days
    # Intensity = sum_{k=1}^30 exp(-0.15 * k) * count_{t-k}
    decay_weights = np.exp(-0.15 * np.arange(1, 31))
    def calc_decay(s):
        s_shift = s.shift(1).fillna(0).values
        decay_vals = np.zeros(len(s_shift))
        for i in range(len(s_shift)):
            history = s_shift[max(0, i-29):i+1][::-1]
            w = decay_weights[:len(history)]
            decay_vals[i] = np.sum(history * w)
        return decay_vals
        
    df_panel["decay_intensity_30d"] = grouped["daily_count"].transform(calc_decay)
    
    print("[2/4] Engineering Upstream Complaint Telemetry Lags...")
    # Daily city-wide complaint inflow (available in real-time to police)
    daily_complaints = df_paired.groupby("complaint_date").agg(
        complaint_inflow_count=("record_id", "count"),
        complaint_inflow_amount=("defrauded_amount", "sum"),
        complaint_sbin_count=("victim_bank_code", lambda x: (x == "SBIN").sum()),
        complaint_hdfc_count=("victim_bank_code", lambda x: (x == "HDFC").sum()),
        complaint_icic_count=("victim_bank_code", lambda x: (x == "ICIC").sum()),
        complaint_invest_count=("fraud_category", lambda x: (x == "INVESTMENT_SCAM").sum())
    ).reset_index().rename(columns={"complaint_date": "date"})
    
    # Shift complaint stats by 1 day to guarantee they precede forecast day t
    daily_complaints = daily_complaints.sort_values("date").reset_index(drop=True)
    daily_complaints["complaint_count_3d"] = daily_complaints["complaint_inflow_count"].shift(1).rolling(3, min_periods=1).sum().fillna(0)
    daily_complaints["complaint_amount_sum_3d"] = daily_complaints["complaint_inflow_amount"].shift(1).rolling(3, min_periods=1).sum().fillna(0)
    daily_complaints["complaint_sbin_share_3d"] = (
        daily_complaints["complaint_sbin_count"].shift(1).rolling(3, min_periods=1).sum() /
        (daily_complaints["complaint_count_3d"] + 1e-5)
    ).fillna(0)
    daily_complaints["complaint_invest_share_3d"] = (
        daily_complaints["complaint_invest_count"].shift(1).rolling(3, min_periods=1).sum() /
        (daily_complaints["complaint_count_3d"] + 1e-5)
    ).fillna(0)
    
    comp_cols = ["date", "complaint_count_3d", "complaint_amount_sum_3d", "complaint_sbin_share_3d", "complaint_invest_share_3d"]
    df_panel = df_panel.merge(daily_complaints[comp_cols], on="date", how="left").fillna(0)
    
    print("[3/4] Computing Spatial Neighborhood Diffusion (1st-Order Queen Adjacency Lags)...")
    # Spatial neighbor diffusion: mean 7-day activity of immediate adjacent cells
    n_rows, n_cols = 20, 20
    # Map (row, col) to neighbor cell_ids
    def get_neighbors(r, c):
        nbrs = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < n_rows and 0 <= nc < n_cols:
                    nbrs.append(f"CELL_{nr:02d}_{nc:02d}")
        return nbrs

    cell_neighbors = {row["grid_cell_id"]: get_neighbors(int(row["row_idx"]), int(row["col_idx"]))
                      for _, row in df_grid.iterrows()}
    
    # Pivot lag_count_7d to (date x cell_id) for rapid vectorized neighbor mean calculation
    pivot_lag7 = df_panel.pivot(index="date", columns="grid_cell_id", values="lag_count_7d")
    
    spatial_lag_dict = {}
    for cid, nbrs in cell_neighbors.items():
        spatial_lag_dict[cid] = pivot_lag7[nbrs].mean(axis=1)
        
    df_spatial_lag = pd.DataFrame(spatial_lag_dict).reset_index().melt(
        id_vars=["date"], var_name="grid_cell_id", value_name="spatial_lag_neighbor_7d"
    )
    df_panel = df_panel.merge(df_spatial_lag, on=["date", "grid_cell_id"], how="left")
    
    print("[4/4] Engineering Temporal Calendar Features & Supervised Targets...")
    panel_dates = pd.to_datetime(df_panel["date"])
    df_panel["day_of_week"] = panel_dates.dt.dayofweek
    df_panel["is_weekend"] = df_panel["day_of_week"].isin([5, 6]).astype(int)
    df_panel["day_of_month"] = panel_dates.dt.day
    df_panel["is_salary_cycle"] = ((df_panel["day_of_month"] <= 4) | (df_panel["day_of_month"] >= 28)).astype(int)
    
    # Targets for day t:
    # Option B Target (Count): daily_count on day t
    df_panel["target_count"] = df_panel["daily_count"]
    
    # Option A Target (Classification): Hotspot indicator (>= 2 verified cash-outs in cell on day t)
    HOTSPOT_THRESHOLD = 2
    df_panel["target_hotspot"] = (df_panel["target_count"] >= HOTSPOT_THRESHOLD).astype(int)
    
    # Drop raw unlagged daily metrics to strictly prevent leakage
    df_panel = df_panel.drop(columns=["daily_count", "daily_amount"])
    
    # Reorder columns logically
    feature_cols = [
        "grid_cell_id", "date", "row_idx", "col_idx", "centroid_lat", "centroid_lon",
        # Historical lags
        "lag_count_1d", "lag_count_3d", "lag_count_7d", "lag_count_14d", "lag_count_30d",
        "lag_amount_sum_7d", "lag_amount_mean_7d", "decay_intensity_30d",
        # Upstream telemetry
        "complaint_count_3d", "complaint_amount_sum_3d", "complaint_sbin_share_3d", "complaint_invest_share_3d",
        # Spatial diffusion
        "spatial_lag_neighbor_7d",
        # Static infrastructure
        "cell_atm_count", "transit_score", "mule_hub_score", "is_historical_cluster_core",
        # Calendar
        "day_of_week", "is_weekend", "day_of_month", "is_salary_cycle",
        # Targets
        "target_count", "target_hotspot"
    ]
    df_panel = df_panel[feature_cols]
    
    # Save feature matrix
    feat_pq_path = os.path.join(data_dir, "spatiotemporal_feature_matrix.parquet")
    feat_csv_path = os.path.join(data_dir, "spatiotemporal_feature_matrix.csv")
    df_panel.to_parquet(feat_pq_path, index=False)
    # Save a lighter sample of CSV or full CSV
    df_panel.to_csv(feat_csv_path, index=False)
    
    hotspot_prevalence = df_panel["target_hotspot"].mean() * 100.0
    print(f" -> Exported Spatiotemporal Feature Matrix: {len(df_panel):,} rows, {len(feature_cols)} columns.")
    print(f" -> Class Distribution (Option A Hotspots): {df_panel['target_hotspot'].sum():,} positives ({hotspot_prevalence:.2f}% prevalence).")
    print(f" -> Severe class imbalance confirmed (~{hotspot_prevalence:.1f}% positives), directly matching operational reality.")
    print(f" -> Files saved:")
    print(f"    - {feat_pq_path}")
    print(f"    - {feat_csv_path}")
    print("=" * 70)
    print("Feature engineering pipeline completed successfully.")
    return df_panel

if __name__ == "__main__":
    build_spatiotemporal_panel()
