from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.ai.rag import rag
from backend.database.session import get_db
from backend.database.crud import (
    create_conversation,
    create_message,
)

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    # Create a new conversation
    conversation = create_conversation(db)

    # Get AI response
    answer = rag.ask(request.question)

    return {
        "conversation_id": conversation.id,
        "question": request.question,
        "answer": answer
    }