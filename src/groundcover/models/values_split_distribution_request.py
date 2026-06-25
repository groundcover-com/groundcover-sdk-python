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


T = TypeVar("T", bound="ValuesSplitDistributionRequest")


@_attrs_define
class ValuesSplitDistributionRequest:
    """
    Attributes:
        end (datetime.datetime): End time of the request range
        start (datetime.datetime): Start time of the request range
        group (Group | Unset):
        limit (int | Unset):
        score_weight (float | Unset):
        selection_group (Group | Unset):
        selectors (list[Selector] | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
    """

    end: datetime.datetime
    start: datetime.datetime
    group: Group | Unset = UNSET
    limit: int | Unset = UNSET
    score_weight: float | Unset = UNSET
    selection_group: Group | Unset = UNSET
    selectors: list[Selector] | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        limit = self.limit

        score_weight = self.score_weight

        selection_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selection_group, Unset):
            selection_group = self.selection_group.to_dict()

        selectors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.selectors, Unset):
            selectors = []
            for selectors_item_data in self.selectors:
                selectors_item = selectors_item_data.to_dict()
                selectors.append(selectors_item)

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
                "start": start,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if limit is not UNSET:
            field_dict["limit"] = limit
        if score_weight is not UNSET:
            field_dict["score_weight"] = score_weight
        if selection_group is not UNSET:
            field_dict["selection_group"] = selection_group
        if selectors is not UNSET:
            field_dict["selectors"] = selectors
        if sources is not UNSET:
            field_dict["sources"] = sources

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

        _group = d.pop("group", UNSET)
        group: Group | Unset
        if isinstance(_group, Unset) or _group is None:
            group = UNSET
        else:
            group = Group.from_dict(_group)

        limit = d.pop("limit", UNSET)

        score_weight = d.pop("score_weight", UNSET)

        _selection_group = d.pop("selection_group", UNSET)
        selection_group: Group | Unset
        if isinstance(_selection_group, Unset) or _selection_group is None:
            selection_group = UNSET
        else:
            selection_group = Group.from_dict(_selection_group)

        _selectors = d.pop("selectors", UNSET)
        selectors: list[Selector] | Unset = UNSET
        if _selectors is not UNSET:
            selectors = []
            for selectors_item_data in _selectors:
                selectors_item = Selector.from_dict(selectors_item_data)

                selectors.append(selectors_item)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        values_split_distribution_request = cls(
            end=end,
            start=start,
            group=group,
            limit=limit,
            score_weight=score_weight,
            selection_group=selection_group,
            selectors=selectors,
            sources=sources,
        )

        values_split_distribution_request.additional_properties = d
        return values_split_distribution_request

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
