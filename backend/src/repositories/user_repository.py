from sqlalchemy.orm import Session
from src.models.user_model import UserModel

class UserRepository:
    
    @staticmethod
    #find user by email
    def get_user_by_email(email: str, db: Session) -> UserModel:
        return db.query(UserModel).filter(UserModel.email == email).first()

    @staticmethod
    #save user to database
    def save_user(user: UserModel, db: Session) -> UserModel:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user