# JobQuest - "Hello World" Prototype (React + FastAPI)

This is the initial "Hello World" prototype for the JobQuest project.
It demonstrates a basic working React frontend (using Vite) and a FastAPI backend connection.

## Project Structure

- `/frontend-react`: Contains the React application for the client-side.
- `/backend-fastapi`: Contains the FastAPI server for the server-side API.

## Prerequisites

- Node.js (v18+ recommended) and npm (or yarn): [https://nodejs.org/](https://nodejs.org/)
- Python (v3.8+ recommended) and pip: [https://www.python.org/](https://www.python.org/)

## Setup and Running the Prototype

1.  **Clone the repository (if applicable):**
    ```bash
    # git clone <your-repo-url>
    # cd jobquest-prototype
    ```

2.  **Setup and Start the Backend Server (FastAPI):**
    Open a terminal window.
    ```bash
    cd backend-fastapi

    # Create and activate virtual environment (first time setup)
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt

    # Run the FastAPI development server
    uvicorn app.main:app --reload --port 8000
    ```
    The backend should now be running on `http://localhost:8000`.
    You can access the API docs at `http://localhost:8000/docs`.

3.  **Setup and Start the Frontend Server (React with Vite):**
    Open a *new, separate* terminal window.
    ```bash
    cd frontend-react

    # Install dependencies (first time setup)
    npm install

    # Run the React development server
    npm run dev
    ```
    The React development server will typically start on `http://localhost:5173` (check terminal output for the exact port).

4.  **View the Application:**
    Open `http://localhost:5173` (or the port shown for React) in your web browser.
    The page should display a "Hello World" message fetched from the FastAPI backend.

## Troubleshooting

- **CORS Errors:** If the frontend cannot fetch data, check the browser's developer console. Ensure the `origins` list in `backend-fastapi/app/main.py` includes the correct URL and port of your running React development server (e.g., `http://localhost:5173`).
- **Backend Not Running:** Ensure the FastAPI server is running in its terminal window before starting/testing the frontend.
- **Port Conflicts:** If port 8000 or 5173 is in use, you can change them.
    - For FastAPI: `uvicorn app.main:app --reload --port <new_port_backend>`
    - For Vite: `npm run dev -- --port <new_port_frontend>` (and update fetch URL in `App.jsx` and CORS origins in `main.py`).