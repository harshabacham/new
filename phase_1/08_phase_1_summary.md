# Phase 1: Executive Summary & Phase 2 Handoff Plan
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Executive Synthesis: The Nine Core Research Answers

```
+---------------------------------------------------------------------------------------------------------+
|                                    NINE CORE RESEARCH ANSWERS AT A GLANCE                               |
+---------------------------------------------------------------------------------------------------------+
|  1. Problem:        Forecasting spatial cells with elevated cybercrime cash-out activity                |
|  2. Utility:        Enables proactive police patrol & bank ATM friction before cash disappears          |
|  3. Established:    Physical muling geography, grid-based ML validity, spatial PAI/PEI metrics          |
|  4. Research Gap:   Connecting upstream complaint bursts to downstream terrestrial cash-out forecasting |
|  5. Data Needed:    Spatiotemporal panels with timestamps, amounts, banks, and verified cell labels     |
|  6. Initial ML:     Option A (Calibrated Random Forest / XGBoost Classification) + Poisson Baseline     |
|  7. Evaluation:     Chronological Walk-Forward Backtesting evaluated via PAI, PEI, Precision@K, PR-AUC  |
|  8. Limitations:    Regulatory banking secrecy, reporting latency decay, zero-inflation, runaway bias   |
|  9. Phase 2 Bridge: Finalize grid resolution (H3 Res 7 vs 1km UTM) & calibrate synthetic generator     |
+---------------------------------------------------------------------------------------------------------+
```

### Q1: What problem are we solving?
We are investigating whether supervised machine learning models can forecast geographic areas (discrete spatial grid cells) exhibiting elevated cybercrime-related cash-withdrawal reporting activity over future operational time windows (e.g., 24–72 hours) based on historical complaint telemetry, financial attributes, banking indicators, and built-environment infrastructure.

### Q2: Why is it useful?
In the cybercrime lifecycle, physical cash extraction at ATMs and cash-points represents the single phase where digital perpetrators or their money mule proxies must interact with terrestrial physical infrastructure. Once stolen balances are liquidated into physical currency, digital fund-freezing mechanisms (such as I4C CFCFRMS lien marks) fail and the digital audit trail terminates. Providing spatial forecasts allows Law Enforcement Agencies (LEAs) to deploy targeted deterrence patrols and banks to implement risk-weighted ATM friction (dynamic limits, stepped-up biometric verification) *before* funds vanish into the untraceable cash economy.

### Q3: What has existing research already established?
Existing literature proves that:
1. Cybercrime cash-out operations rely heavily on physical, localized social and transit networks rather than purely virtual operations [Leukfeldt et al., 2017].
2. Spatial grid discretization combined with supervised tree ensembles (Random Forest) is an empirically validated framework for urban incident forecasting [Lin et al., 2018; Bogomolov et al., 2014].
3. Evaluating spatial predictions via global accuracy or ROC-AUC is misleading; resource-bounded operational evaluations require localized indices such as the Prediction Accuracy Index (PAI) and Predictive Efficiency Index (PEI) [Chainey et al., 2008; White et al., 2023].
4. Predictive policing models risk runaway feedback loops if trained naively on enforcement-driven data without bias mitigation [Ensign et al., 2018; Lum & Isaac, 2016].

### Q4: What research gap can we reasonably investigate?
While existing financial cybercrime machine learning concentrates almost exclusively on digital transaction graphs (AML/fraud detection), and conventional spatial criminology models focus on street violence using physical built-environment POIs, **no established open framework connects upstream cybercrime complaint telemetry to downstream spatiotemporal cash-out forecasting under strict chronological evaluation.** We address this gap with an open, reproducible, leak-free spatiotemporal modeling and explainability pipeline.

### Q5: Which data do we need?
We require spatiotemporal event records containing:
* Upstream complaint metadata: Incident timestamp, complaint registration timestamp, defrauded amount, fraud category, and victim bank code.
* Downstream verification ground truth: Verified withdrawal timestamp, cash amount, and geographic coordinates / grid cell ID.
* Geospatial infrastructure context: Cell ATM density, proximity to commercial transit hubs, and historical spatial lag features (7-day, 14-day, 30-day activity).
Because individual ATM transaction logs are legally confidential under the DPDP Act 2023 and Banking Regulation Act 1949, primary open empirical experimentation will use a mathematically consistent, calibrated synthetic data engine.

### Q6: Which supervised-learning approach should we test first?
We recommend testing **Option A (Spatiotemporal Binary Classification with calibrated probabilistic output)** first, using **Random Forest** and **XGBoost**, benchmarked against **Regularized Logistic Regression** and a **Negative Binomial Count Regressor (Option B)**. Option A directly addresses the operational command decision ("Which Top-$K$ cells should receive surveillance during the next operational window?").

### Q7: How will we evaluate it?
Models will be evaluated strictly via **Rolling-Origin Chronological Walk-Forward Backtesting** (eliminating lookahead bias). Efficacy will be measured using:
* Machine Learning Metrics: Area Under the Precision-Recall Curve (PR-AUC), F1-Score, and Precision@K / Recall@K ($K \in \{5, 10, 20\}$).
* Specialized Spatial Indices: Prediction Accuracy Index (PAI) and Predictive Efficiency Index (PEI).
* Baseline Outperformance: Benchmarking against naive persistent (yesterday=today) and theory-driven chronic flag + boost moving averages [Lee et al., 2020].

### Q8: What limitations could prevent reliable forecasting?
1. Severe zero-inflation and spatial sparsity: Over 90% of grid cells in micro-temporal windows will experience zero events.
2. Reporting latency ("Golden Hour" decay): Victims reporting frauds days after occurrence degrade the temporal correlation between complaint and withdrawal.
3. Multi-jurisdictional spatial dispersion: Cross-state cash sweeps introduce spatial variance that simple local moving averages cannot easily capture.
4. Runaway feedback loops: Directing police surveillance exclusively to historically predicted ATM clusters can distort future ground-truth data generation.

### Q9: What decisions must be resolved before Phase 2?
1. Spatial Index Selection: Finalizing whether to use Uber H3 hexagonal discrete global grid system (Resolution 7 / 8) or uniform Cartesian planar UTM $1\,\text{km} \times 1\,\text{km}$ grid cells.
2. Temporal Window Granularity: Deciding whether the primary forecast interval $\Delta t$ should be 24 hours (tactical daily deployment) or 7 days (strategic weekly patrol scheduling).
3. Synthetic Engine Calibration: Setting macro probability distributions (log-normal fraud amounts, Gamma-distributed layering delays) to match published NCRB 2022 and RBI 2024 empirical proportions.

---

## 2. Phase 1 Completion Checklist

### Table 1: Phase 1 Deliverables & Academic Standards Verification

| Deliverable Artifact | File Name | Status | Quality & Academic Standard Verified |
| :--- | :--- | :--- | :--- |
| **Problem Definition** | `phase_1/01_problem_definition.md` | **COMPLETE** | Official SIH26184 problem statement; 7 measurable objectives; 5 research questions; clear decoupling of Complaint, Transaction, Branch, and Withdrawal locations; non-predictive guardrails formalized. |
| **Literature Review** | `phase_1/02_literature_review.md` | **COMPLETE** | 16 authoritative sources reviewed across all 8 required sub-areas; verified DOIs, author lists, datasets, algorithms, and project relevance; peer-reviewed vs. government reports explicitly distinguished. |
| **Research Gap Analysis** | `phase_1/03_research_gap_analysis.md` | **COMPLETE** | 16-study comparative matrix; 5 deep research gaps formulated; defensible, realistic undergraduate B.Tech scope defined without inflated novelty claims. |
| **Dataset Feasibility** | `phase_1/04_dataset_feasibility.md` | **COMPLETE** | 6 candidate sources investigated; regulatory privacy barriers (DPDP Act 2023, Banking Regulation Act) detailed; mathematical synthetic generation framework formulated; 19-field data dictionary established. |
| **Proposed Methodology** | `phase_1/05_proposed_methodology.md` | **COMPLETE** | Comparative formulation of Option A (Classification) vs. Option B (Regression); candidate algorithms (Logistic, Poisson, RF, XGBoost); DBSCAN role decoupled as exploratory ESDA; 9-stage leak-free pipeline; walk-forward validation diagram. |
| **Evaluation & Ethics** | `phase_1/06_evaluation_and_ethics.md` | **COMPLETE** | 4-tier evaluation strategy; mathematical formulas for PAI, PEI, Precision@K, PR-AUC; zero-guarantee accuracy pledge; 5 responsible AI governance pillars; explicit separation of Association vs. Prediction vs. Proof of Guilt. |
| **BibTeX Bibliography** | `phase_1/07_references.bib` | **COMPLETE** | 19 fully formatted, verified BibTeX records with complete publication metadata. |
| **Phase 1 Summary** | `phase_1/08_phase_1_summary.md` | **COMPLETE** | Nine core research answers synthesized; deliverable verification table; detailed handoff plan for Phase 2. |
| **Master Documentation**| `README.md` | **COMPLETE** | Master navigation hub, repository map, phase sequence, and academic integrity declarations. |

---

## 3. Clear Handoff Plan for Phase 2: Dataset Collection and Validation

With the scientific foundations, mathematical formulations, and governance guardrails established in Phase 1, Phase 2 will transition into concrete data engineering:

```
+----------------------------------------------------------------------------------------------------+
|                                    PHASE 2 WORKSTREAM BREAKDOWN                                    |
+----------------------------------------------------------------------------------------------------+
|  Workstream 2.1: Spatial Boundary & Grid Calibration                                               |
|                  Define urban bounding box; generate H3 / UTM grid GeoDataFrame; map ATM densities.|
|                                                                                                    |
|  Workstream 2.2: Synthetic Data Engine Implementation                                              |
|                  Implement stochastic generator (Poisson complaint bursts, Gamma layering delays,  |
|                  multinomial logit spatial cash-out destination choice).                           |
|                                                                                                    |
|  Workstream 2.3: Data Validation & Quality Assurance Suite                                         |
|                  Automated schema assertion tests; null rate checks; spatiotemporal integrity;      |
|                  statistical validation against macro NCRB / RBI benchmark distributions.          |
|                                                                                                    |
|  Workstream 2.4: Data Storage & Schema Serialization                                               |
|                  Export validated benchmark dataset to Parquet / CSV accompanied by JSON schema.   |
+----------------------------------------------------------------------------------------------------+
```

### Immediate Prerequisites for Phase 2 Launch:
1. Set up the Python data engineering environment with `pandas`, `numpy`, `geopandas`, `shapely`, and `scipy`.
2. Construct the configuration file (`config/phase_2_data_config.yaml`) defining grid bounds, simulation time horizon (e.g., 180 simulated days), and random seed for full reproducibility.
3. Establish unit tests to verify that synthetic cash-out timestamps strictly succeed complaint timestamps ($\Delta \tau > 0$), preventing temporal inversion artifacts.

---
*Document Version: 1.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
