import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [backendMessage, setBackendMessage] = useState('Loading message from backend...')
  const [error, setError] = useState(null)

  const fetchBackendData = async () => {
    setError(null); // Clear previous errors
    setBackendMessage('Fetching...');
    try {
      // Ensure your FastAPI backend is running, typically on port 8000
      const response = await fetch('http://localhost:8000/api/hello');

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status} - ${response.statusText || 'Unknown error'}`);
      }
      const data = await response.json();
      setBackendMessage(data.message);
    } catch (err) {
      console.error("Failed to fetch from backend:", err);
      setBackendMessage('Failed to load message from backend.');
      setError(err.message);
    }
  };

  useEffect(() => {
    fetchBackendData();
  }, []); // Empty dependency array ensures this runs once on component mount

  return (
    <div className="App">
      <header className="App-header">
        <h1>JobQuest "Hello World" Prototype</h1>
        <p>
          <strong>Message from Backend:</strong> {backendMessage}
        </p>
        {error && <p style={{ color: 'red' }}>Error: {error}</p>}
        <button onClick={fetchBackendData}>
          Fetch Message Again
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR (Hot Module Replacement).
        </p>
        <p>
          Backend API docs (if backend is running): <a href="http://localhost:8000/docs" target="_blank" rel="noopener noreferrer">http://localhost:8000/docs</a>
        </p>
      </header>
    </div>
  )
}

export default App