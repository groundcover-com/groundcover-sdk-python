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


T = TypeVar("T", bound="MetricsNamesRequest")


@_attrs_define
class MetricsNamesRequest:
    """
    Attributes:
        end (datetime.datetime | Unset): End specifies the end time for the metric names query.
        filter_ (str | Unset): Filter specifies a search filter to apply to the metric names.
        limit (int | Unset): Limit specifies the maximum number of results to return.
        required (list[str] | Unset): Required specifies a list of metric names that must be included in the results.
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Sources specifies the
            sources to filter the metric names.
        start (datetime.datetime | Unset): Start specifies the start time for the metric names query.
    """

    end: datetime.datetime | Unset = UNSET
    filter_: str | Unset = UNSET
    limit: int | Unset = UNSET
    required: list[str] | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        filter_ = self.filter_

        limit = self.limit

        required: list[str] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

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
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if limit is not UNSET:
            field_dict["limit"] = limit
        if required is not UNSET:
            field_dict["required"] = required
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
        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset) or _end is None:
            end = UNSET
        else:
            end = parse_datetime(_end)

        filter_ = d.pop("filter", UNSET)

        limit = d.pop("limit", UNSET)

        required = cast(list[str], d.pop("required", UNSET))

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

        metrics_names_request = cls(
            end=end,
            filter_=filter_,
            limit=limit,
            required=required,
            sources=sources,
            start=start,
        )

        metrics_names_request.additional_properties = d
        return metrics_names_request

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
