# Phase 3: Spatiotemporal Feature Engineering Methodology
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Spatiotemporal Discretization & Panel Construction

Continuous event records are structured into an expansive spatiotemporal panel:
* **Spatial Units**: $M = 400$ regular planar grid cells ($20 \times 20$ grid, $1\,\text{km} \times 1\,\text{km}$).
* **Temporal Discretization**: Uniform daily operational intervals $\Delta t = 24\,\text{hours}$.
* **Total Panel Dimensions**: $400\,\text{cells} \times 186\,\text{days} = 74,400\,\text{spatiotemporal observations}$.

---

## 2. Engineered Feature Taxonomy (29 Standardized Columns)

Features are partitioned into five substantive categories designed to capture both chronic spatial opportunities and acute temporal triggers:

```
+----------------------------------------------------------------------------------------------------+
|                                    FEATURE TAXONOMY AT A GLANCE                                    |
+----------------------------------------------------------------------------------------------------+
|  1. Temporal Recurrence Lags:       lag_count_1d, 3d, 7d, 14d, 30d; lag_amount_sum/mean_7d         |
|  2. Exponential Temporal Decay:     decay_intensity_30d (half-life decay over 30 days)             |
|  3. Upstream Complaint Telemetry:   complaint_count_3d, amount_3d, sbin_share_3d, invest_share_3d |
|  4. Spatial Diffusion (Queen Lag):  spatial_lag_neighbor_7d (mean 7-day count of adjacent 8 cells)|
|  5. Built-Environment & Static:    cell_atm_count, transit_score, mule_hub_score, cluster_core    |
|  6. Periodic Calendar Indicators:   day_of_week, is_weekend, day_of_month, is_salary_cycle        |
+----------------------------------------------------------------------------------------------------+
```

### Table 1: Feature Dictionary & Causal Rationale

| Feature Name | Type | Mathematical Definition | Operational & Criminological Rationale |
| :--- | :--- | :--- | :--- |
| `lag_count_1d` | Integer | $k_{c, t-1}$ | Immediate short-term persistence of mule sweeps. |
| `lag_count_3d` | Integer | $\sum_{\tau=1}^3 k_{c, t-\tau}$ | Short-term momentum over a 72-hour operational cycle. |
| `lag_count_7d` | Integer | $\sum_{\tau=1}^7 k_{c, t-\tau}$ | Weekly rhythm and operational repeat muling. |
| `lag_count_14d`| Integer | $\sum_{\tau=1}^{14} k_{c, t-\tau}$ | Bi-weekly historical baseline activity. |
| `lag_count_30d`| Integer | $\sum_{\tau=1}^{30} k_{c, t-\tau}$ | Chronic baseline hot spot status (Flag indicator). |
| `decay_intensity_30d` | Float | $\sum_{\tau=1}^{30} e^{-0.15 \tau} k_{c, t-\tau}$ | Exponentially weighted temporal decay modeling recency bias. |
| `complaint_count_3d` | Integer | $\sum_{\tau=1}^3 C_{t-\tau}$ | Upstream metropolitan complaint burst leading to cash-outs. |
| `complaint_sbin_share_3d`| Float | $C_{\text{SBIN}, 3d} / C_{\text{total}, 3d}$ | Proportion of complaints tied to specific banking networks. |
| `complaint_invest_share_3d`| Float | $C_{\text{Invest}, 3d} / C_{\text{total}, 3d}$ | Proportion of high-yield investment scam complaints. |
| `spatial_lag_neighbor_7d`| Float | $\frac{1}{|\mathcal{N}(c)|} \sum_{j \in \mathcal{N}(c)} \text{lag7}_j$ | Contagion and spatial displacement to neighboring cells. |
| `cell_atm_count` | Integer | $N_{\text{ATM}}(c)$ | Built-environment criminal opportunity (cash availability). |
| `transit_score` | Float | $\exp(-d(c, \text{hubs})/\sigma)$ | Proximity to arterial transit corridors for rapid exit. |
| `is_salary_cycle` | Binary | $\mathbb{I}(\text{dom} \le 4 \lor \text{dom} \ge 28)$ | Monthly liquidity surge exploited by fraudsters. |
| `target_count` | Integer | $k_{c, t}$ | **Option B Target: Verified Cash-Out Count on Day t.** |
| `target_hotspot` | Binary | $\mathbb{I}(k_{c, t} \ge 2)$ | **Option A Target: Binary Hotspot Indicator on Day t.** |

---

## 3. Target Distribution and Imbalance Characterization

* **Option B Target (`target_count`)**: Highly zero-inflated (82.4% zero-count observations; range 0 to 8).
* **Option A Target (`target_hotspot`)**: 3,775 positives out of 74,400 observations (**5.07% class prevalence**).
* This 19:1 negative-to-positive class ratio provides an authentic testbed for focal loss, threshold calibration, and spatial Precision@K evaluation in Phase 4.

---
*Document Version: 2.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
