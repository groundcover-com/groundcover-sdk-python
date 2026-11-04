from __future__ import annotations

from enum import Enum


class AttachSyncTargetRequestAttachesASlackThreadToARootSoTheRootsUpdatesArePostedThereProvider(str, Enum):
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
