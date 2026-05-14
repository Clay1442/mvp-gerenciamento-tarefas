from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.task_schema import TaskCreate, TaskResponse
from services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

#Building the endpoint to create a new task
@router.post("/", response_model=TaskResponse)
def create(request: TaskCreate, db: Session = Depends(get_db)):
    return TaskService.create_task(db, request)