from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_result import DiscoveryResult


T = TypeVar("T", bound="DiscoveryResponse")


@_attrs_define
class DiscoveryResponse:
    """
    Attributes:
        is_limit_reached (bool | Unset):
        results (list[DiscoveryResult] | Unset):
    """

    is_limit_reached: bool | Unset = UNSET
    results: list[DiscoveryResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_limit_reached = self.is_limit_reached

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_limit_reached is not UNSET:
            field_dict["isLimitReached"] = is_limit_reached
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_result import DiscoveryResult

        d = dict(src_dict)
        is_limit_reached = d.pop("isLimitReached", UNSET)

        _results = d.pop("results", UNSET)
        results: list[DiscoveryResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = DiscoveryResult.from_dict(results_item_data)

                results.append(results_item)

        discovery_response = cls(
            is_limit_reached=is_limit_reached,
            results=results,
        )

        discovery_response.additional_properties = d
        return discovery_response

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
