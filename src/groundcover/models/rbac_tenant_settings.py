from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="RbacTenantSettings")


@_attrs_define
class RbacTenantSettings:
    """
    Attributes:
        default_policy_uuid (str | Unset):
        default_role (str | Unset): DefaultRole is the old settings, If DefaultPolicyUUID is not empty, this field will
            be ignored
    """

    default_policy_uuid: str | Unset = UNSET
    default_role: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_policy_uuid = self.default_policy_uuid

        default_role = self.default_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_policy_uuid is not UNSET:
            field_dict["defaultPolicyUUID"] = default_policy_uuid
        if default_role is not UNSET:
            field_dict["defaultRole"] = default_role

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
        default_policy_uuid = d.pop("defaultPolicyUUID", UNSET)

        default_role = d.pop("defaultRole", UNSET)

        rbac_tenant_settings = cls(
            default_policy_uuid=default_policy_uuid,
            default_role=default_role,
        )

        rbac_tenant_settings.additional_properties = d
        return rbac_tenant_settings

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
