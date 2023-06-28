from app.api.conifg.database import SessionLocal
from app.api.models.flight_route_model import FlightRouteModel

db = SessionLocal()

def get_all():
    flight_routes = db.query(FlightRouteModel).filter(FlightRouteModel.require_subscription == False).all()
    return flight_routes

def get_all_with_subscription():
    airlines = db.query(FlightRouteModel).all()
    return airlines