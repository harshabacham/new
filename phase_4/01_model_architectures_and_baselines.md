# Phase 4: Supervised Model Architectures, Baselines & Benchmarking Strategy
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Candidate Algorithm Suite

To ensure scientific benchmarking, nine distinct model architectures spanning operational baselines, regularized generalized linear models (GLMs), bagging ensembles, and histogram-based gradient boosted decision trees were evaluated:

```
+----------------------------------------------------------------------------------------------------+
|                                    NINE-MODEL BENCHMARK TAXONOMY                                   |
+----------------------------------------------------------------------------------------------------+
|  1. Baseline 1:   Uniform Random Spatial Allocation (PAI = 1.0 Theoretical Baseline)               |
|  2. Baseline 2:   Naive Persistent Lag (Yesterday = Today)                                         |
|  3. Baseline 3:   Theory-Driven Chronic Flag + Temporary Boost Moving Average (Lee et al., 2020)   |
|  4. Model 4:      L2-Regularized Logistic Regression (Option A Linear Benchmark)                   |
|  5. Model 5:      Poisson GLM Regressor (Option B Statistical Count Benchmark)                     |
|  6. Model 6:      Balanced Random Forest Classifier (Option A Bagging Ensemble)                    |
|  7. Model 7:      Random Forest Regressor (Option B Non-Linear Regressor)                          |
|  8. Model 8:      Histogram Gradient Boosted Classifier (Option A Boosted Trees, LightGBM Engine)  |
|  9. Model 9:      Histogram Gradient Boosted Poisson Regressor (Option B Boosted Count Trees)      |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Walk-Forward Chronological Backtesting Protocol

To strictly eliminate lookahead bias and temporal leakage, models were evaluated under an **expanding-window chronological validation design**:

* **Temporal Separation**: No future records were exposed during feature derivation or training.
* **Final Holdout Window**:
  * **Training Period**: Days 1 to 140 (56,000 spatiotemporal cell-days).
  * **Test Holdout Period**: Days 141 to 186 (18,400 spatiotemporal cell-days, 46 continuous evaluation days).
  * **Holdout Hotspot Prevalence**: 5.07% (932 positive hotspot events across 18,400 grid-day observations).

---

## 3. Four-Tiered Metric Framework

1. **Classification Tier**: Precision, Recall, F1-Score, ROC-AUC, PR-AUC (Average Precision).
2. **Resource-Constrained Tactical Tier**: Precision@10, Recall@10, Precision@20, Recall@20 (measuring utility across police patrol capacity).
3. **Spatial Efficiency Tier**:
   $$\text{PAI} = \frac{n / N}{a / A}, \quad \text{PEI} = \frac{\text{PAI}}{\text{PAI}^*}$$
   Where $a/A = 10/400 = 2.5\%$ of urban space.
4. **Count Regression Tier**: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Poisson Deviance.

---
*Document Version: 2.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
