from backend.database.database import engine
from backend.database.database import Base
from backend.database.session import SessionLocal
from backend.database.crud import get_conversation


Base.metadata.create_all(bind=engine)

db = SessionLocal()

conversation = get_conversation(db, 2)

if conversation:
    print("Conversation found!")
    print("ID:", conversation.id)
    print("Title:", conversation.title)
else:
    print("Conversation not found.")

db.close()