from __future__ import annotations

from enum import Enum


class AssetFindingSuggestionIsTheTopSuggestedFixCarriedOnAFindingKind(str, Enum):
    KEY = "key"
    METRIC = "metric"
    VALUE = "value"

    def __str__(self) -> str:
        return str(self.value)
