from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ApplyPolicyRequest")


@_attrs_define
class ApplyPolicyRequest:
    """
    Attributes:
        emails (list[str]): List of user emails to apply policies to.
        policy_uui_ds (list[str]): List of policy UUIDs to apply.
        override (bool | Unset): If true, replaces existing policies; otherwise appends.
    """

    emails: list[str]
    policy_uui_ds: list[str]
    override: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emails = self.emails

        policy_uui_ds = self.policy_uui_ds

        override = self.override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
                "policyUUIDs": policy_uui_ds,
            }
        )
        if override is not UNSET:
            field_dict["override"] = override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        emails = cast(list[str], d.pop("emails"))

        policy_uui_ds = cast(list[str], d.pop("policyUUIDs"))

        override = d.pop("override", UNSET)

        apply_policy_request = cls(
            emails=emails,
            policy_uui_ds=policy_uui_ds,
            override=override,
        )

        apply_policy_request.additional_properties = d
        return apply_policy_request

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
