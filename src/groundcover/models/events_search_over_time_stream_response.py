from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_velocity_with_labels import MetricVelocityWithLabels


T = TypeVar("T", bound="EventsSearchOverTimeStreamResponse")


@_attrs_define
class EventsSearchOverTimeStreamResponse:
    """
    Attributes:
        data (list[MetricVelocityWithLabels] | Unset):
        done (bool | Unset):
        error (str | Unset):
    """

    data: list[MetricVelocityWithLabels] | Unset = UNSET
    done: bool | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        done = self.done

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if done is not UNSET:
            field_dict["done"] = done
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_velocity_with_labels import MetricVelocityWithLabels

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[MetricVelocityWithLabels] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = MetricVelocityWithLabels.from_dict(data_item_data)

                data.append(data_item)

        done = d.pop("done", UNSET)

        error = d.pop("error", UNSET)

        events_search_over_time_stream_response = cls(
            data=data,
            done=done,
            error=error,
        )

        events_search_over_time_stream_response.additional_properties = d
        return events_search_over_time_stream_response

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
