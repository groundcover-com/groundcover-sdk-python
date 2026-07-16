from __future__ import annotations

from enum import Enum


class ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventResult(str, Enum):
    ALLOW = "allow"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
