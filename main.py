from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modelo.logica import Predic
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hola, mundo!"}



@app.get("/flights")
async def get_flights(airline= None, source= None, destiny= None, steps= None, date= None):
    dateObject = datetime.strptime(date, '%Y-%m-%d')
    if date:
        return [{
            "name": "test flight 1",
            "airline": airline,
            "source": source,
            "destiny": destiny,
            "steps": steps,
            "date": date,
            "price": Predic(airline,source,destiny,int(steps),dateObject.day,dateObject.month,dateObject.year)
        }]

    else:
        return [{
            "name": "test flight 1",
            "airline": airline,
            "source": source,
            "destiny": destiny,
            "steps": steps,
            "date": date,
            "price": 0
        }]
