from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    SmallInteger,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import SearchRunStatus

if TYPE_CHECKING:
    from app.models.search import Search


class SearchRun(Base):
    __tablename__ = "search_runs"
    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'running', 'completed', 'failed')",
            name="ck_search_runs_status",
        ),
        CheckConstraint(
            "progress >= 0 AND progress <= 100",
            name="ck_search_runs_progress_range",
        ),
        CheckConstraint(
            "total_found >= 0",
            name="ck_search_runs_total_found_nonnegative",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    search_id: Mapped[int] = mapped_column(
        ForeignKey("searches.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    status: Mapped[SearchRunStatus] = mapped_column(
        Enum(
            SearchRunStatus,
            name="ck_search_runs_status",
            native_enum=False,
            create_constraint=False,
            values_callable=lambda enum: [member.value for member in enum],
        ),
        nullable=False,
        default=SearchRunStatus.PENDING,
        server_default=SearchRunStatus.PENDING.value,
    )
    progress: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
        default=0,
        server_default="0",
    )
    total_found: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default="0",
    )
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    search: Mapped[Search] = relationship(back_populates="runs")
