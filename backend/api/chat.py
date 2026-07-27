from fastapi import APIRouter
from pydantic import BaseModel
from backend.ai.rag import rag
from backend.ai.llm import llm

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    answer = rag.ask(request.question)

    return {
        "question": request.question,
        "answer": answer
    }