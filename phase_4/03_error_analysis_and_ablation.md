# Phase 4: Error Analysis, Feature Ablation & Operational Trade-offs
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Feature Importance and Ablation Analysis (RQ3)

To answer **Research Question 3 (Feature Efficacy)**, we computed the Gini feature importances and permutation attributions of the best-performing tree models:

```
+----------------------------------------------------------------------------------------------------+
|                                    TOP-10 PREDICTIVE FEATURE RANKING                               |
+----------------------------------------------------------------------------------------------------+
|  1. decay_intensity_30d:      26.8% relative attribution (Exponential historical recency)          |
|  2. lag_count_7d:             18.4% relative attribution (Weekly repeat muling momentum)           |
|  3. cell_atm_count:           14.2% relative attribution (Built-environment terminal opportunity)   |
|  4. spatial_lag_neighbor_7d:  11.5% relative attribution (Queen spatial neighbor diffusion)        |
|  5. lag_count_30d:             8.6% relative attribution (Chronic baseline hot spot indicator)     |
|  6. transit_score:             6.1% relative attribution (Proximity to highway exit corridors)     |
|  7. complaint_count_3d:        5.4% relative attribution (Upstream municipal complaint burst)      |
|  8. mule_hub_score:            4.2% relative attribution (Mule ring territorial affinity)          |
|  9. is_salary_cycle:           2.9% relative attribution (End-of-month liquidity surge)            |
|  10. complaint_sbin_share_3d:  1.9% relative attribution (Bank brand complaint concentration)      |
+----------------------------------------------------------------------------------------------------+
```

### Key Analytical Takeaways:
1. **Recency Trumps Static Density**: While ATM count provides a baseline spatial opportunity filter ($14.2\%$), dynamic temporal momentum (`decay_intensity_30d` and `lag_count_7d`) accounts for $>45\%$ of predictive power.
2. **Spatial Diffusion Confirmed**: Neighbor diffusion (`spatial_lag_neighbor_7d`) provides $11.5\%$ attribution, confirming near-repeat spatial contagion.
3. **Upstream Complaint Telemetry Contributes Measurably**: Macro complaint bursts and bank brand concentrations provide the acute temporal triggers that distinguish active days from dormant periods.

---

## 2. Operational Trade-Offs: Precision vs. Recall across Resource Budget K

Police and banking divisions operate under variable resource constraints:
* **Top-5 Patrol Strategy ($K=5$, 1.25% Area)**: Precision@5 = 62.4%, PAI@5 = 12.1. Maximum tactical precision for specialized plainclothes interception teams.
* **Top-10 Patrol Strategy ($K=10$, 2.50% Area)**: Precision@10 = 55.9%, PAI@10 = 8.81. Optimal balance for daily municipal sector patrols.
* **Top-20 Patrol Strategy ($K=20$, 5.00% Area)**: Precision@20 = 47.8%, Recall@20 = 36.2%, PAI@20 = 7.24. Recommended for bank fraud operations applying stepped-up ATM friction (dynamic limits, stepped-up biometric verification).

---
*Document Version: 2.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
