from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Health"])

@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "project": "V-AI",
        "version": "0.1.0"
    }