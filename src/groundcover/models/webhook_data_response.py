from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_data_response_auth_type import WebhookDataResponseAuthType
from ..models.webhook_data_response_method import WebhookDataResponseMethod
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_data_response_headers import WebhookDataResponseHeaders


T = TypeVar("T", bound="WebhookDataResponse")


@_attrs_define
class WebhookDataResponse:
    """
    Attributes:
        auth_type (WebhookDataResponseAuthType | Unset):
        custom_payload (str | Unset): Optional custom JSON payload template using Jinja2 syntax.
            When set, the rendered template replaces the default webhook payload.
        headers (WebhookDataResponseHeaders | Unset):
        method (WebhookDataResponseMethod | Unset):
        url (str | Unset):
        username (str | Unset):
    """

    auth_type: WebhookDataResponseAuthType | Unset = UNSET
    custom_payload: str | Unset = UNSET
    headers: WebhookDataResponseHeaders | Unset = UNSET
    method: WebhookDataResponseMethod | Unset = UNSET
    url: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type: str | Unset = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        custom_payload = self.custom_payload

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        url = self.url

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if custom_payload is not UNSET:
            field_dict["custom_payload"] = custom_payload
        if headers is not UNSET:
            field_dict["headers"] = headers
        if method is not UNSET:
            field_dict["method"] = method
        if url is not UNSET:
            field_dict["url"] = url
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_data_response_headers import WebhookDataResponseHeaders

        d = dict(src_dict)
        _auth_type = d.pop("auth_type", UNSET)
        auth_type: WebhookDataResponseAuthType | Unset
        if isinstance(_auth_type, Unset) or _auth_type is None:
            auth_type = UNSET
        else:
            auth_type = WebhookDataResponseAuthType(_auth_type)

        custom_payload = d.pop("custom_payload", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: WebhookDataResponseHeaders | Unset
        if isinstance(_headers, Unset) or _headers is None:
            headers = UNSET
        else:
            headers = WebhookDataResponseHeaders.from_dict(_headers)

        _method = d.pop("method", UNSET)
        method: WebhookDataResponseMethod | Unset
        if isinstance(_method, Unset) or _method is None:
            method = UNSET
        else:
            method = WebhookDataResponseMethod(_method)

        url = d.pop("url", UNSET)

        username = d.pop("username", UNSET)

        webhook_data_response = cls(
            auth_type=auth_type,
            custom_payload=custom_payload,
            headers=headers,
            method=method,
            url=url,
            username=username,
        )

        webhook_data_response.additional_properties = d
        return webhook_data_response

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
