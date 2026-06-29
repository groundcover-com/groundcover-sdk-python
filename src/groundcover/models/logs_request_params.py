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
    from ..models.selector import Selector


T = TypeVar("T", bound="LogsRequestParams")


@_attrs_define
class LogsRequestParams:
    """
    Attributes:
        end (datetime.datetime): End time of the request range
        start (datetime.datetime): Start time of the request range
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        enable_stream (bool | Unset):
        group (Group | Unset):
        limit (int | Unset):
        query (str | Unset):
        selectors (list[Selector] | Unset):
        skip (int | Unset):
        sort_order (str | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        truncate_line (bool | Unset):
    """

    end: datetime.datetime
    start: datetime.datetime
    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    enable_stream: bool | Unset = UNSET
    group: Group | Unset = UNSET
    limit: int | Unset = UNSET
    query: str | Unset = UNSET
    selectors: list[Selector] | Unset = UNSET
    skip: int | Unset = UNSET
    sort_order: str | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    truncate_line: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

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

        limit = self.limit

        query = self.query

        selectors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.selectors, Unset):
            selectors = []
            for selectors_item_data in self.selectors:
                selectors_item = selectors_item_data.to_dict()
                selectors.append(selectors_item)

        skip = self.skip

        sort_order = self.sort_order

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        truncate_line = self.truncate_line

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if enable_stream is not UNSET:
            field_dict["enableStream"] = enable_stream
        if group is not UNSET:
            field_dict["group"] = group
        if limit is not UNSET:
            field_dict["limit"] = limit
        if query is not UNSET:
            field_dict["query"] = query
        if selectors is not UNSET:
            field_dict["selectors"] = selectors
        if skip is not UNSET:
            field_dict["skip"] = skip
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if sources is not UNSET:
            field_dict["sources"] = sources
        if truncate_line is not UNSET:
            field_dict["truncateLine"] = truncate_line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )
        from ..models.group import Group
        from ..models.selector import Selector

        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

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

        enable_stream = d.pop("enableStream", UNSET)

        _group = d.pop("group", UNSET)
        group: Group | Unset
        if isinstance(_group, Unset) or _group is None:
            group = UNSET
        else:
            group = Group.from_dict(_group)

        limit = d.pop("limit", UNSET)

        query = d.pop("query", UNSET)

        _selectors = d.pop("selectors", UNSET)
        selectors: list[Selector] | Unset = UNSET
        if _selectors is not UNSET:
            selectors = []
            for selectors_item_data in _selectors:
                selectors_item = Selector.from_dict(selectors_item_data)

                selectors.append(selectors_item)

        skip = d.pop("skip", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        truncate_line = d.pop("truncateLine", UNSET)

        logs_request_params = cls(
            end=end,
            start=start,
            conditions=conditions,
            enable_stream=enable_stream,
            group=group,
            limit=limit,
            query=query,
            selectors=selectors,
            skip=skip,
            sort_order=sort_order,
            sources=sources,
            truncate_line=truncate_line,
        )

        logs_request_params.additional_properties = d
        return logs_request_params

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
