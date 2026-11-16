from __future__ import annotations

from enum import Enum


class ProfilingRuleResponseIsAStoredProfilingRuleOrigin(str, Enum):
    AGENT = "agent"
    API = "api"
    TERRAFORM = "terraform"
    UI = "ui"

    def __str__(self) -> str:
        return str(self.value)
