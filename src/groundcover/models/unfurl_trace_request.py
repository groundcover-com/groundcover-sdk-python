from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="UnfurlTraceRequest")


@_attrs_define
class UnfurlTraceRequest:
    """UnfurlTraceRequest identifies the trace a shared link points at, verbatim
    from the link's drawer state. SpanID and Source drive the eBPF resolution:
    an eBPF drawer's traceId is the span's own raw id, so the propagated id must
    be resolved via span details before the waterfall is queried.

        Attributes:
            time (datetime.datetime):
            trace_id (str):
            source_type (str | Unset): SourceType is the trace's source type ("eBPF", "rum", …).
            span_id (str | Unset):
    """

    time: datetime.datetime
    trace_id: str
    source_type: str | Unset = UNSET
    span_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time.isoformat()

        trace_id = self.trace_id

        source_type = self.source_type

        span_id = self.span_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "traceId": trace_id,
            }
        )
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if span_id is not UNSET:
            field_dict["spanId"] = span_id

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
        time = parse_datetime(d.pop("time"))

        trace_id = d.pop("traceId")

        source_type = d.pop("sourceType", UNSET)

        span_id = d.pop("spanId", UNSET)

        unfurl_trace_request = cls(
            time=time,
            trace_id=trace_id,
            source_type=source_type,
            span_id=span_id,
        )

        unfurl_trace_request.additional_properties = d
        return unfurl_trace_request

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
