from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_request_defines_model_for_dns_request import DnsRequestDefinesModelForDnsRequest
    from ..models.http_request_defines_model_for_http_request import HttpRequestDefinesModelForHttpRequest
    from ..models.ssl_request_defines_model_for_ssl_request import SslRequestDefinesModelForSslRequest
    from ..models.tcp_request_defines_model_for_tcp_request import TcpRequestDefinesModelForTcpRequest
    from ..models.udp_request_defines_model_for_udp_request import UdpRequestDefinesModelForUdpRequest
    from ..models.websocket_request_defines_model_for_websocket_request import (
        WebsocketRequestDefinesModelForWebsocketRequest,
    )


T = TypeVar("T", bound="RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind")


@_attrs_define
class RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind:
    """
    Attributes:
        dns (DnsRequestDefinesModelForDnsRequest | Unset):
        http (HttpRequestDefinesModelForHttpRequest | Unset):
        ssl (SslRequestDefinesModelForSslRequest | Unset):
        tcp (TcpRequestDefinesModelForTcpRequest | Unset):
        udp (UdpRequestDefinesModelForUdpRequest | Unset):
        websocket (WebsocketRequestDefinesModelForWebsocketRequest | Unset):
    """

    dns: DnsRequestDefinesModelForDnsRequest | Unset = UNSET
    http: HttpRequestDefinesModelForHttpRequest | Unset = UNSET
    ssl: SslRequestDefinesModelForSslRequest | Unset = UNSET
    tcp: TcpRequestDefinesModelForTcpRequest | Unset = UNSET
    udp: UdpRequestDefinesModelForUdpRequest | Unset = UNSET
    websocket: WebsocketRequestDefinesModelForWebsocketRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns.to_dict()

        http: dict[str, Any] | Unset = UNSET
        if not isinstance(self.http, Unset):
            http = self.http.to_dict()

        ssl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssl, Unset):
            ssl = self.ssl.to_dict()

        tcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp, Unset):
            tcp = self.tcp.to_dict()

        udp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.udp, Unset):
            udp = self.udp.to_dict()

        websocket: dict[str, Any] | Unset = UNSET
        if not isinstance(self.websocket, Unset):
            websocket = self.websocket.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dns is not UNSET:
            field_dict["dns"] = dns
        if http is not UNSET:
            field_dict["http"] = http
        if ssl is not UNSET:
            field_dict["ssl"] = ssl
        if tcp is not UNSET:
            field_dict["tcp"] = tcp
        if udp is not UNSET:
            field_dict["udp"] = udp
        if websocket is not UNSET:
            field_dict["websocket"] = websocket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_request_defines_model_for_dns_request import DnsRequestDefinesModelForDnsRequest
        from ..models.http_request_defines_model_for_http_request import HttpRequestDefinesModelForHttpRequest
        from ..models.ssl_request_defines_model_for_ssl_request import SslRequestDefinesModelForSslRequest
        from ..models.tcp_request_defines_model_for_tcp_request import TcpRequestDefinesModelForTcpRequest
        from ..models.udp_request_defines_model_for_udp_request import UdpRequestDefinesModelForUdpRequest
        from ..models.websocket_request_defines_model_for_websocket_request import (
            WebsocketRequestDefinesModelForWebsocketRequest,
        )

        d = dict(src_dict)
        _dns = d.pop("dns", UNSET)
        dns: DnsRequestDefinesModelForDnsRequest | Unset
        if isinstance(_dns, Unset) or _dns is None:
            dns = UNSET
        else:
            dns = DnsRequestDefinesModelForDnsRequest.from_dict(_dns)

        _http = d.pop("http", UNSET)
        http: HttpRequestDefinesModelForHttpRequest | Unset
        if isinstance(_http, Unset) or _http is None:
            http = UNSET
        else:
            http = HttpRequestDefinesModelForHttpRequest.from_dict(_http)

        _ssl = d.pop("ssl", UNSET)
        ssl: SslRequestDefinesModelForSslRequest | Unset
        if isinstance(_ssl, Unset) or _ssl is None:
            ssl = UNSET
        else:
            ssl = SslRequestDefinesModelForSslRequest.from_dict(_ssl)

        _tcp = d.pop("tcp", UNSET)
        tcp: TcpRequestDefinesModelForTcpRequest | Unset
        if isinstance(_tcp, Unset) or _tcp is None:
            tcp = UNSET
        else:
            tcp = TcpRequestDefinesModelForTcpRequest.from_dict(_tcp)

        _udp = d.pop("udp", UNSET)
        udp: UdpRequestDefinesModelForUdpRequest | Unset
        if isinstance(_udp, Unset) or _udp is None:
            udp = UNSET
        else:
            udp = UdpRequestDefinesModelForUdpRequest.from_dict(_udp)

        _websocket = d.pop("websocket", UNSET)
        websocket: WebsocketRequestDefinesModelForWebsocketRequest | Unset
        if isinstance(_websocket, Unset) or _websocket is None:
            websocket = UNSET
        else:
            websocket = WebsocketRequestDefinesModelForWebsocketRequest.from_dict(_websocket)

        request_check_request_configuration_only_one_field_should_be_set_based_on_the_check_kind = cls(
            dns=dns,
            http=http,
            ssl=ssl,
            tcp=tcp,
            udp=udp,
            websocket=websocket,
        )

        request_check_request_configuration_only_one_field_should_be_set_based_on_the_check_kind.additional_properties = d
        return request_check_request_configuration_only_one_field_should_be_set_based_on_the_check_kind

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
