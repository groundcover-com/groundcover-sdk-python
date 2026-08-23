from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_count_bucket_counts_units_per_data_source_mapping import (
        IntegrationCountBucketCountsUnitsPerDataSourceMapping,
    )
    from ..models.metric_list_bucket_counts_units_and_lists_the_metrics_responsible import (
        MetricListBucketCountsUnitsAndListsTheMetricsResponsible,
    )


T = TypeVar("T", bound="MissingMetricsBreakdownSplitsMissingMetricsIntoMutuallyExclusiveBuckets")


@_attrs_define
class MissingMetricsBreakdownSplitsMissingMetricsIntoMutuallyExclusiveBuckets:
    """A metric can qualify for several buckets at once (a datadog.* metric that is
    also inactive, say). It is counted in exactly one — chosen by the priority
    order in classifyMissingMetric — and carries a tag for every bucket that
    applies, so nothing is lost to that choice.

        Attributes:
            custom_metrics (MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset):
            datadog_self_observability (MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset):
            inactive_in_datadog (MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset):
            integrations_we_dont_have (IntegrationCountBucketCountsUnitsPerDataSourceMapping | Unset):
            integrations_we_have (IntegrationCountBucketCountsUnitsPerDataSourceMapping | Unset):
            total (int | Unset):
    """

    custom_metrics: MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset = UNSET
    datadog_self_observability: MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset = UNSET
    inactive_in_datadog: MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset = UNSET
    integrations_we_dont_have: IntegrationCountBucketCountsUnitsPerDataSourceMapping | Unset = UNSET
    integrations_we_have: IntegrationCountBucketCountsUnitsPerDataSourceMapping | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_metrics, Unset):
            custom_metrics = self.custom_metrics.to_dict()

        datadog_self_observability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.datadog_self_observability, Unset):
            datadog_self_observability = self.datadog_self_observability.to_dict()

        inactive_in_datadog: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inactive_in_datadog, Unset):
            inactive_in_datadog = self.inactive_in_datadog.to_dict()

        integrations_we_dont_have: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integrations_we_dont_have, Unset):
            integrations_we_dont_have = self.integrations_we_dont_have.to_dict()

        integrations_we_have: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integrations_we_have, Unset):
            integrations_we_have = self.integrations_we_have.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_metrics is not UNSET:
            field_dict["custom_metrics"] = custom_metrics
        if datadog_self_observability is not UNSET:
            field_dict["datadog_self_observability"] = datadog_self_observability
        if inactive_in_datadog is not UNSET:
            field_dict["inactive_in_datadog"] = inactive_in_datadog
        if integrations_we_dont_have is not UNSET:
            field_dict["integrations_we_dont_have"] = integrations_we_dont_have
        if integrations_we_have is not UNSET:
            field_dict["integrations_we_have"] = integrations_we_have
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_count_bucket_counts_units_per_data_source_mapping import (
            IntegrationCountBucketCountsUnitsPerDataSourceMapping,
        )
        from ..models.metric_list_bucket_counts_units_and_lists_the_metrics_responsible import (
            MetricListBucketCountsUnitsAndListsTheMetricsResponsible,
        )

        d = dict(src_dict)
        _custom_metrics = d.pop("custom_metrics", UNSET)
        custom_metrics: MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset
        if isinstance(_custom_metrics, Unset) or _custom_metrics is None:
            custom_metrics = UNSET
        else:
            custom_metrics = MetricListBucketCountsUnitsAndListsTheMetricsResponsible.from_dict(_custom_metrics)

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

        _integrations_we_dont_have = d.pop("integrations_we_dont_have", UNSET)
        integrations_we_dont_have: IntegrationCountBucketCountsUnitsPerDataSourceMapping | Unset
        if isinstance(_integrations_we_dont_have, Unset) or _integrations_we_dont_have is None:
            integrations_we_dont_have = UNSET
        else:
            integrations_we_dont_have = IntegrationCountBucketCountsUnitsPerDataSourceMapping.from_dict(
                _integrations_we_dont_have
            )

        _integrations_we_have = d.pop("integrations_we_have", UNSET)
        integrations_we_have: IntegrationCountBucketCountsUnitsPerDataSourceMapping | Unset
        if isinstance(_integrations_we_have, Unset) or _integrations_we_have is None:
            integrations_we_have = UNSET
        else:
            integrations_we_have = IntegrationCountBucketCountsUnitsPerDataSourceMapping.from_dict(
                _integrations_we_have
            )

        total = d.pop("total", UNSET)

        missing_metrics_breakdown_splits_missing_metrics_into_mutually_exclusive_buckets = cls(
            custom_metrics=custom_metrics,
            datadog_self_observability=datadog_self_observability,
            inactive_in_datadog=inactive_in_datadog,
            integrations_we_dont_have=integrations_we_dont_have,
            integrations_we_have=integrations_we_have,
            total=total,
        )

        missing_metrics_breakdown_splits_missing_metrics_into_mutually_exclusive_buckets.additional_properties = d
        return missing_metrics_breakdown_splits_missing_metrics_into_mutually_exclusive_buckets

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
