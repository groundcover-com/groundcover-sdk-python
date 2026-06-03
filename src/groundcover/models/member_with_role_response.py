from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MemberWithRoleResponse")


@_attrs_define
class MemberWithRoleResponse:
    """
    Attributes:
        created (datetime.datetime | Unset):
        email (str | Unset):
        first_login (datetime.datetime | Unset):
        last_seen (datetime.datetime | Unset):
        owner (bool | Unset):
        role_type (str | Unset):
    """

    created: datetime.datetime | Unset = UNSET
    email: str | Unset = UNSET
    first_login: datetime.datetime | Unset = UNSET
    last_seen: datetime.datetime | Unset = UNSET
    owner: bool | Unset = UNSET
    role_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        email = self.email

        first_login: str | Unset = UNSET
        if not isinstance(self.first_login, Unset):
            first_login = self.first_login.isoformat()

        last_seen: str | Unset = UNSET
        if not isinstance(self.last_seen, Unset):
            last_seen = self.last_seen.isoformat()

        owner = self.owner

        role_type = self.role_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["Created"] = created
        if email is not UNSET:
            field_dict["Email"] = email
        if first_login is not UNSET:
            field_dict["FirstLogin"] = first_login
        if last_seen is not UNSET:
            field_dict["LastSeen"] = last_seen
        if owner is not UNSET:
            field_dict["Owner"] = owner
        if role_type is not UNSET:
            field_dict["RoleType"] = role_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        _created = d.pop("Created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset) or _created is None:
            created = UNSET
        else:
            created = parse_datetime(_created)

        email = d.pop("Email", UNSET)

        _first_login = d.pop("FirstLogin", UNSET)
        first_login: datetime.datetime | Unset
        if isinstance(_first_login, Unset) or _first_login is None:
            first_login = UNSET
        else:
            first_login = parse_datetime(_first_login)

        _last_seen = d.pop("LastSeen", UNSET)
        last_seen: datetime.datetime | Unset
        if isinstance(_last_seen, Unset) or _last_seen is None:
            last_seen = UNSET
        else:
            last_seen = parse_datetime(_last_seen)

        owner = d.pop("Owner", UNSET)

        role_type = d.pop("RoleType", UNSET)

        member_with_role_response = cls(
            created=created,
            email=email,
            first_login=first_login,
            last_seen=last_seen,
            owner=owner,
            role_type=role_type,
        )

        member_with_role_response.additional_properties = d
        return member_with_role_response

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
