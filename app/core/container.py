from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository import *
from app.services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.recommendation",
            "app.api.v1.endpoints.weather",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)
    recommendation_repository = providers.Factory(RecommendationRepository, session_factory=db.provided.session)
    recommendation_service = providers.Factory(RecommendationService, recommendation_repository=recommendation_repository)
