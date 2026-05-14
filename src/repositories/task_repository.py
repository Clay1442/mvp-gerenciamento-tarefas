from sqlalchemy.orm import Session
from models.task_model import Task

class TaskRepository:
    @staticmethod
    def save(db: Session, task: Task):
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def find_all(db: Session):
        return db.query(Task).all()