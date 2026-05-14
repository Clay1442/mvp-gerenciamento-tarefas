from sqlalchemy.orm import Session
from models.task_model import Task
from schemas.task_schema import TaskCreate, TaskUpdate
from fastapi import HTTPException
from repositories.task_repository import TaskRepository

class TaskService:

    #method to create a new task
    @staticmethod
    def create_task(db: Session, task_data: TaskCreate):
        new_task = Task(
            title = task_data.title,
            description = task_data.description
        )
        return TaskRepository.save(db, new_task)
    

    #method to return all tasks
    @staticmethod
    def find_all(db: Session):
        tasks = TaskRepository.find_all(db)
        return tasks
    
    #method to return by id
    @staticmethod
    def find_by_id(db: Session, task_id: int):
        task = TaskRepository.find_by_id(db, task_id)
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    
    @staticmethod
    def update_task(db: Session, task_id: int, task_data: TaskUpdate):
        task = TaskService.find_by_id(db, task_id)

        update_data = task_data.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(task, key, value)
         
        TaskRepository.update(db)
        db.refresh(task)
        return task
    
    @staticmethod
    def delete_task(db: Session, task_id: int):
        task = TaskService.find_by_id(db, task_id)
        TaskRepository.delete(db, task)
        return {"message": "Task deleted successfully"}