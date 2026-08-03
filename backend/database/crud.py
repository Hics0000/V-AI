from sqlalchemy.orm import Session

from backend.database.models import Conversation, Message


def create_conversation(db: Session):
    conversation = Conversation()

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def create_message(
    db: Session,
    conversation_id: int,
    role: str,
    content: str
):
    message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message