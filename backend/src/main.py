from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from src.database import Base, engine
from src.models import task_model, user_model
from src.controllers import task_controller, auth_controller

#this will create the database and tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()


#CORS configuration
origins = [
    "http://localhost:5173",
    "https://mvp-gerenciamento-tarefas.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

#Import Routers
app.include_router(task_controller.router)
app.include_router(auth_controller.router)