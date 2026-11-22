"""
Master Orchestrator: End-to-End Execution of All Five Phases.
Smart India Hackathon 2026 | Problem ID: SIH26184
Cybercrime Cash-Withdrawal Location Forecasting Using Supervised Machine Learning and Geospatial Analytics.
"""

import os
import sys
import time
from datetime import datetime

# Add root directory to path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

def print_banner(phase_name):
    print("\n" + "=" * 80)
    print(f" >>> RUNNING {phase_name.upper()}")
    print("=" * 80)

def main():
    start_time = time.time()
    print("=" * 80)
    print("SMART INDIA HACKATHON 2026 (SIH26184) - END-TO-END PIPELINE ORCHESTRATOR")
    print("B.Tech AI/ML Capstone Project | Supervised Machine Learning & Geospatial Analytics")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # ----------------------------------------------------
    # PHASE 1: Verify Problem Definition & Literature Review
    # ----------------------------------------------------
    print_banner("Phase 1: Verification of Research Foundations")
    from compile_report import build_pdf as compile_phase_1
    compile_phase_1()
    print(" [OK] Phase 1 Research Report Verified & Compiled.")

    # ----------------------------------------------------
    # PHASE 2: Data Generation & Quality Assurance Audit
    # ----------------------------------------------------
    print_banner("Phase 2: Dataset Generation, Schema & Quality Assurance")
    from phase_2.generate_synthetic_data import main as generate_data
    from phase_2.validate_data import run_validation
    from phase_2.compile_phase_2_report import build_pdf as compile_phase_2
    from data_importer import main as import_external_datasets
    
    generate_data()
    val_success = run_validation()
    assert val_success, "Phase 2 Quality Assurance Tests Failed!"
    import_external_datasets()
    compile_phase_2()
    print(" [OK] Phase 2 Data Engineering, Import & Validation Complete.")

    # ----------------------------------------------------
    # PHASE 3: ESDA, Spatial Clustering & Feature Pipeline
    # ----------------------------------------------------
    print_banner("Phase 3: Exploratory Spatial Data Analysis (ESDA) & Feature Pipeline")
    from phase_3.spatial_clustering_esda import run_esda
    from phase_3.spatiotemporal_feature_pipeline import build_spatiotemporal_panel
    from phase_3.compile_phase_3_report import build_pdf as compile_phase_3
    
    run_esda()
    build_spatiotemporal_panel()
    compile_phase_3()
    print(" [OK] Phase 3 ESDA & Feature Engineering Complete.")

    # ----------------------------------------------------
    # PHASE 4: Supervised Training & Walk-Forward Evaluation
    # ----------------------------------------------------
    print_banner("Phase 4: Supervised Model Training & Walk-Forward Backtesting")
    from phase_4.train_and_evaluate import run_phase_4
    from phase_4.advanced_modeling import run_advanced_modeling
    from phase_4.compile_phase_4_report import build_pdf as compile_phase_4
    
    run_phase_4()
    run_advanced_modeling()
    compile_phase_4()
    print(" [OK] Phase 4 Model Training, Stacking & Evaluation Complete.")

    # ----------------------------------------------------
    # PHASE 5: Explainability, GIS Maps & Tactical Briefing
    # ----------------------------------------------------
    print_banner("Phase 5: Explainability, Geospatial GIS Maps & Tactical Briefing")
    from phase_5.explainability_engine import run_explainability
    from phase_5.generate_interactive_map import generate_map
    from phase_5.generate_tactical_briefing import generate_briefing
    from phase_5.export_tactical_packages import generate_tactical_packages
    from phase_5.compile_phase_5_report import build_pdf as compile_phase_5
    
    run_explainability()
    generate_map()
    generate_briefing()
    generate_tactical_packages()
    compile_phase_5()
    print(" [OK] Phase 5 Geospatial Intelligence, Tactical Packages & Dossier Complete.")

    # ----------------------------------------------------
    # CONSOLIDATED MASTER REPORT & PITCH DECK COMPILATION
    # ----------------------------------------------------
    print_banner("Master Capstone Thesis & Presentation Deck Compilation")
    from compile_full_capstone_report import build_master_pdf
    from presentation.compile_pitch_deck import build_pitch_deck
    build_master_pdf()
    build_pitch_deck()
    print(" [OK] Master Capstone Thesis & SIH Pitch Deck Compiled.")

    # ----------------------------------------------------
    # AUTOMATED INTEGRATION TEST SUITE
    # ----------------------------------------------------
    print_banner("Automated System Verification & Unit Test Suite")
    from run_tests import run_all_tests
    test_exit_code = run_all_tests()
    assert test_exit_code == 0, "Test suite execution failed!"
    print(" [OK] All Automated Tests Passed (100% Integrity).")

    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print(f"ALL FIVE PHASES IMPLEMENTED AND VERIFIED SUCCESSFULLY IN {elapsed:.1f} SECONDS!")
    print("=" * 80)
    print("Generated Deliverables & PDF Reports:")
    print(" 1. phase_1/Phase_1_Research_Report.pdf")
    print(" 2. phase_2/Phase_2_Data_Report.pdf")
    print(" 3. phase_3/Phase_3_Feature_Report.pdf")
    print(" 4. phase_4/Phase_4_Modeling_Report.pdf")
    print(" 5. phase_5/Phase_5_Intelligence_Report.pdf")
    print(" 6. phase_5/Phase_5_Tactical_Briefing.pdf")
    print(" 7. Cybercrime_Withdrawal_Forecasting_Final_Report.pdf (Master Capstone Thesis)")
    print(" 8. phase_5/interactive_hotspot_forecast_map.html (Interactive Folium GIS Map)")
    print(" 9. app.py (Interactive Streamlit Tactical Command Dashboard)")
    print("=" * 80)

if __name__ == "__main__":
    main()
