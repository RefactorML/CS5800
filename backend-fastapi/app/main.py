from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="JobQuest API")

# Allow the Vite dev server + production frontend
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://jobquest.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # 👈 tighten in prod if you like
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to JobQuest FastAPI Backend!"}

@app.get("/api/hello")
async def get_hello():
    return {"message": "Hello World from the JobQuest FastAPI Backend!"}

@app.get("/api/divide")
async def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is undefined.")
    return {"result": a / b}
