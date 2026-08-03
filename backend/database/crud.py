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

def get_conversation(
    db: Session,
    conversation_id: int
):
    return db.query(Conversation).filter(
        Conversation.id == conversation_id
    ).first()

def get_messages(
    db: Session,
    conversation_id: int
):
    return (
        db.query(Message)
        .filter(Message.conversation_id == conversation_id)
        .order_by(Message.id.asc())
        .all()
    )