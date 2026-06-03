from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logs_error_velocity_peak import LogsErrorVelocityPeak


T = TypeVar("T", bound="LogsErrorVelocityPeakResponse")


@_attrs_define
class LogsErrorVelocityPeakResponse:
    """
    Attributes:
        logs_error_velocity_peaks (list[LogsErrorVelocityPeak] | Unset):
    """

    logs_error_velocity_peaks: list[LogsErrorVelocityPeak] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs_error_velocity_peaks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.logs_error_velocity_peaks, Unset):
            logs_error_velocity_peaks = []
            for logs_error_velocity_peaks_item_data in self.logs_error_velocity_peaks:
                logs_error_velocity_peaks_item = logs_error_velocity_peaks_item_data.to_dict()
                logs_error_velocity_peaks.append(logs_error_velocity_peaks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logs_error_velocity_peaks is not UNSET:
            field_dict["logs_error_velocity_peaks"] = logs_error_velocity_peaks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logs_error_velocity_peak import LogsErrorVelocityPeak

        d = dict(src_dict)
        _logs_error_velocity_peaks = d.pop("logs_error_velocity_peaks", UNSET)
        logs_error_velocity_peaks: list[LogsErrorVelocityPeak] | Unset = UNSET
        if _logs_error_velocity_peaks is not UNSET:
            logs_error_velocity_peaks = []
            for logs_error_velocity_peaks_item_data in _logs_error_velocity_peaks:
                logs_error_velocity_peaks_item = LogsErrorVelocityPeak.from_dict(logs_error_velocity_peaks_item_data)

                logs_error_velocity_peaks.append(logs_error_velocity_peaks_item)

        logs_error_velocity_peak_response = cls(
            logs_error_velocity_peaks=logs_error_velocity_peaks,
        )

        logs_error_velocity_peak_response.additional_properties = d
        return logs_error_velocity_peak_response

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
