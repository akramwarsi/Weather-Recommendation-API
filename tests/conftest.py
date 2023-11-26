import json
import os

import pytest

os.environ["ENV"] = "test"

if os.getenv("ENV") not in ["test"]:
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)

from fastapi.testclient import TestClient
from loguru import logger
from sqlmodel import SQLModel, create_engine

from app.core.config import configs
from app.core.container import Container
from app.main import AppCreator
from app.model.recommendation import Recommendation


def insert_default_data(conn):
    recommendation_default_file = open("./tests/test_data/recommendations.json", "r")
    recommendation_default_data = json.load(recommendation_default_file)
    for recommendation in recommendation_default_data:
        conn.execute(
            Recommendation.__table__.insert(),
            {
                "min_temperature": recommendation["min_temperature"],
                "max_temperature": recommendation["max_temperature"],
                "feel": recommendation["feel"],
                "outfit": recommendation["outfit"],
                "activity": recommendation["activity"]
            },
        )


def reset_db():
    engine = create_engine(configs.DATABASE_URI)
    logger.info(engine)
    with engine.begin() as conn:
        if "test" in configs.DATABASE_URI:
            SQLModel.metadata.drop_all(conn)
            SQLModel.metadata.create_all(conn)
            insert_default_data(conn)
        else:
            raise Exception("Not in test environment")
    return engine


@pytest.fixture
def client():
    reset_db()
    app_creator = AppCreator()
    app = app_creator.app
    with TestClient(app) as client:
        yield client


@pytest.fixture
def container():
    return Container()


@pytest.fixture
def test_name(request):
    return request.node.name
