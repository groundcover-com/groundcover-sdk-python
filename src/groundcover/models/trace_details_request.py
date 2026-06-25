from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )
    from ..models.group import Group


T = TypeVar("T", bound="TraceDetailsRequest")


@_attrs_define
class TraceDetailsRequest:
    """
    Attributes:
        end (datetime.datetime | Unset):
        group (Group | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        span_id (str | Unset):
        start (datetime.datetime | Unset):
    """

    end: datetime.datetime | Unset = UNSET
    group: Group | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    span_id: str | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        span_id = self.span_id

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if group is not UNSET:
            field_dict["group"] = group
        if sources is not UNSET:
            field_dict["sources"] = sources
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )
        from ..models.group import Group

        d = dict(src_dict)
        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset) or _end is None:
            end = UNSET
        else:
            end = parse_datetime(_end)

        _group = d.pop("group", UNSET)
        group: Group | Unset
        if isinstance(_group, Unset) or _group is None:
            group = UNSET
        else:
            group = Group.from_dict(_group)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        span_id = d.pop("spanId", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset) or _start is None:
            start = UNSET
        else:
            start = parse_datetime(_start)

        trace_details_request = cls(
            end=end,
            group=group,
            sources=sources,
            span_id=span_id,
            start=start,
        )

        trace_details_request.additional_properties = d
        return trace_details_request

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
