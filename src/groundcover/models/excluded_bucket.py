from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_list_bucket_counts_units_and_lists_the_metrics_responsible import (
        MetricListBucketCountsUnitsAndListsTheMetricsResponsible,
    )


T = TypeVar("T", bound="ExcludedBucket")


@_attrs_define
class ExcludedBucket:
    """ExcludedBucket counts units held out of the funnel because their only unmet
    dependency is Datadog's own telemetry: a self-observability metric, or one
    already inactive in Datadog. Migration quality has no bearing on either —
    they were never going to return data — so they are reported separately
    rather than weighing on supported/unsupported like a real gap would.

        Attributes:
            datadog_self_observability (MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset):
            inactive_in_datadog (MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset):
            total (int | Unset):
    """

    datadog_self_observability: MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset = UNSET
    inactive_in_datadog: MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datadog_self_observability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.datadog_self_observability, Unset):
            datadog_self_observability = self.datadog_self_observability.to_dict()

        inactive_in_datadog: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inactive_in_datadog, Unset):
            inactive_in_datadog = self.inactive_in_datadog.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datadog_self_observability is not UNSET:
            field_dict["datadog_self_observability"] = datadog_self_observability
        if inactive_in_datadog is not UNSET:
            field_dict["inactive_in_datadog"] = inactive_in_datadog
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_list_bucket_counts_units_and_lists_the_metrics_responsible import (
            MetricListBucketCountsUnitsAndListsTheMetricsResponsible,
        )

        d = dict(src_dict)
        _datadog_self_observability = d.pop("datadog_self_observability", UNSET)
        datadog_self_observability: MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset
        if isinstance(_datadog_self_observability, Unset) or _datadog_self_observability is None:
            datadog_self_observability = UNSET
        else:
            datadog_self_observability = MetricListBucketCountsUnitsAndListsTheMetricsResponsible.from_dict(
                _datadog_self_observability
            )

        _inactive_in_datadog = d.pop("inactive_in_datadog", UNSET)
        inactive_in_datadog: MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset
        if isinstance(_inactive_in_datadog, Unset) or _inactive_in_datadog is None:
            inactive_in_datadog = UNSET
        else:
            inactive_in_datadog = MetricListBucketCountsUnitsAndListsTheMetricsResponsible.from_dict(
                _inactive_in_datadog
            )

        total = d.pop("total", UNSET)

        excluded_bucket = cls(
            datadog_self_observability=datadog_self_observability,
            inactive_in_datadog=inactive_in_datadog,
            total=total,
        )

        excluded_bucket.additional_properties = d
        return excluded_bucket

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
