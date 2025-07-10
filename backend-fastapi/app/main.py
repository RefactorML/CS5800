from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select


from .database import init_db, get_session
from .models import User
from .schemas import UserCreate, UserOut, AwardRequest
init_db()

app = FastAPI(title="JobQuest API")

# ────── CORS (unchanged) ──────
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://jobquest.vercel.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ────── Startup (unchanged) ──────
@app.on_event("startup")
def on_startup():
    init_db()


# ────── Compatibility endpoints (for existing tests) ──────
@app.get("/")
def read_root():
    return {"message": "Welcome to JobQuest FastAPI Backend!"}


@app.get("/api/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is undefined.")
    return {"result": a / b}


# ────── Hello + MVP gamification endpoints (unchanged) ──────
@app.get("/api/hello")
def hello():
    return {"message": "Hello World from the JobQuest FastAPI Backend!"}


@app.post("/api/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_session)):
    user = User.model_validate(user_in)  # up-to-date SQLModel style
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/api/users/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_session)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@app.post("/api/users/{user_id}/award", response_model=UserOut)
def award_points(user_id: int, award: AwardRequest, db: Session = Depends(get_session)):
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


@app.get("/api/leaderboard", response_model=list[UserOut])
def leaderboard(db: Session = Depends(get_session)):
    stmt = select(User).order_by(User.points.desc()).limit(10)
    return db.exec(stmt).all()
