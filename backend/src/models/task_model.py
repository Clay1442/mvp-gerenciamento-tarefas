from sqlalchemy import Column, Integer, String, Boolean, Enum 
from enums import TaskStatus
from database import Base

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDENTE, nullable=False)