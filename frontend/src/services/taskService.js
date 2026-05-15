import api from './api';

export const getTasks = () => api.get('/tasks/find all');
export const createTask = (task) => api.post('/tasks/', task);
export const updateTaskStatus = (id, status) => api.patch(`/tasks/${id}`, { status });
export const deleteTask = (id) => api.delete(`/tasks/${id}`);