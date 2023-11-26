from app.schema.recommendation_schema import RecommendationResult
from app.repository.recommendation_repository import RecommendationRepository
from app.services.base_service import BaseService


class RecommendationService(BaseService):
    def __init__(self, recommendation_repository: RecommendationRepository):
        self.recommendation_repository = recommendation_repository
        super().__init__(recommendation_repository)

    def get_recommendation(self, temperature, feel):
        matching_recommendation = self.recommendation_repository.read_by_conditions(temperature, feel)

        if matching_recommendation:
            return matching_recommendation

        return RecommendationResult(outfit="", activity="")

