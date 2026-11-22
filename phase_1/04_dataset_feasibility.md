# Phase 1: Dataset Feasibility Study
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Candidate Dataset Investigation & Feasibility Assessment

A critical prerequisite for machine learning research is the objective evaluation of accessible data sources. In this feasibility study, six candidate real-world and benchmark data sources were investigated across Indian statutory repositories, open government portals, and international scientific datasets.

### Table 1: Comprehensive Dataset Feasibility Matrix

| Source / Dataset Name | Official Source URL | Geographic Coverage | Temporal Coverage | Available Fields | Are Withdrawal Locations Available? | Access Restrictions & Licensing | Suitability for Supervised Forecasting |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NCRB "Crime in India" Annual Reports** [1] | [ncrb.gov.in](https://ncrb.gov.in) | India (National, State/UT, 19 metropolitan cities) | Annual (1953–2022 published) | Aggregate case counts by IPC/IT Act sections, disposal rates, broad crime categories | **No**. Only state/city-level annual case tallies. | Open Public Domain (Government of India) | **Unsuitable for micro-forecasting**. Useful only for macro baseline calibration. |
| **Open Government Data (OGD) Platform India** | [data.gov.in](https://data.gov.in) | India (Varying by ministry / state) | Sporadic annual/monthly tables | State-level bank fraud counts, aggregate economic offense metrics | **No**. Strictly administrative summary tables. | Open Government Data License - India (OGDL) | **Unsuitable for micro-forecasting**. Lacks geospatial timestamps and coordinates. |
| **I4C / CFCFRMS Complaint System** [2] | [cybercrime.gov.in](https://cybercrime.gov.in) | India (Pan-India via `1930` & NCRP) | Real-time continuous internal stream | Complaint timestamp, defrauded amount, victim bank, suspect accounts, transaction IDs | **Proprietary/Internal**. Individual ATM cash-out coordinates held in restricted police dockets. | Strictly confidential under Section 43A/72A of IT Act & DPDP Act 2023. | **Ideal operational target, but inaccessible for open academic competitions.** |
| **RBI Annual Reports & Fraud Disclosures** [19] | [rbi.org.in](https://www.rbi.org.in) | India (Commercial banking system) | Annual financial year disclosures | Bank-group aggregate fraud amounts, volume of digital vs. card fraud | **No**. Only national banking system aggregate totals. | Public regulatory reports | **Unsuitable for micro-forecasting**. Useful for macroeconomic proportions only. |
| **PaySim Financial Simulator** [20] | [kaggle.com/datasets/ealaxi/paysim1](https://www.kaggle.com/datasets/ealaxi/paysim1) | Synthetic Mobile Money (African financial system proxy) | 744 hourly time steps (30 days simulated) | `step`, `type`, `amount`, `nameOrig`, `oldbalanceOrg`, `newbalanceOrig`, `nameDest`, `isFraud` | **No**. Contains `CASH_OUT` transaction types, but **zero geographic coordinates or terminal IDs**. | CC BY 4.0 Open License | **Partially suitable for transaction logic, but unsuitable for spatial forecasting.** |
| **Chicago Open Data Portal (Spatial Crime Benchmark)** [21] | [data.cityofchicago.org](https://data.cityofchicago.org) | Chicago, Illinois, USA | 2001–Present (daily updates) | Incident Date, Primary Crime Type, Location Description, Latitude, Longitude, Grid | **Yes**. Contains geocoded financial identity theft & deceptive practice records. | Open City Data License | **High scientific utility as a methodological spatial benchmark**, but non-Indian context. |

---

## 2. Definitive Feasibility Finding: The Regulatory Privacy Barrier

Our empirical inquiry establishes an unambiguous, verified fact:
> **No publicly accessible, lawful dataset in India currently provides paired, event-level cybercrime complaint metadata and granular physical ATM cash-withdrawal geographic coordinates (latitude, longitude, ATM Terminal ID).**

### Why Real ATM Cash-Out Logs Are Quarantined
1. **Digital Personal Data Protection (DPDP) Act 2023 (India)**: Individual transaction logs constitute protected personal and financial data. Exposing timestamps, account balances, and specific ATM locations creates severe re-identification risks for victims and banking customers.
2. **Banking Regulation Act, 1949 & RBI Master Directions on Fraud**: Indian commercial banks are legally mandated to maintain absolute confidentiality regarding customer account transactions and internal fraud alert ledgers. Transaction logs can only be shared with authorized Law Enforcement Agencies (LEAs) under formal judicial or investigative subpoenas (Section 91 of the Code of Criminal Procedure / Section 94 of BNSS).
3. **Operational Security of Investigations**: Publicly disseminating real-time ATM withdrawal clusters would compromise active police surveillance and inform organized cyber syndicates about monitored corridors.

---

## 3. Recommended Technical Strategy: The Realistic Synthetic-Data Prototype

Because public real-world datasets either lack spatial coordinates (PaySim, NCRB) or are legally quarantined (I4C, bank logs), our project adopts the gold-standard academic practice established in financial cybersecurity literature [20]: **constructing a mathematically rigorous, privacy-compliant Synthetic Data Generation Engine**.

### Mathematical Formulation of Synthetic Data Generation
The synthetic generator simulates the physical and spatiotemporal interaction between cybercrime complaint bursts and physical ATM cash extractions across a realistic municipal urban grid (modeled on a representative Indian metropolitan territory, e.g., $20\,\text{km} \times 20\,\text{km}$):

1. **Urban Spatial Discretization**:
   The geographic space $\mathcal{S}$ is partitioned into an $M = 400$ cell planar grid ($20 \times 20$ cells, each $1\,\text{km} \times 1\,\text{km}$) or Uber H3 hexagonal grid (Resolution 7).
2. **Infrastructure Layering**:
   Each cell $c$ is assigned a background banking infrastructure density:
   $$N_{\text{ATM}}(c) \sim \text{Poisson}(\lambda_{\text{infra}}(c))$$
   modulated by distance to commercial centers, arterial highways, and banking clusters.
3. **Upstream Cybercrime Complaint Generation**:
   Daily cybercrime complaints $C_t$ follow an overdispersed Poisson process reflecting macroscopic NCRB/I4C seasonal trends:
   $$C_t \sim \text{NegativeBinomial}(\mu_t, \alpha)$$
   Each complaint $i$ contains: timestamp $t_i$, defrauded amount $A_i$ (log-normal distribution matching RBI fraud figures), victim bank $B_i$, and complaint category (phishing, investment scam, task scam).
4. **Spatiotemporal Cash-Out Coupling**:
   A realistic fraction $\rho \approx 0.65$ of financial complaints transition into cash-out events. The cash-out occurs after a stochastic operational delay $\Delta \tau_i$:
   $$\Delta \tau_i \sim \text{Gamma}(k=3, \, \theta=6\,\text{hours})$$
   representing the time required for digital layering across mule accounts.
5. **Spatial Destination Choice (Gravity / Multinomial Logit Model)**:
   The probability $P(c \mid i)$ that cash-out $i$ occurs in spatial cell $c$ is determined by an urban utility function:
   $$P(c \mid i) = \frac{\exp\left( \beta_1 \log N_{\text{ATM}}(c) + \beta_2 \text{TransitAccessibility}(c) + \beta_3 \text{MuleHubProximity}(c) + \eta_c \right)}{\sum_{c' \in \mathcal{S}} \exp\left( \beta_1 \log N_{\text{ATM}}(c') + \beta_2 \text{TransitAccessibility}(c') + \beta_3 \text{MuleHubProximity}(c') + \eta_{c'} \right)}$$
   where $\eta_c$ represents latent spatial autocorrelation.

### Scientific Validity: What Can and Cannot Be Concluded
* **What CAN Be Concluded**:
  * Algorithmic validity: Proving that supervised machine learning models (Random Forest, XGBoost, Poisson GLMs) can extract non-linear spatiotemporal relationships from complex lagged panels.
  * Pipeline integrity: Validating that the data ingestion, spatial aggregation, feature engineering, and walk-forward backtesting pipelines operate without data leakage.
  * Metric sensitivity: Benchmarking the discriminatory power of spatial evaluation metrics (PAI, PEI, Precision@K).
  * System portability: The developed codebase can be deployed directly onto real I4C or bank data in an authorized environment by merely swapping the data loader.
* **What CANNOT Be Concluded**:
  * Real-world geographic certainty: Predictions generated on synthetic data cannot be used to conduct real-world police raids or infer actual criminal presence in any real city.

---

## 4. Initial Data Dictionary

The project formalizes a standardized schema designed to represent both synthetic benchmark data and real-world investigative feeds.

### Table 2: Proposed Field-Level Data Dictionary

| Field Name | Data Type | Example Value | Description | Classification Category |
| :--- | :--- | :--- | :--- | :--- |
| `record_id` | String / UUID | `"CR-2026-08912"` | Unique anonymized identifier for the complaint record | **Essential** |
| `complaint_timestamp` | ISO-8601 DateTime | `"2026-03-15T10:14:30Z"` | Exact time when the cybercrime report was registered | **Essential** |
| `incident_timestamp` | ISO-8601 DateTime | `"2026-03-14T22:30:00Z"` | Reported time when unauthorized transaction occurred | **Essential** |
| `defrauded_amount` | Float | `48500.00` | Stolen financial amount in Indian Rupees (INR) | **Essential** |
| `fraud_category` | Categorical String | `"INVESTMENT_SCAM"` | Fraud classification type (Phishing, UPI Scam, Investment, Job) | **Essential** |
| `victim_bank_code` | Categorical String | `"SBIN"` | Standard bank identifier code of the victim's account | **Essential** |
| `mule_layer_depth` | Integer | `3` | Number of intermediate mule accounts identified before cash-out | **Optional** |
| `withdrawal_timestamp`| ISO-8601 DateTime | `"2026-03-15T14:45:10Z"` | Exact physical cash dispensing time at ATM/point | **Essential (Ground Truth)** |
| `withdrawal_amount` | Float | `20000.00` | Physical cash amount dispensed at the terminal | **Essential (Ground Truth)** |
| `atm_terminal_id` | String | `"ATM-DEL-NORTH-041"` | Unique physical identifier of the dispensing machine | **Sensitive / Potentially Unavailable** |
| `grid_cell_id` | String | `"H3-8761e0b5fffffff"` | Discrete spatial index (H3 hex ID or UTM $1\,\text{km}$ cell) | **Essential (Spatial Unit)** |
| `latitude` | Float (WGS84) | `28.6139` | Latitude coordinate of verified withdrawal location | **Sensitive (Synthetic / Authorized Real)** |
| `longitude` | Float (WGS84) | `77.2090` | Longitude coordinate of verified withdrawal location | **Sensitive (Synthetic / Authorized Real)** |
| `cell_atm_count` | Integer | `14` | Total registered ATMs/cash-points inside the grid cell | **Essential (Spatial Feature)** |
| `lag_count_7d` | Integer | `12` | Historical withdrawal events in cell over preceding 7 days | **Essential (Engineered Feature)** |
| `lag_count_30d` | Integer | `48` | Historical withdrawal events in cell over preceding 30 days | **Essential (Engineered Feature)** |
| `spatial_lag_neighbor`| Float | `8.4` | Mean historical withdrawal count in first-order adjacent cells | **Essential (Engineered Feature)** |
| `target_count` | Integer | `4` | Number of verified withdrawals in cell during next forecast window | **Essential (Option B Target)** |
| `target_hotspot` | Binary $\{0, 1\}$ | `1` | Indicator if `target_count` exceeds operational threshold $\tau$ | **Essential (Option A Target)** |

### Field Sensitivity Classifications Defined:
1. **Essential**: Mandatory for training, feature engineering, and temporal validation.
2. **Optional**: Secondary auxiliary indicators that enhance predictive performance if present.
3. **Sensitive**: Fields that pose re-identification or operational vulnerability risks; must be perturbed, hashed, or aggregated in demonstration artifacts.
4. **Potentially Unavailable**: Fields that are frequently missing in messy real-world police dockets; models must be robust to their absence.

---
*Document Version: 1.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
