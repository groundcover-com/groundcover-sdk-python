from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )


T = TypeVar("T", bound="MonitorListRequest")


@_attrs_define
class MonitorListRequest:
    """
    Attributes:
        conditions (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Search conditions to
            filter monitors.
        limit (int | Unset): Maximum number of monitors to return (default 1000).
        query (str | Unset): GCQL filter string (filters only, no pipes or aggregations).
            Supported fields: monitor_name, type.
        skip (int | Unset): Number of monitors to skip for pagination.
        sort (str | Unset): Field to sort by: "name" (default) or "type".
    """

    conditions: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    limit: int | Unset = UNSET
    query: str | Unset = UNSET
    skip: int | Unset = UNSET
    sort: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        limit = self.limit

        query = self.query

        skip = self.skip

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if limit is not UNSET:
            field_dict["limit"] = limit
        if query is not UNSET:
            field_dict["query"] = query
        if skip is not UNSET:
            field_dict["skip"] = skip
        if sort is not UNSET:
            field_dict["sort"] = sort

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

        limit = d.pop("limit", UNSET)

        query = d.pop("query", UNSET)

        skip = d.pop("skip", UNSET)

        sort = d.pop("sort", UNSET)

        monitor_list_request = cls(
            conditions=conditions,
            limit=limit,
            query=query,
            skip=skip,
            sort=sort,
        )

        monitor_list_request.additional_properties = d
        return monitor_list_request

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
