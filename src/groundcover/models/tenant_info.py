from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TenantInfo")


@_attrs_define
class TenantInfo:
    """
    Attributes:
        grafana_org_id (str | Unset):
        is_public (bool | Unset):
        org_name (str | Unset):
        tenant_name (str | Unset):
        uuid (str | Unset):
    """

    grafana_org_id: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    org_name: str | Unset = UNSET
    tenant_name: str | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grafana_org_id = self.grafana_org_id

        is_public = self.is_public

        org_name = self.org_name

        tenant_name = self.tenant_name

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grafana_org_id is not UNSET:
            field_dict["GrafanaOrgID"] = grafana_org_id
        if is_public is not UNSET:
            field_dict["IsPublic"] = is_public
        if org_name is not UNSET:
            field_dict["OrgName"] = org_name
        if tenant_name is not UNSET:
            field_dict["TenantName"] = tenant_name
        if uuid is not UNSET:
            field_dict["UUID"] = uuid

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
        grafana_org_id = d.pop("GrafanaOrgID", UNSET)

        is_public = d.pop("IsPublic", UNSET)

        org_name = d.pop("OrgName", UNSET)

        tenant_name = d.pop("TenantName", UNSET)

        uuid = d.pop("UUID", UNSET)

        tenant_info = cls(
            grafana_org_id=grafana_org_id,
            is_public=is_public,
            org_name=org_name,
            tenant_name=tenant_name,
            uuid=uuid,
        )

        tenant_info.additional_properties = d
        return tenant_info

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
