from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    status: bool

    # This allows Pydantic to work with Objects and not just dicts
    class config:
        from_attribute = True       