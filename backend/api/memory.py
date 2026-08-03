from fastapi import APIRouter
from backend.memory.memory import memory

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)


@router.post("/clear")
def clear_memory():

    memory.clear()

    return {
        "message": "Conversation memory cleared."
    }