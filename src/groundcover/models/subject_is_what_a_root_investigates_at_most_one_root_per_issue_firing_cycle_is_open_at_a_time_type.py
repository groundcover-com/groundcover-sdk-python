from __future__ import annotations

from enum import Enum


class SubjectIsWhatARootInvestigatesAtMostOneRootPerIssueFiringCycleIsOpenAtATimeType(str, Enum):
    ISSUE = "issue"

    def __str__(self) -> str:
        return str(self.value)
