from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate
from typing import List
from services.task_service import TaskService
from utils.security import get_current_user
from models.user_model import UserModel

router = APIRouter(prefix="/tasks", tags=["Tasks"])

#Building the endpoint to create a new task
@router.post("/", response_model=TaskResponse)
def create(request: TaskCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return TaskService.create_task(db, request, current_user.id)

#Building the endpoint to find all tasks
@router.get("/find all", response_model=List[TaskResponse])
def find_all(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return TaskService.find_all(current_user.id, db)

#Building the endpoint to find one task
@router.get("/", response_model=TaskResponse)
def find_by_id(task_id: int ,db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return TaskService.find_by_id(db, task_id, current_user.id)

#Building the endpoint to update task
@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, request: TaskUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return TaskService.update_task(db, task_id, request, current_user.id)


#Building the endpoint to Delete task
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    return TaskService.delete_task(db, task_id, current_user.id)