from sqlmodel import Field

from app.model.base_model import BaseModel


class Recommendation(BaseModel, table=True):
    min_temperature: float = Field()
    max_temperature: float = Field()
    feel: str = Field(default="UNKNOWN", nullable=False)
    outfit: str = Field(default="", nullable=True)
    activity: str = Field(default=None, nullable=True)
