@echo off
echo 🏥 Starting Healthcare Web Application...
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python and try again.
    pause
    exit /b 1
)

echo ✅ Python found
echo.

echo 📋 Instructions:
echo This script starts the secure Modular Backend (FastAPI).
echo Renamed route modules:
echo   clinical_chat:   /clinical/chat
echo   document_analyzer: /document/process
echo   csv_processor:   /csv/process
echo   organ_analyzer:  /organ/analyze
echo   transcription:   /transcription/transcribe
echo   translation_service: /translation/translate
echo.
echo To run unified backend instead: python run_app.py
echo API Docs (secured): /secure-docs with x-api-key header
echo.
echo 🚀 Starting backend API server...
echo ⚠️  Keep this window open while using the app
echo.

python main.py

echo.
echo 👋 Backend API server stopped
pause