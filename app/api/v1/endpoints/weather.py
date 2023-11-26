from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.base_schema import Blank
from app.schema.weather_schema import FindWeather, FindWeatherSummary, BaseWeather
from app.schema.recommendation_schema import RecommendationResult
from app.services.recommendation_service import RecommendationService
from app.util.weather_client import get_weather
from app.util.synopsis import summarize

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("", summary="Get Weather Summary & Recommendations by City", response_model=FindWeatherSummary)
@inject
async def get_weather_suummary(
    find_query: FindWeather = Depends(),
    service: RecommendationService = Depends(Provide[Container.recommendation_service]),
):
    weather_update = await get_weather(find_query.city)
    recommendation = service.get_recommendation(weather_update.temperature, weather_update.kind)
    recommendationresult = RecommendationResult(outfit=recommendation.outfit, activity=recommendation.activity)
    synopsis = await summarize(weather_update.temperature, weather_update.kind)
    response = FindWeatherSummary(id=find_query.city, weather=weather_update, recommendation=recommendationresult, synopsis=synopsis)

    return response
