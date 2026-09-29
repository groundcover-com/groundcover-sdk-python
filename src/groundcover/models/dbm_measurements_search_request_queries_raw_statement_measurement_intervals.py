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


T = TypeVar("T", bound="DBMMeasurementsSearchRequestQueriesRawStatementMeasurementIntervals")


@_attrs_define
class DBMMeasurementsSearchRequestQueriesRawStatementMeasurementIntervals:
    """A GCQL query is required. count() counts intervals;
    sum(calls) counts database executions.

        Attributes:
            end (datetime.datetime): End time of the request range
            query (str):
            start (datetime.datetime): Start time of the request range
            sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
    """

    end: datetime.datetime
    query: str
    start: datetime.datetime
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        query = self.query

        start = self.start.isoformat()

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
                "query": query,
                "start": start,
            }
        )
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )

        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

        query = d.pop("query")

        start = parse_datetime(d.pop("start"))

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        dbm_measurements_search_request_queries_raw_statement_measurement_intervals = cls(
            end=end,
            query=query,
            start=start,
            sources=sources,
        )

        dbm_measurements_search_request_queries_raw_statement_measurement_intervals.additional_properties = d
        return dbm_measurements_search_request_queries_raw_statement_measurement_intervals

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
