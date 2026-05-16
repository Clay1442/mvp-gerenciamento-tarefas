import axios from 'axios';

interface ImportMetaEnv {
  readonly VITE_API_URL?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
});

// Add a request interceptor to include the token in the Authorization header
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('@TrelloClone:token');
  
  if (token && config.headers) {
    // Inject the token into the Authorization header
    config.headers.Authorization = `Bearer ${token}`;
  }
  
  return config;
});