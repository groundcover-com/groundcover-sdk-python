from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logs_velocity import LogsVelocity


T = TypeVar("T", bound="LogsVelocityResponse")


@_attrs_define
class LogsVelocityResponse:
    """
    Attributes:
        is_estimate (bool | Unset):
        velocities (list[LogsVelocity] | Unset):
    """

    is_estimate: bool | Unset = UNSET
    velocities: list[LogsVelocity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_estimate = self.is_estimate

        velocities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.velocities, Unset):
            velocities = []
            for velocities_item_data in self.velocities:
                velocities_item = velocities_item_data.to_dict()
                velocities.append(velocities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_estimate is not UNSET:
            field_dict["isEstimate"] = is_estimate
        if velocities is not UNSET:
            field_dict["velocities"] = velocities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logs_velocity import LogsVelocity

        d = dict(src_dict)
        is_estimate = d.pop("isEstimate", UNSET)

        _velocities = d.pop("velocities", UNSET)
        velocities: list[LogsVelocity] | Unset = UNSET
        if _velocities is not UNSET:
            velocities = []
            for velocities_item_data in _velocities:
                velocities_item = LogsVelocity.from_dict(velocities_item_data)

                velocities.append(velocities_item)

        logs_velocity_response = cls(
            is_estimate=is_estimate,
            velocities=velocities,
        )

        logs_velocity_response.additional_properties = d
        return logs_velocity_response

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
