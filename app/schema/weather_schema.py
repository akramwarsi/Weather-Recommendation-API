from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.schema.recommendation_schema import RecommendationResult
from app.util.schema import AllOptional


class BaseWeather(BaseModel):
    temperature: str
    description: str
    kind: str


class FindWeather(BaseModel):
    city: str


class FindWeatherSummary(BaseModel):
    id: str
    weather: Optional[BaseWeather]
    recommendation: Optional[RecommendationResult]
    synopsis: Optional[str]