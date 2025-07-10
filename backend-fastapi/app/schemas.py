from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    points: int
    badges: int


class AwardRequest(BaseModel):
    points: int = 10          # default XP per action
    badge: bool = False       # set True to increment badges
