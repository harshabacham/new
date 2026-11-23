@echo off
title SIH26184 - Web Application Portal
echo ===========================================================================
echo  SMART INDIA HACKATHON 2026 (SIH26184) - WEB APPLICATION PORTAL
echo  Starting Server and Launching Web Interface on http://localhost:8000
echo ===========================================================================
echo.

set PY_EXE="C:\Users\harsh\AppData\Local\Python\pythoncore-3.14-64\python.exe"
if exist %PY_EXE% goto :RUN_LOCAL

echo Using system python...
start http://localhost:8000
python api.py
goto :END

:RUN_LOCAL
echo Opening web application in default browser...
start http://localhost:8000
echo Starting REST API and Web Portal using Python 3.14...
%PY_EXE% api.py

:END
pause
