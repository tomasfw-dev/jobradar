from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.repositories.search_repository import create_search
from app.schemas.search import SearchCreate, SearchResponse

router = APIRouter(prefix="/searches", tags=["searches"])


@router.post("", status_code=201, response_model=SearchResponse)
def create_search_endpoint(
    data: SearchCreate,
    db: Session = Depends(get_db),
) -> SearchResponse:
    search = create_search(db, data)
    return SearchResponse.model_validate(search)
