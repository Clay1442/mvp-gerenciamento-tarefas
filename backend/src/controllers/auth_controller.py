from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.user_schema import UserCreate, UserResponse, TokenResponse, LoginRequest
from src.services.user_service import UserService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(user_data=user_data, db=db)

@router.post("/login", response_model=TokenResponse)
def login_user(login_data: LoginRequest, db: Session = Depends(get_db)):
    return UserService.login_user(login_data=login_data, db=db)

@router.post("/token", response_model=TokenResponse, include_in_schema=True)
def login_for_swagger(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    login_data = LoginRequest(
        email=form_data.username,  
        password=form_data.password
    )
    
    return UserService.login_user(login_data=login_data, db=db)