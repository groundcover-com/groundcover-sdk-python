from __future__ import annotations

from enum import Enum


class SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFromType(str, Enum):
    AUTOMATION = "automation"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
