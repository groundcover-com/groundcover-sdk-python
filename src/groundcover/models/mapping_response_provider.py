from __future__ import annotations

from enum import Enum


class MappingResponseProvider(str, Enum):
    CORALOGIX = "coralogix"
    DATADOG = "datadog"

    def __str__(self) -> str:
        return str(self.value)
