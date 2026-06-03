from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="InviteeDetails")


@_attrs_define
class InviteeDetails:
    """
    Attributes:
        email (str | Unset):
        policy_uui_ds (list[str] | Unset):
        role (str | Unset):
    """

    email: str | Unset = UNSET
    policy_uui_ds: list[str] | Unset = UNSET
    role: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        policy_uui_ds: list[str] | Unset = UNSET
        if not isinstance(self.policy_uui_ds, Unset):
            policy_uui_ds = self.policy_uui_ds

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if policy_uui_ds is not UNSET:
            field_dict["policyUUIDs"] = policy_uui_ds
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        policy_uui_ds = cast(list[str], d.pop("policyUUIDs", UNSET))

        role = d.pop("role", UNSET)

        invitee_details = cls(
            email=email,
            policy_uui_ds=policy_uui_ds,
            role=role,
        )

        invitee_details.additional_properties = d
        return invitee_details

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
