from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="UpdateServiceAccountRequest")


@_attrs_define
class UpdateServiceAccountRequest:
    """
    Attributes:
        service_account_id (str): The UUID of the service account to update.
        email (str | Unset): The new email address for the service account (optional).
        override_policies (bool | Unset):
        policy_uui_ds (list[str] | Unset): A list of policy UUIDs to set for the service account (optional, replaces
            existing). Provide empty list to remove all.
    """

    service_account_id: str
    email: str | Unset = UNSET
    override_policies: bool | Unset = UNSET
    policy_uui_ds: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_account_id = self.service_account_id

        email = self.email

        override_policies = self.override_policies

        policy_uui_ds: list[str] | Unset = UNSET
        if not isinstance(self.policy_uui_ds, Unset):
            policy_uui_ds = self.policy_uui_ds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceAccountId": service_account_id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if override_policies is not UNSET:
            field_dict["overridePolicies"] = override_policies
        if policy_uui_ds is not UNSET:
            field_dict["policyUUIDs"] = policy_uui_ds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        service_account_id = d.pop("serviceAccountId")

        email = d.pop("email", UNSET)

        override_policies = d.pop("overridePolicies", UNSET)

        policy_uui_ds = cast(list[str], d.pop("policyUUIDs", UNSET))

        update_service_account_request = cls(
            service_account_id=service_account_id,
            email=email,
            override_policies=override_policies,
            policy_uui_ds=policy_uui_ds,
        )

        update_service_account_request.additional_properties = d
        return update_service_account_request

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
