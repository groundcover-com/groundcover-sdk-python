from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TcpRequestDefinesModelForTcpRequest")


@_attrs_define
class TcpRequestDefinesModelForTcpRequest:
    """
    Attributes:
        expect_response (bool | Unset):
        host (str | Unset):
        kind (str | Unset):
        port (int | Unset):
        receive_max_bytes (int | Unset):
        send (str | Unset):
        timeout (str | Unset):
    """

    expect_response: bool | Unset = UNSET
    host: str | Unset = UNSET
    kind: str | Unset = UNSET
    port: int | Unset = UNSET
    receive_max_bytes: int | Unset = UNSET
    send: str | Unset = UNSET
    timeout: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expect_response = self.expect_response

        host = self.host

        kind = self.kind

        port = self.port

        receive_max_bytes = self.receive_max_bytes

        send = self.send

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expect_response is not UNSET:
            field_dict["expectResponse"] = expect_response
        if host is not UNSET:
            field_dict["host"] = host
        if kind is not UNSET:
            field_dict["kind"] = kind
        if port is not UNSET:
            field_dict["port"] = port
        if receive_max_bytes is not UNSET:
            field_dict["receiveMaxBytes"] = receive_max_bytes
        if send is not UNSET:
            field_dict["send"] = send
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        expect_response = d.pop("expectResponse", UNSET)

        host = d.pop("host", UNSET)

        kind = d.pop("kind", UNSET)

        port = d.pop("port", UNSET)

        receive_max_bytes = d.pop("receiveMaxBytes", UNSET)

        send = d.pop("send", UNSET)

        timeout = d.pop("timeout", UNSET)

        tcp_request_defines_model_for_tcp_request = cls(
            expect_response=expect_response,
            host=host,
            kind=kind,
            port=port,
            receive_max_bytes=receive_max_bytes,
            send=send,
            timeout=timeout,
        )

        tcp_request_defines_model_for_tcp_request.additional_properties = d
        return tcp_request_defines_model_for_tcp_request

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
