@echo off
REM Avvia il server FastAPI con uvicorn in modalità sviluppo
SetLocal EnableDelayedExpansion
cd /d "%~dp0backend"
uvicorn app.main:app --reload --log-level debug
