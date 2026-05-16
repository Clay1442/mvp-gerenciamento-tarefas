from pydantic import BaseModel, ConfigDict
from enums.TaskStatus import TaskStatus
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.PENDENTE

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None 

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus


    # This allows Pydantic to work with Objects and not just dicts
    model_config = ConfigDict(from_attributes=True)