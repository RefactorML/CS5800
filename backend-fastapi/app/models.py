from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"          # ← NEW (was the reserved word “user”)

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    points: int = 0
    badges: int = 0
