#!/usr/bin/env python3
"""
Lambda Handler for Healthcare AI Backend
Serverless adapter for FastAPI application
"""

import json
import base64
from typing import Dict, Any
from main import app
from mangum import Mangum


# Create Mangum adapter for AWS Lambda
handler = Mangum(app, lifespan="off")


def clinical_chat_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Dedicated Lambda handler for clinical chat endpoint
    Optimized for smaller memory footprint
    """
    try:
        # Import only what's needed for clinical chat
        from backend_api.clinical_chat_api import api_clinical_chat

        # Extract body from Lambda event
        body = event.get('body', '{}')
        if event.get('isBase64Encoded'):
            body = base64.b64decode(body).decode('utf-8')

        # Parse JSON body
        data = json.loads(body) if body else {}

        # Call the clinical chat function directly
        result = api_clinical_chat(
            user_message=data.get('user_message', ''),
            context=data.get('context', ''),
            session_id=data.get('session_id', '')
        )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'
            },
            'body': json.dumps(result)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }


def document_processor_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Dedicated Lambda handler for document processing
    Optimized for larger memory and longer timeout
    """
    try:
        from backend_api.document_api import api_process_document

        # Handle multipart form data or JSON
        body = event.get('body', '{}')
        if event.get('isBase64Encoded'):
            body = base64.b64decode(body).decode('utf-8')

        # For file uploads, you might need to handle multipart data differently
        # This is a simplified version for JSON-based requests
        data = json.loads(body) if body else {}

        result = api_process_document(
            question=data.get('question', ''),
            file_id=data.get('file_id', '')
        )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'
            },
            'body': json.dumps(result)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }


def transcription_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Dedicated Lambda handler for audio transcription
    """
    try:
        from backend_api.transcription_api import api_transcribe_audio

        body = event.get('body', '{}')
        if event.get('isBase64Encoded'):
            body = base64.b64decode(body).decode('utf-8')

        data = json.loads(body) if body else {}

        result = api_transcribe_audio(
            session_id=data.get('session_id', ''),
            language=data.get('language', 'en')
        )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'
            },
            'body': json.dumps(result)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }


def organ_analyzer_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Dedicated Lambda handler for organ analysis
    High memory configuration for image processing
    """
    try:
        from backend_api.organ_analyzer_api import api_analyze_organ_scan

        body = event.get('body', '{}')
        if event.get('isBase64Encoded'):
            body = base64.b64decode(body).decode('utf-8')

        data = json.loads(body) if body else {}

        result = api_analyze_organ_scan(
            organ_type=data.get('organ_type', ''),
            session_id=data.get('session_id', '')
        )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'
            },
            'body': json.dumps(result)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 500,
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }


# Lambda warmup handler
def warmup_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Warmup handler to prevent cold starts
    """
    if event.get('source') == 'serverless-plugin-warmup':
        print('Lambda is being warmed up')
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Lambda warmed up successfully'})
        }

    # If not a warmup event, pass to main handler
    return handler(event, context)


# Health check handler
def health_check_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Health check endpoint for monitoring
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'status': 'healthy',
            'service': 'healthcare-ai-backend',
            'version': '3.0.0',
            'timestamp': context.aws_request_id if context else 'local'
        })
    }
