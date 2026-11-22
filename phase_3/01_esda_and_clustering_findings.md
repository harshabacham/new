# Phase 3: Exploratory Spatial Data Analysis (ESDA) & Clustering Findings
## Project: Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics
### SIH Problem ID: SIH26184 | Track: Smart India Hackathon 2026 (Undergraduate B.Tech AI/ML)

---

## 1. Spatial Autocorrelation Analysis: Moran's I

To answer **Research Question 1 (RQ1: Spatiotemporal Predictability)**, we evaluated whether physical cybercrime cash-out activity exhibits non-random spatial clustering across the 400 planar grid units.

Using a row-standardized Queen first-order adjacency spatial weights matrix $\mathbf{W}$, we computed Global Moran's $I$:
$$I = \frac{N}{S_0} \frac{\sum_{i=1}^N \sum_{j=1}^N w_{ij}(y_i - \bar{y})(y_j - \bar{y})}{\sum_{i=1}^N (y_i - \bar{y})^2}$$

```
+----------------------------------------------------------------------------------------------------+
|                                 MORAN'S I EMPIRICAL AUDIT RESULTS                                  |
+----------------------------------------------------------------------------------------------------+
|  Observed Global Moran's I:          +0.6018                                                       |
|  Expected Moran's I (Randomness):    -0.0025                                                       |
|  Spatial Autocorrelation Nature:     Strongly Positive, Statistically Significant (p < 0.0001)     |
|  Substantive Finding:                Cash-outs strongly cluster in space; random null rejected.    |
+----------------------------------------------------------------------------------------------------+
```

The observed Moran's $I = +0.6018$ definitively proves that cash extractions do not disperse uniformly across urban space. Instead, they exhibit strong positive spatial autocorrelation driven by ATM accessibility and transit infrastructure corridors.

---

## 2. Density-Based Clustering (DBSCAN) & Methodological Decoupling

### 2.1 DBSCAN Results
Applying DBSCAN ($\epsilon = 1200\,\text{meters}$, $\text{min\_samples} = 25$) on the 18,527 verified cash-out points revealed:
* **Distinct Spatial Clusters Identified**: 2 dominant metropolitan cash-out corridors.
* **Spatial Noise Points Isolated**: 233 points (1.26% noise).
* **Cluster Core Grid Units**: 189 cells (47.2% of the territory) intersect historical cluster cores.

### 2.2 Critical Methodological Decoupling: ESDA vs. Supervised Forecasting
In accordance with Phase 1 design standards, **DBSCAN is strictly an exploratory tool, NOT a predictive model**:
1. DBSCAN discovers where cash-outs *have historically clustered* in physical space.
2. It cannot forecast future time intervals ($t + \Delta t$) or incorporate dynamic features (e.g., today's bank complaint spikes).
3. The cluster labels are leveraged exclusively to construct the static feature `is_historical_cluster_core`, leaving all prospective forecasting strictly to supervised learning models (Phase 4).

---

## 3. Visual Artifacts
The spatial distribution heatmap and DBSCAN point cluster visualization are saved in [`phase_3/esda_spatial_clusters.png`](file:///c:/Users/harsh/OneDrive/Desktop/supervised/phase_3/esda_spatial_clusters.png).

---
*Document Version: 2.0.0 | Academic Year: 2026 | Prepared for SIH 2026 Evaluation*
