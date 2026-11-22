@echo off
title SIH26184 - Automated Unit & Integration Test Suite
echo ===========================================================================
echo  SMART INDIA HACKATHON 2026 (SIH26184) - AUTOMATED VERIFICATION SUITE
echo  Running 13 Automated Structural, Temporal & Model Tests
echo ===========================================================================
echo.

set PY_EXE="C:\Users\harsh\AppData\Local\Python\pythoncore-3.14-64\python.exe"
if exist %PY_EXE% goto :RUN_LOCAL

echo Using system python...
python run_tests.py
goto :END

:RUN_LOCAL
echo Running tests using Python 3.14...
%PY_EXE% run_tests.py

:END
pause
