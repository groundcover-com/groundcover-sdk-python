from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logs_datasets import LogsDatasets
    from ..models.logs_missing_bucket import LogsMissingBucket
    from ..models.missing_metrics_breakdown_splits_missing_metrics_into_mutually_exclusive_buckets import (
        MissingMetricsBreakdownSplitsMissingMetricsIntoMutuallyExclusiveBuckets,
    )
    from ..models.value_missing_bucket_lists_units_whose_filter_values_are_absent_in_groundcover import (
        ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover,
    )


T = TypeVar("T", bound="MissingDataSetBucketCoversConvertedUnitsWhoseUnderlyingDatasetIsAbsent")


@_attrs_define
class MissingDataSetBucketCoversConvertedUnitsWhoseUnderlyingDatasetIsAbsent:
    """
    Attributes:
        logs (LogsMissingBucket | Unset): LogsMissingBucket covers units whose log dataset is absent, including the case
            where the log source they filter on is not ingested into groundcover at all.
        metrics (MissingMetricsBreakdownSplitsMissingMetricsIntoMutuallyExclusiveBuckets | Unset): A metric can qualify
            for several buckets at once (a datadog.* metric that is
            also inactive, say). It is counted in exactly one — chosen by the priority
            order in classifyMissingMetric — and carries a tag for every bucket that
            applies, so nothing is lost to that choice.
        missing_env (ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover | Unset):
        tail (LogsDatasets | Unset):
        total (int | Unset):
    """

    logs: LogsMissingBucket | Unset = UNSET
    metrics: MissingMetricsBreakdownSplitsMissingMetricsIntoMutuallyExclusiveBuckets | Unset = UNSET
    missing_env: ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover | Unset = UNSET
    tail: LogsDatasets | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logs, Unset):
            logs = self.logs.to_dict()

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        missing_env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.missing_env, Unset):
            missing_env = self.missing_env.to_dict()

        tail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tail, Unset):
            tail = self.tail.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logs is not UNSET:
            field_dict["logs"] = logs
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if missing_env is not UNSET:
            field_dict["missing_env"] = missing_env
        if tail is not UNSET:
            field_dict["tail"] = tail
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logs_datasets import LogsDatasets
        from ..models.logs_missing_bucket import LogsMissingBucket
        from ..models.missing_metrics_breakdown_splits_missing_metrics_into_mutually_exclusive_buckets import (
            MissingMetricsBreakdownSplitsMissingMetricsIntoMutuallyExclusiveBuckets,
        )
        from ..models.value_missing_bucket_lists_units_whose_filter_values_are_absent_in_groundcover import (
            ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover,
        )

        d = dict(src_dict)
        _logs = d.pop("logs", UNSET)
        logs: LogsMissingBucket | Unset
        if isinstance(_logs, Unset) or _logs is None:
            logs = UNSET
        else:
            logs = LogsMissingBucket.from_dict(_logs)

        _metrics = d.pop("metrics", UNSET)
        metrics: MissingMetricsBreakdownSplitsMissingMetricsIntoMutuallyExclusiveBuckets | Unset
        if isinstance(_metrics, Unset) or _metrics is None:
            metrics = UNSET
        else:
            metrics = MissingMetricsBreakdownSplitsMissingMetricsIntoMutuallyExclusiveBuckets.from_dict(_metrics)

        _missing_env = d.pop("missing_env", UNSET)
        missing_env: ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover | Unset
        if isinstance(_missing_env, Unset) or _missing_env is None:
            missing_env = UNSET
        else:
            missing_env = ValueMissingBucketListsUnitsWhoseFilterValuesAreAbsentInGroundcover.from_dict(_missing_env)

        _tail = d.pop("tail", UNSET)
        tail: LogsDatasets | Unset
        if isinstance(_tail, Unset) or _tail is None:
            tail = UNSET
        else:
            tail = LogsDatasets.from_dict(_tail)

        total = d.pop("total", UNSET)

        missing_data_set_bucket_covers_converted_units_whose_underlying_dataset_is_absent = cls(
            logs=logs,
            metrics=metrics,
            missing_env=missing_env,
            tail=tail,
            total=total,
        )

        missing_data_set_bucket_covers_converted_units_whose_underlying_dataset_is_absent.additional_properties = d
        return missing_data_set_bucket_covers_converted_units_whose_underlying_dataset_is_absent

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
