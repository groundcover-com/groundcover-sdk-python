from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MetricKeyGapAggregatesMissingLabelKeysForOneMetricAcrossUnits")


@_attrs_define
class MetricKeyGapAggregatesMissingLabelKeysForOneMetricAcrossUnits:
    """
    Attributes:
        count (int | Unset):
        keys (list[str] | Unset):
        metric (str | Unset):
    """

    count: int | Unset = UNSET
    keys: list[str] | Unset = UNSET
    metric: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        metric = self.metric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if keys is not UNSET:
            field_dict["keys"] = keys
        if metric is not UNSET:
            field_dict["metric"] = metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        keys = cast(list[str], d.pop("keys", UNSET))

        metric = d.pop("metric", UNSET)

        metric_key_gap_aggregates_missing_label_keys_for_one_metric_across_units = cls(
            count=count,
            keys=keys,
            metric=metric,
        )

        metric_key_gap_aggregates_missing_label_keys_for_one_metric_across_units.additional_properties = d
        return metric_key_gap_aggregates_missing_label_keys_for_one_metric_across_units

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
