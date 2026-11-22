# Phase 1: Problem Definition
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Official Problem Statement

* **Problem ID**: SIH26184
* **Title**: Cybercrime Cash-Withdrawal Location Forecasting
* **Official Description**:
  > *"Estimate likely geographic withdrawal clusters from cybercrime complaint metadata such as time, amount, bank and geography. Classification/regression prototype; geographic feature engineering; evaluation of cluster prediction; actionable-intelligence report."*

The core investigation of this project is to determine whether supervised machine learning algorithms, trained on spatiotemporally aggregated cybercrime complaint metadata and banking telemetry indicators, can forecast geographic areas exhibiting elevated cybercrime-related cash-withdrawal activity during future operational windows.

---

## 2. Background and Motivation

The digitization of financial services in India—driven by the Unified Payments Interface (UPI), Immediate Payment Service (IMPS), Aadhaar-Enabled Payment Systems (AePS), and mobile banking—has revolutionized consumer transactions. However, this transition has coincided with an exponential surge in cyber-enabled financial fraud. According to the National Crime Records Bureau (NCRB) *Crime in India 2022* report, cybercrime incidents registered a 24.4% increase over the preceding year, with financial fraud accounting for over 70% of total reported incidents [1]. The Indian Cyber Crime Coordination Centre (I4C) under the Ministry of Home Affairs (MHA) processes tens of thousands of complaints daily via the National Cybercrime Reporting Portal (`cybercrime.gov.in`) and the national emergency helpline `1930` (Citizen Financial Cyber Fraud Reporting and Management System - CFCFRMS) [2].

In a typical cyber-fraud pipeline—encompassing phishing scams, investment frauds, digital arrest intimidation, and task-based deceptive schemes—the illicit proceeds undergo rapid digital layering. Fraudsters execute swift, multi-tiered electronic fund transfers across compromised or complicit bank accounts (known as "money mule" networks) to evade automated anti-money laundering (AML) circuit breakers [3]. 

However, digital layering represents only the intermediate phase of the crime lifecycle. The critical, culminating objective for cyber syndicates is **physical cash liquidation (cash-out)**. Perpetrators deliberately extract funds as physical currency through Automated Teller Machines (ATMs), Micro-ATMs, and banking correspondent (Bank Mitra) points. Once illicit funds are transformed into physical cash:
1. The real-time digital audit trail is terminated.
2. Inter-bank fund freezing mechanisms (such as CFCFRMS lien marks) become ineffective.
3. The physical cash enters the informal, untraceable cash economy.

The cash-out transaction constitutes the sole phase where the digital perpetrator or their physical proxy (the money mule / cash-runner) must physically interact with terrestrial infrastructure at a concrete geographic coordinate and timestamp [4]. Despite this physical vulnerability, contemporary law enforcement strategies remain primarily reactive, attempting post-hoc forensic tracing long after cash withdrawals have concluded. 

Developing a predictive capability to forecast **geographic areas with elevated withdrawal probability** provides an opportunity to transform law enforcement and banking oversight from reactive incident response to proactive spatial monitoring, risk-weighted surveillance, and timely operational deterrence.

---

## 3. Existing Challenges in Analyzing Cybercrime Withdrawal Records

Analyzing cybercrime withdrawal records presents distinct data science and operational challenges that differentiate it from conventional urban crime forecasting:

1. **Extreme Asymmetry and Spatiotemporal Dispersion**:
   Conventional street crimes (e.g., residential burglary, assault) exhibit strong spatial clustering grounded in routine activity theory and local environmental criminogenic factors. In contrast, cybercrime operates across decoupled spatial domains: the victim, the defrauding syndicate, the intermediate mule bank accounts, and the physical ATM terminal may reside in completely different districts, states, or jurisdictions.

2. **Severe Temporal Reporting Lags ("Golden Hour" Decay)**:
   Victims rarely report fraud instantaneously. While I4C operational guidelines emphasize the "Golden Hour" (the initial 1–2 hours following an unauthorized transaction where digital lien marks can prevent cash-out), the median complaint reporting latency often spans 6 to 48 hours [2]. During this lag, perpetrators execute planned, automated, or distributed cash extractions across physical terminals.

3. **Incomplete, Sparse, and Unstandardized Metadata**:
   Publicly recorded cybercrime complaints frequently contain free-text descriptions, partial account numbers, and unverified bank branch codes without structured geospatial coordinates. Conversely, bank-side ATM terminal transaction logs contain exact coordinates and terminal IDs but are strictly quarantined within proprietary, confidential banking firewalls protected by privacy legislation.

4. **Multi-Jurisdictional Silos**:
   Cybercrime complaint metadata is collected by state police forces and central coordination agencies (I4C), while transaction logs are held by commercial banks and payment network operators (e.g., NPCI). The absence of a unified, real-time shared schema creates fragmented operational visibility.

5. **Operational False Positive Overhead**:
   Unlike fraud detection models operating in software where a false positive triggers a digital 2FA challenge, a spatial prediction deployment involves allocating physical human resources (patrol units, bank security officers, surveillance monitoring). High false alarm rates directly exhaust municipal law enforcement capacity.

---

## 4. Critical Distinction of Geographic Entities

A common error in naive cybercrime analytics is the conflation of different spatial entities recorded in investigative dossiers. In this project, four distinct geographic entities are formally recognized and decoupled:

```
[Victim Home / Device] ----(Files Complaint)----> 1. Complaint Location (Victim Geo)
         |
    (Initiates Fund Transfer via UPI/NetBanking)
         v
[Victim Bank / ISP] ----(Network Gateway IP)----> 2. Reported Transaction Location (Virtual Geo)
         |
    (Layered across Mule Accounts)
         v
[Mule Account IFSC] ----(Branch Record)----------> 3. Bank/Branch Registered Region (Administrative Geo)
         |
    (Debit Card Swiped at Physical Terminal)
         v
[Physical ATM / POS] ---(Dispenses Cash)---------> 4. Verified Withdrawal Location (Physical Cash-Out Geo)
```

### Table 1: Decoupling Spatial Entities in Cybercrime Analysis

| Geographic Entity | Definition | Technical Representation | Why It Cannot Be Used as Cash-Out Proxy |
| :--- | :--- | :--- | :--- |
| **1. Complaint Location** | The physical or administrative location where the victim resides, experiences the loss, or registers the cybercrime report. | Victim's district, postal code, or GPS coordinate of mobile device when dialing `1930`. | A victim living in New Delhi defrauded via a fake investment portal has zero spatial proximity to the ATM in Surat where the mule withdraws the cash. Conflating these attributes causes models to forecast victim residential density rather than criminal cash extraction hotspots. |
| **2. Reported Transaction Location** | The virtual or network point of origin where the fraudulent digital transaction was initiated or processed. | IP address geolocation, cellular cell-tower ID, or gateway server location. | IP geolocation can be masked via Virtual Private Networks (VPNs), proxies, or Tor. Furthermore, digital transaction routing occurs entirely in network cyberspace and does not reflect terrestrial physical cash-out. |
| **3. Bank/Branch Registered Region** | The administrative geographic location of the home branch holding the victim's or mule's bank account. | Indian Financial System Code (IFSC), branch postal code, or bank clearing circle. | Modern digital banking enables non-home branch and inter-bank ATM withdrawals nationwide. A mule account opened online in a Mumbai branch can be liquidated at an ATM terminal in Jaipur or Kolkata. Branch IFSC reflects administrative account creation, not physical cash-out. |
| **4. Verified Withdrawal Location** | The actual physical coordinate and terminal identifier where currency was mechanically dispensed from an ATM, Micro-ATM, or Bank Mitra point. | ATM Terminal Identifier (TID), merchant POS ID, validated latitude/longitude, or high-resolution spatial cell (e.g., H3 hex cell). | **This is the true operational ground truth for cash-out forecasting.** Only this entity represents the physical spatiotemporal convergence of the criminal operative, the physical currency, and the terrestrial terminal. |

**Methodological Imperative**: Models designed in this project exclusively treat the **Verified Withdrawal Location** (or its spatiotemporally aggregated proxy) as the target variable. Complaint metadata (time, claimed amount, bank name, complaint inflow rate) are treated strictly as exogenous predictive features, never as direct spatial labels.

---

## 5. Specific Problem Statement

Formally, let the operational geographic region of interest $\mathcal{S} \subset \mathbb{R}^2$ be partitioned into $M$ non-overlapping spatial cells:
$$\mathcal{S} = \{c_1, c_2, \dots, c_M\}$$
Let continuous time be discretized into uniform, non-overlapping operational time windows of duration $\Delta t$ (e.g., 24 hours, 7 days):
$$\mathcal{T} = \{t_1, t_2, \dots, t_N\}$$

Given historical cybercrime complaint metadata, inter-bank settlement alerts, and spatial infrastructure features observed up to time $t$:
$$\mathcal{H}_t = \{\mathbf{x}_{c, \tau} \mid c \in \mathcal{S}, \, \tau \le t\}$$

The objective is to train a supervised machine learning function $f_\theta$ that maps historical feature vectors $\mathbf{x}_{c, t}$ to an estimated cash-withdrawal outcome $Y_{c, t+\Delta t}$ in cell $c$ during the subsequent forecast horizon $t+\Delta t$:

* **Classification Target**: $Y_{c, t+\Delta t} \in \{0, 1\}$, indicating whether the number of verified cash-withdrawal incidents $k_{c, t+\Delta t}$ will exceed an operational threshold $\tau_{\text{thresh}}$ (i.e., $Y = \mathbb{I}(k_{c, t+\Delta t} \ge \tau_{\text{thresh}})$).
* **Regression Target**: $Y_{c, t+\Delta t} \in \mathbb{R}_{\ge 0}$ (or $\mathbb{Z}_{\ge 0}$), estimating the continuous intensity or discrete count of verified withdrawal incidents $k_{c, t+\Delta t}$.

---

## 6. Aim of the Project

The primary aim of this project is to conceptualize, design, and evaluate a reproducible, academically rigorous supervised machine learning and geospatial analytics framework capable of forecasting spatial grid cells with an elevated likelihood or count of cybercrime cash-withdrawal activity over future time horizons, producing actionable spatial intelligence for authorized investigative and preventive deployment.

---

## 7. Measurable Objectives

To achieve this aim, the project defines seven measurable, time-bounded, and technically concrete objectives:

1. **Objective 1 (Domain Disambiguation & Literature Baseline)**: Formulate a comprehensive taxonomy distinguishing cybercrime spatial entities and synthesize findings from at least 12 peer-reviewed studies across financial fraud, spatial point processes, and predictive policing by the conclusion of Phase 1.
2. **Objective 2 (Data Feasibility & Schema Formalization)**: Evaluate the accessibility, legal restrictions, and structural attributes of candidate cybercrime datasets (I4C, NCRB, open banking, PaySim) and formalize an end-to-end data dictionary and privacy-compliant synthetic data generation specification by Phase 2.
3. **Objective 3 (Spatiotemporal Discretization & Aggregation)**: Implement a spatial partitioning mechanism (e.g., Uber H3 discrete global grid system or uniform planar UTM grids at $1\,\text{km} \times 1\,\text{km}$) and aggregate event-level metadata into structured time-series panels over discrete intervals ($\Delta t \in \{24\,\text{h}, 7\,\text{d}\}$) during Phase 3.
4. **Objective 4 (Geographic Feature Engineering)**: Construct a multi-faceted feature matrix comprising historical lag counts (7-day, 14-day, 30-day moving averages), bank brand concentrations, withdrawal value statistics, and spatial neighbor exposure indices, avoiding temporal leakage during Phase 3.
5. **Objective 5 (Comparative Supervised Modeling)**: Train and benchmark candidate supervised models—including regularized logistic/Poisson regression baselines, Random Forest ensembles, and Gradient Boosted Decision Trees (XGBoost/LightGBM)—against naive persistent and spatial lag baselines under strict chronological cross-validation during Phase 4.
6. **Objective 6 (Rigorous Spatiotemporal Evaluation)**: Quantify predictive efficacy using domain-appropriate spatial and imbalanced metrics, specifically Precision@K, Recall@K, Area Under the Precision-Recall Curve (PR-AUC), and the Predictive Accuracy Index (PAI) [5], demonstrating statistically significant outperformance over naive baselines.
7. **Objective 7 (Interpretable Intelligence Generation)**: Construct an operational intelligence reporting prototype that extracts localized SHAP (SHapley Additive exPlanations) feature attribution scores and renders interactive GIS heatmaps with clear confidence intervals for authorized decision support during Phase 5.

---

## 8. Research Questions

This research investigates five foundational questions:

* **RQ1 (Spatiotemporal Predictability)**: *Does historical cybercrime complaint metadata exhibit sufficient spatial and temporal autocorrelation to enable statistically superior forecasts of cash-withdrawal activity compared to naive random or uniform distributions?*
* **RQ2 (Problem Formulation Trade-offs)**: *How do classification (binary hotspot identification) and regression (incident count forecasting) formulations compare regarding predictive stability, sensitivity to sparse counts, and utility for operational law enforcement resource scheduling?*
* **RQ3 (Feature Efficacy)**: *Which category of features—temporal recurrence lags, financial magnitude aggregations, banking institution indicators, or spatial neighborhood diffusion terms—contributes the greatest predictive power for localized withdrawal forecasting?*
* **RQ4 (Evaluation Metric Alignment)**: *Do standard classification metrics (e.g., ROC-AUC, accuracy) accurately reflect operational utility in highly sparse spatial grids, or do localized spatial metrics (PAI, PEI, Precision@K) provide a more faithful measurement of practical investigative value?*
* **RQ5 (Fairness, Bias, and Interpretability)**: *How can predictive cash-withdrawal models incorporate Explainable AI (XAI) to communicate uncertainty and prevent disparate spatial policing impacts stemming from reporting bias?*

---

## 9. Proposed Scope

### In-Scope:
* Aggregating historical cybercrime complaint and withdrawal metadata across regular spatial grid units (e.g., $1\,\text{km} \times 1\,\text{km}$ or H3 Hexagons Resolution 7/8).
* Formulating and comparing binary classification (hotspot vs. non-hotspot) and discrete regression (count prediction) supervised architectures.
* Developing temporal feature pipelines with strict walk-forward (chronological) splitting to eliminate lookahead bias.
* Applying unsupervised density clustering (DBSCAN / ST-DBSCAN) strictly as an exploratory baseline and spatial feature generator, distinct from the supervised predictive models.
* Benchmarking models using specialized spatial crime forecasting indices (PAI, PEI) alongside machine learning metrics (PR-AUC, F1-score, Precision@K).
* Designing an automated, template-based intelligence briefing summarizing forecasted high-risk zones, key contributing features (SHAP), and uncertainty bands.

### Out-of-Scope (Explicit Guardrails):
* **No Individual Attribution**: The system does **not** identify, profile, or predict individual criminals, suspect identities, or personal banking clients.
* **No Deterministic Crime Prediction**: The system does **not** claim to predict the exact minute, exact street address, or deterministic occurrence of an individual crime event.
* **No Autonomous Policing / Enforcement**: The prototype is strictly a **decision-support tool** for authorized investigators and bank risk officers; it does not trigger automated punitive, account-freezing, or kinetic police actions.
* **No Ingestion of Direct PII**: Real names, national identity numbers (Aadhaar), full credit card numbers (PAN), and plain account credentials are systematically excluded from data pipelines.

---

## 10. Assumptions and Constraints

### Technical Assumptions:
1. **Spatial Boundedness of Cash-Out**: While digital scamming occurs remotely, the conversion of stolen digital balances into cash requires physical interaction with localized terminal infrastructure (ATMs, POS, cash-points).
2. **Persistence and Routine Paths**: Organized mule syndicates tend to optimize cash extraction routes around specific ATM clusters characterized by high cash availability, 24/7 accessibility, proximity to transit corridors, and reduced direct surveillance [4].
3. **Temporal Coherence**: A burst of financial cybercrime complaints reported over a regional banking circle exhibits a delayed, correlated physical withdrawal echo within a predictable temporal window ($\Delta t \approx 12\text{--}72\text{ hours}$).

### Project Constraints:
1. **Confidentiality and Legal Restrictions**: Public access to real-time bank ATM transaction logs and full I4C complaint dockets is restricted under the Digital Personal Data Protection (DPDP) Act 2023, the Banking Regulation Act 1949, and RBI Master Directions.
2. **Data Modality**: Due to regulatory confidentiality, primary empirical validation must be established using an open, rigorously designed, mathematically consistent synthetic data generator calibrated against published aggregate cybercrime statistics (NCRB/RBI/I4C).
3. **Computational Environment**: Algorithms must be feasible for execution on standard workstation hardware (CPU / mid-tier GPU) within standard undergraduate development environments (Python, Scikit-learn, XGBoost, GeoPandas).

---

## 11. Expected Outcomes

1. **Analytical Research Dossier**: A fully documented Phase 1 report establishing the theoretical, mathematical, and practical foundations of cybercrime withdrawal forecasting.
2. **Validated Data Engineering Specification**: A formal data dictionary and reproducible synthetic data generation pipeline simulating realistic spatiotemporal cash-out dynamics.
3. **Supervised ML Prototype Architecture**: A modular, leak-free Python codebase evaluating regularized linear models, tree ensembles, and count regressors under chronological backtesting.
4. **Actionable Intelligence Demonstration**: An interactive geographic dashboard output and standardized intelligence reporting template conveying spatial predictions, PAI scores, and SHAP explanation summaries for tactical decision-makers.

---

## 12. Potential Beneficiaries and Practical Applications

1. **State and National Law Enforcement Agencies (LEAs)**:
   * Tactical resource deployment: Scheduling preventive patrols or plainclothes monitoring around high-probability ATM clusters during identified peak withdrawal windows.
   * Inter-state task force coordination: Identifying recurring cross-border cash-out hubs exploited by inter-state cyber syndicates.
2. **Indian Cyber Crime Coordination Centre (I4C) & State Cyber Cells**:
   * Prioritizing secondary investigation requests: Correlating victim complaints logged via `1930` with predicted geographic zones to expedite CCTV footage preservation requests at specific ATM kiosks before footage is overwritten.
3. **Bank Fraud Risk Management (FRM) & ATM Operations Teams**:
   * Dynamic ATM risk scoring: Triggering elevated friction (e.g., reduced cash withdrawal limits per transaction, biometric/OTP step-up verification, or velocity limits) on high-risk card sweeps conducted at terminals inside forecasted hotspot zones.
   * Cash replenishment optimization: Adjusting cash logistics schedules to prevent fraudulent liquidity draining.

---
*Document Version: 1.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
