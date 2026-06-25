from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )


T = TypeVar("T", bound="SearchKeysRequestV2")


@_attrs_define
class SearchKeysRequestV2:
    """
    Attributes:
        limit (int): Limit is the maximum number of keys to return
        types (list[str]): Types is a slice of types of search keys to retrieve
        end (datetime.datetime | Unset): End is the end time for the metrics keys query
        filter_key (str | Unset): Filter is a string to filter the keys by
        metric_names (list[str] | Unset): Name specifies the metric name to get keys for.
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Sources is a list of sources
            to filter the keys by
        start (datetime.datetime | Unset): Start is the start time for the metrics keys query
    """

    limit: int
    types: list[str]
    end: datetime.datetime | Unset = UNSET
    filter_key: str | Unset = UNSET
    metric_names: list[str] | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        types = self.types

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        filter_key = self.filter_key

        metric_names: list[str] | Unset = UNSET
        if not isinstance(self.metric_names, Unset):
            metric_names = self.metric_names

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "types": types,
            }
        )
        if end is not UNSET:
            field_dict["end"] = end
        if filter_key is not UNSET:
            field_dict["filterKey"] = filter_key
        if metric_names is not UNSET:
            field_dict["metricNames"] = metric_names
        if sources is not UNSET:
            field_dict["sources"] = sources
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )

        d = dict(src_dict)
        limit = d.pop("limit")

        types = cast(list[str], d.pop("types"))

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset) or _end is None:
            end = UNSET
        else:
            end = parse_datetime(_end)

        filter_key = d.pop("filterKey", UNSET)

        metric_names = cast(list[str], d.pop("metricNames", UNSET))

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset) or _start is None:
            start = UNSET
        else:
            start = parse_datetime(_start)

        search_keys_request_v2 = cls(
            limit=limit,
            types=types,
            end=end,
            filter_key=filter_key,
            metric_names=metric_names,
            sources=sources,
            start=start,
        )

        search_keys_request_v2.additional_properties = d
        return search_keys_request_v2

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
