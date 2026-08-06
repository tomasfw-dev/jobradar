from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import SearchModality, SearchSeniority

if TYPE_CHECKING:
    from app.models.search_run import SearchRun


class Search(Base):
    __tablename__ = "searches"

    id: Mapped[int] = mapped_column(primary_key=True)
    query: Mapped[str] = mapped_column(String(200), nullable=False)
    location: Mapped[str | None] = mapped_column(String(200), nullable=True)
    modality: Mapped[SearchModality] = mapped_column(
        Enum(
            SearchModality,
            name="ck_searches_modality",
            native_enum=False,
            create_constraint=True,
            values_callable=lambda enum: [member.value for member in enum],
        ),
        nullable=False,
        default=SearchModality.ALL,
        server_default=SearchModality.ALL.value,
    )
    seniority: Mapped[SearchSeniority] = mapped_column(
        Enum(
            SearchSeniority,
            name="ck_searches_seniority",
            native_enum=False,
            create_constraint=True,
            values_callable=lambda enum: [member.value for member in enum],
        ),
        nullable=False,
        default=SearchSeniority.ALL,
        server_default=SearchSeniority.ALL.value,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    runs: Mapped[list[SearchRun]] = relationship(
        back_populates="search",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
