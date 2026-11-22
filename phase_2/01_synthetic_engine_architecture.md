# Phase 2: Synthetic Data Engine Architecture & Mathematical Foundations
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Motivation and Regulatory Compliance (DPDP Act 2023)

In accordance with findings established in Phase 1 ([04_dataset_feasibility.md](file:///c:/Users/harsh/OneDrive/Desktop/supervised/phase_1/04_dataset_feasibility.md)), primary real-world ATM transaction logs and police investigation dockets are legally quarantined under:
1. **Digital Personal Data Protection (DPDP) Act 2023 (India)**.
2. **Banking Regulation Act 1949 & RBI Master Directions on Financial Fraud**.
3. **Sections 43A and 72A of the Information Technology Act 2000**.

To ensure full statutory compliance, open reproducibility, and rigorous academic evaluation, Phase 2 implements a high-fidelity **Stochastic Synthetic Cybercrime Generation Engine**. This engine simulates the spatiotemporal interaction between upstream cybercrime complaint streams and physical ATM cash extractions across a metropolitan territory (20 km x 20 km; 400 spatial cells).

---

## 2. Mathematical Specification of the Simulation Engine

```
+----------------------------------------------------------------------------------------------------+
|                             STOCHASTIC SYNTHETIC GENERATION PIPELINE                               |
+----------------------------------------------------------------------------------------------------+
|  1. Urban Space:        M = 400 Planar Cells (20x20 grid, 1km x 1km resolution)                    |
|  2. Infrastructure:     N_ATM(c) ~ Poisson(lambda_c), modulated by commercial transit hubs        |
|  3. Daily Complaints:   C_t ~ NegativeBinomial(mu_t, alpha), calibrated on NCRB 2022/23            |
|  4. Defrauded Amounts:  A_i ~ LogNormal(mu=10.35, sigma=0.95), calibrated on RBI Fraud Disclosures |
|  5. Temporal Lags:      Delta_rep ~ Exp(18h) (reporting delay); Delta_layer ~ Gamma(3, 4.8h)       |
|  6. Spatial Choice:     P(c | i) = exp(U_c) / Sum_c' exp(U_c') (Multinomial Logit Destination)     |
+----------------------------------------------------------------------------------------------------+
```

### 2.1 Urban Spatial Discretization
The continuous geographic domain $\mathcal{S} \subset \mathbb{R}^2$ represents a representative metropolitan banking circle (Delhi NCR bounding box: $[28.50^\circ\text{N}, 28.70^\circ\text{N}] \times [77.10^\circ\text{E}, 77.30^\circ\text{E}]$) partitioned into $M = 400$ regular grid cells:
$$\mathcal{S} = \{c_{r, c} \mid r \in \{0, \dots, 19\}, \, c \in \{0, \dots, 19\}\}$$

### 2.2 Built-Environment Infrastructure Layering
Each spatial cell $c$ is assigned an automated teller density $N_{\text{ATM}}(c)$:
$$N_{\text{ATM}}(c) \sim \text{Poisson}(\lambda_{\text{infra}}(c))$$
where:
$$\lambda_{\text{infra}}(c) = \lambda_0 + \gamma_1 \text{TransitAccessibility}(c) + \epsilon_{\text{infra}}$$
Transit accessibility is governed by exponential distance decay to $K=4$ major urban economic hubs:
$$\text{TransitAccessibility}(c) = \exp\left( -\frac{\min_{h} d(c, \text{hub}_h)}{\sigma_{\text{transit}}} \right)$$

### 2.3 Upstream Cybercrime Inflow Process
Daily municipal cybercrime complaints $C_t$ are drawn from an overdispersed Negative Binomial process:
$$C_t \sim \text{NegativeBinomial}(\mu_t, \alpha)$$
where $\mu_t$ incorporates day-of-week seasonality (Monday surges, weekend troughs) and end-of-month salary cycle spikes:
$$\mu_t = \mu_0 \cdot \delta_{\text{dow}}(t) \cdot \delta_{\text{salary}}(t)$$

### 2.4 Physical Cash-Out Coupling & Stochastic Layering Delay
A realistic fraction $\rho = 0.68$ of financial cybercrime complaints convert into physical cash extraction events. The physical cash withdrawal occurs after an operational layering delay $\Delta \tau$:
$$\Delta \tau \sim \text{Gamma}(\kappa = 3.0, \, \theta = 4.8\,\text{hours})$$
Yielding a realistic mean layering duration of $\approx 14.4$ hours during which illicit funds are hopped through mule accounts.

### 2.5 Spatial Destination Choice Model (Multinomial Logit)
The probability $P(c \mid i)$ that cash-out $i$ is executed at terminal infrastructure in cell $c$ follows a random utility framework:
$$U(c) = \beta_1 \ln N_{\text{ATM}}(c) + \beta_2 \text{TransitScore}(c) + \beta_3 \text{MuleRingScore}(c) + \eta_c$$
$$P(c \mid i) = \frac{\exp(U(c))}{\sum_{c' \in \mathcal{S}} \exp(U(c'))}$$
where $\eta_c \sim \mathcal{N}(0, \sigma^2)$ introduces unobserved spatial heterogeneity.

---

## 3. Realism and Calibration Baseline

The generated benchmark dataset covers 181 continuous calendar days (January 1, 2026 to June 30, 2026):
* **Total Generated Complaints**: 27,291
* **Total Verified Physical ATM Cash-Outs**: 18,527 (67.9% conversion rate)
* **Median Defrauded Amount**: INR 30,960.21 (Mean: INR 48,677.25)
* **Average Operational Layering Delay**: 14.65 hours
* **Spatial Entity Decoupling**: 100.0% of events maintain strict separation between victim complaint location and cash-out terminal coordinate.

---
*Document Version: 2.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
