from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_velocity import MetricVelocity


T = TypeVar("T", bound="ListApisLatenciesResponse")


@_attrs_define
class ListApisLatenciesResponse:
    """
    Attributes:
        velocities (list[MetricVelocity] | Unset):
    """

    velocities: list[MetricVelocity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        velocities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.velocities, Unset):
            velocities = []
            for velocities_item_data in self.velocities:
                velocities_item = velocities_item_data.to_dict()
                velocities.append(velocities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if velocities is not UNSET:
            field_dict["velocities"] = velocities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_velocity import MetricVelocity

        d = dict(src_dict)
        _velocities = d.pop("velocities", UNSET)
        velocities: list[MetricVelocity] | Unset = UNSET
        if _velocities is not UNSET:
            velocities = []
            for velocities_item_data in _velocities:
                velocities_item = MetricVelocity.from_dict(velocities_item_data)

                velocities.append(velocities_item)

        list_apis_latencies_response = cls(
            velocities=velocities,
        )

        list_apis_latencies_response.additional_properties = d
        return list_apis_latencies_response

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
