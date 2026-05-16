from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.user_model import UserModel
from src.schemas.user_schema import UserCreate, LoginRequest, TokenResponse
from src.repositories.user_repository import UserRepository # Importa o repositório
from src.utils.security import get_password_hash, verify_password, create_access_token

class UserService:
    #Verification if the email is already registered
    @staticmethod
    def create_user(user_data: UserCreate, db: Session):
        existing_user = UserRepository.get_user_by_email(user_data.email, db)
        
        if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Este e-mail já está cadastrado."
                )
    
        # password hashing
        hashed_pwd = get_password_hash(user_data.password)
    
        
        # Create a new user instance with the hashed password
        new_user = UserModel(
            email=user_data.email,
            hashed_password=hashed_pwd
        )
    
        return UserRepository.save_user(new_user, db)
    
    @staticmethod
    def login_user(login_data: LoginRequest, db: Session) -> TokenResponse:
        # Find the user by email
        user = UserRepository.get_user_by_email(login_data.email, db)
        
        # Message for invalid credentials
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="E-mail ou senha incorretos."
            )

        # Verify the provided password against the stored hashed password
        is_password_correct = verify_password(login_data.password, user.hashed_password)
        if not is_password_correct:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="E-mail ou senha incorretos."
            )

        # if credentials are valid, create a JWT access token
        access_token = create_access_token(data={"sub": user.email})
        
        return TokenResponse(access_token=access_token, token_type="bearer")