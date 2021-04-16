from typing import List, Optional
from pydantic import BaseModel
import datetime

class TaskBase(BaseModel):
    taskname: str

class TaskCreate(TaskBase):
    fullname: str
    organization: str

class Task(TaskBase):
    id: int
    workhours: List[Workhour] = []
    
    class Config:
        orm_mode = True

class WorkhourBase(BaseModel):
    user_id: int
    task_id: int
    day: datetime.date
    hour: float
    description: Optional[str] = None

class WorkhourCreate(WorkhourBase):
    pass

class Workhour(WorkhourBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    # is_active: bool
    workhours: List[Workhour] = []

    class Config:
        orm_mode = True