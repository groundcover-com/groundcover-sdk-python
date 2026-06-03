from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="UdpRequestDefinesModelForUdpRequest")


@_attrs_define
class UdpRequestDefinesModelForUdpRequest:
    """
    Attributes:
        host (str | Unset):
        kind (str | Unset):
        payload (str | Unset):
        port (int | Unset):
        receive_timeout (str | Unset):
    """

    host: str | Unset = UNSET
    kind: str | Unset = UNSET
    payload: str | Unset = UNSET
    port: int | Unset = UNSET
    receive_timeout: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        kind = self.kind

        payload = self.payload

        port = self.port

        receive_timeout = self.receive_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if kind is not UNSET:
            field_dict["kind"] = kind
        if payload is not UNSET:
            field_dict["payload"] = payload
        if port is not UNSET:
            field_dict["port"] = port
        if receive_timeout is not UNSET:
            field_dict["receiveTimeout"] = receive_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        kind = d.pop("kind", UNSET)

        payload = d.pop("payload", UNSET)

        port = d.pop("port", UNSET)

        receive_timeout = d.pop("receiveTimeout", UNSET)

        udp_request_defines_model_for_udp_request = cls(
            host=host,
            kind=kind,
            payload=payload,
            port=port,
            receive_timeout=receive_timeout,
        )

        udp_request_defines_model_for_udp_request.additional_properties = d
        return udp_request_defines_model_for_udp_request

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
