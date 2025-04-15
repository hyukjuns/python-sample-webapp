import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models import Note
from app.database import SessionLocal

# Init App
app = FastAPI()

# DB Session 의존성 주입
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET /notes 모든 메모 조회
@app.get("/notes")
def list_note(db: Session = Depends(get_db_session)):
    return db.query(Note).all()


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="debug", reload=True, access_log=True)