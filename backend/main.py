from fastapi import FastAPI

from backend.api.health import router as health_router
from backend.api.upload import router as upload_router

app = FastAPI(
    title="V",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(upload_router)

@app.get("/")
async def root():
    return {"message": "Welcome to V"}