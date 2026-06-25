from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TestMonitorDisplayControlsHowTheTestNotificationIsPresented")


@_attrs_define
class TestMonitorDisplayControlsHowTheTestNotificationIsPresented:
    """Mirrors the monitor DisplayModel structure.

    Attributes:
        description (str | Unset): Jinja template for the issue description Example: Monitor detected issue with
            severity {{ severity }}.
        header (str | Unset): Jinja template for the issue title/header Example: {{ monitor_name }} is firing.
    """

    description: str | Unset = UNSET
    header: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        header = self.header

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if header is not UNSET:
            field_dict["header"] = header

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
        description = d.pop("description", UNSET)

        header = d.pop("header", UNSET)

        test_monitor_display_controls_how_the_test_notification_is_presented = cls(
            description=description,
            header=header,
        )

        test_monitor_display_controls_how_the_test_notification_is_presented.additional_properties = d
        return test_monitor_display_controls_how_the_test_notification_is_presented

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
