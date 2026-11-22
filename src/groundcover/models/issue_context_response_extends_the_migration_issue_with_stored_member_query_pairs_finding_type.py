from __future__ import annotations

from enum import Enum


class IssueContextResponseExtendsTheMigrationIssueWithStoredMemberQueryPairsFindingType(str, Enum):
    MISSING_KEY = "missing_key"
    MISSING_METRIC = "missing_metric"
    MISSING_VALUE = "missing_value"
    NO_DATA = "no_data"

    def __str__(self) -> str:
        return str(self.value)
