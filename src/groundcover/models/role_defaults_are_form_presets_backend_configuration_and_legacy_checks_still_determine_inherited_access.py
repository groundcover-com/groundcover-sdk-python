from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_defaults_are_form_presets_backend_configuration_and_legacy_checks_still_determine_inherited_access_additional_property import (
    RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccessAdditionalProperty,
)

T = TypeVar("T", bound="RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccess")


@_attrs_define
class RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccess:
    """ """

    additional_properties: dict[
        str,
        RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccessAdditionalProperty,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        role_defaults_are_form_presets_backend_configuration_and_legacy_checks_still_determine_inherited_access = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccessAdditionalProperty(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        role_defaults_are_form_presets_backend_configuration_and_legacy_checks_still_determine_inherited_access.additional_properties = additional_properties
        return role_defaults_are_form_presets_backend_configuration_and_legacy_checks_still_determine_inherited_access

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccessAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccessAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
