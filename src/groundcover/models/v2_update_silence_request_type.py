from __future__ import annotations

from enum import Enum


class V2UpdateSilenceRequestType(str, Enum):
    ONE_TIME = "one_time"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
