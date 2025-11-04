#!/usr/bin/env python3
"""
Healthcare Web Application Launcher
Single command to start both backend APIs and frontend web application
"""

import subprocess
import sys
import time
import os
import signal
import threading
from pathlib import Path
import webbrowser

# Configuration
BASE_DIR = Path(__file__).parent
BACKEND_PORT = 8000
FRONTEND_PORT = 3000
STARTUP_DELAY = 3  # seconds to wait for backend startup

# Process tracking
processes = []


def print_banner():
    """Print application banner"""
    print("""
🏥 Healthcare Web Application Launcher
=====================================
Starting integrated healthcare frontend and backend...
""")


def print_status(message, status="INFO"):
    """Print formatted status message"""
    icons = {
        "INFO": "ℹ️ ",
        "SUCCESS": "✅",
        "ERROR": "❌",
        "WARNING": "⚠️ "
    }
    print(f"{icons.get(status, 'ℹ️ ')} {message}")


def check_port(port):
    """Check if a port is available"""
    import socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', port))
            return True
    except OSError:
        return False


def start_backend():
    """Start the backend API server"""
    print_status("Starting backend API server...")

    if not check_port(BACKEND_PORT):
        print_status(f"Port {BACKEND_PORT} is already in use!", "WARNING")
        print_status("Backend may already be running", "INFO")
        return None

    try:
        # Start main.py backend
        backend_process = subprocess.Popen([
            sys.executable, "main.py"
        ], cwd=BASE_DIR)

        processes.append(("Backend API", backend_process))
        print_status(f"Backend API started on port {BACKEND_PORT}", "SUCCESS")
        return backend_process

    except Exception as e:
        print_status(f"Failed to start backend: {e}", "ERROR")
        return None


def start_frontend():
    """Start the frontend web application"""
    print_status("Starting frontend web application...")

    if not check_port(FRONTEND_PORT):
        print_status(f"Port {FRONTEND_PORT} is already in use!", "WARNING")
        print_status("Frontend may already be running", "INFO")
        return None

    try:
        # Start web_app.py frontend
        frontend_process = subprocess.Popen([
            sys.executable, "web_app.py"
        ], cwd=BASE_DIR)

        processes.append(("Frontend Web App", frontend_process))
        print_status(
            f"Frontend web app started on port {FRONTEND_PORT}", "SUCCESS")
        return frontend_process

    except Exception as e:
        print_status(f"Failed to start frontend: {e}", "ERROR")
        return None


def wait_for_backend():
    """Wait for backend to be ready"""
    import requests
    max_attempts = 30  # 30 seconds timeout

    for attempt in range(max_attempts):
        try:
            response = requests.get(
                f"http://localhost:{BACKEND_PORT}/", timeout=1)
            if response.status_code == 200:
                print_status("Backend API is ready!", "SUCCESS")
                return True
        except:
            pass

        time.sleep(1)
        print(f"⏳ Waiting for backend... ({attempt + 1}/{max_attempts})")

    print_status("Backend startup timeout - continuing anyway", "WARNING")
    return False


def wait_for_frontend():
    """Wait for frontend to be ready"""
    import requests
    max_attempts = 15  # 15 seconds timeout

    for attempt in range(max_attempts):
        try:
            response = requests.get(
                f"http://localhost:{FRONTEND_PORT}/api/health", timeout=1)
            if response.status_code == 200:
                print_status("Frontend web app is ready!", "SUCCESS")
                return True
        except:
            pass

        time.sleep(1)
        print(f"⏳ Waiting for frontend... ({attempt + 1}/{max_attempts})")

    print_status("Frontend startup timeout - continuing anyway", "WARNING")
    return False


def open_browser():
    """Open browser to the application"""
    try:
        url = f"http://localhost:{FRONTEND_PORT}"
        print_status(f"Opening browser to {url}")
        webbrowser.open(url)
    except Exception as e:
        print_status(f"Could not open browser: {e}", "WARNING")
        print_status(
            f"Please manually open: http://localhost:{FRONTEND_PORT}", "INFO")


def cleanup_processes():
    """Clean up all started processes"""
    print_status("Shutting down services...")

    for name, process in processes:
        try:
            if process.poll() is None:  # Process is still running
                print_status(f"Stopping {name}...")
                process.terminate()

                # Wait up to 5 seconds for graceful shutdown
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    print_status(f"Force killing {name}...")
                    process.kill()
                    process.wait()

        except Exception as e:
            print_status(f"Error stopping {name}: {e}", "ERROR")

    print_status("All services stopped", "SUCCESS")


def signal_handler(signum, frame):
    """Handle Ctrl+C gracefully"""
    print("\n")
    print_status("Received shutdown signal...")
    cleanup_processes()
    sys.exit(0)


def monitor_processes():
    """Monitor running processes"""
    while True:
        time.sleep(5)

        for name, process in processes:
            if process.poll() is not None:
                print_status(f"{name} has stopped unexpectedly!", "ERROR")
                return False

        # Check if all processes are still running
        if len(processes) == 0:
            break

    return True


def main():
    """Main application launcher"""
    print_banner()

    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        # Check dependencies
        print_status("Checking dependencies...")

        # Check if required files exist
        required_files = ["main.py", "web_app.py"]
        for file in required_files:
            if not (BASE_DIR / file).exists():
                print_status(f"Required file missing: {file}", "ERROR")
                return 1

        print_status("Dependencies check passed", "SUCCESS")

        # Start backend API
        backend_process = start_backend()

        # Wait for backend to be ready
        if backend_process:
            wait_for_backend()

        # Start frontend web application
        frontend_process = start_frontend()

        # Wait for frontend to be ready
        if frontend_process:
            wait_for_frontend()

        # Print summary
        print("\n" + "="*50)
        print_status("🎉 Healthcare Web Application is now running!", "SUCCESS")
        print("\n📋 Available Services:")
        print(f"   🔧 Backend API:     http://localhost:{BACKEND_PORT}")
        print(f"   📱 Frontend App:    http://localhost:{FRONTEND_PORT}")
        print(f"   📖 API Docs:        http://localhost:{BACKEND_PORT}/docs")
        print(
            f"   💚 Health Check:    http://localhost:{FRONTEND_PORT}/api/health")

        print("\n🌐 Available Pages:")
        print(f"   • Homepage:         http://localhost:{FRONTEND_PORT}/")
        print(
            f"   • Clinical Chat:    http://localhost:{FRONTEND_PORT}/clinical-chat")
        print(
            f"   • Document Analyzer: http://localhost:{FRONTEND_PORT}/document-analyzer")
        print(
            f"   • Speech-to-Text:   http://localhost:{FRONTEND_PORT}/speech-to-text")
        print(
            f"   • Text-to-Speech:   http://localhost:{FRONTEND_PORT}/text-to-speech")
        print(
            f"   • Organ Analyzer:   http://localhost:{FRONTEND_PORT}/organ-analyzer")

        print("\n⚡ Quick Actions:")
        print("   • Press Ctrl+C to stop all services")
        print("   • Check logs above for any errors")
        print("   • Test the APIs using the web interface")
        print("="*50 + "\n")

        # Open browser after a short delay
        threading.Timer(2.0, open_browser).start()

        # Monitor processes
        print_status("Monitoring services... (Press Ctrl+C to stop)")
        monitor_processes()

    except KeyboardInterrupt:
        print("\n")
        print_status("Shutdown requested by user")
    except Exception as e:
        print_status(f"Unexpected error: {e}", "ERROR")
        return 1
    finally:
        cleanup_processes()

    return 0


if __name__ == "__main__":
    sys.exit(main())
