from typing import List, Optional
from pydantic import BaseModel
import datetime

class WorkhourBase(BaseModel):
    user_id: int
    task_id: int
    date: datetime.date
    hour: float
    description: Optional[str] = None

class WorkhourCreate(WorkhourBase):
    pass

class Workhour(WorkhourBase):
    id: int
    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    taskname: str
    fullname: str
    organization: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class UserFull(User):
    workhours: List[Workhour] = []

class TaskFull(Task):
    workhours: List[Workhour] = []

class WorkhourFull(Workhour):
    user: Optional[User]
    task: Optional[Task]
