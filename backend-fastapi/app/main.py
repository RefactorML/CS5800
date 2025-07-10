from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from .models import User
from .schemas import UserCreate, UserOut, AwardRequest
from .database import init_db, get_session

# Ensure database tables exist
init_db()

app = FastAPI(title="JobQuest API")

# CORS settings: allow local dev, Vercel, and Render static site origins
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://jobquest.vercel.app",
    "https://jobquest-frontend-wpm9.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/", tags=["Compatibility"])
def read_root():
    return {"message": "Welcome to JobQuest FastAPI Backend!"}

# Divide endpoint (edge-case test)
@app.get("/api/divide", tags=["Compatibility"])
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is undefined.")
    return {"result": a / b}

# Hello world endpoint
@app.get("/api/hello", tags=["Hello"])
def hello():
    return {"message": "Hello World from the JobQuest FastAPI Backend!"}

# Create a new user (MVP feature)
@app.post("/api/users", response_model=UserOut, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user_in: UserCreate, db: Session = Depends(get_session)):
    user = User.model_validate(user_in)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Read user by ID
@app.get("/api/users/{user_id}", response_model=UserOut, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_session)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user

# Award points/badges to a user
@app.post("/api/users/{user_id}/award", response_model=UserOut, tags=["Users"])
def award_points(
    user_id: int,
    award: AwardRequest,
    db: Session = Depends(get_session),
):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    user.points += award.points
    if award.badge:
        user.badges += 1
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Leaderboard: top 10 users by points
@app.get("/api/leaderboard", response_model=list[UserOut], tags=["Leaderboard"])
def leaderboard(db: Session = Depends(get_session)):
    stmt = select(User).order_by(User.points.desc()).limit(10)
    return db.exec(stmt).all()
