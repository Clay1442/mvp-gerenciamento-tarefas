from sqlalchemy.orm import Session
from models.task_model import Task
from schemas.task_schema import TaskCreate
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