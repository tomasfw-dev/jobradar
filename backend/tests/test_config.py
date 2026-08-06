from pydantic_settings import SettingsConfigDict

from app.core.config import Settings, get_settings


def test_settings_can_be_built_with_explicit_values():
    config = Settings(
        _env_file=None,
        POSTGRES_DB="test_db",
        POSTGRES_USER="test_user",
        POSTGRES_PASSWORD="unused",
        POSTGRES_HOST="localhost",
        POSTGRES_PORT=5432,
        REDIS_URL="redis://localhost:6379/0",
        BACKEND_HOST="0.0.0.0",
        BACKEND_PORT=8000,
        FRONTEND_URL="http://localhost:5173",
    )

    assert config.POSTGRES_DB == "test_db"
    assert config.POSTGRES_USER == "test_user"
    assert config.POSTGRES_HOST == "localhost"
    assert config.POSTGRES_PORT == 5432
    assert config.REDIS_URL == "redis://localhost:6379/0"
    assert config.BACKEND_HOST == "0.0.0.0"
    assert config.BACKEND_PORT == 8000
    assert config.FRONTEND_URL == "http://localhost:5173"


def test_get_settings_uses_environment_variables(monkeypatch):
    monkeypatch.setenv("POSTGRES_DB", "env_db")
    monkeypatch.setenv("POSTGRES_USER", "env_user")
    monkeypatch.setenv("POSTGRES_PASSWORD", "unused")
    monkeypatch.setenv("POSTGRES_HOST", "env.host.test")
    monkeypatch.setenv("POSTGRES_PORT", "5432")
    monkeypatch.setenv("REDIS_URL", "redis://env-redis:6379/0")
    monkeypatch.setenv("BACKEND_HOST", "127.0.0.1")
    monkeypatch.setenv("BACKEND_PORT", "9000")
    monkeypatch.setenv("FRONTEND_URL", "http://localhost:3000")
    monkeypatch.setattr(
        Settings,
        "model_config",
        SettingsConfigDict(extra="ignore"),
    )

    get_settings.cache_clear()
    try:
        config = get_settings()

        assert config.POSTGRES_DB == "env_db"
        assert config.POSTGRES_USER == "env_user"
        assert config.POSTGRES_HOST == "env.host.test"
        assert config.POSTGRES_PORT == 5432
        assert config.REDIS_URL == "redis://env-redis:6379/0"
        assert config.BACKEND_HOST == "127.0.0.1"
        assert config.BACKEND_PORT == 9000
        assert config.FRONTEND_URL == "http://localhost:3000"
    finally:
        get_settings.cache_clear()
