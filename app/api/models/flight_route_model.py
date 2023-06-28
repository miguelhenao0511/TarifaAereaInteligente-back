from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class FlightRouteModel(Base):
    __tablename__ = "flight_route"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    require_subscription = Column(Boolean)