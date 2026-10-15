from __future__ import annotations

from enum import Enum


class InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssueAlreadyHasAnOpenRootToJoinCode(str, Enum):
    INVESTIGATION_EXISTS = "INVESTIGATION_EXISTS"

    def __str__(self) -> str:
        return str(self.value)
