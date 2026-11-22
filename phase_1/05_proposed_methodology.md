# Phase 1: Proposed Technical Methodology
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Formulation of Supervised Learning Targets

To translate the SIH26184 problem statement into a concrete machine learning framework, we formulate and compare two alternative supervised learning paradigms: **Option A (Binary Spatiotemporal Classification)** and **Option B (Discrete Spatiotemporal Count Regression)**.

```
                                SPATIOTEMPORAL FORMULATION PARADIGMS
                                
   [ Spatial Grid: M cells ]  x  [ Temporal Panels: T intervals ]  -->  Input Feature Matrix X_(c, t)
                                            |
                    +-----------------------+-----------------------+
                    |                                               |
                    v                                               v
        OPTION A: CLASSIFICATION                         OPTION B: REGRESSION
    Predict: Y_(c, t+1) in {0, 1}                    Predict: Y_(c, t+1) in {0, 1, 2, ...}
    Threshold: I(Withdrawals >= tau)                 Expected Incident Count lambda_(c, t+1)
```

### Table 1: In-Depth Comparison of Supervised Target Options

| Architectural Dimension | Option A: Spatiotemporal Classification | Option B: Spatiotemporal Count Regression |
| :--- | :--- | :--- |
| **Mathematical Formulation** | $Y_{c, t+\Delta t} = \mathbb{I}(k_{c, t+\Delta t} \ge \tau_{\text{thresh}})$, where $Y \in \{0, 1\}$ | $Y_{c, t+\Delta t} = k_{c, t+\Delta t}$, where $Y \in \mathbb{Z}_{\ge 0}$ |
| **Target Interpretation** | Binary probability $P(\text{Hotspot} \mid \mathbf{x}_{c, t})$ that cell $c$ will exceed activity threshold $\tau_{\text{thresh}}$ in future window $t+\Delta t$. | Expected numerical count $\hat{k}_{c, t+\Delta t}$ of verified withdrawal events occurring in cell $c$ during window $t+\Delta t$. |
| **Primary Strengths** | 1. Directly answers the operational tactical question: "Should we allocate surveillance/patrol to this cell or not?"<br>2. Robust to exact count noise in ultra-sparse cells.<br>3. Enables standard probability threshold tuning and precision-recall trade-offs. | 1. Retains full granular magnitude information (distinguishes 1 event from 15 events).<br>2. Enables direct ranking of cells by expected criminal volume.<br>3. Directly models Poisson / Negative Binomial arrival processes. |
| **Primary Limitations** | 1. Loss of information: treats a cell with 2 withdrawals identically to a cell with 20 withdrawals.<br>2. Sensitivity to arbitrary threshold selection ($\tau_{\text{thresh}} = 1$ vs. $\tau_{\text{thresh}} = 3$). | 1. Severe zero-inflation: 90%+ of spatial cells typically exhibit zero events in micro-windows.<br>2. Standard MSE loss over-penalizes rare extreme count spikes while under-predicting low counts. |
| **Data Requirements** | Requires sufficient positive hotspot occurrences across temporal panels to prevent extreme class imbalance (<0.5% positives). | Requires granular integer count histories and modeling frameworks capable of handling overdispersion (variance $\gg$ mean). |
| **Primary Evaluation Metrics**| PR-AUC, F1-Score, Precision@K, Recall@K, Predictive Accuracy Index (PAI). | Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Poisson Deviance, Predictive Efficiency Index (PEI). |

### Methodological Recommendation for Initial Phase
**We recommend adopting Option A (Classification with calibrated probabilistic output) as our primary baseline formulation, while training Option B (Poisson/Negative Binomial Count Regressors) as a parallel comparative baseline.** 

*Rationale*: Law enforcement and bank fraud operations possess strictly bounded physical response capacities. Tactical decision-makers rarely need to know whether an ATM kiosk will experience exactly 4.2 versus 5.1 fraudulent sweeps; they require a **risk-ranked list of high-priority cells (Top-K Hotspots)** that exhibit a statistically elevated probability of intense activity during the upcoming shift. Calibrated class probabilities from Option A provide an intuitive, threshold-adjustable decision boundary directly aligned with operational Precision@K.

---

## 2. Candidate Machine Learning Algorithms

To ensure rigorous benchmarking, five algorithm classes spanning linear baselines, generalized linear models, tree ensembles, and unsupervised spatial clustering are evaluated:

```
+---------------------------------------------------------------------------------------------------------+
|                                      CANDIDATE ALGORITHM SUITE                                          |
+---------------------------------------------------------------------------------------------------------+
|  1. Regularized Linear Baselines:   L2-Logistic Regression (Classification), Ridge GLM                  |
|  2. Count Process Baselines:        Poisson Regression & Negative Binomial GLM (Option B)               |
|  3. Non-Linear Tree Ensembles:      Random Forest Classifier & Regressor (Breiman, 2001)                |
|  4. Gradient Boosted Trees:         XGBoost / LightGBM (Chen & Guestrin, 2016)                          |
|  5. Exploratory Spatial Clustering: DBSCAN & ST-DBSCAN (Ester et al., 1996; Birant & Kut, 2007)        |
+---------------------------------------------------------------------------------------------------------+
```

### 1. Regularized Logistic Regression (Option A Baseline)
* **Mathematical Basis**: 
  $$P(Y_{c, t+1} = 1 \mid \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b) = \frac{1}{1 + \exp(-(\mathbf{w}^T \mathbf{x} + b))}$$
  Trained with ElasticNet / L2 regularization: $\mathcal{L}(\mathbf{w}) = \mathcal{L}_{\text{BCE}}(\mathbf{w}) + \lambda \|\mathbf{w}\|_2^2$.
* **Role**: Serves as the minimal parametric baseline. If complex tree ensembles cannot outperform regularized logistic regression under walk-forward evaluation, their added complexity is unjustified.

### 2. Poisson and Negative Binomial Regression (Option B Baseline)
* **Mathematical Basis**: 
  $$k_{c, t+1} \sim \text{Poisson}(\lambda_{c, t+1}), \quad \log \lambda_{c, t+1} = \mathbf{w}^T \mathbf{x} + b$$
  Negative Binomial extends Poisson by introducing dispersion parameter $\alpha$ to accommodate overdispersion ($\text{Var}(k) = \lambda + \alpha \lambda^2$).
* **Role**: The standard statistical benchmark for spatial count forecasting [9], providing calibrated incident rate expectations.

### 3. Random Forest (Classifier & Regressor)
* **Mathematical Basis**: Ensemble of $B$ decorrelated decision trees trained via bootstrap aggregation (bagging) with random feature sub-sampling:
  $$\hat{Y}_{\text{RF}}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^B T_b(\mathbf{x})$$
* **Role**: Established benchmark in criminological spatial modeling [6, 7, 9]. Naturally captures complex non-linear feature interactions (e.g., high fraud volume *and* specific bank *and* night hour) without requiring explicit polynomial expansion, and demonstrates high resilience to tabular outliers.

### 4. Extreme Gradient Boosting (XGBoost / LightGBM)
* **Mathematical Basis**: Sequential additive tree boosting minimizing a regularized objective:
  $$\mathcal{L}^{(m)} = \sum_{i} \ell\left( y_i, \, \hat{y}_i^{(m-1)} + f_m(\mathbf{x}_i) \right) + \Omega(f_m)$$
  employing second-order Taylor expansion gradients and tree pruning penalties.
* **Role**: Primary candidate for top predictive performance. Handles sparse features efficiently, supports custom objective functions (such as focal loss for extreme class imbalance), and achieves fast training over large spatiotemporal panels.

### 5. DBSCAN & ST-DBSCAN (Exploratory Spatial Clustering — NOT Supervised Forecasting)
* **Crucial Methodological Distinction**: 
  > **DBSCAN is strictly an unsupervised clustering technique, NOT a supervised forecasting model.**
  
  In this project, DBSCAN [11] and ST-DBSCAN [12] are utilized exclusively for:
  1. **Phase 3 Exploratory Spatial Data Analysis (ESDA)**: Discovering historical geometric clusters of coordinated cash-outs and identifying spatial noise points.
  2. **Spatial Feature Engineering**: Constructing a binary feature `is_historical_cluster_core` indicating whether cell $c$ intersects a dense historical spatial cluster.
  DBSCAN cannot forecast future time windows; supervised forecasting is executed strictly by the classification/regression models above.

---

## 3. End-to-End Conceptual Engineering Pipeline

The operational workflow spans ten connected stages, progressing from raw telemetry to actionable field intelligence:

```
+--------------------+      +--------------------+      +---------------------+
| 1. Data Ingestion  | ---> | 2. Data Validation | ---> | 3. Exploratory ESDA |
| (Complaints, Logs) |      | & Sanitization     |      | & Spatial DBSCAN    |
+--------------------+      +--------------------+      +---------------------+
                                                                   |
+--------------------+      +--------------------+                 v
| 6. Supervised ML   | <--- | 5. Spatiotemporal  | <--- +---------------------+
| Training (RF/XGB)  |      | Aggregation (Grid) |      | 4. Feature Engg     |
+--------------------+      +--------------------+      | (Lags, POI, Banks)  |
         |                                              +---------------------+
         v
+--------------------+      +--------------------+      +---------------------+
| 7. Walk-Forward    | ---> | 8. Geospatial      | ---> | 9. Actionable Intel |
| Chronological Eval |      | Interactive Maps   |      | Report (SHAP/PAI)   |
+--------------------+      +--------------------+      +---------------------+
```

### Detailed Pipeline Stages:
1. **Data Ingestion**: Ingests raw cybercrime complaint metadata (time, amount, bank) and withdrawal verification dockets.
2. **Data Validation & Sanitization**: Enforces strict schema integrity, parses ISO-8601 timestamps, checks coordinate bounding boxes, and filters corrupt records.
3. **Exploratory Analysis & Spatial Clustering (ESDA)**: Computes global Moran's I spatial autocorrelation and runs DBSCAN/ST-DBSCAN to identify historical cluster epicenters.
4. **Feature Engineering**: Calculates rolling temporal lag counts (7-day, 14-day, 30-day), exponential time-decay weights, bank-brand complaint proportions, and nearest-neighbor diffusion terms.
5. **Spatiotemporal Discretization & Aggregation**: Projects event points onto a discrete spatial grid (e.g., $1\,\text{km} \times 1\,\text{km}$ UTM cells or Uber H3 Resolution 7) over uniform temporal intervals ($\Delta t = 24\,\text{hours}$).
6. **Supervised Model Training**: Fits candidate models (Logistic Regression, Poisson GLM, Random Forest, XGBoost) using cross-entropy, focal loss, or Poisson deviance objectives.
7. **Walk-Forward Chronological Evaluation**: Evaluates predictions on holdout future periods using PAI, PEI, Precision@K, Recall@K, and PR-AUC.
8. **Geospatial Visualization**: Generates interactive Folium / Leaflet GIS map layers displaying predicted hotspot polygons, historical incident markers, and confidence bands.
9. **Actionable Intelligence Report Generation**: Compiles an automated analytical dossier for field commanders, detailing high-risk grid coordinates, anticipated withdrawal volume, and top-contributing SHAP feature explanations.

---

## 4. Chronological Validation Scheme (Preventing Temporal Leakage)

A central methodological contribution of our design is the **strict elimination of spatiotemporal data leakage (lookahead bias)**. 

### Why Standard Random Cross-Validation Fails in Spatial ML
If a dataset spanning January to December 2026 is randomly split into 5 folds:
* Training folds will contain records from August 15 in cell $c$.
* Test folds will contain records from March 10 in cell $c$.
* The model effectively "learns the future" to predict the past, exploiting strong localized spatial autocorrelation. This produces artificially inflated F1-scores (>0.95) that collapse entirely when deployed in production.

### Proposed Solution: Rolling-Origin Walk-Forward Validation
We implement an expanding-window chronological backtesting protocol:

```
Temporal Timeline:  |======================================================>
Split 1 (Train):    [ Month 1 - Month 3 ] -> [ Validate: Month 4 ]
Split 2 (Train):    [ Month 1 - Month 4 ] -> [ Validate: Month 5 ]
Split 3 (Train):    [ Month 1 - Month 5 ] -> [ Validate: Month 6 ]
Final Test:         [ Month 1 - Month 8 ] -> [ Holdout Test: Month 9 - Month 10 ]
```

* **Temporal Separation**: For every validation step $t$, the training set contains exclusively records with timestamps $\tau \le t$. 
* **Feature Window Buffer**: Feature calculation for forecast window $t + \Delta t$ uses information strictly available at cutoff $t$.
* **Spatial Buffer (Optional Spatial CV)**: When assessing spatial transferability, spatial cells bordering the validation fold are buffered to eliminate boundary autocorrelation spillover.

---
*Document Version: 1.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
