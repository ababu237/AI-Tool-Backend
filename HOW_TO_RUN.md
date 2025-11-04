# 🏥 Healthcare Web Application - Quick Start Guide

## 🚀 **How to Run Your Complete Healthcare App**

### **✅ Method 1: Two Terminal Windows (Recommended)**

**Step 1 - Start Backend:**

```cmd
# Open Terminal/Command Prompt
# Navigate to your project folder
cd C:\work\si-ai-tool-backend

# Start backend APIs
python main.py
```

_Keep this terminal window open!_

**Step 2 - Start Frontend:**

```cmd
# Open NEW Terminal/Command Prompt
# Navigate to your project folder
cd C:\work\si-ai-tool-backend

# Start frontend web app
python web_app.py
```

_Keep this terminal window open too!_

**Step 3 - Use Your App:**
Open browser to: **http://localhost:3000**

---

### **✅ Method 2: Using Batch Files (Windows)**

**Step 1:** Double-click `start_backend.bat`
**Step 2:** Double-click `start_frontend.bat`  
**Step 3:** Open browser to: **http://localhost:3000**

---

## 🌐 **Your Complete Healthcare Application**

### **📋 Available Features:**

| **Page**              | **URL**                                 | **What It Does**                   |
| --------------------- | --------------------------------------- | ---------------------------------- |
| **Homepage**          | http://localhost:3000/                  | Main dashboard                     |
| **Clinical Chat**     | http://localhost:3000/clinical-chat     | AI medical chat with OpenAI        |
| **Document Analyzer** | http://localhost:3000/document-analyzer | Upload & analyze medical documents |
| **Speech-to-Text**    | http://localhost:3000/speech-to-text    | Convert audio to text              |
| **Text-to-Speech**    | http://localhost:3000/text-to-speech    | Convert text to audio              |
| **Organ Analyzer**    | http://localhost:3000/organ-analyzer    | Analyze medical images             |

---

## ✅ **What You Get:**

### **🔥 Real AI Integration:**

- ✅ **OpenAI GPT** for clinical chat
- ✅ **Whisper API** for audio transcription
- ✅ **Real document analysis**
- ✅ **Automatic audio playback**
- ✅ **File upload capabilities**

### **💎 Professional Features:**

- ✅ **Loading spinners** during processing
- ✅ **Error handling** with user-friendly messages
- ✅ **Success notifications**
- ✅ **Mobile responsive design**
- ✅ **No CORS issues** (single-port architecture)
- ✅ **Session management**

---

## 🛠️ **Troubleshooting**

### **❌ Common Issues:**

**"Port already in use"**

- Close any other applications using ports 8000 or 3000
- Or restart your computer

**"Cannot connect to backend"**

- Make sure `python main.py` is running first
- Check that both terminals are still open

**"Module not found"**

- Run: `pip install -r requirements.txt`

**"OpenAI API error"**

- Check your OpenAI API key in `config/config.json`

---

## 🎯 **Testing Your App**

### **1. Clinical Chat Test:**

1. Go to http://localhost:3000/clinical-chat
2. Type: "What are the symptoms of diabetes?"
3. Should get real AI response + audio

### **2. Document Test:**

1. Go to http://localhost:3000/document-analyzer
2. Upload a PDF file
3. Ask a question about it
4. Should get real analysis

### **3. Audio Test:**

1. Go to http://localhost:3000/speech-to-text
2. Upload an audio file
3. Should get transcription + audio response

---

## 🎉 **Success Indicators**

✅ **Your app is working if:**

- Both terminals show "Uvicorn running" messages
- Browser opens to http://localhost:3000
- Pages load without errors
- API calls show loading spinners
- You get real responses (not "simulated")
- Audio files play automatically

---

## 📞 **Need Help?**

**Check the logs in both terminal windows for error messages.**

**Common URLs:**

- **Main App:** http://localhost:3000
- **API Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:3000/api/health

---

## 🚀 **You're All Set!**

**Your healthcare web application is now a complete, professional system with:**

- 🏥 AI-powered medical chat
- 📄 Document analysis
- 🎤 Audio transcription
- 🔊 Text-to-speech
- 🩻 Medical image analysis
- 📊 CSV processing

**Just run the two commands and start using your app!** 🎉
