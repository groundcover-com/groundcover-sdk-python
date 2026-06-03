from __future__ import annotations

from enum import Enum


class DisplayModelControlsHowTheMonitorIsPresentedTemplateLanguage(str, Enum):
    JINJA2 = "jinja2"

    def __str__(self) -> str:
        return str(self.value)
