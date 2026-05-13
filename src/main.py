from fastapi import FastAPI
from database import engine
from models import task_model

#this will create the database and tables if they don't exist
task_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "online", "message": "Banco de dados verificado/criado!"}