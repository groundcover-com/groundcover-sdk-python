from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="WebsocketRequestDefinesModelForWebsocketRequestExpectMessagesItem")


@_attrs_define
class WebsocketRequestDefinesModelForWebsocketRequestExpectMessagesItem:
    """
    Attributes:
        contains (str | Unset):
        within (str | Unset):
    """

    contains: str | Unset = UNSET
    within: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contains = self.contains

        within = self.within

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contains is not UNSET:
            field_dict["contains"] = contains
        if within is not UNSET:
            field_dict["within"] = within

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
        contains = d.pop("contains", UNSET)

        within = d.pop("within", UNSET)

        websocket_request_defines_model_for_websocket_request_expect_messages_item = cls(
            contains=contains,
            within=within,
        )

        websocket_request_defines_model_for_websocket_request_expect_messages_item.additional_properties = d
        return websocket_request_defines_model_for_websocket_request_expect_messages_item

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
