from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="HttpRequestDefinesModelForHttpRequestAuth")


@_attrs_define
class HttpRequestDefinesModelForHttpRequestAuth:
    """
    Attributes:
        password (str | Unset):
        token (str | Unset):
        type_ (str | Unset):
        username (str | Unset):
    """

    password: str | Unset = UNSET
    token: str | Unset = UNSET
    type_: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        token = self.token

        type_ = self.type_

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if token is not UNSET:
            field_dict["token"] = token
        if type_ is not UNSET:
            field_dict["type"] = type_
        if username is not UNSET:
            field_dict["username"] = username

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
        password = d.pop("password", UNSET)

        token = d.pop("token", UNSET)

        type_ = d.pop("type", UNSET)

        username = d.pop("username", UNSET)

        http_request_defines_model_for_http_request_auth = cls(
            password=password,
            token=token,
            type_=type_,
            username=username,
        )

        http_request_defines_model_for_http_request_auth.additional_properties = d
        return http_request_defines_model_for_http_request_auth

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
