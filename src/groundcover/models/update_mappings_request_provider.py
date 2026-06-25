from __future__ import annotations

from enum import Enum


class UpdateMappingsRequestProvider(str, Enum):
    CORALOGIX = "coralogix"
    DATADOG = "datadog"

    def __str__(self) -> str:
        return str(self.value)
