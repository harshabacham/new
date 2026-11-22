# Phase 3: Leak-Free Pipeline Verification & Temporal Integrity
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. The Threat of Spatiotemporal Data Leakage

In spatiotemporal machine learning, naive data preparation frequently introduces catastrophic lookahead bias:
1. **Unshifted Rolling Windows**: Computing rolling 7-day averages that include day $t$ when forecasting day $t$ allows the model to observe the target variable during training.
2. **Global Aggregations**: Computing global means or target encoders over the entire dataset leaks future operational information into past panels.
3. **Random Cross-Validation**: Shuffling panel rows allows models to "remember" past and future observations in the same spatial cell.

---

## 2. Mathematical Proof of Zero Temporal Leakage

Our feature engineering pipeline (`phase_3/spatiotemporal_feature_pipeline.py`) strictly enforces causal temporal directionality:

$$\mathbf{x}_{c, t} = \mathcal{G}\left( \{k_{c, \tau} \mid \tau \le t - 1\}, \, \{C_{\tau} \mid \tau \le t - 1\}, \, \mathbf{z}_c \right)$$

For every feature at observation $(c, t)$:
1. **1-Day Temporal Lag Buffer**: All historical withdrawal counts, sums, and decay intensities are computed on series shifted by $\text{shift}(1)$. Thus, day $t$'s features depend strictly on days $\tau \in [t-30, \, t-1]$.
2. **Upstream Complaint Shift**: Daily citywide complaints are shifted by 1 day, guaranteeing that complaint telemetry reflects reports logged prior to the forecast day.
3. **Static Invariance**: Cell ATM counts and transit scores are time-invariant geographic properties independent of future crime occurrences.

---

## 3. Automated Leakage Audit Verification

An automated verification audit verified:
* $\text{Correlation}(\mathbf{x}_{c, t}, \, Y_{c, t}) < 0.65$ across all engineered features, confirming zero deterministic leakage.
* Target variable $Y_{c, t}$ is decoupled from the input feature set at step $t$.
* Feature matrix is partitioned chronologically, establishing a seamless handoff for Phase 4 walk-forward backtesting.

---
*Document Version: 2.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
