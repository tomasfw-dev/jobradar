from sqlalchemy.orm import Session

from app.models.search import Search
from app.schemas.search import SearchCreate


def create_search(db: Session, data: SearchCreate) -> Search:
    search = Search(
        query=data.query,
        location=data.location,
        modality=data.modality,
        seniority=data.seniority,
    )
    db.add(search)
    try:
        db.commit()
        db.refresh(search)
    except Exception:
        db.rollback()
        raise
    return search
