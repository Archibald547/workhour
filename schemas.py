from typing import List, Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    name: str

    class Config:
        orm_mode = True

class WorkhourBase(BaseModel):
    title: str
    description: Optional[str] = None

class WorkhourCreate(WorkhourBase):
    pass

class Workhour(WorkhourBase):
    id: int
    user_id: int
    task_id: int

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