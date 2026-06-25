from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="TotalStats")


@_attrs_define
class TotalStats:
    """
    Attributes:
        avg_processing_time_seconds (float | Unset):
        eval_errors (int | Unset):
        eval_errors_percentage (float | Unset):
        exec_errors (int | Unset):
        exec_errors_percentage (float | Unset):
        logs_dropped (int | Unset):
        logs_dropped_rate (float | Unset):
        logs_seen (int | Unset):
        logs_seen_rate (float | Unset):
        processing_time_seconds (float | Unset):
    """

    avg_processing_time_seconds: float | Unset = UNSET
    eval_errors: int | Unset = UNSET
    eval_errors_percentage: float | Unset = UNSET
    exec_errors: int | Unset = UNSET
    exec_errors_percentage: float | Unset = UNSET
    logs_dropped: int | Unset = UNSET
    logs_dropped_rate: float | Unset = UNSET
    logs_seen: int | Unset = UNSET
    logs_seen_rate: float | Unset = UNSET
    processing_time_seconds: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_processing_time_seconds = self.avg_processing_time_seconds

        eval_errors = self.eval_errors

        eval_errors_percentage = self.eval_errors_percentage

        exec_errors = self.exec_errors

        exec_errors_percentage = self.exec_errors_percentage

        logs_dropped = self.logs_dropped

        logs_dropped_rate = self.logs_dropped_rate

        logs_seen = self.logs_seen

        logs_seen_rate = self.logs_seen_rate

        processing_time_seconds = self.processing_time_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_processing_time_seconds is not UNSET:
            field_dict["avgProcessingTimeSeconds"] = avg_processing_time_seconds
        if eval_errors is not UNSET:
            field_dict["evalErrors"] = eval_errors
        if eval_errors_percentage is not UNSET:
            field_dict["evalErrorsPercentage"] = eval_errors_percentage
        if exec_errors is not UNSET:
            field_dict["execErrors"] = exec_errors
        if exec_errors_percentage is not UNSET:
            field_dict["execErrorsPercentage"] = exec_errors_percentage
        if logs_dropped is not UNSET:
            field_dict["logsDropped"] = logs_dropped
        if logs_dropped_rate is not UNSET:
            field_dict["logsDroppedRate"] = logs_dropped_rate
        if logs_seen is not UNSET:
            field_dict["logsSeen"] = logs_seen
        if logs_seen_rate is not UNSET:
            field_dict["logsSeenRate"] = logs_seen_rate
        if processing_time_seconds is not UNSET:
            field_dict["processingTimeSeconds"] = processing_time_seconds

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
        avg_processing_time_seconds = d.pop("avgProcessingTimeSeconds", UNSET)

        eval_errors = d.pop("evalErrors", UNSET)

        eval_errors_percentage = d.pop("evalErrorsPercentage", UNSET)

        exec_errors = d.pop("execErrors", UNSET)

        exec_errors_percentage = d.pop("execErrorsPercentage", UNSET)

        logs_dropped = d.pop("logsDropped", UNSET)

        logs_dropped_rate = d.pop("logsDroppedRate", UNSET)

        logs_seen = d.pop("logsSeen", UNSET)

        logs_seen_rate = d.pop("logsSeenRate", UNSET)

        processing_time_seconds = d.pop("processingTimeSeconds", UNSET)

        total_stats = cls(
            avg_processing_time_seconds=avg_processing_time_seconds,
            eval_errors=eval_errors,
            eval_errors_percentage=eval_errors_percentage,
            exec_errors=exec_errors,
            exec_errors_percentage=exec_errors_percentage,
            logs_dropped=logs_dropped,
            logs_dropped_rate=logs_dropped_rate,
            logs_seen=logs_seen,
            logs_seen_rate=logs_seen_rate,
            processing_time_seconds=processing_time_seconds,
        )

        total_stats.additional_properties = d
        return total_stats

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
