from __future__ import annotations

from enum import Enum


class SessionsSummaryRequestParamsCategory(str, Enum):
    MOBILE_RUM = "mobile-rum"
    RUM = "rum"

    def __str__(self) -> str:
        return str(self.value)
