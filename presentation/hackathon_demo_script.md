# Smart India Hackathon 2026 | Problem ID: SIH26184
## Five-Minute Live Jury Demonstration Script
### Roles: Speaker 1 (Lead Presenter) & Speaker 2 (Live Tech Demonstrator)

---

### Minute 0:00 - 1:00 | The Hook & The Problem Formulation
**Speaker 1:**
> "Respected Jury members, in India today, over 70% of cybercrimes involve financial fraud. When a citizen dials `1930`, funds are transferred across 3 to 4 layers of mule accounts within minutes. But digital layering is only the intermediate phase. The criminal endgame is **physical cash liquidation at ATMs**.
> 
> Once cash is dispensed at an ATM, digital lien marks fail, and the money disappears into the untraceable informal cash economy.
> 
> Problem Statement **SIH26184** asks: *Can we forecast likely geographic withdrawal clusters from cybercrime complaint metadata?*
> 
> Our project answers this question with an academically validated, leak-free supervised machine learning and geospatial framework. Spanning all five engineering phases, we deliver an end-to-end operational platform."

---

### Minute 1:00 - 2:00 | Scientific Rigor, DPDP Compliance & Feature Pipeline
**Speaker 1:**
> "First, we decouple four spatial entities often conflated in naive models: Victim Location, Transaction IP, Mule Home Branch, and Verified Withdrawal Location. Models must forecast verified ATM cash extractions, not victim residences.
> 
> Second, under the Digital Personal Data Protection Act 2023, real ATM logs are legally quarantined. We built a mathematically calibrated synthetic simulation engine matching NCRB and RBI figures across 400 planar cells and 186 days.
> 
> Third, exploratory spatial analysis proved non-random spatial clustering with a Global Moran's I of +0.6018 ($p < 0.0001$). We engineered a leak-free 29-feature spatiotemporal panel over 74,400 cell-day units, enforcing strict 1-day temporal buffers."

---

### Minute 2:00 - 3:15 | Walk-Forward Benchmarks & Breakthrough Results
**Speaker 2 (Displays Screen / Benchmark Chart):**
> "Unlike previous studies that use random cross-validation—which creates catastrophic lookahead data leakage—we evaluated nine candidate models under chronological walk-forward backtesting across 46 continuous operational holdout days.
> 
> The results are definitive:
> 1. Our **Gradient Boosted Decision Tree model achieves a Prediction Accuracy Index (PAI@10) of 8.81**. That is an **8.8-fold concentration of cash withdrawals** compared to random patrol allocation, and a 35% improvement over persistent lag baselines.
> 2. It captures **65.6% of the theoretical maximum possible spatial efficiency (PEI@10 = 0.656)**.
> 3. In an urban environment where baseline hotspot prevalence is only 5.07%, our model delivers a **Precision@10 of 55.9%**—an 11-fold positive enrichment.
> 4. Feature ablation proves that historical temporal recency decay (26.8%) and weekly momentum (18.4%) dominate static infrastructure alone."

---

### Minute 3:15 - 4:15 | Live Platform Demonstration: GIS Dashboard & Real-Time Alert
**Speaker 2 (Interacts with Streamlit Dashboard `app.py`):**
> "Let us look at the live command dashboard running on `app.py`.
> 
> On the left, police commanders can dynamically adjust the patrol budget slider $K$ and risk threshold $\tau$.
> 
> On the interactive Folium GIS map:
> - Crimson red cells represent critical risk areas ($P \ge 70\%$).
> - Warning markers indicate the Top-10 prioritized tactical interception targets.
> - Clicking on any cell displays its localized Explainable AI drivers (e.g., 'Weekly Repeat Withdrawal Burst + High Density ATM Infrastructure') and its 90% conformal uncertainty interval.
> 
> Notice the blue circle markers: this is our **Responsible AI Anti-Bias Safeguard**. We enforce an **80/20 exploitation-exploration patrol split**, deploying 20% of patrols to random cells to continuously collect unbiased ground truth and eliminate runaway feedback loops."

---

### Minute 4:15 - 5:00 | Real-Time Ingestion, API & Responsible AI Defense
**Speaker 1:**
> "To demonstrate production readiness, we also provide a REST API microservice on `api.py` and a streaming complaint simulator. When 35 new investment scam complaints are logged on Helpline `1930`, the simulator models Gamma-distributed layering delays and immediately dispatches tactical alerts to nearby ATM corridors 8 to 14 hours *before* physical cash extraction occurs.
> 
> Finally, our framework adheres strictly to Responsible AI:
> 1. **Epistemic boundary**: Statistical association is NOT proof of guilt. Citizens at predicted ATMs are presumed innocent.
> 2. **Decision support only**: System is technically barred from executing automated arrests or account freezing.
> 3. **100% Automated Test Pass**: 10 of 10 automated unit and integration tests pass with zero errors.
> 
> We are ready for your questions. Thank you."
