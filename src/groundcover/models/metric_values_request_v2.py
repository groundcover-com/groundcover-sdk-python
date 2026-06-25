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


T = TypeVar("T", bound="MetricValuesRequestV2")


@_attrs_define
class MetricValuesRequestV2:
    """
    Attributes:
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        end (datetime.datetime | Unset):
        filter_ (str | Unset):
        key (str | Unset):
        limit (int | Unset):
        names (list[str] | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        start (datetime.datetime | Unset):
    """

    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    filter_: str | Unset = UNSET
    key: str | Unset = UNSET
    limit: int | Unset = UNSET
    names: list[str] | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        filter_ = self.filter_

        key = self.key

        limit = self.limit

        names: list[str] | Unset = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

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
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if end is not UNSET:
            field_dict["end"] = end
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if key is not UNSET:
            field_dict["key"] = key
        if limit is not UNSET:
            field_dict["limit"] = limit
        if names is not UNSET:
            field_dict["names"] = names
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
        _conditions = d.pop("conditions", UNSET)
        conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(
                    conditions_item_data
                )

                conditions.append(conditions_item)

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset) or _end is None:
            end = UNSET
        else:
            end = parse_datetime(_end)

        filter_ = d.pop("filter", UNSET)

        key = d.pop("key", UNSET)

        limit = d.pop("limit", UNSET)

        names = cast(list[str], d.pop("names", UNSET))

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

        metric_values_request_v2 = cls(
            conditions=conditions,
            end=end,
            filter_=filter_,
            key=key,
            limit=limit,
            names=names,
            sources=sources,
            start=start,
        )

        metric_values_request_v2.additional_properties = d
        return metric_values_request_v2

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
