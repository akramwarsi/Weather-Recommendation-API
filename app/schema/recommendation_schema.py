from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.util.schema import AllOptional


class BaseRecommendation(BaseModel):
    min_temperature: float
    max_temperature: float
    feel: str
    outfit: str
    activity: str

    class Config:
        orm_mode = True


class RecommendationResult(BaseModel):
    outfit: str
    activity: str


class Recommendation(ModelBaseInfo, BaseRecommendation, metaclass=AllOptional):
    ...


class FindRecommendation(FindBase, BaseRecommendation, metaclass=AllOptional):
    email__eq: str
    ...


class UpsertRecommendation(BaseRecommendation, metaclass=AllOptional):
    ...


class FindRecommendationResult(BaseModel):
    founds: Optional[List[Recommendation]]
    search_options: Optional[SearchOptions]

class MatchRecommendation(BaseModel):
    temperature: float
    feel: str
