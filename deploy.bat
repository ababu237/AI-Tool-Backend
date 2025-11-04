@echo off
REM Healthcare AI Backend - Windows Deployment Script
REM PowerShell version of the deployment script

echo 🏥 Healthcare AI Backend Deployment
echo ====================================

set STAGE=%1
set REGION=%2

if "%STAGE%"=="" set STAGE=dev
if "%REGION%"=="" set REGION=us-east-1

echo Stage: %STAGE%
echo Region: %REGION%
echo.

echo 📋 Checking prerequisites...

REM Check if AWS CLI is installed
aws --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ AWS CLI is not installed
    exit /b 1
)

REM Check if Serverless Framework is installed
serverless --version >nul 2>&1 || sls --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Serverless Framework is not installed
    echo Install it with: npm install -g serverless
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed
    exit /b 1
)

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed
    exit /b 1
)

echo ✅ Prerequisites check passed

echo 📦 Installing Serverless plugins...
if not exist package.json (
    npm init -y >nul 2>&1
)
npm install --save-dev serverless-python-requirements serverless-plugin-warmup serverless-plugin-split-stacks serverless-domain-manager

echo 🔧 Checking environment configuration...
if not exist .env (
    if exist .env.example (
        echo ⚠️  No .env file found, copying from .env.example
        copy .env.example .env >nul
        echo ❗ Please update .env file with your actual values before deploying
    ) else (
        echo ❌ No environment configuration found
        exit /b 1
    )
)

echo ✅ Environment configuration ready

echo 🐍 Installing Python dependencies...
pip install -r requirements.txt

echo 🧪 Running tests...
if exist pytest.ini (
    python -m pytest unit_tests/ -v --tb=short
    if %errorlevel% neq 0 (
        echo ⚠️  Some tests failed, but continuing deployment...
    )
) else (
    echo 📝 No tests configuration found, skipping tests
)

echo 🚀 Deploying to AWS Lambda...
echo Stage: %STAGE%
echo Region: %REGION%

REM Deploy using Serverless Framework
sls deploy --stage %STAGE% --region %REGION% --verbose
if %errorlevel% neq 0 (
    echo ❌ Deployment failed
    exit /b 1
)

echo.
echo 🎉 Deployment completed successfully!
echo =================================
echo.
echo 📋 Next steps:
echo 1. Check AWS Lambda console for your functions
echo 2. Update your frontend to use the new API Gateway URL
echo 3. Test endpoints using the API Gateway URL
echo.
echo 🔧 Useful commands:
echo • View logs: sls logs -f healthcareApi --stage %STAGE% --tail
echo • Remove deployment: sls remove --stage %STAGE%
echo • Update function: sls deploy function -f healthcareApi --stage %STAGE%
echo.
echo 🏥 Healthcare AI Backend deployment complete!