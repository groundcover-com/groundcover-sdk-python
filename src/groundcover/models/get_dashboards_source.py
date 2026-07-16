from __future__ import annotations

from enum import Enum


class GetDashboardsSource(str, Enum):
    GC_CATALOG = "gc-catalog"
    REGULAR = "regular"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
