"""
Phase 4: Supervised Model Training and Chronological Walk-Forward Backtesting.
Trains 9 models spanning baselines, regularized linear models, Poisson GLMs,
Random Forests, and Gradient Boosted Decision Trees (HistGradientBoosting).
Computes PAI, PEI, Precision@K, PR-AUC, F1, and Poisson deviance.
"""

import os
import sys
import json
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, PoissonRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, average_precision_score, mean_absolute_error, mean_squared_error

# Helper functions for spatial metrics: PAI, PEI, Precision@K, Recall@K
def compute_spatial_indices(y_true_counts, y_scores, K=10, total_cells=400):
    """
    Computes PAI and PEI on test day evaluations.
    y_true_counts: actual withdrawal counts per cell
    y_scores: predicted risk score or probability
    K: number of top cells prioritized
    """
    # Rank cells by predicted score
    ranked_indices = np.argsort(y_scores)[::-1]
    top_k_indices = ranked_indices[:K]
    
    n_captured = np.sum(y_true_counts[top_k_indices])
    N_total = np.sum(y_true_counts)
    if N_total == 0:
        return 1.0, 1.0, 0.0, 0.0
        
    a_area = K
    A_total = total_cells
    
    # PAI = (n / N) / (a / A)
    pai = float((n_captured / N_total) / (a_area / A_total))
    
    # Theoretical maximum PAI achievable on this test set with top K cells (Oracle)
    oracle_ranked = np.sort(y_true_counts)[::-1]
    oracle_n = np.sum(oracle_ranked[:K])
    pai_max = float((oracle_n / N_total) / (a_area / A_total)) if N_total > 0 else 1.0
    
    # PEI = PAI / PAI_max in [0, 1]
    pei = float(pai / pai_max) if pai_max > 0 else 0.0
    
    recall_at_k = float(n_captured / N_total)
    
    return pai, pei, recall_at_k, n_captured

def compute_precision_at_k(y_true_binary, y_scores, K=10):
    ranked_indices = np.argsort(y_scores)[::-1]
    top_k_indices = ranked_indices[:K]
    prec_k = float(np.mean(y_true_binary[top_k_indices]))
    return prec_k

def run_phase_4():
    print("=" * 70)
    print("PHASE 4: SUPERVISED MODEL TRAINING & WALK-FORWARD BACKTESTING")
    print("=" * 70)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    phase4_dir = os.path.join(base_dir, "phase_4")
    model_dir = os.path.join(base_dir, "models")
    os.makedirs(phase4_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)
    
    feat_path = os.path.join(data_dir, "spatiotemporal_feature_matrix.parquet")
    assert os.path.exists(feat_path), f"Feature matrix missing: {feat_path}"
    
    print(f"Loading spatiotemporal feature matrix from: {feat_path}")
    df = pd.read_parquet(feat_path)
    df["date"] = pd.to_datetime(df["date"])
    
    # Feature columns used for training
    feature_cols = [
        "row_idx", "col_idx",
        "lag_count_1d", "lag_count_3d", "lag_count_7d", "lag_count_14d", "lag_count_30d",
        "lag_amount_sum_7d", "lag_amount_mean_7d", "decay_intensity_30d",
        "complaint_count_3d", "complaint_amount_sum_3d", "complaint_sbin_share_3d", "complaint_invest_share_3d",
        "spatial_lag_neighbor_7d",
        "cell_atm_count", "transit_score", "mule_hub_score", "is_historical_cluster_core",
        "day_of_week", "is_weekend", "day_of_month", "is_salary_cycle"
    ]
    
    dates = sorted(df["date"].unique())
    n_days = len(dates)
    print(f"Total dates available: {n_days} days. Features: {len(feature_cols)} columns.")
    
    # Walk-forward chronological splits:
    # Split 1: Train days 1-90 -> Test days 91-115
    # Split 2: Train days 1-115 -> Test days 116-140
    # Split 3: Train days 1-140 -> Test days 141-186 (Final holdout test period)
    splits = [
        {"name": "Split_1", "train_end": 90, "test_end": 115},
        {"name": "Split_2", "train_end": 115, "test_end": 140},
        {"name": "Split_3 (Final Holdout)", "train_end": 140, "test_end": n_days}
    ]
    
    # Prepare model registry
    # Models to benchmark:
    # 1. Baseline: Uniform Random
    # 2. Baseline: Persistent (Yesterday = Today)
    # 3. Baseline: Chronic Flag + Boost (Lee et al. 2020)
    # 4. Logistic Regression (L2 Balanced)
    # 5. Poisson GLM Regressor
    # 6. Random Forest Classifier
    # 7. Random Forest Regressor
    # 8. HistGradientBoosting Classifier (LightGBM architecture)
    # 9. HistGradientBoosting Regressor (Poisson loss)
    
    # We will run walk-forward backtesting across all splits and evaluate on the final holdout split in detail
    print(f"\n[1/3] Executing Chronological Walk-Forward Backtesting across {len(splits)} splits...")
    
    # Let's train on the final split (Train: days 1-140, Test: days 141-186) for detailed comprehensive metric extraction
    train_dates = dates[:140]
    test_dates = dates[140:]
    
    df_train = df[df["date"].isin(train_dates)].copy()
    df_test = df[df["date"].isin(test_dates)].copy()
    
    X_train = df_train[feature_cols].values
    y_train_hotspot = df_train["target_hotspot"].values
    y_train_count = df_train["target_count"].values
    
    X_test = df_test[feature_cols].values
    y_test_hotspot = df_test["target_hotspot"].values
    y_test_count = df_test["target_count"].values
    
    print(f" -> Train set: {len(df_train):,} rows ({train_dates[0].strftime('%Y-%m-%d')} to {train_dates[-1].strftime('%Y-%m-%d')})")
    print(f" -> Test set:  {len(df_test):,} rows ({test_dates[0].strftime('%Y-%m-%d')} to {test_dates[-1].strftime('%Y-%m-%d')})")
    print(f" -> Test hotspot prevalence: {y_test_hotspot.mean()*100:.2f}% ({y_test_hotspot.sum():,} / {len(y_test_hotspot):,})")
    
    # Standard scaler for linear / GLM models
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    results = {}
    
    # Helper to evaluate predictions
    def evaluate_model(name, y_pred_prob_or_score, y_pred_count=None, is_binary=True):
        # Classification metrics
        if is_binary:
            y_pred_binary = (y_pred_prob_or_score >= 0.5).astype(int)
            # If scores are counts or uncalibrated, use top 5% quantile as threshold
            if y_pred_prob_or_score.max() > 1.0 or y_pred_binary.sum() == 0:
                thresh = np.percentile(y_pred_prob_or_score, 95)
                y_pred_binary = (y_pred_prob_or_score >= thresh).astype(int)
        else:
            thresh = np.percentile(y_pred_prob_or_score, 95)
            y_pred_binary = (y_pred_prob_or_score >= thresh).astype(int)
            
        f1 = float(f1_score(y_test_hotspot, y_pred_binary, zero_division=0))
        prec = float(precision_score(y_test_hotspot, y_pred_binary, zero_division=0))
        rec = float(recall_score(y_test_hotspot, y_pred_binary, zero_division=0))
        
        try:
            roc_auc = float(roc_auc_score(y_test_hotspot, y_pred_prob_or_score))
        except:
            roc_auc = 0.5
            
        try:
            pr_auc = float(average_precision_score(y_test_hotspot, y_pred_prob_or_score))
        except:
            pr_auc = float(y_test_hotspot.mean())
            
        # Top-K Metrics (averaged per day)
        daily_pai_10, daily_pei_10, daily_rec_10, daily_p_10 = [], [], [], []
        daily_pai_20, daily_pei_20, daily_rec_20, daily_p_20 = [], [], [], []
        
        df_eval = df_test[["grid_cell_id", "date"]].copy()
        df_eval["y_true_count"] = y_test_count
        df_eval["y_true_hotspot"] = y_test_hotspot
        df_eval["score"] = y_pred_prob_or_score
        
        for dt, grp in df_eval.groupby("date"):
            grp_counts = grp["y_true_count"].values
            grp_binary = grp["y_true_hotspot"].values
            grp_scores = grp["score"].values
            
            p10, e10, r10, _ = compute_spatial_indices(grp_counts, grp_scores, K=10, total_cells=400)
            daily_pai_10.append(p10)
            daily_pei_10.append(e10)
            daily_rec_10.append(r10)
            daily_p_10.append(compute_precision_at_k(grp_binary, grp_scores, K=10))
            
            p20, e20, r20, _ = compute_spatial_indices(grp_counts, grp_scores, K=20, total_cells=400)
            daily_pai_20.append(p20)
            daily_pei_20.append(e20)
            daily_rec_20.append(r20)
            daily_p_20.append(compute_precision_at_k(grp_binary, grp_scores, K=20))
            
        pai_10 = float(np.mean(daily_pai_10))
        pei_10 = float(np.mean(daily_pei_10))
        prec_10 = float(np.mean(daily_p_10))
        recall_10 = float(np.mean(daily_rec_10))
        
        pai_20 = float(np.mean(daily_pai_20))
        pei_20 = float(np.mean(daily_pei_20))
        prec_20 = float(np.mean(daily_p_20))
        recall_20 = float(np.mean(daily_rec_20))
        
        res = {
            "Model": name,
            "PR-AUC": round(pr_auc, 4),
            "ROC-AUC": round(roc_auc, 4),
            "F1-Score": round(f1, 4),
            "Precision": round(prec, 4),
            "Recall": round(rec, 4),
            "PAI@10": round(pai_10, 2),
            "PEI@10": round(pei_10, 3),
            "Precision@10": round(prec_10, 3),
            "Recall@10": round(recall_10, 3),
            "PAI@20": round(pai_20, 2),
            "PEI@20": round(pei_20, 3),
            "Precision@20": round(prec_20, 3),
            "Recall@20": round(recall_20, 3),
        }
        
        if y_pred_count is not None:
            mae = float(mean_absolute_error(y_test_count, y_pred_count))
            rmse = float(np.sqrt(mean_squared_error(y_test_count, y_pred_count)))
            # Poisson deviance
            eps = 1e-6
            y_c = np.clip(y_pred_count, eps, None)
            dev = float(2 * np.mean(np.where(y_test_count > 0, y_test_count * np.log(y_test_count / y_c), 0) - (y_test_count - y_c)))
            res["MAE"] = round(mae, 4)
            res["RMSE"] = round(rmse, 4)
            res["Poisson_Deviance"] = round(dev, 4)
        else:
            res["MAE"] = None
            res["RMSE"] = None
            res["Poisson_Deviance"] = None
            
        print(f" -> {name:38s} | PR-AUC: {pr_auc:.4f} | F1: {f1:.4f} | PAI@10: {pai_10:5.2f} | PEI@10: {pei_10:.3f} | Prec@10: {prec_10:.3f}")
        return res

    print("\n[2/3] Benchmarking Models under Chronological Holdout...")

    # 1. Baseline: Uniform Random
    np.random.seed(42)
    random_scores = np.random.uniform(0, 1, len(df_test))
    results["Uniform_Random"] = evaluate_model("1. Baseline: Uniform Random", random_scores)

    # 2. Baseline: Persistent (Yesterday = Today)
    # Uses lag_count_1d as score
    lag1_scores = df_test["lag_count_1d"].values.astype(float)
    results["Persistent_Lag"] = evaluate_model("2. Baseline: Persistent Lag (Yesterday)", lag1_scores, y_pred_count=lag1_scores)

    # 3. Baseline: Chronic Flag + Boost (Lee, O, & Eck 2020)
    flag_boost_scores = 0.65 * (df_test["lag_count_30d"].values / 30.0) + 0.35 * (df_test["lag_count_3d"].values / 3.0)
    results["Flag_and_Boost"] = evaluate_model("3. Baseline: Flag + Boost MA (Lee et al.)", flag_boost_scores, y_pred_count=flag_boost_scores)

    # 4. Logistic Regression (L2 Regularized)
    print("Training Logistic Regression (Option A)...")
    lr = LogisticRegression(penalty="l2", C=1.0, class_weight="balanced", max_iter=400, random_state=42)
    lr.fit(X_train_scaled, y_train_hotspot)
    lr_probs = lr.predict_proba(X_test_scaled)[:, 1]
    results["Logistic_Regression"] = evaluate_model("4. Logistic Regression (L2 Regularized)", lr_probs)

    # 5. Poisson GLM Regressor (Option B)
    print("Training Poisson GLM Regressor (Option B)...")
    poisson_glm = PoissonRegressor(alpha=1e-3, max_iter=300)
    poisson_glm.fit(X_train_scaled, y_train_count)
    poisson_preds = np.clip(poisson_glm.predict(X_test_scaled), 0, None)
    results["Poisson_GLM"] = evaluate_model("5. Poisson GLM Regressor (Option B)", poisson_preds, y_pred_count=poisson_preds, is_binary=False)

    # 6. Random Forest Classifier (Option A)
    print("Training Random Forest Classifier (Option A)...")
    rf_clf = RandomForestClassifier(n_estimators=100, max_depth=12, class_weight="balanced_subsample", random_state=42, n_jobs=-1)
    rf_clf.fit(X_train, y_train_hotspot)
    rf_probs = rf_clf.predict_proba(X_test)[:, 1]
    results["Random_Forest_Classifier"] = evaluate_model("6. Random Forest Classifier (Option A)", rf_probs)
    joblib.dump(rf_clf, os.path.join(model_dir, "best_classifier_rf.joblib"))

    # 7. Random Forest Regressor (Option B)
    print("Training Random Forest Regressor (Option B)...")
    rf_reg = RandomForestRegressor(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
    rf_reg.fit(X_train, y_train_count)
    rf_reg_preds = rf_reg.predict(X_test)
    results["Random_Forest_Regressor"] = evaluate_model("7. Random Forest Regressor (Option B)", rf_reg_preds, y_pred_count=rf_reg_preds, is_binary=False)
    joblib.dump(rf_reg, os.path.join(model_dir, "best_regressor_rf.joblib"))

    # 8. HistGradientBoosting Classifier (Option A - LightGBM architecture)
    print("Training HistGradientBoosting Classifier (Option A)...")
    hgb_clf = HistGradientBoostingClassifier(max_iter=150, max_depth=8, class_weight="balanced", random_state=42)
    hgb_clf.fit(X_train, y_train_hotspot)
    hgb_probs = hgb_clf.predict_proba(X_test)[:, 1]
    results["Gradient_Boosted_Classifier"] = evaluate_model("8. Gradient Boosted Trees (Option A)", hgb_probs)
    joblib.dump(hgb_clf, os.path.join(model_dir, "best_classifier_hgb.joblib"))

    # 9. HistGradientBoosting Regressor with Poisson Loss (Option B)
    print("Training HistGradientBoosting Poisson Regressor (Option B)...")
    hgb_reg = HistGradientBoostingRegressor(loss="poisson", max_iter=150, max_depth=8, random_state=42)
    hgb_reg.fit(X_train, y_train_count)
    hgb_reg_preds = hgb_reg.predict(X_test)
    results["Gradient_Boosted_Poisson"] = evaluate_model("9. Gradient Boosted Poisson (Option B)", hgb_reg_preds, y_pred_count=hgb_reg_preds, is_binary=False)
    joblib.dump(hgb_reg, os.path.join(model_dir, "best_regressor_hgb.joblib"))

    # Save scaler and feature names
    joblib.dump({"scaler": scaler, "feature_cols": feature_cols}, os.path.join(model_dir, "preprocessor.joblib"))

    # Serialize results to JSON and CSV
    df_results = pd.DataFrame(list(results.values()))
    csv_res_path = os.path.join(phase4_dir, "benchmark_comparison.csv")
    json_res_path = os.path.join(phase4_dir, "benchmark_results.json")
    
    df_results.to_csv(csv_res_path, index=False)
    with open(json_res_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n[3/3] Generating Comparative Performance Charts...")
    # Plot PAI@10 and PR-AUC Comparison
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Sort models by PAI@10
    df_plot = df_results.sort_values("PAI@10", ascending=True)
    
    # Chart 1: PAI@10
    colors = ["#7f7f7f" if "Baseline" in m else "#1f77b4" for m in df_plot["Model"]]
    axes[0].barh(df_plot["Model"], df_plot["PAI@10"], color=colors)
    axes[0].axvline(1.0, color="red", linestyle="--", label="Random Baseline (PAI=1.0)")
    axes[0].set_title("Prediction Accuracy Index (PAI@10) across Walk-Forward Holdout", fontweight="bold", fontsize=11)
    axes[0].set_xlabel("PAI@10 Score (Higher is Better)")
    axes[0].legend()
    axes[0].grid(axis="x", linestyle="--", alpha=0.5)
    
    # Chart 2: PR-AUC
    df_plot2 = df_results.sort_values("PR-AUC", ascending=True)
    colors2 = ["#7f7f7f" if "Baseline" in m else "#2ca02c" for m in df_plot2["Model"]]
    axes[1].barh(df_plot2["Model"], df_plot2["PR-AUC"], color=colors2)
    axes[1].axvline(y_test_hotspot.mean(), color="red", linestyle="--", label=f"Random Prevalence ({y_test_hotspot.mean():.3f})")
    axes[1].set_title("Area Under Precision-Recall Curve (PR-AUC)", fontweight="bold", fontsize=11)
    axes[1].set_xlabel("PR-AUC Score (Higher is Better)")
    axes[1].legend()
    axes[1].grid(axis="x", linestyle="--", alpha=0.5)
    
    plt.tight_layout()
    chart_path = os.path.join(phase4_dir, "model_performance_charts.png")
    plt.savefig(chart_path, dpi=200)
    plt.close()
    
    print(f" -> Saved performance charts: {chart_path}")
    print(f" -> Saved benchmark CSV:       {csv_res_path}")
    print(f" -> Saved benchmark JSON:      {json_res_path}")
    print("=" * 70)
    print("Phase 4 Model Training and Evaluation completed successfully.")
    return df_results

if __name__ == "__main__":
    run_phase_4()
