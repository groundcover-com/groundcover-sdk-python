from __future__ import annotations

from enum import Enum


class SessionDetailsRequestParamsCategory(str, Enum):
    MOBILE_RUM = "mobile-rum"
    RUM = "rum"

    def __str__(self) -> str:
        return str(self.value)
