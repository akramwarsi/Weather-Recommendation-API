from contextlib import AbstractContextManager
from typing import Callable
from app.core.exceptions import DuplicatedError, NotFoundError

from sqlalchemy.orm import Session

from app.model.recommendation import Recommendation
from app.repository.base_repository import BaseRepository


class RecommendationRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        self.model = Recommendation
        super().__init__(session_factory, Recommendation)

    def read_by_conditions(self, temperature, feel):
        
        with self.session_factory() as session:
            query = session.query(self.model)
            query = query.filter(feel.lower() == self.model.feel).filter(self.model.min_temperature < temperature).filter(self.model.max_temperature > temperature).first()
            return query
