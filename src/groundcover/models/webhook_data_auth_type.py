from __future__ import annotations

from enum import Enum


class WebhookDataAuthType(str, Enum):
    BASIC = "basic"
    BEARER = "bearer"

    def __str__(self) -> str:
        return str(self.value)
