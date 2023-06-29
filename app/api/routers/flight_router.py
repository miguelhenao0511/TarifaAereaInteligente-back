from fastapi import APIRouter, Request, Response
from app.api.services import flight_route_service, airline_service, user_service
from modelo.logica import Datos_Pronostico, Fecha
from datetime import datetime

router = APIRouter()

@router.get("/airlines")
def get_airlines(request: Request):
    auth = request.headers.get("Auth")
    if (auth == None):
        return airline_service.get_all()
    user_service.openConnection()
    user = user_service.getById(auth)
    if (user == None or user.active_subscription == False):
        user_service.closeConnection()
        return airline_service.get_all()
    user_service.closeConnection()
    return airline_service.get_all_with_subscription()

@router.get("/routes")
def get_routes(request: Request):
    auth = request.headers.get("Auth")
    if (auth == None):
        return flight_route_service.get_all()
    user_service.openConnection()
    user = user_service.getById(auth)
    if (user == None or user.active_subscription == False):
        user_service.closeConnection()
        return flight_route_service.get_all()
    user_service.closeConnection()
    return flight_route_service.get_all_with_subscription()

@router.post("/prices")
async def get_routes(request: Request, response: Response):
    try:
        data = await request.json()
        airlines = data["airlines"]
        route_from = data["route_from"]
        route_to = data["route_to"]
        steps = data["steps"] if data["steps"] != None else 1
        date = data["date"] if data["date"] != None else datetime.now().strftime('%Y-%m-%d')
        days = data["days"] if data["days"] != None or data["days"] != "" else 1
        dates = Fecha(date, days)
        predicts = []
        for airline in airlines:
            predicts.append({"airline": airline, "prices": Datos_Pronostico(airline, route_from, route_to, steps, date, days)})
        return {
            "airlines": airlines,
            "route_from": route_from,
            "route_to": route_to,
            "steps": steps,
            "date": date,
            "days": days,
            "dates": dates,
            "prices": predicts  
            }
    except:
        response.status_code = 500    
        return {"messages": "Failed to get prices"}
