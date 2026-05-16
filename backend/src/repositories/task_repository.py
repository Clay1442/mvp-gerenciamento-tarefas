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
    def find_all_by_user(db: Session, user_id: int):
        return db.query(Task).filter(Task.user_id == user_id).all()

    @staticmethod
    def find_by_id_and_user(db: Session, task_id: int, user_id: int):
        return db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()

    @staticmethod
    def delete(db: Session, task: Task):
        db.delete(task)
        db.commit()

    @staticmethod
    def update(db: Session):
        db.commit()