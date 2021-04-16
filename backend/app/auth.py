from fastapi_login import LoginManager
from app import config
from app.database import SessionLocal
from app import models

SECRET = config.settings.SECRET
login_manager = LoginManager(SECRET, '/user/login')

@login_manager.user_loader
def get_user(user_id: int):
	db = SessionLocal()
	return db.query(models.User).filter(models.User.id == user_id).first()

# @login_manager.user_loader
# def get_user(username: str):
# 	db = SessionLocal()
# 	return db.query(models.User).filter(models.User.username == username).first()