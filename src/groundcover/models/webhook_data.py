from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_data_auth_type import WebhookDataAuthType
from ..models.webhook_data_method import WebhookDataMethod
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_data_headers import WebhookDataHeaders


T = TypeVar("T", bound="WebhookData")


@_attrs_define
class WebhookData:
    """
    Attributes:
        url (str):
        api_key (str | Unset): API key / token for bearer authentication.
        auth_type (WebhookDataAuthType | Unset): Authentication type: "", "basic", or "bearer". Example: bearer.
        custom_payload (str | Unset): Optional custom JSON payload template using Jinja2 syntax.
            When set, the rendered template replaces the default webhook payload.
            Available variables: status, alert_name, summary, description, severity, fingerprint,
            monitor_name, monitor_id, cluster, env, namespace, workload, timestamp,
            notification_count, labels, urls, value, threshold, state, query, creator. Example: {"text": "{{ alert_name }}",
            "severity": "{{ severity }}"}.
        headers (WebhookDataHeaders | Unset): Custom HTTP headers to include in the request. Example: {'X-Custom-
            Header': 'value'}.
        method (WebhookDataMethod | Unset): HTTP method to use (GET, POST, PUT, or DELETE). Defaults to POST. Example:
            POST.
        password (str | Unset): Password for basic authentication.
        username (str | Unset): Username for basic authentication.
    """

    url: str
    api_key: str | Unset = UNSET
    auth_type: WebhookDataAuthType | Unset = UNSET
    custom_payload: str | Unset = UNSET
    headers: WebhookDataHeaders | Unset = UNSET
    method: WebhookDataMethod | Unset = UNSET
    password: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        api_key = self.api_key

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

        password = self.password

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if custom_payload is not UNSET:
            field_dict["custom_payload"] = custom_payload
        if headers is not UNSET:
            field_dict["headers"] = headers
        if method is not UNSET:
            field_dict["method"] = method
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_data_headers import WebhookDataHeaders

        d = dict(src_dict)
        url = d.pop("url")

        api_key = d.pop("api_key", UNSET)

        _auth_type = d.pop("auth_type", UNSET)
        auth_type: WebhookDataAuthType | Unset
        if isinstance(_auth_type, Unset) or _auth_type is None:
            auth_type = UNSET
        else:
            auth_type = WebhookDataAuthType(_auth_type)

        custom_payload = d.pop("custom_payload", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: WebhookDataHeaders | Unset
        if isinstance(_headers, Unset) or _headers is None:
            headers = UNSET
        else:
            headers = WebhookDataHeaders.from_dict(_headers)

        _method = d.pop("method", UNSET)
        method: WebhookDataMethod | Unset
        if isinstance(_method, Unset) or _method is None:
            method = UNSET
        else:
            method = WebhookDataMethod(_method)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        webhook_data = cls(
            url=url,
            api_key=api_key,
            auth_type=auth_type,
            custom_payload=custom_payload,
            headers=headers,
            method=method,
            password=password,
            username=username,
        )

        webhook_data.additional_properties = d
        return webhook_data

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
