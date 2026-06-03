from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SeatsUsageItem")


@_attrs_define
class SeatsUsageItem:
    """
    Attributes:
        email (str | Unset):
        first_login (datetime.datetime | Unset):
        is_active (bool | Unset):
        last_login (datetime.datetime | Unset):
        policy_names (list[str] | Unset):
        policy_uui_ds (list[str] | Unset):
        role_type (str | Unset):
        sso_driven (bool | Unset):
    """

    email: str | Unset = UNSET
    first_login: datetime.datetime | Unset = UNSET
    is_active: bool | Unset = UNSET
    last_login: datetime.datetime | Unset = UNSET
    policy_names: list[str] | Unset = UNSET
    policy_uui_ds: list[str] | Unset = UNSET
    role_type: str | Unset = UNSET
    sso_driven: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_login: str | Unset = UNSET
        if not isinstance(self.first_login, Unset):
            first_login = self.first_login.isoformat()

        is_active = self.is_active

        last_login: str | Unset = UNSET
        if not isinstance(self.last_login, Unset):
            last_login = self.last_login.isoformat()

        policy_names: list[str] | Unset = UNSET
        if not isinstance(self.policy_names, Unset):
            policy_names = self.policy_names

        policy_uui_ds: list[str] | Unset = UNSET
        if not isinstance(self.policy_uui_ds, Unset):
            policy_uui_ds = self.policy_uui_ds

        role_type = self.role_type

        sso_driven = self.sso_driven

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if first_login is not UNSET:
            field_dict["firstLogin"] = first_login
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if last_login is not UNSET:
            field_dict["lastLogin"] = last_login
        if policy_names is not UNSET:
            field_dict["policyNames"] = policy_names
        if policy_uui_ds is not UNSET:
            field_dict["policyUUIDs"] = policy_uui_ds
        if role_type is not UNSET:
            field_dict["roleType"] = role_type
        if sso_driven is not UNSET:
            field_dict["ssoDriven"] = sso_driven

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        _first_login = d.pop("firstLogin", UNSET)
        first_login: datetime.datetime | Unset
        if isinstance(_first_login, Unset) or _first_login is None:
            first_login = UNSET
        else:
            first_login = parse_datetime(_first_login)

        is_active = d.pop("isActive", UNSET)

        _last_login = d.pop("lastLogin", UNSET)
        last_login: datetime.datetime | Unset
        if isinstance(_last_login, Unset) or _last_login is None:
            last_login = UNSET
        else:
            last_login = parse_datetime(_last_login)

        policy_names = cast(list[str], d.pop("policyNames", UNSET))

        policy_uui_ds = cast(list[str], d.pop("policyUUIDs", UNSET))

        role_type = d.pop("roleType", UNSET)

        sso_driven = d.pop("ssoDriven", UNSET)

        seats_usage_item = cls(
            email=email,
            first_login=first_login,
            is_active=is_active,
            last_login=last_login,
            policy_names=policy_names,
            policy_uui_ds=policy_uui_ds,
            role_type=role_type,
            sso_driven=sso_driven,
        )

        seats_usage_item.additional_properties = d
        return seats_usage_item

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
