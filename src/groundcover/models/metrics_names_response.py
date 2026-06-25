from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metrics_names_result_enriched import MetricsNamesResultEnriched


T = TypeVar("T", bound="MetricsNamesResponse")


@_attrs_define
class MetricsNamesResponse:
    """
    Attributes:
        is_limit_reached (bool | Unset): IsLimitReached indicates whether the query limit was reached.
        metrics (list[MetricsNamesResultEnriched] | Unset): Metrics is the list of enriched metric results.
    """

    is_limit_reached: bool | Unset = UNSET
    metrics: list[MetricsNamesResultEnriched] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_limit_reached = self.is_limit_reached

        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_limit_reached is not UNSET:
            field_dict["isLimitReached"] = is_limit_reached
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_names_result_enriched import MetricsNamesResultEnriched

        d = dict(src_dict)
        is_limit_reached = d.pop("isLimitReached", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: list[MetricsNamesResultEnriched] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = MetricsNamesResultEnriched.from_dict(metrics_item_data)

                metrics.append(metrics_item)

        metrics_names_response = cls(
            is_limit_reached=is_limit_reached,
            metrics=metrics,
        )

        metrics_names_response.additional_properties = d
        return metrics_names_response

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
