from __future__ import annotations

from enum import Enum


class ConnectorMCPCapabilityDescribesAnMCPSourceExposedByAFirstClassConnectorAuthState(str, Enum):
    AWAITING_AUTH = "awaiting_auth"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
