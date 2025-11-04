🔧 Healthcare App - Troubleshooting Guide

## 🚨 Current Issue: {"detail":"Not Found"}

This error means you're accessing a URL that doesn't exist. Let me help you fix this!

## ✅ Step 1: Make Sure Both Services Are Running

### Backend Check:

Open PowerShell #1 and run:

```cmd
python main.py
```

You should see: "Uvicorn running on http://0.0.0.0:8000"

### Frontend Check:

Open PowerShell #2 and run:

```cmd
python web_app.py
```

You should see: "Uvicorn running on http://0.0.0.0:3000"

## 🌐 Step 2: Test These EXACT URLs

### ✅ CORRECT URLs (should work):

- http://localhost:3000/ ← Homepage
- http://localhost:3000/clinical-chat ← Clinical Chat
- http://localhost:3000/document-analyzer ← Document Analyzer
- http://localhost:3000/speech-to-text ← Speech to Text
- http://localhost:3000/text-to-speech ← Text to Speech
- http://localhost:3000/organ-analyzer ← Organ Analyzer

### ❌ WRONG URLs (will show "Not Found"):

- http://localhost:8000/ ← Backend only (no pages)
- http://localhost:3000/clinical_chat ← Wrong (underscore)
- http://localhost:3000/docs ← Wrong port
- http://localhost:8000/clinical-chat ← Wrong port

## 🧪 Step 3: Quick Test

1. Make sure BOTH PowerShell windows are running
2. Open browser to: http://localhost:3000/
3. You should see the homepage, not an error

## 🔍 Step 4: If Still Getting "Not Found"

### Check What You're Accessing:

- Are you going to http://localhost:3000/ (correct)?
- Or http://localhost:8000/ (wrong - this is backend only)?

### Check Services:

Run in a new PowerShell:

```cmd
netstat -ano | findstr ":3000"
netstat -ano | findstr ":8000"
```

Both should show LISTENING processes.

## 🎯 Most Common Causes:

1. **Wrong URL**: Using port 8000 instead of 3000
2. **Services Not Running**: One or both stopped
3. **Wrong Path**: Using underscores instead of hyphens
4. **Cache Issue**: Browser cached old error

## ✅ Quick Fix Commands:

```cmd
# Kill any stuck processes
taskkill /f /im python.exe

# Restart backend (PowerShell #1)
cd C:\work\si-ai-tool-backend
python main.py

# Restart frontend (PowerShell #2)
cd C:\work\si-ai-tool-backend
python web_app.py

# Test in browser
# Go to: http://localhost:3000/
```

## 📞 Tell me:

1. What exact URL are you trying to access?
2. Are both PowerShell windows still showing "Uvicorn running"?
3. What do you see when you go to http://localhost:3000/ ?
