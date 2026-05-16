import axios from 'axios';

export const api = axios.create({
baseURL: (import.meta.env['VITE_API_URL'] as string) || 'http://localhost:8000',
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