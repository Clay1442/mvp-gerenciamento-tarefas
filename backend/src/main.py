from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from database import Base, engine
from models import task_model, user_model
from controllers import task_controller, auth_controller

#this will create the database and tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()


#CORS configuration
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"], # Permite todos os cabeçalhos
)

#Import Routers
app.include_router(task_controller.router)
app.include_router(auth_controller.router)