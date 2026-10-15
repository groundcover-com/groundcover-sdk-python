from __future__ import annotations

from enum import Enum


class SourceIsWhatOpenedARootInvestigationAtMostOneRootPerIssueIsOpenAtATimeType(str, Enum):
    ISSUE = "issue"

    def __str__(self) -> str:
        return str(self.value)
