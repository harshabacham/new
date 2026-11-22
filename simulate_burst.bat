@echo off
title SIH26184 - Helpline 1930 Live Burst Simulator
echo ===========================================================================
echo  SMART INDIA HACKATHON 2026 (SIH26184) - REAL-TIME COMPLAINT STREAM SIMULATOR
echo  Simulating Helpline 1930 Incoming Cybercrime Bursts
echo ===========================================================================
echo.

set PY_EXE="C:\Users\harsh\AppData\Local\Python\pythoncore-3.14-64\python.exe"
if exist %PY_EXE% goto :RUN_LOCAL

echo Using system python...
python simulate_realtime_feed.py
goto :END

:RUN_LOCAL
echo Triggering streaming simulator using Python 3.14...
%PY_EXE% simulate_realtime_feed.py

:END
pause
