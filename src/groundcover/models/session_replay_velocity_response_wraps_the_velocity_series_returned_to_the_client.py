from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_velocity_with_labels import MetricVelocityWithLabels


T = TypeVar("T", bound="SessionReplayVelocityResponseWrapsTheVelocitySeriesReturnedToTheClient")


@_attrs_define
class SessionReplayVelocityResponseWrapsTheVelocitySeriesReturnedToTheClient:
    """
    Attributes:
        series (list[MetricVelocityWithLabels] | Unset):
    """

    series: list[MetricVelocityWithLabels] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_velocity_with_labels import MetricVelocityWithLabels

        d = dict(src_dict)
        _series = d.pop("series", UNSET)
        series: list[MetricVelocityWithLabels] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = MetricVelocityWithLabels.from_dict(series_item_data)

                series.append(series_item)

        session_replay_velocity_response_wraps_the_velocity_series_returned_to_the_client = cls(
            series=series,
        )

        session_replay_velocity_response_wraps_the_velocity_series_returned_to_the_client.additional_properties = d
        return session_replay_velocity_response_wraps_the_velocity_series_returned_to_the_client

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
