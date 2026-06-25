from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_labels import MetricLabels
    from ..models.sample_pair import SamplePair


T = TypeVar("T", bound="MetricVelocityWithLabels")


@_attrs_define
class MetricVelocityWithLabels:
    """
    Attributes:
        metric (MetricLabels | Unset):
        velocity (list[SamplePair] | Unset):
    """

    metric: MetricLabels | Unset = UNSET
    velocity: list[SamplePair] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric.to_dict()

        velocity: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.velocity, Unset):
            velocity = []
            for velocity_item_data in self.velocity:
                velocity_item = velocity_item_data.to_dict()
                velocity.append(velocity_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric is not UNSET:
            field_dict["metric"] = metric
        if velocity is not UNSET:
            field_dict["velocity"] = velocity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_labels import MetricLabels
        from ..models.sample_pair import SamplePair

        d = dict(src_dict)
        _metric = d.pop("metric", UNSET)
        metric: MetricLabels | Unset
        if isinstance(_metric, Unset) or _metric is None:
            metric = UNSET
        else:
            metric = MetricLabels.from_dict(_metric)

        _velocity = d.pop("velocity", UNSET)
        velocity: list[SamplePair] | Unset = UNSET
        if _velocity is not UNSET:
            velocity = []
            for velocity_item_data in _velocity:
                velocity_item = SamplePair.from_dict(velocity_item_data)

                velocity.append(velocity_item)

        metric_velocity_with_labels = cls(
            metric=metric,
            velocity=velocity,
        )

        metric_velocity_with_labels.additional_properties = d
        return metric_velocity_with_labels

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
