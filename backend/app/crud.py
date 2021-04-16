from sqlalchemy.orm import Session
from app import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
    	username=user.username, 
    	password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

''''''

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_task_by_taskname(db: Session, taskname: str):
    return db.query(models.Task).filter(models.Task.taskname == taskname).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
    	taskname=task.taskname, 
    	fullname=task.fullname, 
    	organization=task.organization)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_workhour(db: Session, workhour_id: int):
    return db.query(models.Workhour).filter(models.Workhour.id == workhour_id).first()

def get_workhours(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Workhour).offset(skip).limit(limit).all()

def get_workhours_by_user_id(db: Session, user_id: str):
    return db.query(models.Workhour).filter(models.Workhour.user_id == user_id)

def get_workhours_by_task_id(db: Session, task_id: str):
    return db.query(models.Workhour).filter(models.Workhour.task_id == task_id)

def create_workhour(db: Session, workhour: schemas.WorkhourCreate):
    db_workhour = models.Workhour(
    	user_id=workhour.user_id, 
    	task_id=workhour.task_id, 
    	day=workhour.day, 
    	hour=workhour.hour, 
    	description=workhour.description)
    db.add(db_workhour)
    db.commit()
    db.refresh(db_workhour)
    return db_workhour

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()

# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item