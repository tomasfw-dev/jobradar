from fastapi import FastAPI
from pydantic import BaseModel

from app.api.routes.searches import router as searches_router


class HealthResponse(BaseModel):
    status: str
    service: str


app = FastAPI(title="JobRadar API", version="0.1.0")
app.include_router(searches_router)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="jobradar-api")
