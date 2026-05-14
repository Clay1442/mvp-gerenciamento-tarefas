from fastapi import FastAPI
from database import engine
from models import task_model
from controllers import task_controller

#this will create the database and tables if they don't exist
task_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Import Routers
app.include_router(task_controller.router)