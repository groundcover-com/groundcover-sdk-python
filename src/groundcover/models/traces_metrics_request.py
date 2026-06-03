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


T = TypeVar("T", bound="TracesMetricsRequest")


@_attrs_define
class TracesMetricsRequest:
    """
    Attributes:
        end (datetime.datetime): End time of the request range
        start (datetime.datetime): Start time of the request range
        optimized_end (datetime.datetime | Unset):
        optimized_start (datetime.datetime | Unset):
        bucket_resolution (str | Unset):
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        enable_stream (bool | Unset):
        group (Group | Unset):
        optimize_search (bool | Unset):
        query (str | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
    """

    end: datetime.datetime
    start: datetime.datetime
    optimized_end: datetime.datetime | Unset = UNSET
    optimized_start: datetime.datetime | Unset = UNSET
    bucket_resolution: str | Unset = UNSET
    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    enable_stream: bool | Unset = UNSET
    group: Group | Unset = UNSET
    optimize_search: bool | Unset = UNSET
    query: str | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        optimized_end: str | Unset = UNSET
        if not isinstance(self.optimized_end, Unset):
            optimized_end = self.optimized_end.isoformat()

        optimized_start: str | Unset = UNSET
        if not isinstance(self.optimized_start, Unset):
            optimized_start = self.optimized_start.isoformat()

        bucket_resolution = self.bucket_resolution

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        enable_stream = self.enable_stream

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        optimize_search = self.optimize_search

        query = self.query

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )
        if optimized_end is not UNSET:
            field_dict["OptimizedEnd"] = optimized_end
        if optimized_start is not UNSET:
            field_dict["OptimizedStart"] = optimized_start
        if bucket_resolution is not UNSET:
            field_dict["bucketResolution"] = bucket_resolution
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if enable_stream is not UNSET:
            field_dict["enableStream"] = enable_stream
        if group is not UNSET:
            field_dict["group"] = group
        if optimize_search is not UNSET:
            field_dict["optimizeSearch"] = optimize_search
        if query is not UNSET:
            field_dict["query"] = query
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )
        from ..models.group import Group

        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

        start = parse_datetime(d.pop("start"))

        _optimized_end = d.pop("OptimizedEnd", UNSET)
        optimized_end: datetime.datetime | Unset
        if isinstance(_optimized_end, Unset) or _optimized_end is None:
            optimized_end = UNSET
        else:
            optimized_end = parse_datetime(_optimized_end)

        _optimized_start = d.pop("OptimizedStart", UNSET)
        optimized_start: datetime.datetime | Unset
        if isinstance(_optimized_start, Unset) or _optimized_start is None:
            optimized_start = UNSET
        else:
            optimized_start = parse_datetime(_optimized_start)

        bucket_resolution = d.pop("bucketResolution", UNSET)

        _conditions = d.pop("conditions", UNSET)
        conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(
                    conditions_item_data
                )

                conditions.append(conditions_item)

        enable_stream = d.pop("enableStream", UNSET)

        _group = d.pop("group", UNSET)
        group: Group | Unset
        if isinstance(_group, Unset) or _group is None:
            group = UNSET
        else:
            group = Group.from_dict(_group)

        optimize_search = d.pop("optimizeSearch", UNSET)

        query = d.pop("query", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        traces_metrics_request = cls(
            end=end,
            start=start,
            optimized_end=optimized_end,
            optimized_start=optimized_start,
            bucket_resolution=bucket_resolution,
            conditions=conditions,
            enable_stream=enable_stream,
            group=group,
            optimize_search=optimize_search,
            query=query,
            sources=sources,
        )

        traces_metrics_request.additional_properties = d
        return traces_metrics_request

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
