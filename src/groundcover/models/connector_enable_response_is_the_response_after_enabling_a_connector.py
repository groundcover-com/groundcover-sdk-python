from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_enable_response_is_the_response_after_enabling_a_connector_data import (
        ConnectorEnableResponseIsTheResponseAfterEnablingAConnectorData,
    )


T = TypeVar("T", bound="ConnectorEnableResponseIsTheResponseAfterEnablingAConnector")


@_attrs_define
class ConnectorEnableResponseIsTheResponseAfterEnablingAConnector:
    """
    Attributes:
        data (ConnectorEnableResponseIsTheResponseAfterEnablingAConnectorData | Unset): Provider-specific connector
            metadata. Install responses can include provider setup data such as manifest_json and manifest_url.
        id (str | Unset): The credential ID of the org-level enablement Example: 550e8400-e29b-41d4-a716-446655440000.
        name (str | Unset): The credential name Example: org.
        provider (str | Unset): The provider name Example: cursor.
        status (str | Unset): The credential status Example: active.
    """

    data: ConnectorEnableResponseIsTheResponseAfterEnablingAConnectorData | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    provider: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        id = self.id

        name = self.name

        provider = self.provider

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if provider is not UNSET:
            field_dict["provider"] = provider
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_enable_response_is_the_response_after_enabling_a_connector_data import (
            ConnectorEnableResponseIsTheResponseAfterEnablingAConnectorData,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ConnectorEnableResponseIsTheResponseAfterEnablingAConnectorData | Unset
        if isinstance(_data, Unset) or _data is None:
            data = UNSET
        else:
            data = ConnectorEnableResponseIsTheResponseAfterEnablingAConnectorData.from_dict(_data)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        provider = d.pop("provider", UNSET)

        status = d.pop("status", UNSET)

        connector_enable_response_is_the_response_after_enabling_a_connector = cls(
            data=data,
            id=id,
            name=name,
            provider=provider,
            status=status,
        )

        connector_enable_response_is_the_response_after_enabling_a_connector.additional_properties = d
        return connector_enable_response_is_the_response_after_enabling_a_connector

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
