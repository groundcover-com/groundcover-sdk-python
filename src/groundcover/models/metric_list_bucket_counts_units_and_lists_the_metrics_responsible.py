from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tagged_metric_names_a_metric_plus_every_classification_that_applies_to_it import (
        TaggedMetricNamesAMetricPlusEveryClassificationThatAppliesToIt,
    )


T = TypeVar("T", bound="MetricListBucketCountsUnitsAndListsTheMetricsResponsible")


@_attrs_define
class MetricListBucketCountsUnitsAndListsTheMetricsResponsible:
    """
    Attributes:
        count (int | Unset):
        metrics (list[TaggedMetricNamesAMetricPlusEveryClassificationThatAppliesToIt] | Unset):
    """

    count: int | Unset = UNSET
    metrics: list[TaggedMetricNamesAMetricPlusEveryClassificationThatAppliesToIt] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tagged_metric_names_a_metric_plus_every_classification_that_applies_to_it import (
            TaggedMetricNamesAMetricPlusEveryClassificationThatAppliesToIt,
        )

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: list[TaggedMetricNamesAMetricPlusEveryClassificationThatAppliesToIt] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = TaggedMetricNamesAMetricPlusEveryClassificationThatAppliesToIt.from_dict(
                    metrics_item_data
                )

                metrics.append(metrics_item)

        metric_list_bucket_counts_units_and_lists_the_metrics_responsible = cls(
            count=count,
            metrics=metrics,
        )

        metric_list_bucket_counts_units_and_lists_the_metrics_responsible.additional_properties = d
        return metric_list_bucket_counts_units_and_lists_the_metrics_responsible

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
