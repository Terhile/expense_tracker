
from fastapi import APIRouter

from api.v1.endpoints import expense_routes
from api.v1.endpoints import users_routes


api_routes = APIRouter()
api_routes.include_router(users_routes.router)
api_routes.include_router(expense_routes.router)
