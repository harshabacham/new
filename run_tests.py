"""
Test Runner Script for SIH26184 Verification Suite.
Runs unittest test runner and generates an executive test audit summary.
"""

import unittest
import sys
import os
import time

def run_all_tests():
    print("=" * 75)
    print("RUNNING AUTOMATED UNIT & INTEGRATION TEST SUITE (SIH26184)")
    print("=" * 75)
    
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")
    
    start_time = time.time()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    elapsed = time.time() - start_time
    
    print("\n" + "=" * 75)
    print("TEST SUITE EXECUTION SUMMARY")
    print("=" * 75)
    print(f"Total Tests Executed: {result.testsRun}")
    print(f"Passed:              {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failed:              {len(result.failures)}")
    print(f"Errors:              {len(result.errors)}")
    print(f"Execution Duration:  {elapsed:.2f} seconds")
    print("=" * 75)
    
    if result.wasSuccessful():
        print("ALL TESTS PASSED WITH 100% SUCCESS RATE. SYSTEM READY FOR EVALUATION.")
        return 0
    else:
        print("CRITICAL: TEST FAILURES DETECTED.")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
