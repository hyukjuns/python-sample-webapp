from sqlmodel import Session, SQLModel
from app.database import engine
from app.models import Note

def init_db():
    SQLModel.metadata.create_all(engine)
    print("✅---> note table created.")

    with Session(engine) as session:
        init_notes = [
            Note(user="testuser1", note="hello world 1!"),
            Note(user="testuser2", note="hello world 2!"),
            Note(user="testuser3", note="hello world 3!"),
        ]
        session.add_all(init_notes)
        session.commit()
        print("✅---> Initial note data inserted.")

    print("✅---> Database initialized.")

if __name__ == "__main__":
    init_db()