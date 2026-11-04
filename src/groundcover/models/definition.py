from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.definition_permissions_item import DefinitionPermissionsItem
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_defaults_are_form_presets_backend_configuration_and_legacy_checks_still_determine_inherited_access import (
        RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccess,
    )


T = TypeVar("T", bound="Definition")


@_attrs_define
class Definition:
    """
    Attributes:
        defaults (RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccess | Unset):
        permissions (list[DefinitionPermissionsItem] | Unset):
    """

    defaults: RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccess | Unset = UNSET
    permissions: list[DefinitionPermissionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        defaults: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value
                permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_defaults_are_form_presets_backend_configuration_and_legacy_checks_still_determine_inherited_access import (
            RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccess,
        )

        d = dict(src_dict)
        _defaults = d.pop("defaults", UNSET)
        defaults: RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccess | Unset
        if isinstance(_defaults, Unset) or _defaults is None:
            defaults = UNSET
        else:
            defaults = (
                RoleDefaultsAreFormPresetsBackendConfigurationAndLegacyChecksStillDetermineInheritedAccess.from_dict(
                    _defaults
                )
            )

        _permissions = d.pop("permissions", UNSET)
        permissions: list[DefinitionPermissionsItem] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = DefinitionPermissionsItem(permissions_item_data)

                permissions.append(permissions_item)

        definition = cls(
            defaults=defaults,
            permissions=permissions,
        )

        definition.additional_properties = d
        return definition

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
