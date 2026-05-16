from sqlalchemy.orm import Session
from models.task_model import Task
from schemas.task_schema import TaskCreate, TaskUpdate
from fastapi import HTTPException
from repositories.task_repository import TaskRepository
from fastapi import status
from utils.security import get_current_user
from models.user_model import UserModel

class TaskService:

    #method to create a new task
    @staticmethod
    def create_task(db: Session, task_data: TaskCreate, user_id: int):
        new_task = Task(
            title = task_data.title,
            description = task_data.description,
            user_id = user_id
        )
        return TaskRepository.save(db, new_task)
    

    #method to return all tasks
    @staticmethod
    def find_all(user_id: int, db: Session):
        tasks = TaskRepository.find_all_by_user(db, user_id)
        return tasks
    
    #method to return by id
    @staticmethod
    def find_by_id(db: Session, task_id: int, user_id: int):
        task = TaskRepository.find_by_id_and_user(db, task_id, user_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    
    #method to update task
    @staticmethod
    def update_task(db: Session, task_id: int, task_data: TaskUpdate, user_id: int):
        task = TaskRepository.find_by_id_and_user(db, task_id, user_id)
        
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Tarefa não encontrada ou você não tem permissão para editá-la."
            )
        
        update_data = task_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(task, key, value)

        TaskRepository.update(db)
        db.refresh(task)
        return task
    
    #method to delete task
    @staticmethod
    def delete_task(db: Session, task_id: int, user_id: int):
        task = TaskRepository.find_by_id_and_user(db, task_id, user_id)

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Tarefa não encontrada ou você não tem permissão para deletá-la."
            )

        TaskRepository.delete(db, task)
        return {"message": "Task deleted successfully"}