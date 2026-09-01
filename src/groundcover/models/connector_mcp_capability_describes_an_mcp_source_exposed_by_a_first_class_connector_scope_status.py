from __future__ import annotations

from enum import Enum


class ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnectorScopeStatus(str, Enum):
    FULL = "full"
    PARTIAL = "partial"

    def __str__(self) -> str:
        return str(self.value)
