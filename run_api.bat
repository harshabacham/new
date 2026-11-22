@echo off
title SIH26184 - High-Throughput REST API Microservice
echo ===========================================================================
echo  SMART INDIA HACKATHON 2026 (SIH26184) - REST API MICROSERVICE
echo  Serving Endpoints on http://localhost:8000
echo ===========================================================================
echo.

set PY_EXE="C:\Users\harsh\AppData\Local\Python\pythoncore-3.14-64\python.exe"
if exist %PY_EXE% goto :RUN_LOCAL

echo Using system python...
python api.py
goto :END

:RUN_LOCAL
echo Starting API service using Python 3.14...
%PY_EXE% api.py

:END
pause
