from fastapi_login import LoginManager
from workhour import config
from workhour.database import SessionLocal
from workhour import models

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