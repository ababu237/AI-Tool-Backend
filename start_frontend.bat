@echo off
echo 🌐 Starting Healthcare Frontend...
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

echo 📋 Make sure backend is running first!
echo    Run start_backend.bat in another window
echo.
echo 🚀 Starting frontend web application...
echo 🌐 Will open at: http://localhost:3000
echo ⚠️  Keep this window open while using the app
echo.

timeout /t 3 >nul

python web_app.py

echo.
echo 👋 Frontend web application stopped
pause