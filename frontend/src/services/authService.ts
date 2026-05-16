import { api } from './api';

export const login = (data: object) => api.post('/auth/login', data);
export const register = (data: object) => api.post('/auth/register', data);