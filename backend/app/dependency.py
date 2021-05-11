from app.database import SessionLocal
from app import models
import bcrypt

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_default_data():
	hpassword = bcrypt.hashpw(bytes("password123", 'utf-8'), bcrypt.gensalt())
	db = SessionLocal()
	objects = [
	    models.User(username="Archie", fullname="Archibald Weng", password=hpassword),
	    models.User(username="Boris", fullname="Boris Tien", password=hpassword),
	    models.User(username="Larry", fullname="Larry Chuang", password=hpassword),
	    models.Task(taskname="TIIP", fullname="TIIP-全方位減碳系統服務平台開發計畫", organization="永智"),
	    models.Task(taskname="瑞振工業-盤查及SBTi專案", fullname="瑞振工業溫室氣體管理專案", organization="瑞振工業公司"),
	    models.Task(taskname="108台電-碳限制計畫", fullname="台電公司碳限制管理及對策研析計畫", organization="台灣電力股份有限公司環境保護處"),

	]
	db.bulk_save_objects(objects)
	db.commit()
	# db.refresh(db_user)
	db.close()