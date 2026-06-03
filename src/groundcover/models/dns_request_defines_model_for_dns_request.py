from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="DnsRequestDefinesModelForDnsRequest")


@_attrs_define
class DnsRequestDefinesModelForDnsRequest:
    """
    Attributes:
        dnssec (bool | Unset):
        domain (str | Unset):
        kind (str | Unset):
        port (int | Unset):
        record_type (str | Unset):
        resolver (str | Unset):
        timeout (str | Unset):
    """

    dnssec: bool | Unset = UNSET
    domain: str | Unset = UNSET
    kind: str | Unset = UNSET
    port: int | Unset = UNSET
    record_type: str | Unset = UNSET
    resolver: str | Unset = UNSET
    timeout: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dnssec = self.dnssec

        domain = self.domain

        kind = self.kind

        port = self.port

        record_type = self.record_type

        resolver = self.resolver

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dnssec is not UNSET:
            field_dict["dnssec"] = dnssec
        if domain is not UNSET:
            field_dict["domain"] = domain
        if kind is not UNSET:
            field_dict["kind"] = kind
        if port is not UNSET:
            field_dict["port"] = port
        if record_type is not UNSET:
            field_dict["recordType"] = record_type
        if resolver is not UNSET:
            field_dict["resolver"] = resolver
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        dnssec = d.pop("dnssec", UNSET)

        domain = d.pop("domain", UNSET)

        kind = d.pop("kind", UNSET)

        port = d.pop("port", UNSET)

        record_type = d.pop("recordType", UNSET)

        resolver = d.pop("resolver", UNSET)

        timeout = d.pop("timeout", UNSET)

        dns_request_defines_model_for_dns_request = cls(
            dnssec=dnssec,
            domain=domain,
            kind=kind,
            port=port,
            record_type=record_type,
            resolver=resolver,
            timeout=timeout,
        )

        dns_request_defines_model_for_dns_request.additional_properties = d
        return dns_request_defines_model_for_dns_request

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
