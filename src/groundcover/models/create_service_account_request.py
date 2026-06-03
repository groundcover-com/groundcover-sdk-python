from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateServiceAccountRequest")


@_attrs_define
class CreateServiceAccountRequest:
    """
    Attributes:
        email (str): The email address associated with the service account.
        name (str): The desired name for the service account.
        policy_uui_ds (list[str]): A list of policy UUIDs to assign to the service account.
    """

    email: str
    name: str
    policy_uui_ds: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name = self.name

        policy_uui_ds = self.policy_uui_ds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "name": name,
                "policyUUIDs": policy_uui_ds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        email = d.pop("email")

        name = d.pop("name")

        policy_uui_ds = cast(list[str], d.pop("policyUUIDs"))

        create_service_account_request = cls(
            email=email,
            name=name,
            policy_uui_ds=policy_uui_ds,
        )

        create_service_account_request.additional_properties = d
        return create_service_account_request

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
