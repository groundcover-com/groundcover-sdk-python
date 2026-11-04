from __future__ import annotations

from enum import Enum


class SyncTargetAttachmentAnswersAnAttachTheRootAndWhatBecameOfTheThreadOutcome(str, Enum):
    ALREADY_ATTACHED = "already_attached"
    ATTACHED = "attached"
    ATTACHED_TO_ANOTHER_ROOT = "attached_to_another_root"

    def __str__(self) -> str:
        return str(self.value)
