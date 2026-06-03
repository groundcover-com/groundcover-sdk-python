from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="NotificationSettingsResponse")


@_attrs_define
class NotificationSettingsResponse:
    """
    Attributes:
        disable_renotification (bool | Unset): Whether re-notifications are disabled Example: True.
        renotification_interval (str | Unset): The interval between re-notifications Example: 4h.
    """

    disable_renotification: bool | Unset = UNSET
    renotification_interval: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable_renotification = self.disable_renotification

        renotification_interval = self.renotification_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable_renotification is not UNSET:
            field_dict["disableRenotification"] = disable_renotification
        if renotification_interval is not UNSET:
            field_dict["renotificationInterval"] = renotification_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        disable_renotification = d.pop("disableRenotification", UNSET)

        renotification_interval = d.pop("renotificationInterval", UNSET)

        notification_settings_response = cls(
            disable_renotification=disable_renotification,
            renotification_interval=renotification_interval,
        )

        notification_settings_response.additional_properties = d
        return notification_settings_response

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
