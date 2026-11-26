from __future__ import annotations

from enum import Enum


class ExplainResponseIsAnExplainsStateResultIsSetOnceTheStatusIsSucceededStatus(str, Enum):
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    TIMED_OUT = "timed_out"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
