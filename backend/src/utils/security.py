from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.user_model import UserModel
from src.repositories.user_repository import UserRepository
import jwt
import bcrypt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#find the secret key, algorithm and token expiration time from environment variables, 
# with default values for local development
SECRET_KEY = os.getenv("SECRET_KEY", "chave_padrao_local_super_secreta")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Function to hash a plain password
def get_password_hash(password: str) -> str:
    # Convert the password to bytes, as bcrypt works with byte strings
    pwd_bytes = password.encode('utf-8')
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    
    # Return the hashed password as a string (decode from bytes)
    return hashed.decode('utf-8')

# Function to verify a plain password against a hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Convert both the plain password and the hashed password to bytes for comparison
    pwd_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    
    # Use bcrypt's checkpw function to verify the password
    return bcrypt.checkpw(pwd_bytes, hashed_bytes)

# Function to create a JWT access token
def create_access_token(data: dict) -> str:
    """"create a JWT access token with an expiration time."""
    to_encode = data.copy()
    
    # Set the expiration time for the token
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    # Encode the token using the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Define the OAuth2 scheme for token extraction from requests
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# Function to decode and verify a JWT token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserModel:

    # Define a common exception for invalid credentials to avoid repetition   
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token de autenticação inválido ou expirado.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode the JWT token to extract the payload
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        
        if email is None:
            raise credentials_exception
            
    except jwt.PyJWTError:
        raise credentials_exception

    #Find the user in the database using the email extracted from the token
    user = UserRepository.get_user_by_email(email, db)
    if user is None:
        raise credentials_exception

    #return the user object if the token is valid and the user exists
    return user