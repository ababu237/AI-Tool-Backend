import uvicorn

if __name__ == "__main__":
    uvicorn.run("unified_backend.main_backend:app",
                host="0.0.0.0", port=8000, reload=True)
