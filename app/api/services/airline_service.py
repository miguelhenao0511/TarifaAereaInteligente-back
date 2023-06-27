from app.api.conifg.database import SessionLocal
from app.api.models.airline_model import AirlineModel

def get_all():
    db = SessionLocal()
    airlines = db.query(AirlineModel).all()
    return airlines