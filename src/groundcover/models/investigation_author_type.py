from __future__ import annotations

from enum import Enum


class InvestigationAuthorType(str, Enum):
    AGENT = "agent"
    SERVICE_ACCOUNT = "service_account"
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
