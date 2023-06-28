from fastapi import APIRouter, Request, Response
from app.api.services import user_service
from app.api.models.user_model import UserModel
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login")
async def login(request: Request, response: Response):
    data = await request.json()
    user = user_service.getByEmail(data["email"])
    if (user != None and pwd_context.verify(data["password"], user.password)):
        return {"message": "Login success", "user": user}
    response.status_code = 400
    return {"message": "Invalid user/password"}

@router.post("/logout")
def logout():
    return {"message": "logout"}


@router.post("/user")
async def login(request: Request, response: Response):
    data = await request.json()
    user = user_service.getByEmail(data["email"])
    if (user == None):
        new_user = UserModel(first_name = data["first_name"], last_name = data["last_name"], email = data["email"], password = pwd_context.hash(data["password"]), active_subscription = False)
        new_user = user_service.addUser(new_user)
        return {"message": "Create user successfully!!", "user": new_user}
    response.status_code = 400
    return {"message": "Email already exists!!"}

@router.put("/user/{id}")
async def login(request: Request, response: Response, id):
    user = user_service.getById(id)
    if (user != None):
        data = await request.json()
        if (data["first_name"] != user.first_name):
            user.first_name = data["first_name"]
        if (data["last_name"] != user.last_name):
            user.last_name = data["last_name"]
        if (data["email"] != user.email):
            user.email = data["email"]
        if (data["password"] != ""):
            user.password = pwd_context.hash(data["password"])
        user = user_service.updateUser(user)
        return {"message": "Update user successfully!!", "user": user}
        
    response.status_code = 404
    return {"message": "User not found"}

@router.put("/user/{id}/activate_subscription")
async def login(request: Request, response: Response, id):
    user = user_service.getById(id)
    if (user != None):
        user.active_subscription = True
        user = user_service.updateUser(user)
        return {"message": "Activate subscription successfully!!", "user": user}
        
    response.status_code = 404
    return {"message": "User not found"}

@router.put("/user/{id}/deactivate_subscription")
async def login(request: Request, response: Response, id):
    user = user_service.getById(id)
    if (user != None):
        user.active_subscription = False
        user = user_service.updateUser(user)
        return {"message": "Activate subscription successfully!!", "user": user}
        
    response.status_code = 404
    return {"message": "User not found"}