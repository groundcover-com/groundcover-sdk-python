from __future__ import annotations

from enum import Enum


class PermissionsContainsExplicitOverridesOnlyAMissingFeatureInheritsLegacyAuthorizationAdditionalProperty(str, Enum):
    EDIT = "edit"
    NO_ACCESS = "no_access"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
