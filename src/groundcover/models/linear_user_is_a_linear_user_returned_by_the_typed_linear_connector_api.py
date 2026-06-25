from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="LinearUserIsALinearUserReturnedByTheTypedLinearConnectorAPI")


@_attrs_define
class LinearUserIsALinearUserReturnedByTheTypedLinearConnectorAPI:
    """
    Attributes:
        active (bool | Unset):
        app (bool | Unset):
        archived (bool | Unset):
        display_name (str | Unset):
        email (str | Unset):
        id (str | Unset):
        is_assignable (bool | Unset):
        name (str | Unset):
        supports_agent_sessions (bool | Unset):
    """

    active: bool | Unset = UNSET
    app: bool | Unset = UNSET
    archived: bool | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    id: str | Unset = UNSET
    is_assignable: bool | Unset = UNSET
    name: str | Unset = UNSET
    supports_agent_sessions: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        app = self.app

        archived = self.archived

        display_name = self.display_name

        email = self.email

        id = self.id

        is_assignable = self.is_assignable

        name = self.name

        supports_agent_sessions = self.supports_agent_sessions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if app is not UNSET:
            field_dict["app"] = app
        if archived is not UNSET:
            field_dict["archived"] = archived
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if is_assignable is not UNSET:
            field_dict["is_assignable"] = is_assignable
        if name is not UNSET:
            field_dict["name"] = name
        if supports_agent_sessions is not UNSET:
            field_dict["supports_agent_sessions"] = supports_agent_sessions

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
        active = d.pop("active", UNSET)

        app = d.pop("app", UNSET)

        archived = d.pop("archived", UNSET)

        display_name = d.pop("display_name", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        is_assignable = d.pop("is_assignable", UNSET)

        name = d.pop("name", UNSET)

        supports_agent_sessions = d.pop("supports_agent_sessions", UNSET)

        linear_user_is_a_linear_user_returned_by_the_typed_linear_connector_api = cls(
            active=active,
            app=app,
            archived=archived,
            display_name=display_name,
            email=email,
            id=id,
            is_assignable=is_assignable,
            name=name,
            supports_agent_sessions=supports_agent_sessions,
        )

        linear_user_is_a_linear_user_returned_by_the_typed_linear_connector_api.additional_properties = d
        return linear_user_is_a_linear_user_returned_by_the_typed_linear_connector_api

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
