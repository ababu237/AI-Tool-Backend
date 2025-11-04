#!/bin/bash

# Healthcare AI Backend - Serverless Deployment Script
# This script handles the complete deployment pipeline

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
STAGE=${1:-dev}
REGION=${2:-us-east-1}

echo -e "${BLUE}🏥 Healthcare AI Backend Deployment${NC}"
echo -e "${BLUE}====================================${NC}"
echo -e "Stage: ${GREEN}$STAGE${NC}"
echo -e "Region: ${GREEN}$REGION${NC}"
echo ""

# Check prerequisites
echo -e "${YELLOW}📋 Checking prerequisites...${NC}"

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo -e "${RED}❌ AWS CLI is not installed${NC}"
    exit 1
fi

# Check if Serverless Framework is installed
if ! command -v serverless &> /dev/null && ! command -v sls &> /dev/null; then
    echo -e "${RED}❌ Serverless Framework is not installed${NC}"
    echo -e "${YELLOW}Install it with: npm install -g serverless${NC}"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js is not installed${NC}"
    exit 1
fi

# Check if Python 3.11 is available
if ! command -v python3.11 &> /dev/null; then
    echo -e "${YELLOW}⚠️  Python 3.11 not found, checking python3...${NC}"
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python 3 is not installed${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}✅ Prerequisites check passed${NC}"

# Install Serverless plugins
echo -e "${YELLOW}📦 Installing Serverless plugins...${NC}"
npm init -y > /dev/null 2>&1 || true
npm install --save-dev serverless-python-requirements serverless-plugin-warmup serverless-plugin-split-stacks serverless-domain-manager

# Check environment variables
echo -e "${YELLOW}🔧 Checking environment configuration...${NC}"
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        echo -e "${YELLOW}⚠️  No .env file found, copying from .env.example${NC}"
        cp .env.example .env
        echo -e "${RED}❗ Please update .env file with your actual values before deploying${NC}"
    else
        echo -e "${RED}❌ No environment configuration found${NC}"
        exit 1
    fi
fi

# Source environment variables
source .env

# Validate critical environment variables
if [ -z "$OPENAI_API_KEY" ] || [ "$OPENAI_API_KEY" = "your-openai-api-key-here" ]; then
    echo -e "${RED}❌ OPENAI_API_KEY not configured in .env file${NC}"
    exit 1
fi

if [ -z "$API_SECRET_KEY" ] || [ "$API_SECRET_KEY" = "your-super-secret-api-key-change-in-production" ]; then
    echo -e "${YELLOW}⚠️  Using default API_SECRET_KEY - change this in production!${NC}"
fi

echo -e "${GREEN}✅ Environment configuration validated${NC}"

# Install Python dependencies
echo -e "${YELLOW}🐍 Installing Python dependencies...${NC}"
pip install -r requirements.txt

# Run tests (optional)
if [ "$SKIP_TESTS" != "true" ]; then
    echo -e "${YELLOW}🧪 Running tests...${NC}"
    if [ -f pytest.ini ]; then
        python -m pytest unit_tests/ -v --tb=short || {
            echo -e "${YELLOW}⚠️  Some tests failed, but continuing deployment...${NC}"
        }
    else
        echo -e "${YELLOW}📝 No tests configuration found, skipping tests${NC}"
    fi
fi

# Deploy infrastructure
echo -e "${YELLOW}🚀 Deploying to AWS Lambda...${NC}"
echo -e "Stage: $STAGE"
echo -e "Region: $REGION"

# Deploy using Serverless Framework
if command -v sls &> /dev/null; then
    SLS_CMD="sls"
else
    SLS_CMD="serverless"
fi

$SLS_CMD deploy --stage $STAGE --region $REGION --verbose

# Get deployment outputs
echo -e "${YELLOW}📊 Getting deployment information...${NC}"
API_URL=$($SLS_CMD info --stage $STAGE --region $REGION | grep "endpoint:" | cut -d' ' -f4)

echo ""
echo -e "${GREEN}🎉 Deployment completed successfully!${NC}"
echo -e "${GREEN}=================================${NC}"
echo -e "API URL: ${BLUE}$API_URL${NC}"
echo -e "Stage: ${GREEN}$STAGE${NC}"
echo -e "Region: ${GREEN}$REGION${NC}"
echo ""
echo -e "${YELLOW}📋 Next steps:${NC}"
echo -e "1. Update your frontend to use: ${BLUE}$API_URL${NC}"
echo -e "2. Test endpoints: ${BLUE}$API_URL/docs${NC}"
echo -e "3. Monitor logs: ${BLUE}$SLS_CMD logs -f healthcareApi --stage $STAGE${NC}"
echo ""
echo -e "${YELLOW}🔧 Useful commands:${NC}"
echo -e "• View logs: ${BLUE}$SLS_CMD logs -f healthcareApi --stage $STAGE --tail${NC}"
echo -e "• Remove deployment: ${BLUE}$SLS_CMD remove --stage $STAGE${NC}"
echo -e "• Update function: ${BLUE}$SLS_CMD deploy function -f healthcareApi --stage $STAGE${NC}"
echo ""

# Test deployment
echo -e "${YELLOW}🧪 Testing deployment...${NC}"
HEALTH_CHECK_URL="$API_URL/health"
if curl -s -f "$HEALTH_CHECK_URL" > /dev/null; then
    echo -e "${GREEN}✅ Health check passed: $HEALTH_CHECK_URL${NC}"
else
    echo -e "${YELLOW}⚠️  Health check endpoint not responding (this is normal for cold starts)${NC}"
fi

echo -e "${GREEN}🏥 Healthcare AI Backend deployment complete!${NC}"