from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MetricMapping")


@_attrs_define
class MetricMapping:
    """
    Attributes:
        groundcover_metric (str | Unset):
        source_metric (str | Unset):
    """

    groundcover_metric: str | Unset = UNSET
    source_metric: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groundcover_metric = self.groundcover_metric

        source_metric = self.source_metric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groundcover_metric is not UNSET:
            field_dict["groundcover_metric"] = groundcover_metric
        if source_metric is not UNSET:
            field_dict["source_metric"] = source_metric

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
        groundcover_metric = d.pop("groundcover_metric", UNSET)

        source_metric = d.pop("source_metric", UNSET)

        metric_mapping = cls(
            groundcover_metric=groundcover_metric,
            source_metric=source_metric,
        )

        metric_mapping.additional_properties = d
        return metric_mapping

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
