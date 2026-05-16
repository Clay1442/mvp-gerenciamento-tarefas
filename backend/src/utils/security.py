import jwt
import bcrypt
from datetime import datetime, timedelta, timezone

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


#temporary secret key for JWT token generation. In a 
# production environment, this should be stored securely and not hardcoded.
SECRET_KEY = "sua_chave_secreta_super_segura_e_longa_aqui"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


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