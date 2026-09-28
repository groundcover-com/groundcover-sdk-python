from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_recovery_threshold import V2RecoveryThreshold


T = TypeVar("T", bound="V2FiringThreshold")


@_attrs_define
class V2FiringThreshold:
    """FiringThreshold is the static-threshold condition. Values cardinality is
    per-operator: 1 scalar, 2 ascending.

        Attributes:
            operator (str | Unset):
            recovery (V2RecoveryThreshold | Unset): RecoveryThreshold is the hysteresis condition; its region must not
                overlap
                the firing one. Operator is the author's choice from the recovery-capable
                set — required, never defaulted.
            values (list[float] | Unset):
    """

    operator: str | Unset = UNSET
    recovery: V2RecoveryThreshold | Unset = UNSET
    values: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator

        recovery: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recovery, Unset):
            recovery = self.recovery.to_dict()

        values: list[float] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operator is not UNSET:
            field_dict["operator"] = operator
        if recovery is not UNSET:
            field_dict["recovery"] = recovery
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_recovery_threshold import V2RecoveryThreshold

        d = dict(src_dict)
        operator = d.pop("operator", UNSET)

        _recovery = d.pop("recovery", UNSET)
        recovery: V2RecoveryThreshold | Unset
        if isinstance(_recovery, Unset) or _recovery is None:
            recovery = UNSET
        else:
            recovery = V2RecoveryThreshold.from_dict(_recovery)

        values = cast(list[float], d.pop("values", UNSET))

        v2_firing_threshold = cls(
            operator=operator,
            recovery=recovery,
            values=values,
        )

        v2_firing_threshold.additional_properties = d
        return v2_firing_threshold

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
