from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables from .env file (optional for this simple example)
load_dotenv()

app = FastAPI(title="JobQuest API")

# Get allowed origins from environment variable or use a default
# For development, you might allow specific localhost ports
# For production, you'd list your actual frontend domain(s)
allowed_origins_str = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
origins = [origin.strip() for origin in allowed_origins_str.split(',')]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)

@app.get("/")
async def read_root():
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to JobQuest FastAPI Backend!"}

@app.get("/api/hello")
async def get_hello_world():
    """
    A simple endpoint that returns a Hello World message.
    """
    return {"message": "Hello World from the JobQuest FastAPI Backend!"}

# To run: uvicorn app.main:app --reload --port 8000
# (Ensure venv is activated and you are in the backend-fastapi directory)