from __future__ import annotations

from enum import Enum


class MissingGroundcoverIntegrationKind(str, Enum):
    CONNECTOR = "connector"
    DATA_SOURCE = "data_source"

    def __str__(self) -> str:
        return str(self.value)
