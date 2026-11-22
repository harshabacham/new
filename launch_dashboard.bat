@echo off
title SIH26184 - Tactical Command Dashboard
echo ===========================================================================
echo  SMART INDIA HACKATHON 2026 (SIH26184) - TACTICAL COMMAND DASHBOARD
echo  Cybercrime Cash-Withdrawal Location Forecasting Platform
echo ===========================================================================
echo.

set PY_EXE="C:\Users\harsh\AppData\Local\Python\pythoncore-3.14-64\python.exe"
if exist %PY_EXE% goto :RUN_LOCAL

echo Using system python...
python -m streamlit run app.py
goto :END

:RUN_LOCAL
echo Launching Streamlit dashboard using Python 3.14...
%PY_EXE% -m streamlit run app.py

:END
pause
