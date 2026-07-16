from __future__ import annotations

from enum import Enum


class ClaudeSendEventRequestIsTheRequestBodyForSendingASessionEventType(str, Enum):
    USER_INTERRUPT = "user.interrupt"
    USER_MESSAGE = "user.message"
    USER_TOOL_CONFIRMATION = "user.tool_confirmation"

    def __str__(self) -> str:
        return str(self.value)
