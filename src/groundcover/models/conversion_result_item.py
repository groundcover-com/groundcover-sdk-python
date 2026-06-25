from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversion_warning import ConversionWarning
    from ..models.monitor import Monitor


T = TypeVar("T", bound="ConversionResultItem")


@_attrs_define
class ConversionResultItem:
    """
    Attributes:
        conversion_warnings (list[ConversionWarning] | Unset):
        monitor (Monitor | Unset): Monitor represents a Datadog monitor
    """

    conversion_warnings: list[ConversionWarning] | Unset = UNSET
    monitor: Monitor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversion_warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conversion_warnings, Unset):
            conversion_warnings = []
            for conversion_warnings_item_data in self.conversion_warnings:
                conversion_warnings_item = conversion_warnings_item_data.to_dict()
                conversion_warnings.append(conversion_warnings_item)

        monitor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversion_warnings is not UNSET:
            field_dict["conversionWarnings"] = conversion_warnings
        if monitor is not UNSET:
            field_dict["monitor"] = monitor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_warning import ConversionWarning
        from ..models.monitor import Monitor

        d = dict(src_dict)
        _conversion_warnings = d.pop("conversionWarnings", UNSET)
        conversion_warnings: list[ConversionWarning] | Unset = UNSET
        if _conversion_warnings is not UNSET:
            conversion_warnings = []
            for conversion_warnings_item_data in _conversion_warnings:
                conversion_warnings_item = ConversionWarning.from_dict(conversion_warnings_item_data)

                conversion_warnings.append(conversion_warnings_item)

        _monitor = d.pop("monitor", UNSET)
        monitor: Monitor | Unset
        if isinstance(_monitor, Unset) or _monitor is None:
            monitor = UNSET
        else:
            monitor = Monitor.from_dict(_monitor)

        conversion_result_item = cls(
            conversion_warnings=conversion_warnings,
            monitor=monitor,
        )

        conversion_result_item.additional_properties = d
        return conversion_result_item

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
