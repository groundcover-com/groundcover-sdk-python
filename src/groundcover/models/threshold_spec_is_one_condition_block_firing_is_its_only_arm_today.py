from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_firing_threshold import V2FiringThreshold


T = TypeVar("T", bound="ThresholdSpecIsOneConditionBlockFiringIsItsOnlyArmToday")


@_attrs_define
class ThresholdSpecIsOneConditionBlockFiringIsItsOnlyArmToday:
    """
    Attributes:
        firing (V2FiringThreshold | Unset): FiringThreshold is the static-threshold condition. Values cardinality is
            per-operator: 1 scalar, 2 ascending.
    """

    firing: V2FiringThreshold | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        firing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.firing, Unset):
            firing = self.firing.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firing is not UNSET:
            field_dict["firing"] = firing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_firing_threshold import V2FiringThreshold

        d = dict(src_dict)
        _firing = d.pop("firing", UNSET)
        firing: V2FiringThreshold | Unset
        if isinstance(_firing, Unset) or _firing is None:
            firing = UNSET
        else:
            firing = V2FiringThreshold.from_dict(_firing)

        threshold_spec_is_one_condition_block_firing_is_its_only_arm_today = cls(
            firing=firing,
        )

        threshold_spec_is_one_condition_block_firing_is_its_only_arm_today.additional_properties = d
        return threshold_spec_is_one_condition_block_firing_is_its_only_arm_today

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
