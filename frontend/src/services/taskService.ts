import { api } from './api'; 

// Define the TaskData interface to represent the structure of task data
export interface TaskData {
  title: string;
  description?: string;
  status: string;
}

export const getTasks = () => api.get('/tasks/find all');

export const createTask = (task: TaskData) => api.post('/tasks/', task);

export const updateTaskStatus = (id: number, status: string) => api.patch(`/tasks/${id}`, { status });

export const deleteTask = (id: number) => api.delete(`/tasks/${id}`);