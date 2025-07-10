import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [msg, setMsg] = useState(null);
  const [error, setError] = useState(null);
  const API_BASE = import.meta.env.VITE_API_URL;

  async function fetchMsg() {
    try {
      const res = await fetch(`${API_BASE}/api/hello`);
      if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
      const data = await res.json();
      setMsg(data.message);
      setError(null);
    } catch (err) {
      setMsg(null);
      setError(err.message);
    }
  }

  useEffect(() => {
    fetchMsg();
  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>JobQuest "Hello World" Prototype</h1>

      {msg && (
        <p>
          Message from Backend: <strong>{msg}</strong>
        </p>
      )}

      {error && (
        <>
          <p style={{ color: 'red' }}>Failed to load message from backend.</p>
          <code>{error}</code>
        </>
      )}

      <button onClick={fetchMsg}>Fetch Message Again</button>

      <p style={{ marginTop: '1rem' }}>
        Edit <code>src/App.jsx</code> and save to test HMR.
      </p>

      <p>
        Backend API docs:{' '}
        <a href={`${API_BASE}/docs`} target="_blank" rel="noreferrer">
          {API_BASE}/docs
        </a>
      </p>
    </div>
  );
}

export default App;
