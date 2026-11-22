# Phase 2: Standardized Data Dictionary and Schema Specification
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Schema Overview

The Phase 2 dataset adheres strictly to the 19-field data dictionary formalized in Phase 1 ([04_dataset_feasibility.md](file:///c:/Users/harsh/OneDrive/Desktop/supervised/phase_1/04_dataset_feasibility.md)). Datasets are serialized in high-performance Apache Parquet and standard CSV formats under [`data/`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/data).

---

## 2. Complete Field-Level Specification

### Table 1: Field-Level Data Dictionary

| # | Field Name | Data Type | Nullable | Example Value | Description | Role in Machine Learning Pipeline |
| :- | :--- | :--- | :-: | :--- | :--- | :--- |
| 1 | `record_id` | String | No | `"CR-2026-0008412"` | Unique anonymized cybercrime docket identifier | Primary Key / Event Linkage |
| 2 | `complaint_timestamp` | ISO-8601 | No | `"2026-03-12T14:22:15"` | Timestamp when victim logged complaint via `1930` / portal | Upstream Telemetry Predictor |
| 3 | `incident_timestamp` | ISO-8601 | No | `"2026-03-11T21:40:00"` | Timestamp when fraudulent digital transfer occurred | Temporal Ordering Anchor |
| 4 | `defrauded_amount` | Float | No | `45000.00` | Total stolen funds in Indian Rupees (INR) | Financial Magnitude Feature |
| 5 | `fraud_category` | Categorical | No | `"INVESTMENT_SCAM"` | Scam typology (Investment, Job, Phishing, Arrest, Loan) | Categorical Feature Driver |
| 6 | `victim_bank_code` | Categorical | No | `"SBIN"` | Originating banking institution code of the victim | Institutional Exposure Feature |
| 7 | `victim_lat` | Float | No | `28.6142` | Latitude where victim resides/reported | Spatial Decoupling Verification |
| 8 | `victim_lon` | Float | No | `77.2089` | Longitude where victim resides/reported | Spatial Decoupling Verification |
| 9 | `reporting_delay_hours` | Float | No | `16.70` | Latency between fraud occurrence and complaint filing | Upstream Telemetry Feature |
| 10 | `is_cash_out` | Binary $\{0,1\}$ | No | `1` | Indicator if complaint resulted in physical cash-out | Event Conversion Filter |
| 11 | `withdrawal_timestamp` | ISO-8601 | Yes | `"2026-03-12T08:15:30"` | Physical cash dispensing timestamp at terminal | **Ground-Truth Target Anchor** |
| 12 | `withdrawal_amount` | Float | Yes | `25000.00` | Cash amount mechanically dispensed at ATM (INR) | Ground-Truth Magnitude |
| 13 | `grid_cell_id` | String | Yes | `"CELL_08_12"` | Discrete spatial grid cell identifier ($1\,\text{km} \times 1\,\text{km}$) | **Spatial Partition Key** |
| 14 | `latitude` | Float | Yes | `28.5832` | Latitude coordinate of verified physical cash-out | Spatial Verification Ground Truth |
| 15 | `longitude` | Float | Yes | `77.2215` | Longitude coordinate of verified physical cash-out | Spatial Verification Ground Truth |
| 16 | `atm_terminal_id` | String | Yes | `"ATM-CELL_08_12-014"` | Physical terminal identifier at cash-point | Infrastructure Identifier |
| 17 | `cell_atm_count` | Integer | Yes | `24` | Total operational ATMs registered in spatial cell | Static Infrastructure Feature |
| 18 | `transit_score` | Float | Yes | `0.8520` | Transit hub accessibility score $\in [0, 1]$ | Built-Environment Feature |
| 19 | `mule_hub_score` | Float | Yes | `1.9420` | Proximity score to known mule syndication corridors | Spatial Attractor Feature |
| 20 | `mule_layer_depth` | Integer | Yes | `3` | Number of intermediate mule digital hops | Financial Network Indicator |
| 21 | `layering_delay_hours` | Float | Yes | `10.59` | Temporal duration between incident and cash liquidation | Muling Operational Metric |

---

## 3. Storage and Serialization Artifacts

The serialized dataset artifacts are stored under [`data/`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/data):
* `grid_cells.csv`: 400 spatial grid cells with geographic bounding boxes, centroids, ATM counts, and transit scores.
* `cybercrime_complaints.csv`: 27,291 complaint records.
* `verified_withdrawals.csv`: 18,527 verified physical ATM cash extraction records.
* `cybercrime_paired_events.csv` / `.parquet`: Master coupled event-level dataset.
* `validation_summary.json`: Automated test report validating 100% schema and causal integrity.

---
*Document Version: 2.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
