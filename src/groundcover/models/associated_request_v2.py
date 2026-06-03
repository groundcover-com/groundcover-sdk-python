from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.associated_filter import AssociatedFilter
    from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
        ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
    )


T = TypeVar("T", bound="AssociatedRequestV2")


@_attrs_define
class AssociatedRequestV2:
    """
    Attributes:
        end (datetime.datetime): End time for the search
        key (str): Key to search for values
        limit (int): Limit is the maximum number of results to return
        start (datetime.datetime): Start time for the search
        filter_associated (list[AssociatedFilter] | Unset): Filter associated is a list of filters
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset): Sources is a list of sources
            to filter the values by
    """

    end: datetime.datetime
    key: str
    limit: int
    start: datetime.datetime
    filter_associated: list[AssociatedFilter] | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        key = self.key

        limit = self.limit

        start = self.start.isoformat()

        filter_associated: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_associated, Unset):
            filter_associated = []
            for filter_associated_item_data in self.filter_associated:
                filter_associated_item = filter_associated_item_data.to_dict()
                filter_associated.append(filter_associated_item)

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
                "key": key,
                "limit": limit,
                "start": start,
            }
        )
        if filter_associated is not UNSET:
            field_dict["filterAssociated"] = filter_associated
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.associated_filter import AssociatedFilter
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )

        d = dict(src_dict)
        end = parse_datetime(d.pop("end"))

        key = d.pop("key")

        limit = d.pop("limit")

        start = parse_datetime(d.pop("start"))

        _filter_associated = d.pop("filterAssociated", UNSET)
        filter_associated: list[AssociatedFilter] | Unset = UNSET
        if _filter_associated is not UNSET:
            filter_associated = []
            for filter_associated_item_data in _filter_associated:
                filter_associated_item = AssociatedFilter.from_dict(filter_associated_item_data)

                filter_associated.append(filter_associated_item)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        associated_request_v2 = cls(
            end=end,
            key=key,
            limit=limit,
            start=start,
            filter_associated=filter_associated,
            sources=sources,
        )

        associated_request_v2.additional_properties = d
        return associated_request_v2

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
