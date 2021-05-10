from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas, config
from app.dependency import get_db
from app.auth import login_manager
from sqlalchemy.orm import Session
from typing import List

from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

import bcrypt
from datetime import datetime, timedelta

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
    user.password = bcrypt.hashpw(bytes(user.password, 'utf-8'), bcrypt.gensalt())
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/test")
def test_bcrpt():
    password = "123"
    bpassword = bytes(password, 'utf-8')
    password2 = "122"
    bpassword2 = bytes(password2, 'utf-8')
    hpassword = bcrypt.hashpw(bpassword, bcrypt.gensalt())
    return {
        "password": password,
        "bpassword": bpassword,
        "hpassword": hpassword,
        "len bpassword": len(bpassword),
        "len hpassword": len(hpassword),
        "check hpassword": bcrypt.checkpw(bpassword, hpassword),
        "check hpassword2": bcrypt.checkpw(bpassword2, hpassword)
    }

@router.get('/protected', response_model=schemas.User)
def protected_route(user=Depends(login_manager)):
    return user

@router.post('/login', response_model=schemas.UserToken)
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = data.username
    password = data.password
    user = crud.get_user_by_username(db, username=username)
    if not user:
        raise HTTPException(status_code=400, detail="Username not found")
    elif not bcrypt.checkpw(bytes(data.password, 'utf-8'), bytes(user.password, 'utf-8')):
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token = login_manager.create_access_token(
        data={'sub': user.id},
        expires=timedelta(hours=24)
    )
    user.token = access_token
    user.expiration = datetime.now() + timedelta(hours=24)
    return user
    # return {'token': access_token}

@router.get("/{user_id}", response_model=schemas.UserFull)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user




# @router.get('/v/protected')
# def protected_route():
#     return {'user': "user"}

# @router.post("/{user_id}/workhour/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @router.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items