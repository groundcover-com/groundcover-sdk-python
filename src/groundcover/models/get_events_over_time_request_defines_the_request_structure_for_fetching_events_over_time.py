from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_events_over_time_request_defines_the_request_structure_for_fetching_events_over_time_sort_by import (
    GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortBy,
)
from ..models.get_events_over_time_request_defines_the_request_structure_for_fetching_events_over_time_sort_order import (
    GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortOrder,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )
    from ..models.group import Group


T = TypeVar("T", bound="GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime")


@_attrs_define
class GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTime:
    """
    Attributes:
        end (datetime.datetime): End time of the request range
        sort_by (GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortBy): Field to sort
            events by.
        sort_order (GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortOrder): Sort order.
        start (datetime.datetime): Start time of the request range
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        group (Group | Unset):
        limit (int | Unset): Maximum number of events to return.
        query (str | Unset):
        skip (int | Unset): Number of events to skip (for pagination).
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Source filters for events.
        with_raw_events (bool | Unset): Include raw event data in the response.
    """

    end: datetime.datetime
    sort_by: GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortBy
    sort_order: GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortOrder
    start: datetime.datetime
    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    group: Group | Unset = UNSET
    limit: int | Unset = UNSET
    query: str | Unset = UNSET
    skip: int | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    with_raw_events: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        sort_by = self.sort_by.value

        sort_order = self.sort_order.value

        start = self.start.isoformat()

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        limit = self.limit

        query = self.query

        skip = self.skip

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        with_raw_events = self.with_raw_events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "start": start,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if group is not UNSET:
            field_dict["group"] = group
        if limit is not UNSET:
            field_dict["limit"] = limit
        if query is not UNSET:
            field_dict["query"] = query
        if skip is not UNSET:
            field_dict["skip"] = skip
        if sources is not UNSET:
            field_dict["sources"] = sources
        if with_raw_events is not UNSET:
            field_dict["withRawEvents"] = with_raw_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )
        from ..models.group import Group

        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

        sort_by = GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortBy(d.pop("sortBy"))

        sort_order = GetEventsOverTimeRequestDefinesTheRequestStructureForFetchingEventsOverTimeSortOrder(
            d.pop("sortOrder")
        )

        start = parse_datetime(d.pop("start"))

        _conditions = d.pop("conditions", UNSET)
        conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(
                    conditions_item_data
                )

                conditions.append(conditions_item)

        _group = d.pop("group", UNSET)
        group: Group | Unset
        if isinstance(_group, Unset) or _group is None:
            group = UNSET
        else:
            group = Group.from_dict(_group)

        limit = d.pop("limit", UNSET)

        query = d.pop("query", UNSET)

        skip = d.pop("skip", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        with_raw_events = d.pop("withRawEvents", UNSET)

        get_events_over_time_request_defines_the_request_structure_for_fetching_events_over_time = cls(
            end=end,
            sort_by=sort_by,
            sort_order=sort_order,
            start=start,
            conditions=conditions,
            group=group,
            limit=limit,
            query=query,
            skip=skip,
            sources=sources,
            with_raw_events=with_raw_events,
        )

        get_events_over_time_request_defines_the_request_structure_for_fetching_events_over_time.additional_properties = d
        return get_events_over_time_request_defines_the_request_structure_for_fetching_events_over_time

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
