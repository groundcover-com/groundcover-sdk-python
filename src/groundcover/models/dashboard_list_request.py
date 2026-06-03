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


T = TypeVar("T", bound="DashboardListRequest")


@_attrs_define
class DashboardListRequest:
    """
    Attributes:
        limit (int | Unset): Maximum number of dashboards to return (default 1000).
        query (str | Unset): GCQL filter string (filters only, no pipes or aggregations).
            Supported fields: name, description.
        skip (int | Unset): Number of dashboards to skip for pagination.
        sort (str | Unset): Field to sort by: "name" (default) or "description".
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Source conditions for
            cluster/env filtering (ignored for dashboards).
    """

    limit: int | Unset = UNSET
    query: str | Unset = UNSET
    skip: int | Unset = UNSET
    sort: str | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        query = self.query

        skip = self.skip

        sort = self.sort

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if query is not UNSET:
            field_dict["query"] = query
        if skip is not UNSET:
            field_dict["skip"] = skip
        if sort is not UNSET:
            field_dict["sort"] = sort
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )

        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        query = d.pop("query", UNSET)

        skip = d.pop("skip", UNSET)

        sort = d.pop("sort", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        dashboard_list_request = cls(
            limit=limit,
            query=query,
            skip=skip,
            sort=sort,
            sources=sources,
        )

        dashboard_list_request.additional_properties = d
        return dashboard_list_request

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
