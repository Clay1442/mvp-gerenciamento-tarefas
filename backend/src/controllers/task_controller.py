from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate
from typing import List
from services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

#Building the endpoint to create a new task
@router.post("/", response_model=TaskResponse)
def create(request: TaskCreate, db: Session = Depends(get_db)):
    return TaskService.create_task(db, request)

#Building the endpoint to find all tasks
@router.get("find all/", response_model=List[TaskResponse])
def find_all(db: Session = Depends(get_db)):
    return TaskService.find_all(db)

#Building the endpoint to find one task
@router.get("/", response_model=TaskResponse)
def find_by_id(task_id = int ,db: Session = Depends(get_db)):
    return TaskService.find_by_id(db, task_id)

#Building the endpoint to update task
@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, request: TaskUpdate, db: Session = Depends(get_db)):
    return TaskService.update_task(db, task_id, request)


#Building the endpoint to Delete task
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return TaskService.delete_task(db, task_id)