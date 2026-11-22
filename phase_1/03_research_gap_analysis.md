# Phase 1: Research Gap Analysis
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Comparative Analysis of Existing Literature

To rigorously identify the boundary between existing scientific literature and the specific objectives of SIH26184, the sixteen authoritative sources reviewed in Phase 1 are synthesized in Table 1 below across data sources, modeling techniques, evaluation strategies, operational limitations, and project relevance.

### Table 1: Comprehensive Literature Comparison Matrix

| Study | Year | Data | Method | Evaluation | Limitation | Relevance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Leukfeldt, Kleemans, & Stol** [4] | 2017 | 18 Dutch police investigation dossiers (40 criminal networks) | Social Network Analysis (SNA), qualitative content analysis | Network centrality, qualitative tie density | Retrospective police files; Western European context; no predictive machine learning | Proves money muling cash-out relies on physical, localized social and urban infrastructure |
| **Chainey, Tompson, & Uhlig** [5] | 2008 | London Metropolitan Police crime records (burglary, robbery) | Spatial point patterns, Kernel Density Estimation (KDE), spatial ellipses | Prediction Accuracy Index (PAI), hit rates | Evaluates static spatial density; lacks dynamic time-series features or ML classifiers | Defines the foundational spatial efficiency evaluation metric (PAI) used in this project |
| **Lin, Yen, & Yu** [6] | 2018 | Taipei City crime records + OpenStreetMap (OSM) POI data | Uniform grid ($500\,\text{m}$), Random Forest, SVM, Logistic Regression | Precision, Recall, F1-Score, ROC-AUC | Planar grid only; no rolling-origin temporal backtesting; street crime focus | Proves viability of grid-based supervised machine learning with geographic POI features |
| **Bogomolov et al.** [7] | 2014 | London crime incidents + mobile telecom CDRs + census data | $200\,\text{m}$ grid discretization, Random Forest binary classifier | Classification accuracy, Precision, Recall | Relies on proprietary mobile phone CDRs; random CV causes temporal leakage | Demonstrates binary hotspot classification over discrete cells using aggregated human activity features |
| **Mohler et al.** [8] | 2011 | LAPD geocoded residential burglary & vehicle theft records | Self-exciting point process (ETAS point process via EM) | Spatial search area hit rates, prospective capture percentage | High computational cost; cannot ingest structured tabular bank metadata or transaction attributes | Justifies spatiotemporal decay features: recent events temporarily boost localized event probabilities |
| **Wheeler & Steenbeek** [9] | 2021 | Dallas Police crime incidents + environmental risk features | Penalized Poisson GLM, Random Forest Regressor, Boosted Trees | MAE, RMSE, Poisson Deviance, Precision@K, PAI | Conventional violent crime; static street segment units; no transaction stream data | Benchmarks count regression vs. tree ensembles; guides our Option A vs. Option B model selection |
| **Lee, O, & Eck** [10] | 2020 | Portland Police Bureau 5-year crime incident records | "Flag-and-Boost" theory-driven moving average algorithm | Predictive Efficiency Index (PEI), PAI across 1-wk to 1-mo horizons | Heuristic manual thresholding; lacks automated multi-feature interactions | Establishes a competitive baseline heuristic (chronic flag + temporary boost moving average) |
| **Ester et al.** [11] | 1996 | Synthetic spatial benchmarks + spatial point databases | Density-Based Spatial Clustering of Applications with Noise (DBSCAN) | Cluster silhouette, noise identification ratio | Static Euclidean distance; cannot handle temporal progression or non-spatial features | Core unsupervised clustering baseline for Phase 3 Exploratory Spatial Data Analysis (ESDA) |
| **Birant & Kut** [12] | 2007 | Spatial oceanographic temperature sensor dockets | Spatiotemporal DBSCAN (ST-DBSCAN with dual $\varepsilon_1, \varepsilon_2$) | Spatiotemporal cluster purity, noise filtering accuracy | Descriptive unsupervised clustering only; cannot forecast future occurrences | Enables discovery of coordinated spatiotemporal withdrawal bursts across historical logs |
| **Adepeju, Rosser, & Cheng** [13] | 2016 | London Metropolitan Police burglary records | Spatial point process models across micro-grids ($50\text{--}500\,\text{m}$) | PAI, Recurrent Operational Hit Rate, Spatial Sparsity Ratio | Evaluated only point process & KDE outputs; no supervised gradient boosting models | Proves PAI is sensitive to study area size; mandates pairing PAI with Precision@K and PR-AUC |
| **White, Hunt, & Green** [14] | 2023 | NIJ Crime Forecasting Challenge multi-city police datasets | Mathematical analysis of spatial forecasting indices | Predictive Efficiency Index (PEI), resource-constrained PAI | Retrospective evaluation of static polygons; no probabilistic ML calibration | Establishes PEI as our secondary spatial metric to measure efficiency against theoretical maximum |
| **Assumpção et al.** [15] | 2022 | Large-scale proprietary transactional banking graphs | Heterogeneous Graph Neural Networks (GNN), multi-task learning | PR-AUC, F1-Score, False Positive Reduction at 99% Recall | Purely topological graph space; completely omits physical geographic cash-out locations | Highlights the core research gap: fraud detection focuses on digital graphs, ignoring spatial cash-out |
| **Ensign et al.** [16] | 2018 | Polya urn mathematical simulation + Oakland crime records | Mathematical feedback loop modeling, dynamical systems | Disparate impact ratio, sampling probability divergence | Evaluated victimless drug crime; financial fraud has victim-driven reporting dynamics | Alerts our project to sampling bias risks when directing spatial surveillance to predicted ATM clusters |
| **Lum & Isaac** [17] | 2016 | Oakland arrest dockets vs. NSDUH ground-truth health survey | Predictive point process modeling, demographic spatial mapping | Demographic disparity ratios, geographic risk distributions | Examines police discretion crimes rather than financial complaint telemetry | Emphasizes that models predict *reported activity*, not absolute ground-truth crime |
| **Lundberg & Lee** [18] | 2017 | Standard benchmark datasets in finance and healthcare | TreeSHAP, Shapley Additive exPlanations, cooperative game theory | Local accuracy, consistency, computational throughput | Computational overhead on dense spatiotemporal panels | Powers our Phase 5 intelligence module to provide interpretable feature attribution for flagged cells |
| **NCRB & I4C Reports** [1, 2] | 2023–2024 | Nationwide Indian cybercrime complaints (`cybercrime.gov.in`, `1930`) | Descriptive statistical aggregation, administrative tracking | Annual case growth rates, disposal rates, fund lien totals | Aggregate state-level statistics; lacks micro-level spatial coordinates or ML models | Establishes the empirical macro baseline of Indian financial cybercrime to calibrate synthetic data |

---

## 2. In-Depth Investigation of Research Gaps

A systematic analysis of Table 1 reveals five foundational research gaps at the intersection of financial fraud detection, spatiotemporal forecasting, and law enforcement analytics:

```
+---------------------------------------------------------------------------------------------------------+
|                                     THE FIVE CORE RESEARCH GAPS                                         |
+---------------------------------------------------------------------------------------------------------+
|                                                                                                         |
|  GAP 1: Digital Fraud Detection vs. Terrestrial Cash-Out Forecasting                                    |
|         [Existing ML focuses on digital transaction graphs; ignores where cash physically leaves]       |
|                                                                                                         |
|  GAP 2: Spatiotemporal Feature Engineering for Decoupled Financial Crimes                              |
|         [Conventional crime ML uses street network POIs; cybercrime needs banking & lag diffusion]      |
|                                                                                                         |
|  GAP 3: Evaluation Integrity & Temporal Leakage in Spatial ML                                           |
|         [Standard studies use random k-fold cross-validation; creates severe future-data leakage]       |
|                                                                                                         |
|  GAP 4: Ground-Truth Granularity vs. Strict Banking Confidentiality                                     |
|         [Real ATM logs are legally protected; absence of standardized open synthetic benchmarks]        |
|                                                                                                         |
|  GAP 5: Black-Box Spatial Predictions vs. Actionable Investigative Intelligence                         |
|         [Police cannot act on opaque risk heatmaps; require local SHAP explanations & uncertainty bands]|
|                                                                                                         |
+---------------------------------------------------------------------------------------------------------+
```

### Gap 1: Financial Fraud Analytics Focuses on Virtual Transaction Graphs, Neglecting Physical Cash-Out Geography
* **State of the Art**: Current state-of-the-art machine learning in financial cybercrime centers heavily on **digital fraud detection** and **Anti-Money Laundering (AML)** transaction monitoring [15]. Researchers employ Graph Neural Networks (GNNs), isolation forests, and sequence models (LSTM) to detect fraudulent accounts, identity theft, or synthetic mule rings within inter-bank transfer ledgers.
* **The Unaddressed Need**: These approaches operate entirely in topological graph space or virtual cyberspace. They track money moving from Account A to Account B to Account C, but they terminate their analytical scope once the digital transfer is flagged or cleared. In reality, criminal syndicates rely on physical cash extraction (ATMs, Micro-ATMs, Bank Mitras) to finalize the theft [4]. There is an absence of research connecting upstream cybercrime complaint telemetry (complaint volume, defrauded amounts, victim bank identities) to downstream **geographic cash-out forecasting**.

### Gap 2: Conventional Spatial Crime Forecasting Models Fail to Account for Decoupled Cybercrime Dynamics
* **State of the Art**: Spatial crime forecasting literature (e.g., Lin et al. [6], Mohler et al. [8], Wheeler & Steenbeek [9]) has advanced significantly for traditional street crimes (residential burglary, commercial robbery, vehicle theft). These models rely heavily on physical opportunity structures: street connectivity, bar density, commercial zoning, and localized social disorganization.
* **The Unaddressed Need**: Cyber-enabled financial fraud violates the fundamental spatial assumptions of traditional criminology. The perpetrator, victim, intermediate accounts, and physical ATM terminal operate across decoupled geographies (as formalized in Section 4 of `01_problem_definition.md`). Applying conventional spatial crime models directly to cybercrime records produces flawed predictions because the explanatory drivers are not street intersections or liquor stores, but **banking infrastructure density, regional complaint velocity, inter-bank settlement delays, and transportation hubs facilitating mule mobility**.

### Gap 3: Methodological Flaws in Evaluating Spatiotemporal Grid Forecasts (Temporal Leakage)
* **State of the Art**: A substantial portion of published spatial machine learning literature evaluates models using standard random $k$-fold cross-validation or out-of-bag validation (e.g., Bogomolov et al. [7]).
* **The Unaddressed Need**: Random splitting across spatiotemporal panels causes **catastrophic future-data leakage (lookahead bias)**. Because spatial and temporal processes exhibit strong autocorrelation, randomly holding out observations allows the model to train on future records in spatial cell $c$ at time $t+1$ to predict past records in cell $c$ at time $t$. To establish valid scientific credibility, models must be evaluated strictly using **chronological walk-forward (rolling-origin) temporal splitting**, where the training set strictly precedes the validation and test sets in time.

### Gap 4: Ground-Truth Scarcity and the Lack of Open, Privacy-Compliant Benchmarks
* **State of the Art**: Real-world cybercrime investigative dockets (held by I4C/police) and ATM withdrawal transaction logs (held by commercial banks) are strictly proprietary and protected by statutory privacy legislation (DPDP Act 2023, Banking Regulation Act 1949). Consequently, studies that use real data are non-reproducible, while open-source projects frequently rely on unverified toy datasets.
* **The Unaddressed Need**: The research community lacks an open, statistically grounded **synthetic benchmark generation framework** that realistically simulates the spatiotemporal interaction between cybercrime complaint bursts and physical ATM cash-outs while preserving full privacy. Developing such a framework allows algorithmic architectures to be benchmarked openly and transferred to authorized environments without code restructuring.

### Gap 5: Disconnect Between Academic Model Outputs and Operational Law Enforcement Utility
* **State of the Art**: Academic ML papers frequently report aggregate metrics such as ROC-AUC or global accuracy.
* **The Unaddressed Need**: Global accuracy and ROC-AUC are operationally meaningless to law enforcement agencies facing severe resource constraints. Police departments cannot patrol an entire municipal area based on an aggregate AUC score of 0.85; they require prioritized top-$K$ spatial allocations evaluated via **Precision@K**, **PAI**, and **PEI** [5, 13, 14]. Furthermore, black-box predictions lack investigative credibility: detectives and bank risk officers require **interpretable feature attributions (SHAP)** that explain why a specific grid cell is flagged, enabling informed, accountable decisions [18].

---

## 3. Defensible Research Scope for an Undergraduate B.Tech Project

In defining the novelty and scope of this undergraduate project, we adhere strictly to academic honesty and feasibility constraints:
* **We do NOT claim to be the first to apply machine learning to crime.** Criminological ML is well established [5, 6, 8, 9].
* **We do NOT claim to predict individual criminal identities or individual ATM transactions in real time.** Such claims are technically unsupportable and legally hazardous.
* **Our Specific, Defensible Contribution**: We investigate whether **spatiotemporal aggregation of cybercrime complaint metadata paired with banking infrastructure indicators can forecast elevated cash-withdrawal intensity across spatial grid cells under strict chronological validation, evaluated using specialized spatial metrics (PAI, PEI) and interpreted via Explainable AI.**

This defined scope represents an academically rigorous, technically viable, and practically valuable contribution directly aligned with the SIH26184 problem specification.

---
*Document Version: 1.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
