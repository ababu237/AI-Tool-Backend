# 🚀 Healthcare AI Backend - Serverless Deployment Guide

## 📋 **Overview**

This serverless configuration deploys your Healthcare AI Backend APIs to AWS Lambda using the Serverless Framework. The setup includes:

- **FastAPI Application** running on AWS Lambda
- **API Gateway** for HTTP routing
- **S3 Bucket** for file storage
- **CloudWatch** for logging and monitoring
- **Multiple deployment strategies** (monolithic + microservices)

---

## 🏗️ **Architecture**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │────│   API Gateway   │────│   Lambda        │
│   (React)       │    │   (HTTP API)    │    │   (FastAPI)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                       ┌─────────────────┐             │
                       │   S3 Storage    │─────────────┘
                       │   (Files)       │
                       └─────────────────┘
                                │
                       ┌─────────────────┐
                       │   CloudWatch    │
                       │   (Logs)        │
                       └─────────────────┘
```

---

## 🛠️ **Prerequisites**

### **Required Tools:**

```bash
# 1. Node.js (for Serverless Framework)
node --version  # Should be v14+

# 2. Python 3.11
python3.11 --version

# 3. AWS CLI
aws --version

# 4. Serverless Framework
npm install -g serverless
```

### **AWS Configuration:**

```bash
# Configure AWS credentials
aws configure
# or use environment variables:
export AWS_ACCESS_KEY_ID=your-key
export AWS_SECRET_ACCESS_KEY=your-secret
export AWS_DEFAULT_REGION=us-east-1
```

---

## ⚡ **Quick Start**

### **1. Environment Setup**

```bash
# Copy environment template
cp .env.example .env

# Edit environment variables
nano .env  # or use your favorite editor
```

**Required Environment Variables:**

```bash
# .env file
OPENAI_API_KEY=sk-your-openai-api-key-here
API_SECRET_KEY=your-super-secret-api-key
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
AWS_REGION=us-east-1
STAGE=dev
```

### **2. Deploy to AWS**

**Linux/Mac:**

```bash
chmod +x deploy.sh
./deploy.sh dev us-east-1
```

**Windows:**

```cmd
deploy.bat dev us-east-1
```

**Manual Deployment:**

```bash
# Install dependencies
npm install

# Deploy
sls deploy --stage dev --region us-east-1
```

---

## 📁 **Deployment Strategies**

### **Strategy 1: Monolithic (Default)**

- Single Lambda function for all endpoints
- Lower cold start frequency
- Simpler management
- Good for development

### **Strategy 2: Microservices**

- Separate Lambda functions per service
- Independent scaling
- Isolated failures
- Better for production

**Enable microservices mode:**

```yaml
# In serverless.yml, uncomment individual functions:
functions:
  clinicalChat: # Uncomment this section
  documentProcessor: # Uncomment this section
  # etc...
```

---

## 🔧 **Configuration Options**

### **Memory & Timeout Settings:**

```yaml
# serverless.yml
provider:
  memorySize: 1024 # Default: 1GB RAM
  timeout: 300 # Default: 5 minutes

functions:
  healthcareApi:
    memorySize: 1024 # Override per function
    timeout: 180 # 3 minutes for API
```

### **Environment Variables:**

```yaml
# serverless.yml
provider:
  environment:
    OPENAI_API_KEY: ${env:OPENAI_API_KEY}
    API_SECRET_KEY: ${env:API_SECRET_KEY}
    STAGE: ${self:provider.stage}
```

### **CORS Configuration:**

```yaml
# Already configured for your frontend
allow_origins:
  - http://localhost:3000
  - https://yourdomain.com
```

---

## 📊 **Monitoring & Logging**

### **View Logs:**

```bash
# Real-time logs
sls logs -f healthcareApi --stage dev --tail

# Historical logs
sls logs -f healthcareApi --stage dev --startTime 1h
```

### **CloudWatch Dashboard:**

- Go to AWS Console → CloudWatch
- Find log group: `/aws/lambda/healthcare-ai-dev`

### **Performance Monitoring:**

```bash
# Function metrics
aws cloudwatch get-metric-statistics \
  --namespace AWS/Lambda \
  --metric-name Duration \
  --dimensions Name=FunctionName,Value=healthcare-ai-dev
```

---

## 🚀 **Scaling Configuration**

### **Concurrent Executions:**

```yaml
# serverless.yml
provider:
  reservedConcurrency: 100 # Max concurrent executions

functions:
  healthcareApi:
    reservedConcurrency: 50 # Per function limit
```

### **Auto-scaling Settings:**

```yaml
# API Gateway throttling
custom:
  apiGatewayThrottling:
    maxRequestsPerSecond: 1000
    maxConcurrentRequests: 500
```

---

## 💰 **Cost Optimization**

### **1. Layer Optimization:**

```yaml
# Large dependencies in layers
custom:
  pythonRequirements:
    layer: true # Reduces deployment size
    slim: true # Remove unnecessary files
```

### **2. Memory Optimization:**

```yaml
# Right-size your functions
functions:
  clinicalChat:
    memorySize: 512 # Lightweight text processing
  organAnalyzer:
    memorySize: 2048 # Heavy image processing
```

### **3. Warmup Configuration:**

```yaml
# Prevent cold starts (costs ~$1/month)
custom:
  warmup:
    enabled: true
    prewarm: true
```

---

## 🔒 **Security Best Practices**

### **1. API Key Authentication:**

```python
# Already implemented in lambda_handler.py
headers = event.get('headers', {})
api_key = headers.get('Authorization', '').replace('Bearer ', '')
```

### **2. Environment Security:**

```bash
# Never commit these files
echo ".env" >> .gitignore
echo "config/config.json" >> .gitignore
```

### **3. IAM Permissions:**

```yaml
# Minimal IAM permissions in serverless.yml
provider:
  iam:
    role:
      statements:
        - Effect: Allow
          Action: s3:GetObject
          Resource: "arn:aws:s3:::healthcare-ai-storage-${self:provider.stage}/*"
```

---

## 🧪 **Testing**

### **Local Testing:**

```bash
# Run FastAPI locally
python main.py

# Test with serverless-offline
npm install serverless-offline
sls offline start
```

### **Lambda Testing:**

```bash
# Invoke specific function
sls invoke -f healthcareApi --stage dev --data '{"body": "{\"test\": true}"}'

# Test HTTP endpoint
curl -X POST https://your-api-gateway-url.amazonaws.com/dev/clinical_chat \
  -H "Content-Type: application/json" \
  -d '{"user_message": "Hello"}'
```

---

## 📦 **Deployment Commands**

### **Common Operations:**

```bash
# Deploy everything
sls deploy --stage prod

# Deploy single function
sls deploy function -f healthcareApi --stage prod

# Update environment variables only
sls deploy --stage prod --force

# View deployment info
sls info --stage prod

# Remove deployment
sls remove --stage prod
```

### **Stage Management:**

```bash
# Deploy to different environments
sls deploy --stage dev     # Development
sls deploy --stage staging # Staging
sls deploy --stage prod    # Production
```

---

## 🔧 **Troubleshooting**

### **Common Issues:**

**1. Package Size Too Large:**

```bash
# Solution: Use layers for large dependencies
custom:
  pythonRequirements:
    layer: true
    slim: true
    noDeploy:
      - boto3      # Already available in Lambda
      - botocore
```

**2. Cold Start Issues:**

```bash
# Solution: Enable warmup
custom:
  warmup:
    enabled: true
```

**3. Memory/Timeout Errors:**

```yaml
# Solution: Increase limits
functions:
  healthcareApi:
    memorySize: 2048
    timeout: 900 # 15 minutes max
```

**4. CORS Errors:**

```yaml
# Solution: Check CORS configuration
allow_origins: ["https://yourfrontend.com"]
```

### **Debug Commands:**

```bash
# Check function logs
sls logs -f healthcareApi --stage dev --tail

# Test function locally
sls invoke local -f healthcareApi --data '{"test": true}'

# Check CloudFormation stack
aws cloudformation describe-stacks --stack-name healthcare-ai-backend-dev
```

---

## 🌐 **Custom Domain Setup**

### **1. Configure Domain:**

```yaml
# serverless.yml
custom:
  customDomain:
    domainName: api.yourdomain.com
    certificateName: "*.yourdomain.com"
    createRoute53Record: true
```

### **2. Deploy Domain:**

```bash
sls create_domain --stage prod
sls deploy --stage prod
```

---

## 📈 **Production Checklist**

- [ ] Environment variables configured
- [ ] Custom domain setup
- [ ] SSL certificate configured
- [ ] API authentication enabled
- [ ] Rate limiting configured
- [ ] Monitoring & alerts setup
- [ ] Backup strategy defined
- [ ] Cost monitoring enabled
- [ ] Security audit completed
- [ ] Load testing performed

---

## 🎯 **Next Steps**

1. **Deploy to Development:** `./deploy.sh dev`
2. **Test All Endpoints:** Use the API Gateway URL
3. **Update Frontend:** Point to new Lambda URL
4. **Monitor Performance:** Check CloudWatch metrics
5. **Plan Production:** Review security & scaling
6. **Setup CI/CD:** Automate deployments

---

## 📞 **Support**

**Useful Resources:**

- [Serverless Framework Docs](https://www.serverless.com/framework/docs/)
- [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/)
- [FastAPI with Lambda](https://mangum.io/)

**Common Commands Reference:**

```bash
# View all available commands
sls --help

# Plugin specific help
sls create_domain --help
sls warmup --help
```

🎉 **Your Healthcare AI Backend is now ready for serverless deployment!**
