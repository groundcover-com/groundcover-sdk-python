from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metrics_discovery_result import MetricsDiscoveryResult


T = TypeVar("T", bound="MetricsDiscoveryResponse")


@_attrs_define
class MetricsDiscoveryResponse:
    """
    Attributes:
        name (str | Unset):
        results (list[MetricsDiscoveryResult] | Unset):
    """

    name: str | Unset = UNSET
    results: list[MetricsDiscoveryResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_discovery_result import MetricsDiscoveryResult

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _results = d.pop("results", UNSET)
        results: list[MetricsDiscoveryResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = MetricsDiscoveryResult.from_dict(results_item_data)

                results.append(results_item)

        metrics_discovery_response = cls(
            name=name,
            results=results,
        )

        metrics_discovery_response.additional_properties = d
        return metrics_discovery_response

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
