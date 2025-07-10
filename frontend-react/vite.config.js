import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Forward every /api/* request to FastAPI running on port 8000
      '/api': 'http://localhost:8000',
    },
  },
});
