from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery")


@_attrs_define
class ConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery:
    """
    Attributes:
        id (str): ID is the Slack channel ID used for delivery.
        name (str | Unset): Name is the channel display name shown by channel selectors; optional.
    """

    id: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

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
        id = d.pop("id")

        name = d.pop("name", UNSET)

        connected_app_channel_identifies_a_slack_channel_for_slack_app_delivery = cls(
            id=id,
            name=name,
        )

        connected_app_channel_identifies_a_slack_channel_for_slack_app_delivery.additional_properties = d
        return connected_app_channel_identifies_a_slack_channel_for_slack_app_delivery

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
