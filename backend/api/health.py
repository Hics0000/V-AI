from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "project": "V-AI"
    }