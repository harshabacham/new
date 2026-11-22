"""
Comprehensive Automated Unit and Integration Test Suite.
Verifies all five phases: data schemas, temporal causality, zero-leakage,
model inference, evaluation metrics (PAI, PEI), GIS generation, and REST API.
"""

import os
import sys
import json
import unittest
import numpy as np
import pandas as pd
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

class TestCybercrimeForecastingPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_dir = BASE_DIR
        cls.data_dir = os.path.join(BASE_DIR, "data")
        cls.phase1_dir = os.path.join(BASE_DIR, "phase_1")
        cls.phase2_dir = os.path.join(BASE_DIR, "phase_2")
        cls.phase3_dir = os.path.join(BASE_DIR, "phase_3")
        cls.phase4_dir = os.path.join(BASE_DIR, "phase_4")
        cls.phase5_dir = os.path.join(BASE_DIR, "phase_5")
        cls.model_dir = os.path.join(BASE_DIR, "models")
        cls.reports_dir = os.path.join(BASE_DIR, "reports")

    # ==================== TEST SUITE 1: PHASE 1 FOUNDATIONS ====================
    def test_01_phase1_deliverables_exist(self):
        """Verify Phase 1 research documents and compiled report exist."""
        required_files = [
            "01_problem_definition.md", "02_literature_review.md",
            "03_research_gap_analysis.md", "04_dataset_feasibility.md",
            "05_proposed_methodology.md", "06_evaluation_and_ethics.md",
            "07_references.bib", "08_phase_1_summary.md",
            "Phase_1_Research_Report.pdf"
        ]
        for f in required_files:
            f_path = os.path.join(self.phase1_dir, f)
            self.assertTrue(os.path.exists(f_path), f"Phase 1 file missing: {f}")

    def test_02_bibtex_citations(self):
        """Verify BibTeX database contains required peer-reviewed records."""
        bib_path = os.path.join(self.phase1_dir, "07_references.bib")
        with open(bib_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("@article{leukfeldt2017", content)
        self.assertIn("@article{chainey2008", content)
        self.assertIn("@article{lin2018", content)

    # ==================== TEST SUITE 2: PHASE 2 DATA ENGINE ====================
    def test_03_grid_integrity(self):
        """Verify 20x20 grid geometry and ATM density."""
        grid_path = os.path.join(self.data_dir, "grid_cells.csv")
        self.assertTrue(os.path.exists(grid_path))
        df_grid = pd.read_csv(grid_path)
        self.assertEqual(len(df_grid), 400, "Grid must contain exactly 400 cells (20x20)")
        self.assertTrue((df_grid["cell_atm_count"] > 0).all(), "All cells must have ATM infrastructure")
        self.assertGreaterEqual(df_grid["lat_min"].min(), 28.49)
        self.assertLessEqual(df_grid["lat_max"].max(), 28.71)

    def test_04_temporal_causality_and_decoupling(self):
        """Verify 100% causal temporal ordering and geographic entity decoupling."""
        pair_path = os.path.join(self.data_dir, "cybercrime_paired_events.parquet")
        self.assertTrue(os.path.exists(pair_path))
        df_paired = pd.read_parquet(pair_path)
        
        cashouts = df_paired[df_paired["is_cash_out"] == 1]
        self.assertGreater(len(cashouts), 10000, "Should generate > 10,000 cash-out events")
        
        t_inc = pd.to_datetime(cashouts["incident_timestamp"])
        t_comp = pd.to_datetime(cashouts["complaint_timestamp"])
        t_with = pd.to_datetime(cashouts["withdrawal_timestamp"])
        
        # Incident strictly precedes complaint & cash-out
        self.assertTrue((t_comp >= t_inc).all(), "Temporal violation: Complaint precedes Incident!")
        self.assertTrue((t_with > t_inc).all(), "Temporal violation: Cash-out precedes Incident!")
        
        # Spatial decoupling
        decoupled = (cashouts["victim_lat"] != cashouts["latitude"]) | (cashouts["victim_lon"] != cashouts["longitude"])
        self.assertTrue(decoupled.all(), "Entity violation: Conflation of Victim and Cash-Out locations!")

    # ==================== TEST SUITE 3: PHASE 3 FEATURES & ESDA ====================
    def test_05_spatiotemporal_panel_dimensions(self):
        """Verify spatiotemporal panel shape and class imbalance."""
        feat_path = os.path.join(self.data_dir, "spatiotemporal_feature_matrix.parquet")
        self.assertTrue(os.path.exists(feat_path))
        df_feat = pd.read_parquet(feat_path)
        
        self.assertEqual(len(df_feat), 74400, "Panel must contain 74,400 cell-day units")
        self.assertEqual(len(df_feat.columns), 29, "Feature matrix must contain 29 standardized columns")
        
        # Class imbalance check
        pos_rate = df_feat["target_hotspot"].mean()
        self.assertTrue(0.03 <= pos_rate <= 0.08, f"Hotspot rate {pos_rate} should reflect realistic crime sparsity")

    def test_06_leakage_prevention(self):
        """Verify features at day t do not deterministically expose day t targets."""
        feat_path = os.path.join(self.data_dir, "spatiotemporal_feature_matrix.parquet")
        df_feat = pd.read_parquet(feat_path)
        
        # Test correlation between shifted lag_count_1d and target_count
        corr = df_feat[["lag_count_1d", "target_count"]].corr().iloc[0, 1]
        self.assertLess(corr, 0.70, "Suspiciously high correlation indicating potential data leakage")

    # ==================== TEST SUITE 4: PHASE 4 MODEL BENCHMARKS ====================
    def test_07_model_artifacts_loadable(self):
        """Verify saved model artifacts can be loaded and predict without errors."""
        clf_path = os.path.join(self.model_dir, "best_classifier_hgb.joblib")
        reg_path = os.path.join(self.model_dir, "best_regressor_hgb.joblib")
        prep_path = os.path.join(self.model_dir, "preprocessor.joblib")
        
        self.assertTrue(os.path.exists(clf_path))
        self.assertTrue(os.path.exists(reg_path))
        
        clf = joblib.load(clf_path)
        reg = joblib.load(reg_path)
        prep = joblib.load(prep_path)
        
        # Test inference with dummy mock vector
        dummy_x = np.zeros((1, len(prep["feature_cols"])))
        prob = clf.predict_proba(dummy_x)[:, 1]
        count = reg.predict(dummy_x)
        
        self.assertTrue(0.0 <= prob[0] <= 1.0, "Probability must be bounded in [0, 1]")
        self.assertGreaterEqual(count[0], 0.0, "Count prediction must be non-negative")

    def test_08_benchmark_outperformance(self):
        """Verify model achieves statistically superior PAI@10 and PEI@10 over baselines."""
        bench_path = os.path.join(self.phase4_dir, "benchmark_results.json")
        self.assertTrue(os.path.exists(bench_path))
        
        with open(bench_path, "r") as f:
            bench = json.load(f)
            
        gbt_pai = bench["Gradient_Boosted_Classifier"]["PAI@10"]
        rand_pai = bench["Uniform_Random"]["PAI@10"]
        gbt_prec10 = bench["Gradient_Boosted_Classifier"]["Precision@10"]
        
        self.assertGreater(gbt_pai, 7.5, f"Expected PAI@10 > 7.5, got {gbt_pai}")
        self.assertGreater(gbt_pai, rand_pai * 5.0, "Model must outperform random baseline by at least 5x")
        self.assertGreater(gbt_prec10, 0.45, f"Expected Precision@10 > 45%, got {gbt_prec10}")

    # ==================== TEST SUITE 5: PHASE 5 DELIVERABLES ====================
    def test_09_geospatial_map_and_briefing(self):
        """Verify interactive Folium map and tactical intelligence briefings exist."""
        map_path = os.path.join(self.phase5_dir, "interactive_hotspot_forecast_map.html")
        brief_md = os.path.join(self.phase5_dir, "tactical_intelligence_briefing.md")
        brief_pdf = os.path.join(self.phase5_dir, "Phase_5_Tactical_Briefing.pdf")
        master_pdf = os.path.join(BASE_DIR, "Cybercrime_Withdrawal_Forecasting_Final_Report.pdf")
        
        self.assertTrue(os.path.exists(map_path) and os.path.getsize(map_path) > 10000)
        self.assertTrue(os.path.exists(brief_md))
        self.assertTrue(os.path.exists(brief_pdf) and os.path.getsize(brief_pdf) > 3000)
        self.assertTrue(os.path.exists(master_pdf) and os.path.getsize(master_pdf) > 20000)

    # ==================== TEST SUITE 6: REST API VERIFICATION ====================
    def test_10_api_endpoints(self):
        """Verify REST API responds with valid status and JSON schemas."""
        from starlette.testclient import TestClient
        from api import app
        
        client = TestClient(app)
        
        # Test /health
        res_health = client.get("/health")
        self.assertEqual(res_health.status_code, 200)
        self.assertEqual(res_health.json()["status"], "HEALTHY")
        
        # Test /api/v1/forecasts
        res_fc = client.get("/api/v1/forecasts?limit=5")
        self.assertEqual(res_fc.status_code, 200)
        fc_data = res_fc.json()
        self.assertEqual(len(fc_data["results"]), 5)
        self.assertIn("hotspot_probability", fc_data["results"][0])
        
        # Test /api/v1/forecasts/{cell_id}
        res_cell = client.get("/api/v1/forecasts/CELL_03_15")
        self.assertEqual(res_cell.status_code, 200)
        self.assertEqual(res_cell.json()["grid_cell_id"], "CELL_03_15")
        
        # Test /api/v1/benchmarks
        res_b = client.get("/api/v1/benchmarks")
        self.assertEqual(res_b.status_code, 200)
        self.assertIn("summary_findings", res_b.json())

    # ==================== TEST SUITE 7: EXTERNAL DATASETS & ADAPTERS ====================
    def test_11_external_dataset_imports(self):
        """Verify real-world Chicago and PaySim imported datasets exist and are schema-compliant."""
        chi_path = os.path.join(self.data_dir, "imported_chicago_financial_crime.csv")
        pay_path = os.path.join(self.data_dir, "imported_paysim_sample.csv")
        
        self.assertTrue(os.path.exists(chi_path), "Imported Chicago real-world crime dataset missing")
        self.assertTrue(os.path.exists(pay_path), "Imported PaySim simulator dataset missing")
        
        df_chi = pd.read_csv(chi_path)
        self.assertGreaterEqual(len(df_chi), 2000, "Chicago dataset should contain >= 2,000 real-world records")
        self.assertIn("grid_cell_id", df_chi.columns)
        self.assertIn("defrauded_amount", df_chi.columns)
        self.assertTrue((df_chi["latitude"] > 40.0).all(), "Coordinates must reflect Chicago bounding box")
        
        # Test Universal Dataset Adapter
        from data_importer import UniversalDatasetAdapter
        mock_df = pd.DataFrame({
            "Time": ["2026-05-01 12:00:00"],
            "Loss": [45000.0],
            "Lat": [28.614],
            "Lon": [77.209],
            "Offense": ["UPI Phishing"],
            "Bank": ["SBIN"]
        })
        std_df = UniversalDatasetAdapter.ingest_custom_dataframe(mock_df)
        self.assertEqual(len(std_df), 1)
        self.assertEqual(std_df.iloc[0]["fraud_category"], "UPI Phishing")

    # ==================== TEST SUITE 8: ADVANCED ML ENSEMBLE & CALIBRATION ====================
    def test_12_advanced_ml_ensemble_and_calibration(self):
        """Verify Champion Stacked Ensemble and Probability Calibrator load and infer accurately."""
        stack_path = os.path.join(self.model_dir, "champion_stacked_classifier.joblib")
        cal_path = os.path.join(self.model_dir, "calibrated_classifier.joblib")
        bench_adv_path = os.path.join(self.phase4_dir, "advanced_benchmark_results.json")
        diag_img_path = os.path.join(self.phase4_dir, "advanced_diagnostic_curves.png")
        
        self.assertTrue(os.path.exists(stack_path), "Champion Stacked Classifier artifact missing")
        self.assertTrue(os.path.exists(cal_path), "Calibrated Classifier artifact missing")
        self.assertTrue(os.path.exists(bench_adv_path), "Advanced benchmark JSON missing")
        self.assertTrue(os.path.exists(diag_img_path), "4-Panel diagnostic curves missing")
        
        prep = joblib.load(os.path.join(self.model_dir, "preprocessor.joblib"))
        stacked_clf = joblib.load(stack_path)
        cal_clf = joblib.load(cal_path)
        
        dummy_x = np.zeros((1, len(prep["feature_cols"])))
        p_stack = stacked_clf.predict_proba(dummy_x)[:, 1]
        p_cal = cal_clf.predict_proba(dummy_x)[:, 1]
        
        self.assertTrue(0.0 <= p_stack[0] <= 1.0)
        self.assertTrue(0.0 <= p_cal[0] <= 1.0)
        
        with open(bench_adv_path, "r") as f:
            adv_res = json.load(f)
        self.assertGreater(adv_res["stacked_ensemble"]["ROC-AUC"], 0.90)
        self.assertGreater(adv_res["probability_calibration"]["calibration_gain_pct"], 50.0)

    # ==================== TEST SUITE 9: TACTICAL EXPORTS & GEOJSON ====================
    def test_13_tactical_exports_and_geojson(self):
        """Verify standard GeoJSON and multi-agency tactical dispatch CSV packages exist and are valid."""
        geojson_path = os.path.join(self.data_dir, "hotspot_forecast_cells.geojson")
        dispatch_path = os.path.join(self.base_dir, "reports", "police_patrol_dispatch_orders.csv")
        bank_path = os.path.join(self.base_dir, "reports", "bank_atm_friction_directives.csv")
        summary_path = os.path.join(self.base_dir, "reports", "executive_summary_card.json")
        
        self.assertTrue(os.path.exists(geojson_path), "GeoJSON feature collection missing")
        self.assertTrue(os.path.exists(dispatch_path), "Police patrol dispatch CSV missing")
        self.assertTrue(os.path.exists(bank_path), "Bank ATM friction directives CSV missing")
        self.assertTrue(os.path.exists(summary_path), "Executive summary JSON missing")
        
        # Verify GeoJSON structure
        with open(geojson_path, "r", encoding="utf-8") as f:
            gj = json.load(f)
        self.assertEqual(gj["type"], "FeatureCollection")
        self.assertEqual(len(gj["features"]), 400)
        self.assertIn("priority_rank", gj["features"][0]["properties"])
        self.assertEqual(gj["features"][0]["geometry"]["type"], "Polygon")
        
        # Verify Dispatch CSV
        df_disp = pd.read_csv(dispatch_path)
        self.assertGreaterEqual(len(df_disp), 20)
        self.assertIn("Operational_Role", df_disp.columns)
        self.assertIn("Standard_Operating_Procedure", df_disp.columns)
        
        # Verify Bank CSV
        df_bank = pd.read_csv(bank_path)
        self.assertGreaterEqual(len(df_bank), 20)
        self.assertIn("Terminal_Risk_Tier", df_bank.columns)
        self.assertIn("Recommended_Switch_Action", df_bank.columns)

if __name__ == "__main__":
    unittest.main()
