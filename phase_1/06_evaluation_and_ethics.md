# Phase 1: Evaluation Framework, Ethics & Responsible AI
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Comprehensive Evaluation Framework

Evaluating spatiotemporal predictive models requires metrics tailored to extreme spatial sparsity, severe class imbalance, and bounded operational resources. Standard global accuracy is deceptive in spatial grids where 95% of cells experience zero crime events (a naive "always predict zero" model would yield 95% accuracy while possessing zero operational value). 

We establish a multi-tiered evaluation strategy encompassing machine learning classification metrics, count regression metrics, domain-specific spatial efficiency indices, and naive baseline benchmarks.

```
+----------------------------------------------------------------------------------------------------+
|                                    MULTI-TIERED EVALUATION MATRIX                                  |
+----------------------------------------------------------------------------------------------------+
|  Tier 1: Machine Learning Metrics     --> PR-AUC, F1-Score, Precision@K, Recall@K, MAE, Poisson Dev |
|  Tier 2: Spatial Forecasting Metrics  --> Prediction Accuracy Index (PAI), Predictive Efficiency (PEI)|
|  Tier 3: Comparative Baselines        --> Persistent (Yesterday=Today), Chronic Flag + Boost MA   |
|  Tier 4: Validation Strategy          --> Rolling-Origin Chronological Walk-Forward Backtesting    |
+----------------------------------------------------------------------------------------------------+
```

### Table 1: Mathematical Specification of Evaluation Metrics

| Metric Category | Metric Name | Mathematical Formula | Operational Interpretation in SIH26184 |
| :--- | :--- | :--- | :--- |
| **Classification** | **Precision** | $\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$ | Percentage of predicted cash-out cells that actually experienced verified cash-out activity. High precision prevents wasted police patrol hours. |
| **Classification** | **Recall (Hit Rate)** | $\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$ | Percentage of all actual cash-out cells that were successfully anticipated by the model. High recall prevents unmonitored cash liquidation. |
| **Classification** | **F1-Score** | $F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$ | Harmonic mean balancing false alarm reduction with criminal activity capture. |
| **Classification** | **PR-AUC** | $\text{PR-AUC} = \int_{0}^{1} P(R) \, dR$ | Area under the Precision-Recall curve across all probability thresholds. Highly robust to extreme class imbalance. |
| **Resource-Constrained**| **Precision@K** | $\text{Precision@K} = \frac{\sum_{i=1}^K y_{(i)}}{K}$ | Precision evaluated exclusively across the Top-$K$ highest-risk cells (e.g., $K=10$ or $K=20$), directly reflecting the maximum patrol capacity of local police divisions. |
| **Resource-Constrained**| **Recall@K** | $\text{Recall@K} = \frac{\sum_{i=1}^K y_{(i)}}{\sum_{c=1}^M y_c}$ | Fraction of total municipal cash withdrawals captured within the Top-$K$ prioritized cells. |
| **Spatial Index** | **Prediction Accuracy Index (PAI)** [5] | $\text{PAI} = \frac{n / N}{a / A}$ | Ratio of captured withdrawal events ($n/N$) to the geographic area targeted ($a/A$). Measures spatial concentration efficiency. |
| **Spatial Index** | **Predictive Efficiency Index (PEI)** [14] | $\text{PEI} = \frac{\text{PAI}}{\text{PAI}^*}$ | Percentage of mathematically maximum achievable spatial efficiency achieved by the model on the test partition ($\text{PEI} \in [0, 1]$). |
| **Count Regression**| **Mean Absolute Error (MAE)** | $\text{MAE} = \frac{1}{M} \sum_{c=1}^M \|y_c - \hat{y}_c\|$ | Average absolute deviation between predicted and observed cash-out counts across all grid cells. |
| **Count Regression**| **Poisson Deviance** | $D = 2 \sum_{c=1}^M \left[ y_c \log\left(\frac{y_c}{\hat{y}_c}\right) - (y_c - \hat{y}_c) \right]$ | Log-likelihood goodness-of-fit measurement for Poisson count processes, penalizing count miscalibration properly. |

### Comparative Benchmark Baselines
Every candidate machine learning model must be evaluated against three non-trivial operational baselines:
1. **Uniform Random Spatial Allocation**: Allocating patrol capacity uniformly at random across spatial cells (theoretical baseline where $\text{PAI} = 1.0$).
2. **Persistent Lag Baseline (Yesterday = Today)**: Predicting that future cash withdrawals will occur in the exact same cells that experienced withdrawals during the preceding 24 hours.
3. **Chronic Flag + Temporary Boost Moving Average (Lee et al. [10])**: A theory-driven moving average benchmark computing a weighted sum of 30-day historical density ("flag") and 3-day recent complaint spikes ("boost").

**Academic Integrity Pledge**:
> *In accordance with rigorous academic standards, this project makes **no upfront promises of arbitrary accuracy percentages** (e.g., "our model will achieve 98% accuracy"). Actual numerical performance metrics will be objectively recorded and reported strictly following empirical experimental execution in Phase 4.*

---

## 2. Ethics, Privacy, and Responsible AI Governance

Forecasting crime-related geographic activity involves sensitive intersectional dimensions of civil liberties, algorithmic fairness, and data privacy. The framework adheres strictly to the **Digital Personal Data Protection (DPDP) Act 2023 (India)**, the **Information Technology Act 2000**, and the **ACM / IEEE Code of Ethics**.

```
+---------------------------------------------------------------------------------------------------------+
|                                    RESPONSIBLE AI GOVERNANCE PILLARS                                    |
+---------------------------------------------------------------------------------------------------------+
|  1. Personal Data Protection       --> Zero PII ingestion; strict k-anonymity; DPDP Act 2023 compliance|
|  2. Spatial Aggregation            --> Modeling across coarse grid cells; zero individual surveillance  |
|  3. Bias & Fairness Mitigation     --> Active monitoring for runaway feedback loops (Ensign et al., 2018)|
|  4. Epistemic Guardrail            --> Association != Prediction != Guilt; zero automated enforcement  |
|  5. Human-in-the-Loop Protocol     --> Investigative decision-support only; mandatory human review     |
+---------------------------------------------------------------------------------------------------------+
```

### Pillar 1: Personal Data Protection and Data Minimization
* **Zero PII Ingestion**: The machine learning data pipeline strictly excludes Personally Identifiable Information (PII). Full names, mobile phone numbers, national identity numbers (Aadhaar), complete 16-digit debit card numbers (PAN), and net-banking credentials are systematically excluded from training datasets.
* **Identifier Hashing**: Sensitive operational identifiers (such as bank branch codes or terminal IDs) are irreversibly hashed using salted SHA-256 before model ingestion.
* **Synthetic Data Demonstration**: Public demonstrations, Hackathon jury presentations, and code repositories use exclusively synthetic, mathematically simulated transaction records to guarantee zero leakage of real-world investigative secrets.

### Pillar 2: Geographic Aggregation as a Privacy Safeguard
* Models operate strictly on **spatially aggregated grid units** (e.g., $1\,\text{km} \times 1\,\text{km}$ planar cells or H3 Resolution 7 hexagons covering $\sim 5\,\text{km}^2$).
* Predictions indicate macroscopic spatial cell risk scores; they **never pinpoint private residential addresses, individual shop counters, or personal mobile devices**. This spatial coarsening provides mathematical $k$-anonymity, ensuring that predictions describe urban environment risk rather than individual behavioral tracking.

### Pillar 3: Algorithmic Bias, Reporting Disparities & Feedback Loops
* **The Reporting Disparity Trap**: As established by Lum & Isaac [17], police and complaint records reflect *reporting behavior* rather than absolute ground-truth crime. High-density commercial districts with automated bank reporting log incidents rapidly, whereas marginalized or rural populations may delay reporting due to digital illiteracy or lack of awareness of the `1930` helpline.
* **Mitigating Runaway Feedback Loops**: Deploying surveillance exclusively to historically predicted ATM clusters risks generating an artificial feedback loop (Ensign et al. [16]): police detect more mules at monitored ATMs simply because they are actively watching them, reinforcing future model predictions. 
  * *Countermeasure*: Our framework recommends an **exploration-exploitation split** for tactical resource allocation: 80% of monitoring resources are allocated to top predicted cells (exploitation), while 20% are allocated across randomly sampled background cells (exploration) to gather unbiased ground-truth validation data.

### Pillar 4: The Epistemic Boundary: Association vs. Prediction vs. Proof of Guilt
A foundational ethical guardrail is the explicit separation of three distinct epistemic concepts:

```
[ Spatial Association ]   =/=>   [ Probabilistic Prediction ]   =/=>   [ Proof of Criminal Guilt ]
(Cell has 10 ATMs &             (Cell has 65% probability of           (A citizen withdrawing cash
 commercial transit)             elevated withdrawals tomorrow)         at this ATM is a criminal)
```

1. **Association**: A statistical correlation between built infrastructure (ATMs, highways) and historical withdrawal complaints.
2. **Prediction**: A conditional statistical forecast that an operational cell will experience elevated cash extraction activity during an upcoming window.
3. **Proof of Guilt**: **A predicted hotspot is NOT proof of criminal activity.**
   * A citizen withdrawing cash at an ATM located inside a forecasted hotspot is presumed entirely innocent.
   * Under Indian jurisprudence (Indian Evidence Act 1872 / Bharatiya Sakshya Adhiniyam 2023), statistical machine learning outputs constitute purely investigative intelligence leads, not legal evidence of individual culpability.
   * **The system must never claim to identify individual criminals or establish criminal guilt.**

### Pillar 5: Human-in-the-Loop Operational Protocol
* The software architecture is designed strictly as a **decision-support tool** for authorized human investigators and bank risk officers.
* The system is technically barred from executing automated punitive actions (e.g., automated account freezing, automated police dispatch, or automated transaction blocking).
* Every generated intelligence briefing includes explicit **epistemic uncertainty bounds** (e.g., 90% confidence intervals via conformal prediction) and top-contributing SHAP feature explanations, enabling human officers to critically evaluate and contextualize algorithmic suggestions before taking operational action.

---
*Document Version: 1.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
