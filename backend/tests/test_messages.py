from backend.database.session import SessionLocal
from backend.database.crud import get_messages


db = SessionLocal()

messages = get_messages(db, 2)

for message in messages:
    print(
        f"{message.role}: {message.content}"
    )

db.close()