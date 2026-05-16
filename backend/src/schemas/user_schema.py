from pydantic import BaseModel, EmailStr

#schemas for user creation and response
class UserCreate(BaseModel):
    email: EmailStr 
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str        

