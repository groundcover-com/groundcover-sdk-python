from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matching_route import MatchingRoute


T = TypeVar("T", bound="SearchResponse")


@_attrs_define
class SearchResponse:
    """
    Attributes:
        matching_routes (list[MatchingRoute] | Unset): List of notification routes that match the monitor attributes
    """

    matching_routes: list[MatchingRoute] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matching_routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matching_routes, Unset):
            matching_routes = []
            for matching_routes_item_data in self.matching_routes:
                matching_routes_item = matching_routes_item_data.to_dict()
                matching_routes.append(matching_routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if matching_routes is not UNSET:
            field_dict["matchingRoutes"] = matching_routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matching_route import MatchingRoute

        d = dict(src_dict)
        _matching_routes = d.pop("matchingRoutes", UNSET)
        matching_routes: list[MatchingRoute] | Unset = UNSET
        if _matching_routes is not UNSET:
            matching_routes = []
            for matching_routes_item_data in _matching_routes:
                matching_routes_item = MatchingRoute.from_dict(matching_routes_item_data)

                matching_routes.append(matching_routes_item)

        search_response = cls(
            matching_routes=matching_routes,
        )

        search_response.additional_properties = d
        return search_response

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
