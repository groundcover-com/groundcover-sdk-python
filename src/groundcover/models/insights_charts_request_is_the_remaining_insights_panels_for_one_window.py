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


T = TypeVar("T", bound="InsightsChartsRequestIsTheRemainingInsightsPanelsForOneWindow")


@_attrs_define
class InsightsChartsRequestIsTheRemainingInsightsPanelsForOneWindow:
    """BucketDuration is the sentiment interval, parsed as the search-time-series
    routes parse theirs; empty uses the same bucket size as the existing
    time-series charts. TimeZone is an IANA time zone name and defaults to the
    request's time zone, then UTC.

        Attributes:
            end (datetime.datetime): End time of the request range
            start (datetime.datetime): Start time of the request range
            bucket_duration (str | Unset): BucketDuration is the sentiment interval as a whole number of seconds in a
                duration string with the units s, m and h, such as "10s", "5m", "1h" or
                "24h" (there is no d unit: "1d" answers 400); empty picks one from the
                window. A bucket longer than the window gives one bucket. Example: 10s.
            query (str | Unset): Query is the goal list's gcQL filter; pipes are not supported yet. Free text searches the
                goal title as the other search routes do: each word matches a whole word of the title and a quoted phrase must
                also appear in it, ignoring case; title is also a filter field, where title:"..." is an exact match and
                title:*word* a case-insensitive LIKE. Each other term names a known field (a goal field, a short judgment field
                such as outcome, or <evalKey>.<fieldKey>).
                A value of an enum or boolean Eval field must be one of its options.
                The goal time field is timestamp; _time is not accepted.
                The request window is [start, end): end is exclusive.
            sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Page-level conditions, ANDed
                with query; same fields and rules as query.
            time_zone (str | Unset): TimeZone is an IANA name for the sentiment buckets; empty uses the request time zone,
                then UTC.
    """

    end: datetime.datetime
    start: datetime.datetime
    bucket_duration: str | Unset = UNSET
    query: str | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    time_zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        bucket_duration = self.bucket_duration

        query = self.query

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )
        if bucket_duration is not UNSET:
            field_dict["bucketDuration"] = bucket_duration
        if query is not UNSET:
            field_dict["query"] = query
        if sources is not UNSET:
            field_dict["sources"] = sources
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )

        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

        start = parse_datetime(d.pop("start"))

        bucket_duration = d.pop("bucketDuration", UNSET)

        query = d.pop("query", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        time_zone = d.pop("timeZone", UNSET)

        insights_charts_request_is_the_remaining_insights_panels_for_one_window = cls(
            end=end,
            start=start,
            bucket_duration=bucket_duration,
            query=query,
            sources=sources,
            time_zone=time_zone,
        )

        insights_charts_request_is_the_remaining_insights_panels_for_one_window.additional_properties = d
        return insights_charts_request_is_the_remaining_insights_panels_for_one_window

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
