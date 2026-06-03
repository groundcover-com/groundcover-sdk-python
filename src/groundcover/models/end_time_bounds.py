from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EndTimeBounds")


@_attrs_define
class EndTimeBounds:
    """It provides GCQL _time filter override: when GCQL contains _time filters, they replace
    the request's Start/End. Original bounds are preserved for cross-domain fallback.

        Attributes:
            end (datetime.datetime): End time of the request range
            start (datetime.datetime): Start time of the request range
    """

    end: datetime.datetime
    start: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

        start = parse_datetime(d.pop("start"))

        end_time_bounds = cls(
            end=end,
            start=start,
        )

        end_time_bounds.additional_properties = d
        return end_time_bounds

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
