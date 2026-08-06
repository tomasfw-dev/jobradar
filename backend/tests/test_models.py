from sqlalchemy import CheckConstraint

from app.db.base import Base
from app.models import Search, SearchRun
from app.models.enums import SearchModality, SearchRunStatus, SearchSeniority


def test_table_names():
    assert Search.__tablename__ == "searches"
    assert SearchRun.__tablename__ == "search_runs"


def test_models_registered_in_metadata():
    assert "searches" in Base.metadata.tables
    assert "search_runs" in Base.metadata.tables


def test_search_run_foreign_key_references_search():
    foreign_keys = list(SearchRun.__table__.c.search_id.foreign_keys)
    assert len(foreign_keys) == 1

    foreign_key = foreign_keys[0]
    assert foreign_key.column.table.name == "searches"
    assert foreign_key.column.name == "id"
    assert foreign_key.ondelete == "CASCADE"


def test_search_run_check_constraints_exist():
    check_names = {
        constraint.name
        for constraint in SearchRun.__table__.constraints
        if isinstance(constraint, CheckConstraint)
    }

    assert "ck_search_runs_progress_range" in check_names
    assert "ck_search_runs_total_found_nonnegative" in check_names


def test_enum_values():
    assert SearchModality.ALL.value == "all"
    assert SearchModality.REMOTE.value == "remote"
    assert SearchModality.HYBRID.value == "hybrid"
    assert SearchModality.ONSITE.value == "onsite"

    assert SearchSeniority.ALL.value == "all"
    assert SearchSeniority.TRAINEE.value == "trainee"
    assert SearchSeniority.JUNIOR.value == "junior"
    assert SearchSeniority.SEMI_SENIOR.value == "semi-senior"
    assert SearchSeniority.SENIOR.value == "senior"

    assert SearchRunStatus.PENDING.value == "pending"
    assert SearchRunStatus.RUNNING.value == "running"
    assert SearchRunStatus.COMPLETED.value == "completed"
    assert SearchRunStatus.FAILED.value == "failed"
