from enum import Enum


class SearchModality(str, Enum):
    ALL = "all"
    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"


class SearchSeniority(str, Enum):
    ALL = "all"
    TRAINEE = "trainee"
    JUNIOR = "junior"
    SEMI_SENIOR = "semi-senior"
    SENIOR = "senior"


class SearchRunStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
