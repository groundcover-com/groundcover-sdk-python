from __future__ import annotations

from enum import Enum


class CreateIngestionKeyRequestType(str, Enum):
    RUM = "rum"
    SENSOR = "sensor"
    THIRDPARTY = "thirdParty"

    def __str__(self) -> str:
        return str(self.value)
