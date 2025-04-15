from sqlmodel import SQLModel, Field
from typing import Optional

class Note(SQLModel, table=True):
    __tablename__ = "note"
    id: Optional[int] = Field(default=None, primary_key=True)
    user: str
    note: str
