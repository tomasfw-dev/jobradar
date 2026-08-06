import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

import app.models  # noqa: F401
from app.db.base import Base
from app.db.dependencies import get_db
from app.main import app

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


def test_create_search_returns_201_and_expected_data(client):
    response = client.post(
        "/searches",
        json={
            "query": "Python Developer",
            "location": "Buenos Aires",
            "modality": "remote",
            "seniority": "junior",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["query"] == "Python Developer"
    assert data["location"] == "Buenos Aires"
    assert data["modality"] == "remote"
    assert data["seniority"] == "junior"
    assert isinstance(data["id"], int)
    assert data["created_at"] is not None
    assert data["updated_at"] is not None


def test_create_search_defaults_to_all(client):
    response = client.post("/searches", json={"query": "Node.js"})

    assert response.status_code == 201
    data = response.json()
    assert data["modality"] == "all"
    assert data["seniority"] == "all"
    assert data["location"] is None


def test_create_search_strips_query(client):
    response = client.post("/searches", json={"query": "  FastAPI  "})

    assert response.status_code == 201
    assert response.json()["query"] == "FastAPI"


def test_create_search_empty_location_becomes_null(client):
    response = client.post(
        "/searches",
        json={"query": "Backend", "location": "   "},
    )

    assert response.status_code == 201
    assert response.json()["location"] is None


def test_create_search_whitespace_query_returns_422(client):
    response = client.post("/searches", json={"query": "   "})

    assert response.status_code == 422


def test_create_search_invalid_modality_returns_422(client):
    response = client.post(
        "/searches",
        json={"query": "Backend", "modality": "invalid"},
    )

    assert response.status_code == 422
