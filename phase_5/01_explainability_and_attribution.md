# Phase 5: Explainable AI (XAI) & Local Feature Attribution Methodology
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Operational Need for Explainable AI in Law Enforcement & Banking

Deploying machine learning models in policing and banking introduces serious accountability imperatives:
1. **Investigative Due Process**: Police patrol commanders cannot deploy tactical squads to specific neighborhoods on the basis of an uninterpretable "black-box" risk score. Field officers require concrete causal explanations (e.g., "7-day repeat muling momentum combined with a 40% surge in investment scam complaints").
2. **Bank Fraud Risk Proportionality**: Bank Risk Officers need explanatory justification to institute friction (e.g., lowering ATM cash withdrawal limits or requiring step-up 2FA) without penalizing legitimate commercial customers.
3. **Statutory Non-Discrimination**: Models must demonstrate that predictions are driven by financial cybercrime telemetry and built infrastructure, rather than protected demographic or socioeconomic attributes.

---

## 2. Mathematical Attribution Engine: Tree Attributions & Normalized Z-Deltas

For each prioritized spatial cell $c \in \mathcal{S}$ on forecast day $t$, the localized feature attribution vector $\boldsymbol{\phi}(c, t)$ decomposes the prediction into additive contributions:

$$\hat{y}(c, t) = \bar{y} + \sum_{j=1}^P \phi_j(c, t)$$

Where:
$$\phi_j(c, t) = w_j \cdot \left( \frac{x_{c, t, j} - \mu_j}{\sigma_j} \right)$$
* $w_j$ represents the global importance weight of feature $j$ derived from tree split gains.
* $x_{c, t, j}$ is the observed value of feature $j$ in cell $c$ on day $t$.
* $\mu_j, \sigma_j$ are the historical background mean and standard deviation of feature $j$.

The system automatically ranks the top positive drivers $\phi_j > 0$ and translates them into plain-language operational summaries (e.g., `"Historical Recency Momentum (30d) | Weekly Repeat Withdrawal Burst"`).

---

## 3. Conformal Prediction Uncertainty Bounds

Point forecasts of cash-out counts can be dangerously deceptive if they fail to communicate statistical uncertainty. Phase 5 computes **90% Conformal Prediction Intervals**:

$$\hat{C}_{90}(c) = \left[ \max\left(0, \, \hat{k}_c - \hat{q}_{0.90}\right), \quad \hat{k}_c + \hat{q}_{0.90} \right]$$

Where $\hat{q}_{0.90}$ is the 90th percentile of absolute calibration residuals evaluated on the chronological walk-forward holdout set.

---
*Document Version: 2.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
