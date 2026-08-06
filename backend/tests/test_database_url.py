from app.core.config import Settings
from app.db.session import build_database_url


def test_build_database_url_uses_expected_components():
    config = Settings(
        _env_file=None,
        POSTGRES_DB="jobradar_test",
        POSTGRES_USER="test_user",
        POSTGRES_PASSWORD="unused",
        POSTGRES_HOST="db.example.test",
        POSTGRES_PORT=5432,
        REDIS_URL="redis://localhost:6379/0",
        BACKEND_HOST="0.0.0.0",
        BACKEND_PORT=8000,
        FRONTEND_URL="http://localhost:5173",
    )

    url = build_database_url(config)

    assert url.drivername == "postgresql+psycopg"
    assert url.host == "db.example.test"
    assert url.port == 5432
    assert url.database == "jobradar_test"
