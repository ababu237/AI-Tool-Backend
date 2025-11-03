# Healthcare Backend APIs - Complete Contract Documentation

## 📋 **OVERVIEW**

This document provides a comprehensive contract for the 6 healthcare backend APIs built with FastAPI. Each API serves specific medical and healthcare data processing functions with multi-language support and audio output capabilities.

### **System Architecture**

- **Framework**: FastAPI with Python 3.9+
- **AI Integration**: OpenAI GPT-4.0-turbo, Whisper
- **Machine Learning**: PyTorch, TorchVision (ResNet50, InceptionV3)
- **Multi-language**: Google Translator, Language Detection
- **Audio**: Text-to-Speech (gTTS)
- **Data Processing**: Pandas, LangChain, FAISS Vector Search

---

## 🏥 **API 1: CLINICAL CHAT API**

### **Purpose**

AI-powered medical consultation assistant providing healthcare advice with multi-language support.

### **Base URL**: `http://localhost:8001`

### **Key Features**

- Medical query processing with OpenAI GPT-4.0
- Multi-language input/output translation
- Text-to-speech audio responses
- Conversation history tracking
- CORS enabled for web integration

### **Endpoints**

#### **1. Medical Consultation**

```http
POST /clinical_chat
```

**Input Parameters (Form Data)**:

```json
{
  "query": "string (required) - Medical question or symptom description",
  "output_language": "string (required) - Target language code (e.g., 'en', 'es', 'fr')"
}
```

**Example Input**:

```json
{
  "query": "What are the symptoms of diabetes?",
  "output_language": "en"
}
```

**Output Response**:

```json
{
  "question": "What are the symptoms of diabetes?",
  "translated_response": "Common symptoms of diabetes include increased thirst, frequent urination, fatigue, blurred vision, and unexplained weight loss. If you experience these symptoms, please consult a healthcare professional.",
  "audio_url": "/get_audio/audio_12345.mp3",
  "conversation_history": [
    {
      "question": "What are the symptoms of diabetes?",
      "answer": "Common symptoms of diabetes include...",
      "audio_url": "/get_audio/audio_12345.mp3"
    }
  ]
}
```

#### **2. Audio File Retrieval**

```http
GET /get_audio/{filename}
```

**Response**: Audio file (MP3 format)

---

## 📄 **API 2: DOCUMENT PROCESSING API**

### **Purpose**

PDF document analysis with AI-powered Q&A capabilities and multi-language support.

### **Base URL**: `http://localhost:8003`

### **Key Features**

- PDF text extraction and processing
- Vector-based document search (FAISS)
- Multi-language Q&A with OpenAI
- Conversation history for follow-up questions
- File ID system for subsequent queries

### **Endpoints**

#### **1. Document Processing & Q&A**

```http
POST /process_document
```

**Input Parameters (Multipart Form)**:

```json
{
  "file": "file (optional) - PDF document (for initial upload)",
  "file_id": "string (optional) - File ID for follow-up questions",
  "question": "string (required) - Question about the document",
  "output_language": "string (optional, default: 'en') - Response language"
}
```

**Example Input (Initial Upload)**:

```json
{
  "file": "[PDF FILE]",
  "question": "What is the main topic of this document?",
  "output_language": "en"
}
```

**Example Input (Follow-up Question)**:

```json
{
  "file_id": "abc123-def456-ghi789",
  "question": "What are the key recommendations?",
  "output_language": "es"
}
```

**Output Response**:

```json
{
  "response": "The main topic of this document is healthcare data management and patient privacy protocols.",
  "audio_url": "/audio/response_67890.mp3",
  "conversation_history": [
    {
      "question": "What is the main topic of this document?",
      "answer": "The main topic of this document is healthcare data management..."
    }
  ],
  "file_id": "abc123-def456-ghi789"
}
```

#### **2. Test Endpoint**

```http
POST /test_document
```

**Input Parameters**:

```json
{
  "test_query": "string (optional, default: 'What is this API for?')",
  "output_language": "string (optional, default: 'en')"
}
```

---

## 📊 **API 3: CSV FILE PROCESSING API**

### **Purpose**

CSV data analysis with AI-powered insights, translations, and conversational data exploration.

### **Base URL**: `http://localhost:8002`

### **Key Features**

- CSV data upload and processing
- AI-powered data analysis with LangChain
- Multi-language data translation
- Conversational data exploration
- File ID system for continued analysis

### **Endpoints**

#### **1. CSV Processing & Analysis**

```http
POST /process_csv
```

**Input Parameters (Multipart Form)**:

```json
{
  "file": "file (optional) - CSV file for initial upload",
  "file_id": "string (optional) - File ID for subsequent questions",
  "question": "string (required) - Question about the CSV data",
  "output_language": "string (optional, default: 'en') - Response language"
}
```

**Example Input (Initial Upload)**:

```json
{
  "file": "[CSV FILE]",
  "question": "What are the main trends in this data?",
  "output_language": "en"
}
```

**Example Input (Follow-up Analysis)**:

```json
{
  "file_id": "csv_789xyz",
  "question": "Show me the correlation between age and blood pressure",
  "output_language": "fr"
}
```

**Output Response**:

```json
{
  "response": "Based on the analysis, there's a positive correlation between age and blood pressure in your dataset. The correlation coefficient is 0.73, indicating a strong relationship.",
  "audio_url": "/audio/test_csv_12345.mp3",
  "insights": {
    "analysis_type": "correlation_analysis",
    "correlation_coefficient": 0.73,
    "statistical_significance": "p < 0.001"
  },
  "conversation_history": [
    {
      "question": "What are the main trends in this data?",
      "answer": "The data shows several interesting trends..."
    }
  ]
}
```

#### **2. Test CSV Endpoint**

```http
POST /test_csv
```

**Input Parameters**:

```json
{
  "test_question": "string (optional, default: 'What insights can you provide?')",
  "output_language": "string (optional, default: 'en')"
}
```

---

## 🫁 **API 4: ORGAN ANALYZER API**

### **Purpose**

Medical image analysis using multiple AI models for organ scan interpretation.

### **Base URL**: `http://localhost:8004`

### **Key Features**

- Multi-model AI analysis (ResNet50, InceptionV3, VGG16, EfficientNet)
- Medical image classification (Normal/Abnormal)
- Organ-specific model selection
- Confidence scoring and model comparison
- Medical recommendations with OpenAI integration
- Multi-language support for medical reports

### **Endpoints**

#### **1. Organ Scan Analysis**

```http
POST /analyze_organ_scan
```

**Input Parameters (Multipart Form)**:

```json
{
  "image": "file (required) - Medical scan image (JPEG, PNG)",
  "organ": "string (required) - Organ type ('lung', 'heart', 'brain', etc.)",
  "input_language": "string (required) - Input language code",
  "output_language": "string (required) - Output language code"
}
```

**Example Input**:

```json
{
  "image": "[MEDICAL_SCAN_IMAGE.jpg]",
  "organ": "lung",
  "input_language": "en",
  "output_language": "es"
}
```

**Output Response**:

```json
{
  "organ": "lung",
  "diagnosis": "Normal",
  "model_used": "ResNet50",
  "confidence_score": 0.87,
  "recommendations": {
    "explanation": "El análisis muestra tejido pulmonar normal sin anomalías detectables.",
    "risks": "No se detectaron riesgos significativos en esta exploración.",
    "dietary_suggestions": "Mantener una dieta equilibrada rica en antioxidantes.",
    "medications": "Siga las prescripciones de su médico.",
    "exercises": "Ejercicio regular recomendado por profesional sanitario.",
    "precautions": "Revisiones médicas regulares recomendadas."
  },
  "audio_url": "/get_audio/audio_98765.mp3"
}
```

#### **2. Test Organ Analyzer**

```http
POST /test_organ_analyzer
```

**Input Parameters**:

```json
{
  "organ": "string (optional, default: 'lung')",
  "input_language": "string (optional, default: 'en')",
  "output_language": "string (optional, default: 'en')"
}
```

---

## 🎤 **API 5: TRANSCRIPTION API**

### **Purpose**

Audio transcription using OpenAI Whisper with translation and text-to-speech capabilities.

### **Base URL**: `http://localhost:8005`

### **Key Features**

- Audio file transcription with OpenAI Whisper
- Automatic language detection
- Multi-language translation
- Text-to-speech output generation
- Multiple audio format support

### **Endpoints**

#### **1. Audio Transcription**

```http
POST /transcribe_audio
```

**Input Parameters (Multipart Form)**:

```json
{
  "audio_file": "file (required) - Audio file (MP3, WAV, FLAC, OGG)",
  "output_language": "string (optional, default: 'en') - Target language for translation"
}
```

**Example Input**:

```json
{
  "audio_file": "[AUDIO_FILE.mp3]",
  "output_language": "fr"
}
```

**Output Response**:

```json
{
  "original_text": "Hello, I would like to schedule an appointment with my doctor.",
  "translated_text": "Bonjour, j'aimerais prendre rendez-vous avec mon médecin.",
  "detected_language": "en",
  "target_language": "fr",
  "audio_url": "/get_audio/test_transcription_54321.mp3",
  "processing_time": "2.3 seconds"
}
```

#### **2. Test Transcription**

```http
POST /test_transcription
```

**Input Parameters**:

```json
{
  "test_text": "string (optional, default: 'Hello, this is a test transcription')",
  "output_language": "string (optional, default: 'en')"
}
```

---

## 🌐 **API 6: TRANSLATE TEXT API**

### **Purpose**

Multi-language text translation with text-to-speech audio generation.

### **Base URL**: `http://localhost:8006`

### **Key Features**

- Multi-language text translation
- Automatic source language detection
- Text-to-speech audio generation
- Simple and fast translation service
- Support for 100+ languages

### **Endpoints**

#### **1. Text Translation**

```http
POST /translate_text
```

**Input Parameters (Form Data)**:

```json
{
  "text": "string (required) - Text to translate",
  "output_language": "string (required) - Target language code"
}
```

**Example Input**:

```json
{
  "text": "Good morning, how are you feeling today?",
  "output_language": "es"
}
```

**Output Response**:

```json
{
  "original_text": "Good morning, how are you feeling today?",
  "translated_text": "Buenos días, ¿cómo te sientes hoy?",
  "source_language": "en",
  "target_language": "es",
  "audio_url": "/get_audio/translate_11111.mp3"
}
```

#### **2. Audio File Retrieval**

```http
GET /get_audio/{filename}
```

**Response**: Audio file (MP3 format)

---

## 🔧 **COMMON CONFIGURATIONS**

### **Environment Setup**

```json
{
  "config_file": "config/config.json",
  "required_keys": {
    "OPENAI_API_KEY": "Your OpenAI API key for GPT and Whisper",
    "TRANSLATION_API_KEY": "Optional: Custom translation service key"
  }
}
```

### **CORS Configuration**

All APIs support CORS with origins:

- `http://localhost:3000`
- `http://127.0.0.1:3000`

### **Error Handling**

Standard HTTP status codes:

- `200`: Success
- `400`: Bad Request (invalid parameters)
- `404`: Not Found (file/resource not found)
- `422`: Validation Error (missing required fields)
- `500`: Internal Server Error

### **Audio File Management**

- **Format**: MP3
- **Storage**: Temporary local storage
- **Cleanup**: Automatic background cleanup
- **Access**: Via `/get_audio/{filename}` endpoint

---

## 📝 **USAGE EXAMPLES**

### **Multi-Step Workflow Example**

1. **Upload medical document** (Document API)
2. **Analyze patient data** (CSV API)
3. **Process medical images** (Organ Analyzer API)
4. **Transcribe audio notes** (Transcription API)
5. **Translate reports** (Translate API)
6. **Get medical advice** (Clinical Chat API)

### **Integration Example**

```python
import requests

# Step 1: Upload and analyze document
doc_response = requests.post("http://localhost:8003/process_document",
    files={"file": open("patient_report.pdf", "rb")},
    data={"question": "What are the patient's vital signs?", "output_language": "en"})

# Step 2: Get medical consultation
chat_response = requests.post("http://localhost:8001/clinical_chat",
    data={"query": "Explain these vital signs", "output_language": "es"})

# Step 3: Translate for patient
translate_response = requests.post("http://localhost:8006/translate_text",
    data={"text": chat_response.json()["translated_response"], "output_language": "fr"})
```

---

## 🚀 **DEPLOYMENT**

### **Individual API Startup**

```bash
# Clinical Chat API
python backend_api/clinical_chat_api.py  # Port 8001

# CSV File API
python backend_api/csv_file_api.py       # Port 8002

# Document API
python backend_api/document_api.py       # Port 8003

# Organ Analyzer API
python backend_api/organ_analyzer_api.py # Port 8004

# Transcription API
python backend_api/transcription_api.py  # Port 8005

# Translate Text API
python backend_api/translate_text_api.py # Port 8006
```

### **API Documentation**

Each API provides interactive documentation at:

- `http://localhost:[PORT]/docs` (Swagger UI)
- `http://localhost:[PORT]/redoc` (ReDoc)

---

## ⚡ **PERFORMANCE & LIMITATIONS**

### **Current Test Coverage**

- **Overall**: 89% code coverage
- **Perfect Coverage**: translate_text_api (100%), transcription_api (100%)
- **High Coverage**: clinical_chat_api (94%), csv_file_api (91%)
- **Good Coverage**: document_api (85%), organ_analyzer_api (84%)

### **Rate Limits**

- OpenAI API: Subject to your OpenAI account limits
- Google Translate: Rate limited by Google's free tier
- File Upload: Max file size varies by API

### **Supported File Formats**

- **Images**: JPEG, PNG (Organ Analyzer)
- **Documents**: PDF (Document API)
- **Data**: CSV (CSV API)
- **Audio**: MP3, WAV, FLAC, OGG (Transcription API)

---

## 📞 **SUPPORT & CONTACT**

This comprehensive contract covers all functionality, input/output formats, and usage patterns for the healthcare backend API suite. Each API is designed for integration into larger healthcare applications with consistent patterns and multi-language support.

**Last Updated**: September 30, 2025
**API Version**: 1.0.0
**Coverage**: 89% (752 total statements tested)
