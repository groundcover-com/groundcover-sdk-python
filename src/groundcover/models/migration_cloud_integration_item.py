from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MigrationCloudIntegrationItem")


@_attrs_define
class MigrationCloudIntegrationItem:
    """
    Attributes:
        conversion_status (str): The conversion status for this integration.
        install_state (str): The install state for this integration.
        integration_name (str): The integration name/identifier.
        provider (str): The cloud provider type.
        converted_payload (str | Unset): The converted payload.
    """

    conversion_status: str
    install_state: str
    integration_name: str
    provider: str
    converted_payload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversion_status = self.conversion_status

        install_state = self.install_state

        integration_name = self.integration_name

        provider = self.provider

        converted_payload = self.converted_payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversionStatus": conversion_status,
                "installState": install_state,
                "integrationName": integration_name,
                "provider": provider,
            }
        )
        if converted_payload is not UNSET:
            field_dict["convertedPayload"] = converted_payload

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
        conversion_status = d.pop("conversionStatus")

        install_state = d.pop("installState")

        integration_name = d.pop("integrationName")

        provider = d.pop("provider")

        converted_payload = d.pop("convertedPayload", UNSET)

        migration_cloud_integration_item = cls(
            conversion_status=conversion_status,
            install_state=install_state,
            integration_name=integration_name,
            provider=provider,
            converted_payload=converted_payload,
        )

        migration_cloud_integration_item.additional_properties = d
        return migration_cloud_integration_item

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
