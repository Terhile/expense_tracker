from fastapi import FastAPI
from api.v1 import routers
from database import models
from database.crud.crud_base import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(routers.api_routes)


@app.get("/home")
async def home(skip: int = 0, limit: int = 10):
    return {"message": "welcome to daily expense tracker api"}
