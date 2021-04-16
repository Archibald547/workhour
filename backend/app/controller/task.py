from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas, config
from app.dependency import get_db
from app.auth import login_manager
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    prefix="/task",
    tags=["task"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_taskname(db, taskname=task.taskname)
    if db_task:
        raise HTTPException(status_code=400, detail="Taskname already registered")
    return crud.create_task(db=db, task=task)


@router.get("/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.get('/protected', response_model=schemas.User)
def protected_route(user=Depends(login_manager)):
    return user

@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
