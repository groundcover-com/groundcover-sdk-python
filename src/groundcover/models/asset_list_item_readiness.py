from __future__ import annotations

from enum import Enum


class AssetListItemReadiness(str, Enum):
    MIGRATED = "migrated"
    MISSING_DATA = "missing_data"
    NEEDS_REVIEW = "needs_review"
    NOT_EVALUATED = "not_evaluated"
    READY = "ready"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
