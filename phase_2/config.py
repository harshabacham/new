"""
Configuration parameters for Phase 2 Synthetic Data Generation and Calibration.
Calibrated against NCRB 'Crime in India 2022/2023' and RBI Annual Fraud Reports 2023-24.
"""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class GridConfig:
    n_rows: int = 20
    n_cols: int = 20
    min_lat: float = 28.5000
    max_lat: float = 28.7000
    min_lon: float = 77.1000
    max_lon: float = 77.3000
    crs: str = "EPSG:4326"

@dataclass
class SimulationConfig:
    start_date: str = "2026-01-01"
    end_date: str = "2026-06-30" # 181 days
    random_seed: int = 42
    
    # Macro Complaint Arrival (Negative Binomial: mean ~145 complaints/day)
    daily_complaints_mean: float = 145.0
    daily_complaints_dispersion: float = 1.6
    
    # Financial parameters (LogNormal INR amounts calibrated to RBI statistics)
    amount_log_mean: float = 10.35  # Median ~INR 31,000, mean ~INR 48,000
    amount_log_sigma: float = 0.95
    min_amount: float = 3000.0
    max_amount: float = 2500000.0
    
    # Cash-out conversion probability (fraction of complaints leading to physical cash extraction)
    cash_out_conversion_rate: float = 0.68
    
    # Muling Layering Delay (Gamma distribution: shape=3.0, scale=4.8 hours -> mean ~14.4 hours)
    delay_gamma_shape: float = 3.0
    delay_gamma_scale_hours: float = 4.8
    
    # Distribution of fraud categories (NCRB 2022/2023 empirical proportions)
    fraud_categories: Dict[str, float] = None
    
    # Bank brand market share in cyber fraud complaints (I4C CFCFRMS 2024 proxy)
    bank_market_share: Dict[str, float] = None

    def __post_init__(self):
        if self.fraud_categories is None:
            self.fraud_categories = {
                "INVESTMENT_SCAM": 0.34,
                "TASK_JOB_SCAM": 0.26,
                "UPI_PHISHING": 0.20,
                "DIGITAL_ARREST": 0.12,
                "LOAN_APP_EXTORTION": 0.08
            }
        if self.bank_market_share is None:
            self.bank_market_share = {
                "SBIN": 0.32,
                "HDFC": 0.22,
                "ICIC": 0.18,
                "PUNB": 0.13,
                "UTIB": 0.09,
                "CBIN": 0.06
            }

GRID_CONFIG = GridConfig()
SIM_CONFIG = SimulationConfig()
