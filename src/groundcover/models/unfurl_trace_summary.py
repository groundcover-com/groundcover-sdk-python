from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unfurl_slowest_span import UnfurlSlowestSpan


T = TypeVar("T", bound="UnfurlTraceSummary")


@_attrs_define
class UnfurlTraceSummary:
    """UnfurlTraceSummary is the flat card-ready summary of a trace: exactly what a
    link-unfurl card renders, nothing more. TraceID is the resolved (propagated)
    id — the trace's stable identity regardless of which span the link came from.

        Attributes:
            duration_seconds (float | Unset):
            error_count (int | Unset):
            limit_reached (bool | Unset): LimitReached marks a trace that reached UnfurlSpanLimit: SpanCount is then
                a floor, not the trace's size.
            operation_name (str | Unset):
            resource (str | Unset):
            slowest_span (UnfurlSlowestSpan | Unset): UnfurlSlowestSpan is the slowest span of the trace excluding the
                card's root
                (which would just restate the trace duration).
            span_count (int | Unset):
            span_name (str | Unset):
            trace_id (str | Unset):
    """

    duration_seconds: float | Unset = UNSET
    error_count: int | Unset = UNSET
    limit_reached: bool | Unset = UNSET
    operation_name: str | Unset = UNSET
    resource: str | Unset = UNSET
    slowest_span: UnfurlSlowestSpan | Unset = UNSET
    span_count: int | Unset = UNSET
    span_name: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_seconds = self.duration_seconds

        error_count = self.error_count

        limit_reached = self.limit_reached

        operation_name = self.operation_name

        resource = self.resource

        slowest_span: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slowest_span, Unset):
            slowest_span = self.slowest_span.to_dict()

        span_count = self.span_count

        span_name = self.span_name

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if error_count is not UNSET:
            field_dict["errorCount"] = error_count
        if limit_reached is not UNSET:
            field_dict["limitReached"] = limit_reached
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name
        if resource is not UNSET:
            field_dict["resource"] = resource
        if slowest_span is not UNSET:
            field_dict["slowestSpan"] = slowest_span
        if span_count is not UNSET:
            field_dict["spanCount"] = span_count
        if span_name is not UNSET:
            field_dict["spanName"] = span_name
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unfurl_slowest_span import UnfurlSlowestSpan

        d = dict(src_dict)
        duration_seconds = d.pop("durationSeconds", UNSET)

        error_count = d.pop("errorCount", UNSET)

        limit_reached = d.pop("limitReached", UNSET)

        operation_name = d.pop("operationName", UNSET)

        resource = d.pop("resource", UNSET)

        _slowest_span = d.pop("slowestSpan", UNSET)
        slowest_span: UnfurlSlowestSpan | Unset
        if isinstance(_slowest_span, Unset) or _slowest_span is None:
            slowest_span = UNSET
        else:
            slowest_span = UnfurlSlowestSpan.from_dict(_slowest_span)

        span_count = d.pop("spanCount", UNSET)

        span_name = d.pop("spanName", UNSET)

        trace_id = d.pop("traceId", UNSET)

        unfurl_trace_summary = cls(
            duration_seconds=duration_seconds,
            error_count=error_count,
            limit_reached=limit_reached,
            operation_name=operation_name,
            resource=resource,
            slowest_span=slowest_span,
            span_count=span_count,
            span_name=span_name,
            trace_id=trace_id,
        )

        unfurl_trace_summary.additional_properties = d
        return unfurl_trace_summary

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
