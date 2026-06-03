from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="DistributedTraceSummaryResult")


@_attrs_define
class DistributedTraceSummaryResult:
    """
    Attributes:
        execution_time_percentage (float | Unset):
        execution_time_total (float | Unset):
        service_name (str | Unset):
        span_count (int | Unset):
    """

    execution_time_percentage: float | Unset = UNSET
    execution_time_total: float | Unset = UNSET
    service_name: str | Unset = UNSET
    span_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_time_percentage = self.execution_time_percentage

        execution_time_total = self.execution_time_total

        service_name = self.service_name

        span_count = self.span_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_time_percentage is not UNSET:
            field_dict["executionTimePercentage"] = execution_time_percentage
        if execution_time_total is not UNSET:
            field_dict["executionTimeTotal"] = execution_time_total
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if span_count is not UNSET:
            field_dict["spanCount"] = span_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        execution_time_percentage = d.pop("executionTimePercentage", UNSET)

        execution_time_total = d.pop("executionTimeTotal", UNSET)

        service_name = d.pop("serviceName", UNSET)

        span_count = d.pop("spanCount", UNSET)

        distributed_trace_summary_result = cls(
            execution_time_percentage=execution_time_percentage,
            execution_time_total=execution_time_total,
            service_name=service_name,
            span_count=span_count,
        )

        distributed_trace_summary_result.additional_properties = d
        return distributed_trace_summary_result

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
