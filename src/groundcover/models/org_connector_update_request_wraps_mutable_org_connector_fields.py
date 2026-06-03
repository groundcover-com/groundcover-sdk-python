from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_connector_update_request_wraps_mutable_org_connector_fields_data import (
        OrgConnectorUpdateRequestWrapsMutableOrgConnectorFieldsData,
    )


T = TypeVar("T", bound="OrgConnectorUpdateRequestWrapsMutableOrgConnectorFields")


@_attrs_define
class OrgConnectorUpdateRequestWrapsMutableOrgConnectorFields:
    """For Slack, `name` may be set at the top level and `data` may include
    `client_secret` and/or `app_token`. For MCP, `data` may include
    `admin_token`. Omitted `data` is treated as an empty object.

        Attributes:
            data (OrgConnectorUpdateRequestWrapsMutableOrgConnectorFieldsData | Unset): Provider-specific connector data.
            name (str | Unset): Optional connector display name. Example: platform-alerts.
    """

    data: OrgConnectorUpdateRequestWrapsMutableOrgConnectorFieldsData | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_connector_update_request_wraps_mutable_org_connector_fields_data import (
            OrgConnectorUpdateRequestWrapsMutableOrgConnectorFieldsData,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: OrgConnectorUpdateRequestWrapsMutableOrgConnectorFieldsData | Unset
        if isinstance(_data, Unset) or _data is None:
            data = UNSET
        else:
            data = OrgConnectorUpdateRequestWrapsMutableOrgConnectorFieldsData.from_dict(_data)

        name = d.pop("name", UNSET)

        org_connector_update_request_wraps_mutable_org_connector_fields = cls(
            data=data,
            name=name,
        )

        org_connector_update_request_wraps_mutable_org_connector_fields.additional_properties = d
        return org_connector_update_request_wraps_mutable_org_connector_fields

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
