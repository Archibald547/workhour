from fastapi import APIRouter, Depends, HTTPException
from workhour import schemas
from workhour import crud, schemas
from workhour.dependency import get_db
from sqlalchemy.orm import Session
from typing import List

from fastapi_login import LoginManager
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

SECRET = "super-secret-key"
manager = LoginManager(SECRET, '/user/login')


router = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = data.username
    password = data.password

    user = crud.get_user_by_username(db, username=username)
    if not user:
        raise HTTPException(status_code=400, detail="Username not found")
    elif password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token = manager.create_access_token(
        data={'sub': username}
    )
    return {'token': access_token}

# @router.post("/{user_id}/workhour/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @router.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items