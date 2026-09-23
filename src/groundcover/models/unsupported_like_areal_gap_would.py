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


T = TypeVar("T", bound="UnsupportedLikeArealGapWould")


@_attrs_define
class UnsupportedLikeArealGapWould:
    """A unit confirmed inactive in Datadog (IssueDDInactiveOrMissing) no longer
    lands here — see StageDDMetricInactive and DDMetricInactiveBucket, its own
    green success bucket under SupportedConverted. The former InactiveInDatadog
    field here was removed rather than kept as an always-zero counter: nothing
    outside this package ever read it (the funnelviz decoder only reads Total,
    and the CLI summary printer never printed Excluded at all), so there was no
    reader to preserve compatibility for.

        Attributes:
            datadog_self_observability (MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset):
            total (int | Unset):
    """

    datadog_self_observability: MetricListBucketCountsUnitsAndListsTheMetricsResponsible | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datadog_self_observability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.datadog_self_observability, Unset):
            datadog_self_observability = self.datadog_self_observability.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datadog_self_observability is not UNSET:
            field_dict["datadog_self_observability"] = datadog_self_observability
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

        total = d.pop("total", UNSET)

        unsupported_like_areal_gap_would = cls(
            datadog_self_observability=datadog_self_observability,
            total=total,
        )

        unsupported_like_areal_gap_would.additional_properties = d
        return unsupported_like_areal_gap_would

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
