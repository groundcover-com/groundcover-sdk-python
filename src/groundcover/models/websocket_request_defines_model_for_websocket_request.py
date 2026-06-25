from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.websocket_request_defines_model_for_websocket_request_expect_messages_item import (
        WebsocketRequestDefinesModelForWebsocketRequestExpectMessagesItem,
    )
    from ..models.websocket_request_defines_model_for_websocket_request_headers import (
        WebsocketRequestDefinesModelForWebsocketRequestHeaders,
    )
    from ..models.websocket_request_defines_model_for_websocket_request_send_messages_item import (
        WebsocketRequestDefinesModelForWebsocketRequestSendMessagesItem,
    )


T = TypeVar("T", bound="WebsocketRequestDefinesModelForWebsocketRequest")


@_attrs_define
class WebsocketRequestDefinesModelForWebsocketRequest:
    """
    Attributes:
        expect_messages (list[WebsocketRequestDefinesModelForWebsocketRequestExpectMessagesItem] | Unset):
        headers (WebsocketRequestDefinesModelForWebsocketRequestHeaders | Unset):
        kind (str | Unset):
        send_messages (list[WebsocketRequestDefinesModelForWebsocketRequestSendMessagesItem] | Unset):
        subprotocols (list[str] | Unset):
        url (str | Unset):
    """

    expect_messages: list[WebsocketRequestDefinesModelForWebsocketRequestExpectMessagesItem] | Unset = UNSET
    headers: WebsocketRequestDefinesModelForWebsocketRequestHeaders | Unset = UNSET
    kind: str | Unset = UNSET
    send_messages: list[WebsocketRequestDefinesModelForWebsocketRequestSendMessagesItem] | Unset = UNSET
    subprotocols: list[str] | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expect_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expect_messages, Unset):
            expect_messages = []
            for expect_messages_item_data in self.expect_messages:
                expect_messages_item = expect_messages_item_data.to_dict()
                expect_messages.append(expect_messages_item)

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        kind = self.kind

        send_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.send_messages, Unset):
            send_messages = []
            for send_messages_item_data in self.send_messages:
                send_messages_item = send_messages_item_data.to_dict()
                send_messages.append(send_messages_item)

        subprotocols: list[str] | Unset = UNSET
        if not isinstance(self.subprotocols, Unset):
            subprotocols = self.subprotocols

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expect_messages is not UNSET:
            field_dict["expectMessages"] = expect_messages
        if headers is not UNSET:
            field_dict["headers"] = headers
        if kind is not UNSET:
            field_dict["kind"] = kind
        if send_messages is not UNSET:
            field_dict["sendMessages"] = send_messages
        if subprotocols is not UNSET:
            field_dict["subprotocols"] = subprotocols
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.websocket_request_defines_model_for_websocket_request_expect_messages_item import (
            WebsocketRequestDefinesModelForWebsocketRequestExpectMessagesItem,
        )
        from ..models.websocket_request_defines_model_for_websocket_request_headers import (
            WebsocketRequestDefinesModelForWebsocketRequestHeaders,
        )
        from ..models.websocket_request_defines_model_for_websocket_request_send_messages_item import (
            WebsocketRequestDefinesModelForWebsocketRequestSendMessagesItem,
        )

        d = dict(src_dict)
        _expect_messages = d.pop("expectMessages", UNSET)
        expect_messages: list[WebsocketRequestDefinesModelForWebsocketRequestExpectMessagesItem] | Unset = UNSET
        if _expect_messages is not UNSET:
            expect_messages = []
            for expect_messages_item_data in _expect_messages:
                expect_messages_item = WebsocketRequestDefinesModelForWebsocketRequestExpectMessagesItem.from_dict(
                    expect_messages_item_data
                )

                expect_messages.append(expect_messages_item)

        _headers = d.pop("headers", UNSET)
        headers: WebsocketRequestDefinesModelForWebsocketRequestHeaders | Unset
        if isinstance(_headers, Unset) or _headers is None:
            headers = UNSET
        else:
            headers = WebsocketRequestDefinesModelForWebsocketRequestHeaders.from_dict(_headers)

        kind = d.pop("kind", UNSET)

        _send_messages = d.pop("sendMessages", UNSET)
        send_messages: list[WebsocketRequestDefinesModelForWebsocketRequestSendMessagesItem] | Unset = UNSET
        if _send_messages is not UNSET:
            send_messages = []
            for send_messages_item_data in _send_messages:
                send_messages_item = WebsocketRequestDefinesModelForWebsocketRequestSendMessagesItem.from_dict(
                    send_messages_item_data
                )

                send_messages.append(send_messages_item)

        subprotocols = cast(list[str], d.pop("subprotocols", UNSET))

        url = d.pop("url", UNSET)

        websocket_request_defines_model_for_websocket_request = cls(
            expect_messages=expect_messages,
            headers=headers,
            kind=kind,
            send_messages=send_messages,
            subprotocols=subprotocols,
            url=url,
        )

        websocket_request_defines_model_for_websocket_request.additional_properties = d
        return websocket_request_defines_model_for_websocket_request

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
