from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_values_request_type import SearchValuesRequestType
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )
    from ..models.group import Group


T = TypeVar("T", bound="SearchValuesRequest")


@_attrs_define
class SearchValuesRequest:
    """
    Attributes:
        key (str): Key to search for values
        limit (int): Limit specifies the maximum number of results to return
        type_ (SearchValuesRequestType): Type of the search values
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Conditions specifies
            additional conditions to filter the search values
        enable_stream (bool | Unset): EnableStream indicates whether to enable streaming of results
        end (datetime.datetime | Unset): End time for the search
            Required: true for logs, traces, events, issues; not required for entities
        filter_ (str | Unset): Filter to apply to the search values
        filter_group (Group | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Sources specifies the
            sources to filter the search values
        start (datetime.datetime | Unset): Start time for the search
            Required: true for logs, traces, events, issues; not required for entities
    """

    key: str
    limit: int
    type_: SearchValuesRequestType
    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    enable_stream: bool | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    filter_: str | Unset = UNSET
    filter_group: Group | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        limit = self.limit

        type_ = self.type_.value

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        enable_stream = self.enable_stream

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        filter_ = self.filter_

        filter_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_group, Unset):
            filter_group = self.filter_group.to_dict()

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
                "key": key,
                "limit": limit,
                "type": type_,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if enable_stream is not UNSET:
            field_dict["enableStream"] = enable_stream
        if end is not UNSET:
            field_dict["end"] = end
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if filter_group is not UNSET:
            field_dict["filterGroup"] = filter_group
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
        from ..models.group import Group

        d = dict(src_dict)
        key = d.pop("key")

        limit = d.pop("limit")

        type_ = SearchValuesRequestType(d.pop("type"))

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

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset) or _end is None:
            end = UNSET
        else:
            end = parse_datetime(_end)

        filter_ = d.pop("filter", UNSET)

        _filter_group = d.pop("filterGroup", UNSET)
        filter_group: Group | Unset
        if isinstance(_filter_group, Unset) or _filter_group is None:
            filter_group = UNSET
        else:
            filter_group = Group.from_dict(_filter_group)

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

        search_values_request = cls(
            key=key,
            limit=limit,
            type_=type_,
            conditions=conditions,
            enable_stream=enable_stream,
            end=end,
            filter_=filter_,
            filter_group=filter_group,
            sources=sources,
            start=start,
        )

        search_values_request.additional_properties = d
        return search_values_request

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
