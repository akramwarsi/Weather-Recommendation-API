from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.base_schema import Blank
from app.schema.recommendation_schema import FindRecommendation, FindRecommendationResult, UpsertRecommendation, Recommendation, MatchRecommendation
from app.services.recommendation_service import RecommendationService

router = APIRouter(prefix="/recommendation", tags=["recommendation"])


@router.get("", summary="Get the list of Recommendations", response_model=FindRecommendationResult)
@inject
async def get_recommendation_list(
    find_query: FindRecommendation = Depends(),
    service: RecommendationService = Depends(Provide[Container.recommendation_service]),
):
    return service.get_list(find_query)

@router.get("/Testing", summary="Get Filtered Recommendations", response_model=Recommendation)
@inject
async def get_recommendation_filter(
    find_query: MatchRecommendation = Depends(),
    service: RecommendationService = Depends(Provide[Container.recommendation_service]),
):
    return service.get_recommendation(find_query.temperature, find_query.feel)

@router.get("/{id}", response_model=Recommendation)
@inject
async def get_recommendation(
    id: int,
    service: RecommendationService = Depends(Provide[Container.recommendation_service]),
):
    return service.get_by_id(id)


@router.post("", response_model=Recommendation)
@inject
async def create_recommendation(
    recommendation: UpsertRecommendation,
    service: RecommendationService = Depends(Provide[Container.recommendation_service]),
):
    return service.add(recommendation)


@router.patch("/{id}", response_model=Recommendation)
@inject
async def update_recommendation(
    id: int,
    recommendation: UpsertRecommendation,
    service: RecommendationService = Depends(Provide[Container.recommendation_service]),
):
    return service.patch(id, recommendation)


@router.delete("/{id}", response_model=Blank)
@inject
async def delete_recommendation(
    id: int,
    service: RecommendationService = Depends(Provide[Container.recommendation_service]),
):
    return service.remove_by_id(id)
