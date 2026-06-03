from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CursorGetMeResponseIsTheResponseForTheGetMeEndpoint")


@_attrs_define
class CursorGetMeResponseIsTheResponseForTheGetMeEndpoint:
    """
    Attributes:
        api_key_name (str | Unset):
        created_at (str | Unset):
        user_email (str | Unset):
    """

    api_key_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    user_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_name = self.api_key_name

        created_at = self.created_at

        user_email = self.user_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key_name is not UNSET:
            field_dict["api_key_name"] = api_key_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if user_email is not UNSET:
            field_dict["user_email"] = user_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        api_key_name = d.pop("api_key_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        user_email = d.pop("user_email", UNSET)

        cursor_get_me_response_is_the_response_for_the_get_me_endpoint = cls(
            api_key_name=api_key_name,
            created_at=created_at,
            user_email=user_email,
        )

        cursor_get_me_response_is_the_response_for_the_get_me_endpoint.additional_properties = d
        return cursor_get_me_response_is_the_response_for_the_get_me_endpoint

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
