from fastapi import FastAPI

from backend.api.chat import router as chat_router
from backend.api.health import router as health_router
from backend.api.upload import router as upload_router
from backend.api.memory import router as memory_router
from backend.database.database import create_database

create_database()

app = FastAPI(title="V AI")


app.include_router(chat_router)
app.include_router(health_router)
app.include_router(upload_router)
app.include_router(memory_router)

@app.get("/")
def root():
    return {"message": "Welcome to V AI"}