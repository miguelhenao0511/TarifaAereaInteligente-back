from app.api.conifg.database import SessionLocal
from app.api.models.airline_model import AirlineModel

db = SessionLocal()

def get_all():
    airlines = db.query(AirlineModel).filter(AirlineModel.require_subscription == False).all()
    return airlines

def get_all_with_subscription():
    airlines = db.query(AirlineModel).all()
    return airlines