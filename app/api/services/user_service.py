from app.api.conifg.database import SessionLocal
from app.api.models.user_model import UserModel


db = None
def openConnection():
    global db
    db = SessionLocal()

def closeConnection():
    global db
    if db is not None:
        db.close()
        db = None
    
def getById(id):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    return user

def getByEmail(email):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    return user

def addUser(user: UserModel):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def updateUser(user: UserModel):
    db.merge(user)
    db.commit()
    db.refresh(user)
    return user