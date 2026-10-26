from __future__ import annotations

from enum import Enum


class SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATimeType(str, Enum):
    ISSUE = "issue"

    def __str__(self) -> str:
        return str(self.value)
