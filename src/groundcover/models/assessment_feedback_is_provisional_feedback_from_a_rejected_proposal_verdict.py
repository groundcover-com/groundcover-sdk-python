from __future__ import annotations

from enum import Enum


class AssessmentFeedbackIsProvisionalFeedbackFromARejectedProposalVerdict(str, Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
