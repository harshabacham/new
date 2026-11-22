@echo off
title SIH26184 - Master Pipeline Orchestrator
echo ===========================================================================
echo  SMART INDIA HACKATHON 2026 (SIH26184) - END-TO-END PIPELINE ORCHESTRATOR
echo  Executes All 5 Phases, Data Ingestion, Model Stacking, Reports & Tests
echo ===========================================================================
echo.

set PY_EXE="C:\Users\harsh\AppData\Local\Python\pythoncore-3.14-64\python.exe"
if exist %PY_EXE% goto :RUN_LOCAL

echo Using system python...
python run_all_phases.py
goto :END

:RUN_LOCAL
echo Executing pipeline using Python 3.14...
%PY_EXE% run_all_phases.py

:END
pause
