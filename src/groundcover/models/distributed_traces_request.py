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


T = TypeVar("T", bound="DistributedTracesRequest")


@_attrs_define
class DistributedTracesRequest:
    """
    Attributes:
        limit (int | Unset):
        source_type (str | Unset):
        sources (list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset):
        time (datetime.datetime | Unset):
        trace_id (str | Unset):
    """

    limit: int | Unset = UNSET
    source_type: str | Unset = UNSET
    sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        source_type = self.source_type

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if sources is not UNSET:
            field_dict["sources"] = sources
        if time is not UNSET:
            field_dict["time"] = time
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_specifies_a_search_condition_based_on_a_column_and_filters import (
            ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters,
        )

        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        source_type = d.pop("sourceType", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ConditionSpecifiesASearchConditionBasedOnAColumnAndFilters.from_dict(sources_item_data)

                sources.append(sources_item)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset) or _time is None:
            time = UNSET
        else:
            time = parse_datetime(_time)

        trace_id = d.pop("traceId", UNSET)

        distributed_traces_request = cls(
            limit=limit,
            source_type=source_type,
            sources=sources,
            time=time,
            trace_id=trace_id,
        )

        distributed_traces_request.additional_properties = d
        return distributed_traces_request

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
