from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnectorOAuthStartResponseContainsTheProviderAuthorizationURL")


@_attrs_define
class ConnectorOAuthStartResponseContainsTheProviderAuthorizationURL:
    """
    Attributes:
        authorize_url (str | Unset): URL the frontend should navigate to for provider authorization. Example:
            https://slack.com/oauth/v2/authorize?client_id=....
    """

    authorize_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorize_url = self.authorize_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorize_url is not UNSET:
            field_dict["authorize_url"] = authorize_url

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
        authorize_url = d.pop("authorize_url", UNSET)

        connector_o_auth_start_response_contains_the_provider_authorization_url = cls(
            authorize_url=authorize_url,
        )

        connector_o_auth_start_response_contains_the_provider_authorization_url.additional_properties = d
        return connector_o_auth_start_response_contains_the_provider_authorization_url

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
