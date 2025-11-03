# 🏥 Healthcare Backend APIs

A comprehensive healthcare backend system with 6 specialized AI-powered APIs for medical consultations, document analysis, data processing, medical imaging, audio transcription, and multi-language translation.

## 🎯 Overview

This project provides a complete healthcare backend infrastructure with the following APIs:

- **Clinical Chat API** (Port 8001) - AI-powered medical consultation assistant
- **CSV File API** (Port 8000) - CSV data analysis with AI insights
- **Document API** (Port 8003) - PDF document analysis and Q&A
- **Organ Analyzer API** (Port 8004) - Medical image analysis using AI models
- **Transcription API** (Port 8005) - Audio transcription using OpenAI Whisper
- **Translation API** (Port 8006) - Multi-language text translation

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Activate virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

# Install required packages
pip install -r requirements.txt
```

### 2. Start All APIs (Recommended)

Use the main launcher script to start all APIs simultaneously:

```bash
# Start all APIs
python main.py

# Check API status
python main.py --check

# Get help
python main.py --help
```

### 3. Start Individual APIs (Alternative)

If you prefer to start APIs individually:

```bash
cd backend_api

# Clinical Chat API (Port 8001)
python clinical_chat_api.py

# CSV File API (Port 8000)
python csv_file_api.py

# Document API (Port 8003)
python document_api.py

# Organ Analyzer API (Port 8004)
python organ_analyzer_api.py

# Transcription API (Port 8005)
python transcription_api.py

# Translation API (Port 8006)
python translate_text_api.py
```

## 📚 API Documentation

Once the APIs are running, access interactive documentation:

- **Clinical Chat**: http://localhost:8001/docs
- **CSV Processing**: http://localhost:8000/docs
- **Document Analysis**: http://localhost:8003/docs
- **Organ Analysis**: http://localhost:8004/docs
- **Audio Transcription**: http://localhost:8005/docs
- **Text Translation**: http://localhost:8006/docs

## 📖 API Contract & Examples

- **[API_CONTRACT.md](./API_CONTRACT.md)** - Comprehensive API documentation
- **[POSTMAN_API_CONTRACT.md](./POSTMAN_API_CONTRACT.md)** - Postman-style examples with cURL commands

## 🔧 Configuration

1. **OpenAI API Key**: Add your OpenAI API key to `config/config.json`:

   ```json
   {
     "OPENAI_API_KEY": "your_openai_api_key_here"
   }
   ```

2. **Environment Variables**: Optional `.env` file for additional configuration

## 🧪 Testing

```bash
# Run all unit tests
python -m pytest unit_tests/

# Run tests with coverage
python -m pytest unit_tests/ --cov=backend_api

# Run specific API tests
python -m pytest unit_tests/test_clinical_chat_api.py
```

## 📊 Features

### Clinical Chat API

- AI-powered medical consultations
- Multi-language support
- Audio response generation
- Conversation history tracking

### CSV File API

- Intelligent data analysis
- Statistical insights
- Multi-format support
- AI-generated recommendations

### Document API

- PDF document processing
- Q&A capabilities
- Multi-document support
- Context-aware responses

### Organ Analyzer API

- Medical image analysis
- AI model predictions
- Health recommendations
- Multi-organ support

### Transcription API

- Audio-to-text conversion
- Multi-language transcription
- Translation capabilities
- OpenAI Whisper integration

### Translation API

- Multi-language translation
- Text-to-speech output
- Language detection
- Google Translator integration

## 🛠 Development

### Project Structure

```
si-ai-tool-backend/
├── main.py                 # Main launcher script
├── backend_api/           # API implementations
├── config/                # Configuration files
├── unit_tests/           # Test files
├── requirements.txt      # Python dependencies
├── API_CONTRACT.md       # API documentation
└── POSTMAN_API_CONTRACT.md # Postman examples
```

### Main Launcher Features

The `main.py` script provides:

- **Concurrent startup** of all APIs
- **Health monitoring** and status checks
- **Graceful shutdown** handling
- **Process management** and error recovery
- **Real-time status** reporting

### Usage Examples

```bash
# Check what's running
python main.py --check

# Output:
# 🔍 Checking API Status...
#    Clinical Chat API         🟢 RUNNING    http://localhost:8001
#    CSV File API              🟢 RUNNING    http://localhost:8000
#    Document API              🟢 RUNNING    http://localhost:8003
#    Organ Analyzer API        🟢 RUNNING    http://localhost:8004
#    Transcription API         🔴 STOPPED    http://localhost:8005
#    Translation API           🟢 RUNNING    http://localhost:8006
# 📊 Summary: 5/6 APIs are running
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:

1. Check the [API documentation](./API_CONTRACT.md)
2. Review [Postman examples](./POSTMAN_API_CONTRACT.md)
3. Run `python main.py --check` to diagnose issues
4. Check individual API logs for detailed error information

## 🔄 Updates

- **v1.0.0** - Initial release with all 6 healthcare APIs
- **v1.1.0** - Added main launcher script with process management
- **v1.2.0** - Enhanced error handling and health monitoring
