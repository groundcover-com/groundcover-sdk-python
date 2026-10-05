from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TenantConnectorSettingsResponse")


@_attrs_define
class TenantConnectorSettingsResponse:
    """
    Attributes:
        new_connectors_enabled_by_default (bool | Unset): Whether connectors that first appear on a backend (for example
            in a later
            release) start enabled. Existing connectors are never changed.
    """

    new_connectors_enabled_by_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_connectors_enabled_by_default = self.new_connectors_enabled_by_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_connectors_enabled_by_default is not UNSET:
            field_dict["newConnectorsEnabledByDefault"] = new_connectors_enabled_by_default

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
        new_connectors_enabled_by_default = d.pop("newConnectorsEnabledByDefault", UNSET)

        tenant_connector_settings_response = cls(
            new_connectors_enabled_by_default=new_connectors_enabled_by_default,
        )

        tenant_connector_settings_response.additional_properties = d
        return tenant_connector_settings_response

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
