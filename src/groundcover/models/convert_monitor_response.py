from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversion_result_item import ConversionResultItem


T = TypeVar("T", bound="ConvertMonitorResponse")


@_attrs_define
class ConvertMonitorResponse:
    """
    Attributes:
        data (ConversionResultItem | Unset):
        error (str | Unset):
        success (bool | Unset):
    """

    data: ConversionResultItem | Unset = UNSET
    error: str | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        error = self.error

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if error is not UNSET:
            field_dict["error"] = error
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_result_item import ConversionResultItem

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ConversionResultItem | Unset
        if isinstance(_data, Unset) or _data is None:
            data = UNSET
        else:
            data = ConversionResultItem.from_dict(_data)

        error = d.pop("error", UNSET)

        success = d.pop("success", UNSET)

        convert_monitor_response = cls(
            data=data,
            error=error,
            success=success,
        )

        convert_monitor_response.additional_properties = d
        return convert_monitor_response

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
