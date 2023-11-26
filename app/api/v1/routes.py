from fastapi import APIRouter

from app.api.v1.endpoints.recommendation import router as recommendation_router
from app.api.v1.endpoints.weather import router as weather_router

routers = APIRouter()
router_list = [recommendation_router, weather_router]

for router in router_list:
    routers.include_router(router)
