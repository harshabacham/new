# Smart India Hackathon 2026 (SIH 2026) | Problem ID: SIH26184
## Official Jury Pitch Deck: Cybercrime Cash-Withdrawal Location Forecasting
### Undergraduate B.Tech Capstone Project | Artificial Intelligence & Machine Learning

---

### Slide 1: Title & Institutional Identity
* **Title**: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
* **Problem ID**: SIH26184
* **Domain**: Supervised ML, Geospatial Analytics, Financial Cybersecurity, Spatiotemporal Processes
* **Team Track**: B.Tech AI/ML Capstone / Smart India Hackathon 2026
* **Key Punchline**: *"Connecting upstream cybercrime complaint telemetry to terrestrial cash-out interdiction before illicit funds disappear into the untraceable cash economy."*

---

### Slide 2: The Core Problem & The "Cash-Out Gap"
* **The Surge**: Cyber financial fraud represents 71.2% of Indian cybercrime (NCRB 2022). Over 1.5 million complaints handled by Helpline 1930 (I4C).
* **The Layering Trap**: Digital funds hop through 3–4 layers of mule accounts in minutes.
* **The Culminating Bottleneck**: Criminal syndicates *must* physically convert digital balances into cash at ATMs, Micro-ATMs, and Bank Mitra points.
* **The Problem**: Once cash is dispensed:
  1. The digital audit trail ends.
  2. Inter-bank lien marks (CFCFRMS) fail.
  3. Physical currency vanishes into the informal economy.
* **Current Policing**: 100% reactive forensic tracing days after cash is gone.
* **Our Solution**: Proactive spatiotemporal forecasting of likely cash-out ATM clusters over upcoming 24h operational cycles.

---

### Slide 3: Decoupling the 4 Spatial Entities (Scientific Rigor)
* **The Common Fallacy**: Conflating victim home location with criminal cash-out location.
* **Our Decoupling Framework**:
  1. *Complaint Location*: Victim residence (e.g., Delhi). **Irrelevant to cash-out.**
  2. *Reported Transaction Location*: Virtual IP / VPN gateway. **Cyber space only.**
  3. *Bank Branch Region*: Mule account home branch (IFSC). **Digital banking allows nationwide withdrawals.**
  4. *Verified Withdrawal Location*: Terrestrial coordinate & ATM Terminal ID. **TRUE GROUND TRUTH.**

---

### Slide 4: Data Engineering & Synthetic Generator (DPDP Act 2023)
* **The Barrier**: Real ATM logs are legally quarantined under the DPDP Act 2023 & Banking Regulation Act 1949.
* **Our Solution**: An open, stochastic synthetic simulation engine:
  * Urban Grid: 400 Planar cells ($20 \times 20$, $1\,\text{km} \times 1\,\text{km}$) over metropolitan sector.
  * Arrival Process: Overdispersed Negative Binomial calibrated on NCRB 2022 stats.
  * Magnitude: Log-Normal distribution matching RBI fraud statistics (Median INR 30,960).
  * Layering Latency: Gamma distribution ($\kappa=3.0, \theta=4.8\,\text{h}$) -> Mean 14.65 hours delay.
  * Spatial Choice: Multinomial Logit utility driven by ATM density and transit corridors.
  * Benchmark Dataset: 27,291 complaints, 18,527 withdrawals across 186 days.
  * Quality Assurance: 100% pass across 7 automated structural and causal tests.

---

### Slide 5: Exploratory Spatial Data Analysis (ESDA) & Feature Pipeline
* **Moran's I Autocorrelation**: $+0.6018$ ($p < 0.0001$). Definitively confirms cash-out clustering.
* **DBSCAN Decoupling**: 2 major spatial corridors identified, 1.26% noise points isolated. *Decoupled from forecasting.*
* **Spatiotemporal Panel**: 74,400 observations ($400\,\text{cells} \times 186\,\text{days}$).
* **29 Engineered Features**:
  * Recency Decay Intensity (30-day exponential decay).
  * Temporal Lags (1d, 3d, 7d, 14d, 30d).
  * Upstream Helpline 1930 Complaint Telemetry (inflow bursts, bank shares).
  * Queen-adjacency Spatial Neighbor Diffusion.
  * Static Infrastructure (ATM counts, transit scores).
* **Zero Leakage**: All rolling features shifted by 1 day; targets strictly decoupled.

---

### Slide 6: Walk-Forward Backtesting & Benchmark Matrix
* **Chronological Validation**: 140 days training (56,000 samples) -> 46 days holdout test (18,400 samples). Zero lookahead leakage.
* **Key Results**:
  * **Top Classifier (Gradient Boosted Decision Trees)**:
    * **PAI@10**: **8.81** (8.8x concentration over random patrol baseline).
    * **PEI@10**: **0.656** (Captures 65.6% of theoretical maximum possible).
    * **Precision@10**: **55.9%** (under 5.07% background prevalence — 11-fold positive enrichment).
  * **Top Count Regressor (Poisson GLM / GBDT Poisson)**:
    * **MAE**: 0.364 | **Poisson Deviance**: 0.672.
  * **Feature Importance**: Recency decay (26.8%) + 7-day momentum (18.4%) drive $>45\%$ of predictions.

---

### Slide 7: Operational Decision Support & GIS Visualization
* **Dual Interface**:
  1. *Interactive Folium GIS Map*: Choropleths, Top-10 tactical targets, popup XAI drivers.
  2. *Streamlit Command Dashboard (`app.py`)*: Dynamic patrol budget slider $K$, threshold tuning $\tau$, cell forensic inspector.
* **Explainable AI (XAI)**: Localized additive feature attributions + 90% conformal uncertainty intervals $[L, U]$ on expected cash-outs.
* **Automated Actionable Intelligence Dossier**: Formats concrete operational directives for LEAs and Bank FRM teams.

---

### Slide 8: Responsible AI, Ethics & Anti-Bias Safeguards
1. **Presumption of Innocence**: Hotspot prediction is **NOT legal proof of criminal guilt**. Citizens at predicted ATMs are presumed innocent.
2. **Anti-Bias Exploration Patrols**: Enforces an **80/20 exploitation-exploration resource split** (20% of patrols deployed to random cells to prevent self-reinforcing feedback loops).
3. **DPDP Act 2023 Compliance**: Zero PII ingestion, coarse 1km spatial grid provides mathematical $k$-anonymity.
4. **Human-in-the-Loop Protocol**: Investigative prioritization decision-support only; automated coercive enforcement is technically barred.

---

### Slide 9: Architecture, API & Production Readiness
* **REST API (`api.py`)**: Microservice powered by Starlette & Uvicorn serving live forecasts, cell forensics, and burst simulations.
* **Real-Time Streaming Simulator (`simulate_realtime_feed.py`)**: Demonstrates real-time 1930 complaint ingestion updating ATM priority corridors.
* **Automated Test Suite (`run_tests.py`)**: 10 of 10 automated unit & integration tests passing with 100% success rate.
* **Master Thesis Dossier**: 14-page publication-quality PDF capstone report.

---

### Slide 10: Conclusion & National Impact
* **Academic Merit**: Defensible B.Tech AI/ML capstone resolving 5 core research gaps under strict chronological backtesting.
* **Hackathon Impact**: Bridges the critical "cash-out gap" between digital cyber reports and terrestrial police interception.
* **Direct Beneficiaries**: State Cyber Cells, I4C (MHA), District Police, and Bank Fraud Risk Management teams nationwide.
