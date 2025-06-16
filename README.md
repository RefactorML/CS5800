# JobQuest - Prototype (React + FastAPI)

Initial "Hello World" prototype for the JobQuest project (CS5800).
This demonstrates a React frontend connecting to a FastAPI backend.

## Project Structure

- `/frontend-react`: React client application (Vite).
- `/backend-fastapi`: FastAPI server API.

## Prerequisites

- Node.js (v18+) & npm (or yarn)
- Python (v3.8+) & pip

## Running the Application

**1. Start Backend (FastAPI):**

   In a terminal:
   ```bash
   cd backend-fastapi

   # First-time setup:
   python -m venv venv
   # Activate:
   #   Windows: venv\Scripts\activate
   #   macOS/Linux: source venv/bin/activate
   pip install -r requirements.txt

   # Run server:
   uvicorn app.main:app --reload --port 8000