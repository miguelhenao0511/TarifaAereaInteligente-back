from app.api.conifg.database import SessionLocal
from app.api.models.flight_route_model import FlightRouteModel

def get_all():
    db = SessionLocal()
    flight_routes = db.query(FlightRouteModel).all()
    return flight_routes