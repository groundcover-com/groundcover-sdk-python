from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SpanSource")


@_attrs_define
class SpanSource:
    """
    Attributes:
        span_id (str):
        timestamp (datetime.datetime): Timestamp is the span's start; it keeps the lookup to the span's own partition.
        trace_id (str):
    """

    span_id: str
    timestamp: datetime.datetime
    trace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        span_id = self.span_id

        timestamp = self.timestamp.isoformat()

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "span_id": span_id,
                "timestamp": timestamp,
                "trace_id": trace_id,
            }
        )

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
        span_id = d.pop("span_id")

        timestamp = parse_datetime(d.pop("timestamp"))

        trace_id = d.pop("trace_id")

        span_source = cls(
            span_id=span_id,
            timestamp=timestamp,
            trace_id=trace_id,
        )

        span_source.additional_properties = d
        return span_source

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
