from fastapi import FastAPI

app = FastAPI(
    title="V-AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to V AI"
    }