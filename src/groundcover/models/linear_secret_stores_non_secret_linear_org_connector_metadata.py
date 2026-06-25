from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="LinearSecretStoresNonSecretLinearOrgConnectorMetadata")


@_attrs_define
class LinearSecretStoresNonSecretLinearOrgConnectorMetadata:
    """
    Attributes:
        connector_id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        workspace_id (str):  Example: 0f806c8d-2e37-4b1a-b2f9-6f42fd7f6d87.
        workspace_name (str):  Example: groundcover.
        workspace_url_key (str | Unset):  Example: groundcover.
    """

    connector_id: str
    workspace_id: str
    workspace_name: str
    workspace_url_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_id = self.connector_id

        workspace_id = self.workspace_id

        workspace_name = self.workspace_name

        workspace_url_key = self.workspace_url_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connector_id": connector_id,
                "workspace_id": workspace_id,
                "workspace_name": workspace_name,
            }
        )
        if workspace_url_key is not UNSET:
            field_dict["workspace_url_key"] = workspace_url_key

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
        connector_id = d.pop("connector_id")

        workspace_id = d.pop("workspace_id")

        workspace_name = d.pop("workspace_name")

        workspace_url_key = d.pop("workspace_url_key", UNSET)

        linear_secret_stores_non_secret_linear_org_connector_metadata = cls(
            connector_id=connector_id,
            workspace_id=workspace_id,
            workspace_name=workspace_name,
            workspace_url_key=workspace_url_key,
        )

        linear_secret_stores_non_secret_linear_org_connector_metadata.additional_properties = d
        return linear_secret_stores_non_secret_linear_org_connector_metadata

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
