from fastapi import APIRouter
from app.api.services import flight_route_service, airline_service

router = APIRouter()

@router.get("/airlines")
def get_airlines():
    return airline_service.get_all()

@router.get("/routes")
def get_routes():
    return flight_route_service.get_all()