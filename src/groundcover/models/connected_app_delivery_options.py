from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnectedAppDeliveryOptions")


@_attrs_define
class ConnectedAppDeliveryOptions:
    """ConnectedAppDeliveryOptions carries per-app delivery options for direct-to-connected-app
    monitor notifications. Fields are app-type specific; unrelated fields are ignored.

        Attributes:
            channels (list[str] | Unset): Channels lists Slack channel IDs to post to (slack-app connected apps).
                Multiple channels result in one notification per channel via dispatch-center fanout.
    """

    channels: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: list[str] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels

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
        channels = cast(list[str], d.pop("channels", UNSET))

        connected_app_delivery_options = cls(
            channels=channels,
        )

        connected_app_delivery_options.additional_properties = d
        return connected_app_delivery_options

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
