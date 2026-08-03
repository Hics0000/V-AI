from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.ai.rag import rag
from backend.database.session import get_db
from backend.database.crud import (
    create_conversation,
    create_message,
    get_conversation,
    get_messages
)

router = APIRouter()


"""class ChatRequest(BaseModel):
    question: str"""

class ChatRequest(BaseModel):
    question: str
    conversation_id: int | None = None

@router.post("/chat")
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    # Check whether the user provided a conversation ID
    if request.conversation_id:

        conversation = get_conversation(
            db,
            request.conversation_id
        )

        # Conversation doesn't exist
        if conversation is None:
            return {
                "error": "Conversation not found"
            }

    else:
        # No conversation ID → create a new conversation
        conversation = create_conversation(db)

    # Save user's question
    create_message(
        db=db,
        conversation_id=conversation.id,
        role="user",
        content=request.question
    )

    # Generate AI response
    history = get_messages(
        db,
        conversation.id
    )   

    answer = rag.ask(
        request.question,
        history
    )

    # Save AI response
    create_message(
        db=db,
        conversation_id=conversation.id,
        role="assistant",
        content=answer
    )

    return {
        "conversation_id": conversation.id,
        "question": request.question,
        "answer": answer
    }