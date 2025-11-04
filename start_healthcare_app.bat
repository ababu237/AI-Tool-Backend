@echo off
REM Healthcare Web Application Launcher - Windows Batch Script
REM Simple one-click launcher for Windows users

echo 🏥 Healthcare Web Application Launcher
echo =====================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

REM Check if required files exist
if not exist "main.py" (
    echo ❌ main.py not found
    echo Please run this script from the healthcare backend directory
    pause
    exit /b 1
)

if not exist "web_app.py" (
    echo ❌ web_app.py not found
    echo Please run this script from the healthcare backend directory
    pause
    exit /b 1
)

echo ✅ Prerequisites check passed
echo.

REM Install requirements if needed
echo 📦 Checking Python dependencies...
pip install -r requirements.txt >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Warning: Could not install some dependencies
)

echo ✅ Dependencies ready
echo.

REM Start the application
echo 🚀 Starting Healthcare Web Application...
echo.
echo ⚠️  If this is your first time running the app:
echo    1. Make sure you have configured your OpenAI API key
echo    2. Check that no other applications are using ports 8000 or 3000
echo.
echo Press Ctrl+C to stop the application when you're done
echo.

python start_healthcare_app.py

echo.
echo 👋 Healthcare Web Application has stopped
pause