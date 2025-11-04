#!/usr/bin/env python3
"""
Healthcare Web Application Server
Unified server that serves frontend screens and integrates with backend APIs
Eliminates CORS issues and provides seamless frontend-backend integration
"""

import os
import json
import uvicorn
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Request, HTTPException, Form, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import asyncio

# Configuration
APP_PORT = 3000  # Single port for everything
BACKEND_API_URL = "http://localhost:8000"  # Your main.py backend
BASE_DIR = Path(__file__).parent
FRONTEND_DIR = BASE_DIR / "frontend_screens"

# Create FastAPI app
app = FastAPI(
    title="Healthcare Web Application",
    description="Unified healthcare frontend and backend integration",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HTTP Client for backend API calls
http_client = httpx.AsyncClient(timeout=300.0)

# ============================================================================
# FRONTEND ROUTES (Serve HTML Pages)
# ============================================================================


@app.get("/", response_class=HTMLResponse)
async def homepage():
    """Serve the homepage"""
    html_file = FRONTEND_DIR / "index.html"
    if html_file.exists():
        return FileResponse(html_file)
    raise HTTPException(status_code=404, detail="Homepage not found")


@app.get("/clinical-chat", response_class=HTMLResponse)
async def clinical_chat_page():
    """Serve clinical chat page"""
    html_file = FRONTEND_DIR / "clinical_chat.html"
    if html_file.exists():
        return FileResponse(html_file)
    raise HTTPException(status_code=404, detail="Clinical chat page not found")


@app.get("/document-analyzer", response_class=HTMLResponse)
async def document_analyzer_page():
    """Serve document analyzer page"""
    html_file = FRONTEND_DIR / "healthcare-assistant-document-analyzer.html"
    if html_file.exists():
        return FileResponse(html_file)
    raise HTTPException(
        status_code=404, detail="Document analyzer page not found")


@app.get("/speech-to-text", response_class=HTMLResponse)
async def speech_to_text_page():
    """Serve speech to text page"""
    html_file = FRONTEND_DIR / "speech-to-text.html"
    if html_file.exists():
        return FileResponse(html_file)
    raise HTTPException(
        status_code=404, detail="Speech to text page not found")


@app.get("/text-to-speech", response_class=HTMLResponse)
async def text_to_speech_page():
    """Serve text to speech page"""
    html_file = FRONTEND_DIR / "healthcare-assistant-text-to-speech.html"
    if html_file.exists():
        return FileResponse(html_file)
    raise HTTPException(
        status_code=404, detail="Text to speech page not found")


@app.get("/organ-analyzer", response_class=HTMLResponse)
async def organ_analyzer_page():
    """Serve organ analyzer page"""
    html_file = FRONTEND_DIR / "organ-analyzer.html"
    if html_file.exists():
        return FileResponse(html_file)
    raise HTTPException(
        status_code=404, detail="Organ analyzer page not found")

# ============================================================================
# API PROXY ROUTES (Forward to Backend APIs)
# ============================================================================


@app.post("/api/clinical_chat")
async def proxy_clinical_chat(request: Request):
    """Proxy clinical chat requests to backend API"""
    try:
        body = await request.body()
        headers = {"Content-Type": "application/json"}

        response = await http_client.post(
            f"{BACKEND_API_URL}/clinical_chat",
            content=body,
            headers=headers
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Backend API error: {str(e)}"}
        )


@app.post("/api/process_document")
async def proxy_process_document(
    file: UploadFile = File(...),
    question: str = Form(...)
):
    """Proxy document processing requests to backend API"""
    try:
        # Forward file upload to backend
        files = {"file": (file.filename, await file.read(), file.content_type)}
        data = {"question": question}

        response = await http_client.post(
            f"{BACKEND_API_URL}/process_document",
            files=files,
            data=data
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Document processing error: {str(e)}"}
        )


@app.post("/api/transcribe_audio")
async def proxy_transcribe_audio(
    audio_file: UploadFile = File(...),
    session_id: str = Form(...),
    language: str = Form(default="en")
):
    """Proxy audio transcription requests to backend API"""
    try:
        files = {"audio_file": (audio_file.filename, await audio_file.read(), audio_file.content_type)}
        data = {"session_id": session_id, "language": language}

        response = await http_client.post(
            f"{BACKEND_API_URL}/transcribe_audio",
            files=files,
            data=data
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Audio transcription error: {str(e)}"}
        )


@app.post("/api/translate_text")
async def proxy_translate_text(request: Request):
    """Proxy text translation requests to backend API"""
    try:
        body = await request.body()
        headers = {"Content-Type": "application/json"}

        response = await http_client.post(
            f"{BACKEND_API_URL}/translate_text",
            content=body,
            headers=headers
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Translation error: {str(e)}"}
        )


@app.post("/api/process_csv")
async def proxy_process_csv(
    csv_file: UploadFile = File(...),
    target_language: str = Form(...),
    session_id: str = Form(...)
):
    """Proxy CSV processing requests to backend API"""
    try:
        files = {"csv_file": (csv_file.filename, await csv_file.read(), csv_file.content_type)}
        data = {"target_language": target_language, "session_id": session_id}

        response = await http_client.post(
            f"{BACKEND_API_URL}/process_csv",
            files=files,
            data=data
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"CSV processing error: {str(e)}"}
        )


@app.post("/api/analyze_organ_scan")
async def proxy_analyze_organ_scan(
    scan_image: UploadFile = File(...),
    organ_type: str = Form(...),
    session_id: str = Form(...)
):
    """Proxy organ scan analysis requests to backend API"""
    try:
        files = {"scan_image": (scan_image.filename, await scan_image.read(), scan_image.content_type)}
        data = {"organ_type": organ_type, "session_id": session_id}

        response = await http_client.post(
            f"{BACKEND_API_URL}/analyze_organ_scan",
            files=files,
            data=data
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Organ scan analysis error: {str(e)}"}
        )

# ============================================================================
# INFO ENDPOINTS (For API Status)
# ============================================================================


@app.get("/api/info")
async def api_info():
    """Get overall API information"""
    try:
        response = await http_client.get(f"{BACKEND_API_URL}/")
        backend_status = "connected"
    except:
        backend_status = "disconnected"

    return {
        "service": "Healthcare Web Application",
        "version": "1.0.0",
        "status": "running",
        "backend_status": backend_status,
        "frontend_screens": [
            "/",
            "/clinical-chat",
            "/document-analyzer",
            "/speech-to-text",
            "/text-to-speech",
            "/organ-analyzer"
        ],
        "api_endpoints": [
            "/api/clinical_chat",
            "/api/process_document",
            "/api/transcribe_audio",
            "/api/translate_text",
            "/api/process_csv",
            "/api/analyze_organ_scan"
        ]
    }


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    try:
        response = await http_client.get(f"{BACKEND_API_URL}/")
        backend_healthy = response.status_code == 200
    except:
        backend_healthy = False

    return {
        "status": "healthy" if backend_healthy else "degraded",
        "frontend": "healthy",
        "backend": "healthy" if backend_healthy else "unhealthy",
        "timestamp": __import__('datetime').datetime.now().isoformat()
    }

# ============================================================================
# STATIC FILE SERVING
# ============================================================================

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

# Serve JavaScript integration files directly


@app.get("/js/{filename}")
async def serve_javascript(filename: str):
    """Serve JavaScript files"""
    js_file = FRONTEND_DIR / filename
    if js_file.exists() and filename.endswith('.js'):
        return FileResponse(js_file, media_type="application/javascript")
    raise HTTPException(status_code=404, detail="JavaScript file not found")

# ============================================================================
# APPLICATION STARTUP
# ============================================================================


@app.on_event("startup")
async def startup_event():
    """Application startup event"""
    print("🏥 Healthcare Web Application Starting...")
    print(f"📱 Frontend: http://localhost:{APP_PORT}")
    print(f"🔗 Backend API: {BACKEND_API_URL}")
    print("✅ Application ready!")


@app.on_event("shutdown")
async def shutdown_event():
    """Application shutdown event"""
    await http_client.aclose()
    print("👋 Healthcare Web Application Shutting Down...")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("🚀 Starting Healthcare Web Application...")
    print(f"🌐 URL: http://localhost:{APP_PORT}")
    print("📋 Available pages:")
    print("   • Homepage: http://localhost:3000/")
    print("   • Clinical Chat: http://localhost:3000/clinical-chat")
    print("   • Document Analyzer: http://localhost:3000/document-analyzer")
    print("   • Speech to Text: http://localhost:3000/speech-to-text")
    print("   • Text to Speech: http://localhost:3000/text-to-speech")
    print("   • Organ Analyzer: http://localhost:3000/organ-analyzer")
    print("")
    print("⚠️  Make sure your backend API is running on port 8000!")
    print("   Run: python main.py")
    print("")

    uvicorn.run(
        "web_app:app",
        host="0.0.0.0",
        port=APP_PORT,
        reload=True,
        log_level="info"
    )
