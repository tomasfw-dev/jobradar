from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.models.enums import SearchModality, SearchSeniority


class SearchCreate(BaseModel):
    query: str = Field(max_length=200)
    location: str | None = Field(default=None, max_length=200)
    modality: SearchModality = SearchModality.ALL
    seniority: SearchSeniority = SearchSeniority.ALL

    @field_validator("query", mode="before")
    @classmethod
    def strip_query(cls, value: object) -> object:
        if isinstance(value, str):
            return value.strip()
        return value

    @field_validator("query")
    @classmethod
    def reject_empty_query(cls, value: str) -> str:
        if not value:
            raise ValueError("query must not be empty")
        return value

    @field_validator("location", mode="before")
    @classmethod
    def normalize_location(cls, value: object) -> object:
        if value is None:
            return None
        if isinstance(value, str):
            stripped = value.strip()
            return stripped or None
        return value


class SearchResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    query: str
    location: str | None
    modality: SearchModality
    seniority: SearchSeniority
    created_at: datetime
    updated_at: datetime
