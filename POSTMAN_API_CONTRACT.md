# 🏥 Healthcare Backend APIs - Postman-Style Contract

## 📋 **OVERVIEW**

Complete API documentation with Postman-style request/response examples for 6 healthcare backend APIs. Each API includes detailed curl commands, request formats, and actual response examples.

---

## 🏥 **API 1: CLINICAL CHAT API**

**Base URL**: `http://localhost:8001`  
**Purpose**: AI-powered medical consultation assistant

### **Endpoint: Medical Consultation**

#### **Request Details**

```
POST /clinical_chat
Content-Type: multipart/form-data
```

#### **Postman Setup**

- **Method**: POST
- **URL**: `http://localhost:8001/clinical_chat`
- **Body Type**: form-data
- **Headers**: `Content-Type: multipart/form-data`

#### **Request Parameters**

| Parameter       | Type   | Required | Description                                 |
| --------------- | ------ | -------- | ------------------------------------------- |
| query           | string | Yes      | Medical question or symptom description     |
| output_language | string | Yes      | Target language code (en, es, fr, de, etc.) |

#### **Example Request (Postman Body - form-data)**

```
Key: query
Value: What are the common symptoms of high blood pressure?

Key: output_language
Value: en
```

#### **cURL Example**

```bash
curl -X POST "http://localhost:8001/clinical_chat" \
  -H "Content-Type: multipart/form-data" \
  -F "query=What are the common symptoms of high blood pressure?" \
  -F "output_language=en"
```

#### **Response Example (200 OK)**

```json
{
  "question": "What are the common symptoms of high blood pressure?",
  "translated_response": "Common symptoms of high blood pressure include headaches, shortness of breath, dizziness, chest pain, visual changes, and blood in urine. However, high blood pressure often has no symptoms, which is why it's called the 'silent killer.' Regular monitoring is essential.",
  "audio_url": "/get_audio/audio_4f8b2c1a-9e3d-4b2c-8a1f-2d3e4f5a6b7c.mp3",
  "conversation_history": [
    {
      "question": "What are the common symptoms of high blood pressure?",
      "answer": "Common symptoms of high blood pressure include headaches, shortness of breath...",
      "audio_url": "/get_audio/audio_4f8b2c1a-9e3d-4b2c-8a1f-2d3e4f5a6b7c.mp3"
    }
  ]
}
```

#### **Example Request in Spanish**

```bash
curl -X POST "http://localhost:8001/clinical_chat" \
  -F "query=¿Cuáles son los síntomas de la diabetes?" \
  -F "output_language=es"
```

#### **Response Example (Spanish)**

```json
{
  "question": "¿Cuáles son los síntomas de la diabetes?",
  "translated_response": "Los síntomas comunes de la diabetes incluyen sed excesiva, micción frecuente, fatiga, visión borrosa, pérdida de peso inexplicable y heridas que sanan lentamente. Si experimenta estos síntomas, consulte a un profesional de la salud.",
  "audio_url": "/get_audio/audio_7a9b3c2d-1e4f-5g6h-7i8j-9k0l1m2n3o4p.mp3",
  "conversation_history": [...]
}
```

---

## 📄 **API 2: DOCUMENT PROCESSING API**

**Base URL**: `http://localhost:8003`  
**Purpose**: PDF document analysis and Q&A

### **Endpoint: Process Document**

#### **Request Details**

```
POST /process_document
Content-Type: multipart/form-data
```

#### **Postman Setup - Initial Document Upload**

- **Method**: POST
- **URL**: `http://localhost:8003/process_document`
- **Body Type**: form-data

#### **Request Parameters (Initial Upload)**

| Parameter       | Type   | Required | Description                     |
| --------------- | ------ | -------- | ------------------------------- |
| file            | file   | Yes      | PDF document to analyze         |
| question        | string | Yes      | Question about the document     |
| output_language | string | No       | Response language (default: en) |

#### **Example Request (Postman Body - form-data)**

```
Key: file
Value: [SELECT FILE] medical_report.pdf

Key: question
Value: What are the patient's vital signs mentioned in this report?

Key: output_language
Value: en
```

#### **cURL Example (Initial Upload)**

```bash
curl -X POST "http://localhost:8003/process_document" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/medical_report.pdf" \
  -F "question=What are the patient's vital signs mentioned in this report?" \
  -F "output_language=en"
```

#### **Response Example (Initial Upload)**

```json
{
  "response": "Based on the medical report, the patient's vital signs are: Blood Pressure: 140/90 mmHg (elevated), Heart Rate: 88 bpm (normal), Temperature: 98.6°F (normal), Respiratory Rate: 16 breaths/min (normal), Oxygen Saturation: 97% (normal). The elevated blood pressure requires monitoring.",
  "audio_url": "/audio/response_8c7b6a5d-4e3f-2g1h-9i0j-1k2l3m4n5o6p.mp3",
  "conversation_history": [
    {
      "question": "What are the patient's vital signs mentioned in this report?",
      "answer": "Based on the medical report, the patient's vital signs are..."
    }
  ],
  "file_id": "doc_abc123def456ghi789"
}
```

#### **Follow-up Question Request**

```
Key: file_id
Value: doc_abc123def456ghi789

Key: question
Value: What medications are prescribed?

Key: output_language
Value: en
```

#### **cURL Example (Follow-up)**

```bash
curl -X POST "http://localhost:8003/process_document" \
  -F "file_id=doc_abc123def456ghi789" \
  -F "question=What medications are prescribed?" \
  -F "output_language=en"
```

#### **Response Example (Follow-up)**

```json
{
  "response": "The prescribed medications include: Lisinopril 10mg daily for blood pressure management, Metformin 500mg twice daily for diabetes control, and Atorvastatin 20mg daily for cholesterol management. All medications should be taken as directed.",
  "audio_url": "/audio/followup_9d8c7b6a-5e4f-3g2h-1i0j-2k3l4m5n6o7p.mp3",
  "conversation_history": [
    {
      "question": "What are the patient's vital signs mentioned in this report?",
      "answer": "Based on the medical report, the patient's vital signs are..."
    },
    {
      "question": "What medications are prescribed?",
      "answer": "The prescribed medications include: Lisinopril 10mg daily..."
    }
  ]
}
```

---

## 📊 **API 3: CSV FILE PROCESSING API**

**Base URL**: `http://localhost:8002`  
**Purpose**: CSV data analysis with AI insights

### **Endpoint: Process CSV**

#### **Request Details**

```
POST /process_csv
Content-Type: multipart/form-data
```

#### **Postman Setup**

- **Method**: POST
- **URL**: `http://localhost:8002/process_csv`
- **Body Type**: form-data

#### **Request Parameters (Initial Upload)**

| Parameter       | Type   | Required | Description                     |
| --------------- | ------ | -------- | ------------------------------- |
| file            | file   | Yes      | CSV file to analyze             |
| question        | string | Yes      | Question about the data         |
| output_language | string | No       | Response language (default: en) |

#### **Example Request (Postman Body - form-data)**

```
Key: file
Value: [SELECT FILE] patient_data.csv

Key: question
Value: What is the average age of patients in this dataset?

Key: output_language
Value: en
```

#### **Sample CSV Data (patient_data.csv)**

```csv
patient_id,age,gender,blood_pressure,heart_rate,diagnosis
P001,45,M,140/90,88,Hypertension
P002,32,F,120/80,72,Normal
P003,67,M,150/95,94,Hypertension
P004,28,F,110/70,68,Normal
P005,55,M,135/85,82,Pre-hypertension
```

#### **cURL Example**

```bash
curl -X POST "http://localhost:8002/process_csv" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/patient_data.csv" \
  -F "question=What is the average age of patients in this dataset?" \
  -F "output_language=en"
```

#### **Response Example**

```json
{
  "response": "Based on the analysis of the patient dataset, the average age is 45.4 years. The dataset contains 5 patients with ages ranging from 28 to 67 years. The age distribution shows: 2 patients in their 20s-30s, 2 patients in their 40s-50s, and 1 patient in their 60s.",
  "audio_url": "/audio/test_csv_6e5d4c3b-2a1f-9g8h-7i6j-5k4l3m2n1o0p.mp3",
  "insights": {
    "analysis_type": "statistical_summary",
    "total_patients": 5,
    "average_age": 45.4,
    "age_range": "28-67",
    "gender_distribution": { "M": 3, "F": 2 }
  },
  "conversation_history": [
    {
      "question": "What is the average age of patients in this dataset?",
      "answer": "Based on the analysis of the patient dataset, the average age is 45.4 years..."
    }
  ]
}
```

#### **Follow-up Analysis Request**

```bash
curl -X POST "http://localhost:8002/process_csv" \
  -F "file_id=csv_xyz789abc123" \
  -F "question=Show correlation between age and blood pressure" \
  -F "output_language=en"
```

#### **Follow-up Response Example**

```json
{
  "response": "There is a positive correlation between age and blood pressure in this dataset. The correlation coefficient is 0.78, indicating a strong relationship. Patients over 50 show consistently higher blood pressure readings (average 142/87 mmHg) compared to patients under 40 (average 115/75 mmHg).",
  "audio_url": "/audio/correlation_analysis_5f4e3d2c-1b0a-8g7h-6i5j-4k3l2m1n0o9p.mp3",
  "insights": {
    "analysis_type": "correlation_analysis",
    "correlation_coefficient": 0.78,
    "statistical_significance": "p < 0.05",
    "age_groups": {
      "under_40": { "avg_bp": "115/75", "count": 2 },
      "over_50": { "avg_bp": "142/87", "count": 2 }
    }
  }
}
```

---

## 🫁 **API 4: ORGAN ANALYZER API**

**Base URL**: `http://localhost:8004`  
**Purpose**: Medical image analysis using AI models

### **Endpoint: Analyze Organ Scan**

#### **Request Details**

```
POST /analyze_organ_scan
Content-Type: multipart/form-data
```

#### **Postman Setup**

- **Method**: POST
- **URL**: `http://localhost:8004/analyze_organ_scan`
- **Body Type**: form-data

#### **Request Parameters**

| Parameter       | Type   | Required | Description                           |
| --------------- | ------ | -------- | ------------------------------------- |
| image           | file   | Yes      | Medical scan image (JPEG, PNG)        |
| organ           | string | Yes      | Organ type (lung, heart, brain, etc.) |
| input_language  | string | Yes      | Input language code                   |
| output_language | string | Yes      | Output language code                  |

#### **Example Request (Postman Body - form-data)**

```
Key: image
Value: [SELECT FILE] lung_xray.jpg

Key: organ
Value: lung

Key: input_language
Value: en

Key: output_language
Value: en
```

#### **cURL Example**

```bash
curl -X POST "http://localhost:8004/analyze_organ_scan" \
  -H "Content-Type: multipart/form-data" \
  -F "image=@/path/to/lung_xray.jpg" \
  -F "organ=lung" \
  -F "input_language=en" \
  -F "output_language=en"
```

#### **Response Example (Normal Result)**

```json
{
  "organ": "lung",
  "diagnosis": "Normal",
  "model_used": "ResNet50",
  "confidence_score": 0.87,
  "recommendations": {
    "explanation": "The lung scan analysis shows normal tissue structure with no detectable abnormalities. The AI model confidence is high at 87%.",
    "risks": "No significant risks detected in this scan. Continue regular health maintenance.",
    "dietary_suggestions": "Maintain a diet rich in antioxidants including berries, leafy greens, and fish. Avoid processed foods and excessive sodium.",
    "medications": "No medications indicated based on this normal scan. Follow your doctor's existing prescriptions.",
    "exercises": "Regular cardiovascular exercise recommended: 30 minutes of moderate activity 5 times per week. Include breathing exercises.",
    "precautions": "Regular medical check-ups recommended. Avoid smoking and secondhand smoke exposure. Monitor for any respiratory symptoms."
  },
  "audio_url": "/get_audio/audio_3e2d1c0b-9a8f-7g6h-5i4j-3k2l1m0n9o8p.mp3"
}
```

#### **Example Request (Spanish Output)**

```bash
curl -X POST "http://localhost:8004/analyze_organ_scan" \
  -F "image=@/path/to/heart_scan.jpg" \
  -F "organ=heart" \
  -F "input_language=en" \
  -F "output_language=es"
```

#### **Response Example (Spanish, Abnormal Result)**

```json
{
  "organ": "heart",
  "diagnosis": "Abnormal",
  "model_used": "InceptionV3",
  "confidence_score": 0.92,
  "recommendations": {
    "explanation": "El análisis del corazón muestra anomalías que requieren atención médica. El modelo de IA tiene una confianza alta del 92%.",
    "risks": "Se detectaron riesgos potenciales. Consulte inmediatamente con un cardiólogo para evaluación adicional.",
    "dietary_suggestions": "Dieta baja en sodio y grasas saturadas. Incluya omega-3, frutas y verduras. Evite alimentos procesados.",
    "medications": "Siga las prescripciones de su cardiólogo. Pueden ser necesarios medicamentos para el corazón.",
    "exercises": "Ejercicio suave bajo supervisión médica. Evite actividad intensa hasta evaluación completa.",
    "precautions": "Busque atención médica inmediata. Monitoree síntomas como dolor en el pecho, dificultad para respirar o mareos."
  },
  "audio_url": "/get_audio/audio_7b6a5d4c-3e2f-1g0h-9i8j-7k6l5m4n3o2p.mp3"
}
```

### **Test Endpoint**

#### **Request Details**

```
POST /test_organ_analyzer
Content-Type: multipart/form-data
```

#### **Example Request**

```bash
curl -X POST "http://localhost:8004/test_organ_analyzer" \
  -F "organ=lung" \
  -F "input_language=en" \
  -F "output_language=fr"
```

#### **Test Response Example**

```json
{
  "message": "Organ Analyzer API test successful",
  "organ": "lung",
  "diagnosis": "Test Mode - Normal",
  "model_used": "Test Model",
  "confidence_score": 0.95,
  "recommendations": {
    "explanation": "Ceci est une analyse de test pour l'organe poumon",
    "risks": "Aucun risque détecté en mode test",
    "dietary_suggestions": "Maintenez une alimentation saine",
    "medications": "Aucun médicament nécessaire pour le test",
    "exercises": "Exercice régulier recommandé",
    "precautions": "Ceci est uniquement des données de test"
  },
  "audio_url": "/get_audio/test_organ_2f1e0d9c-8b7a-6g5h-4i3j-2k1l0m9n8o7p.mp3",
  "note": "This is a test endpoint. For actual organ analysis, use /analyze_organ_scan with image upload"
}
```

---

## 🎤 **API 5: TRANSCRIPTION API**

**Base URL**: `http://localhost:8005`  
**Purpose**: Audio transcription using OpenAI Whisper

### **Endpoint: Transcribe Audio**

#### **Request Details**

```
POST /transcribe_audio
Content-Type: multipart/form-data
```

#### **Postman Setup**

- **Method**: POST
- **URL**: `http://localhost:8005/transcribe_audio`
- **Body Type**: form-data

#### **Request Parameters**

| Parameter       | Type   | Required | Description                      |
| --------------- | ------ | -------- | -------------------------------- |
| audio_file      | file   | Yes      | Audio file (MP3, WAV, FLAC, OGG) |
| output_language | string | No       | Target language (default: en)    |

#### **Example Request (Postman Body - form-data)**

```
Key: audio_file
Value: [SELECT FILE] patient_consultation.mp3

Key: output_language
Value: en
```

#### **cURL Example**

```bash
curl -X POST "http://localhost:8005/transcribe_audio" \
  -H "Content-Type: multipart/form-data" \
  -F "audio_file=@/path/to/patient_consultation.mp3" \
  -F "output_language=en"
```

#### **Response Example (English Audio)**

```json
{
  "original_text": "Good morning doctor. I have been experiencing chest pain and shortness of breath for the past two days. The pain gets worse when I exercise.",
  "translated_text": "Good morning doctor. I have been experiencing chest pain and shortness of breath for the past two days. The pain gets worse when I exercise.",
  "detected_language": "en",
  "target_language": "en",
  "audio_url": "/get_audio/test_transcription_9c8b7a6d-5e4f-3g2h-1i0j-9k8l7m6n5o4p.mp3",
  "processing_time": "3.2 seconds"
}
```

#### **Example Request (Spanish Translation)**

```bash
curl -X POST "http://localhost:8005/transcribe_audio" \
  -F "audio_file=@/path/to/english_consultation.mp3" \
  -F "output_language=es"
```

#### **Response Example (Translated to Spanish)**

```json
{
  "original_text": "I need to schedule a follow-up appointment for my blood pressure medication.",
  "translated_text": "Necesito programar una cita de seguimiento para mi medicamento para la presión arterial.",
  "detected_language": "en",
  "target_language": "es",
  "audio_url": "/get_audio/transcription_8d7c6b5a-4e3f-2g1h-0i9j-8k7l6m5n4o3p.mp3",
  "processing_time": "2.8 seconds"
}
```

### **Test Endpoint**

#### **Request Details**

```
POST /test_transcription
Content-Type: multipart/form-data
```

#### **Example Request**

```bash
curl -X POST "http://localhost:8005/test_transcription" \
  -F "test_text=Patient reports mild headache and dizziness" \
  -F "output_language=fr"
```

#### **Test Response Example**

```json
{
  "message": "Transcription API test successful",
  "original_text": "Patient reports mild headache and dizziness",
  "translated_text": "Le patient signale un léger mal de tête et des vertiges",
  "source_language": "en",
  "target_language": "fr",
  "audio_url": "/get_audio/test_transcription_7e6d5c4b-3a2f-1g0h-9i8j-7k6l5m4n3o2p.mp3"
}
```

---

## 🌐 **API 6: TRANSLATE TEXT API**

**Base URL**: `http://localhost:8006`  
**Purpose**: Multi-language text translation

### **Endpoint: Translate Text**

#### **Request Details**

```
POST /translate_text
Content-Type: multipart/form-data
```

#### **Postman Setup**

- **Method**: POST
- **URL**: `http://localhost:8006/translate_text`
- **Body Type**: form-data

#### **Request Parameters**

| Parameter       | Type   | Required | Description          |
| --------------- | ------ | -------- | -------------------- |
| text            | string | Yes      | Text to translate    |
| output_language | string | Yes      | Target language code |

#### **Example Request (Postman Body - form-data)**

```
Key: text
Value: Your blood pressure is within normal range. Continue taking your medication as prescribed.

Key: output_language
Value: es
```

#### **cURL Example**

```bash
curl -X POST "http://localhost:8006/translate_text" \
  -H "Content-Type: multipart/form-data" \
  -F "text=Your blood pressure is within normal range. Continue taking your medication as prescribed." \
  -F "output_language=es"
```

#### **Response Example (English to Spanish)**

```json
{
  "original_text": "Your blood pressure is within normal range. Continue taking your medication as prescribed.",
  "translated_text": "Su presión arterial está dentro del rango normal. Continúe tomando su medicamento según lo prescrito.",
  "source_language": "en",
  "target_language": "es",
  "audio_url": "/get_audio/translate_6f5e4d3c-2b1a-0g9h-8i7j-6k5l4m3n2o1p.mp3"
}
```

#### **Example Request (French to English)**

```bash
curl -X POST "http://localhost:8006/translate_text" \
  -F "text=J'ai des douleurs abdominales depuis hier soir" \
  -F "output_language=en"
```

#### **Response Example (French to English)**

```json
{
  "original_text": "J'ai des douleurs abdominales depuis hier soir",
  "translated_text": "I have had abdominal pain since last night",
  "source_language": "fr",
  "target_language": "en",
  "audio_url": "/get_audio/translate_5e4d3c2b-1a0f-9g8h-7i6j-5k4l3m2n1o0p.mp3"
}
```

#### **Example Request (German to Italian)**

```bash
curl -X POST "http://localhost:8006/translate_text" \
  -F "text=Ich brauche einen Termin beim Kardiologen" \
  -F "output_language=it"
```

#### **Response Example (German to Italian)**

```json
{
  "original_text": "Ich brauche einen Termin beim Kardiologen",
  "translated_text": "Ho bisogno di un appuntamento con il cardiologo",
  "source_language": "de",
  "target_language": "it",
  "audio_url": "/get_audio/translate_4d3c2b1a-0f9e-8g7h-6i5j-4k3l2m1n0o9p.mp3"
}
```

---

## 🔧 **COMMON ENDPOINTS**

### **Audio File Retrieval (All APIs)**

```
GET /get_audio/{filename}
```

#### **Example Request**

```bash
curl -X GET "http://localhost:8001/get_audio/audio_4f8b2c1a-9e3d-4b2c-8a1f-2d3e4f5a6b7c.mp3"
```

#### **Response**

- **Content-Type**: `audio/mpeg`
- **Body**: Binary audio data (MP3 file)

### **Root Endpoint Information (All APIs)**

```
GET /
```

#### **Example Response (Clinical Chat API)**

```json
{
  "message": "Clinical Chat API",
  "description": "AI-powered medical assistant with multi-language support",
  "endpoints": {
    "clinical_chat": "POST /clinical_chat",
    "get_audio": "GET /get_audio/{filename}",
    "documentation": "/docs"
  },
  "usage": {
    "endpoint": "/clinical_chat",
    "method": "POST",
    "parameters": {
      "query": "Your medical question",
      "output_language": "Language code (e.g., 'en', 'es', 'fr')"
    }
  }
}
```

---

## 🚨 **ERROR RESPONSES**

### **400 Bad Request**

```json
{
  "error": "Invalid file format. Only PDF files are supported."
}
```

### **422 Validation Error**

```json
{
  "detail": [
    {
      "loc": ["body", "query"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### **500 Internal Server Error**

```json
{
  "error": "OpenAI API key not configured."
}
```

### **404 Not Found**

```json
{
  "error": "File not found"
}
```

---

## 🛠 **POSTMAN COLLECTION SETUP**

### **Environment Variables**

Create a Postman environment with these variables:

```json
{
  "clinical_chat_url": "http://localhost:8001",
  "document_url": "http://localhost:8003",
  "csv_url": "http://localhost:8002",
  "organ_analyzer_url": "http://localhost:8004",
  "transcription_url": "http://localhost:8005",
  "translate_url": "http://localhost:8006"
}
```

### **Pre-request Scripts**

Add this to Postman pre-request scripts for file upload endpoints:

```javascript
// For file upload endpoints
pm.request.headers.add({
  key: "Content-Type",
  value: "multipart/form-data",
});
```

### **Tests Scripts**

Add these test scripts to validate responses:

```javascript
// Basic response validation
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Response has required fields", function () {
  const jsonData = pm.response.json();
  pm.expect(jsonData).to.have.property("audio_url");
});

pm.test("Audio URL is valid", function () {
  const jsonData = pm.response.json();
  pm.expect(jsonData.audio_url).to.include("/get_audio/");
});
```

---

## 📊 **SAMPLE DATA FILES**

### **Sample PDF Content (medical_report.pdf)**

```
PATIENT MEDICAL REPORT
======================
Patient ID: P12345
Name: John Smith
Date: 2025-09-30

VITAL SIGNS:
- Blood Pressure: 140/90 mmHg
- Heart Rate: 88 bpm
- Temperature: 98.6°F
- Respiratory Rate: 16 breaths/min
- Oxygen Saturation: 97%

MEDICATIONS:
- Lisinopril 10mg daily
- Metformin 500mg twice daily
- Atorvastatin 20mg daily
```

### **Sample CSV Content (patient_data.csv)**

```csv
patient_id,age,gender,blood_pressure_systolic,blood_pressure_diastolic,heart_rate,diagnosis
P001,45,M,140,90,88,Hypertension
P002,32,F,120,80,72,Normal
P003,67,M,150,95,94,Hypertension
P004,28,F,110,70,68,Normal
P005,55,M,135,85,82,Pre-hypertension
```

---

## 🚀 **QUICK START COLLECTION**

Import this Postman collection JSON to get started immediately:

```json
{
  "info": {
    "name": "Healthcare APIs Collection",
    "description": "Complete collection for all 6 healthcare backend APIs",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Clinical Chat API",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "formdata",
          "formdata": [
            {
              "key": "query",
              "value": "What are the symptoms of high blood pressure?",
              "type": "text"
            },
            {
              "key": "output_language",
              "value": "en",
              "type": "text"
            }
          ]
        },
        "url": {
          "raw": "{{clinical_chat_url}}/clinical_chat",
          "host": ["{{clinical_chat_url}}"],
          "path": ["clinical_chat"]
        }
      }
    }
  ]
}
```

This contract provides complete Postman-style documentation with realistic examples for all healthcare APIs, making integration and testing straightforward.
