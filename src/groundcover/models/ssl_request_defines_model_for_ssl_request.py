from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SslRequestDefinesModelForSslRequest")


@_attrs_define
class SslRequestDefinesModelForSslRequest:
    """
    Attributes:
        host (str | Unset):
        kind (str | Unset):
        min_version (str | Unset):
        port (int | Unset):
        sni (str | Unset):
        timeout (str | Unset):
        verify (bool | Unset):
    """

    host: str | Unset = UNSET
    kind: str | Unset = UNSET
    min_version: str | Unset = UNSET
    port: int | Unset = UNSET
    sni: str | Unset = UNSET
    timeout: str | Unset = UNSET
    verify: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        kind = self.kind

        min_version = self.min_version

        port = self.port

        sni = self.sni

        timeout = self.timeout

        verify = self.verify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if kind is not UNSET:
            field_dict["kind"] = kind
        if min_version is not UNSET:
            field_dict["minVersion"] = min_version
        if port is not UNSET:
            field_dict["port"] = port
        if sni is not UNSET:
            field_dict["sni"] = sni
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if verify is not UNSET:
            field_dict["verify"] = verify

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        kind = d.pop("kind", UNSET)

        min_version = d.pop("minVersion", UNSET)

        port = d.pop("port", UNSET)

        sni = d.pop("sni", UNSET)

        timeout = d.pop("timeout", UNSET)

        verify = d.pop("verify", UNSET)

        ssl_request_defines_model_for_ssl_request = cls(
            host=host,
            kind=kind,
            min_version=min_version,
            port=port,
            sni=sni,
            timeout=timeout,
            verify=verify,
        )

        ssl_request_defines_model_for_ssl_request.additional_properties = d
        return ssl_request_defines_model_for_ssl_request

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
