from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filters_with_estimated_map_response import FiltersWithEstimatedMapResponse


T = TypeVar("T", bound="SessionsFiltersResponse")


@_attrs_define
class SessionsFiltersResponse:
    """
    Attributes:
        filters (FiltersWithEstimatedMapResponse | Unset):
    """

    filters: FiltersWithEstimatedMapResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filters_with_estimated_map_response import FiltersWithEstimatedMapResponse

        d = dict(src_dict)
        _filters = d.pop("filters", UNSET)
        filters: FiltersWithEstimatedMapResponse | Unset
        if isinstance(_filters, Unset) or _filters is None:
            filters = UNSET
        else:
            filters = FiltersWithEstimatedMapResponse.from_dict(_filters)

        sessions_filters_response = cls(
            filters=filters,
        )

        sessions_filters_response.additional_properties = d
        return sessions_filters_response

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
