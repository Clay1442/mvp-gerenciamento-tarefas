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

    @staticmethod
    def find_by_id(db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()    
    
    @staticmethod
    def delete(db: Session, task: Task):
        db.delete(task)
        db.commit()

    @staticmethod
    def update(db: Session):
        db.commit()