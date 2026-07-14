from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.detection_signal import DetectionSignal


T = TypeVar("T", bound="Detection")


@_attrs_define
class Detection:
    """Detection groups the signals used to suggest dashboard relevance for a
    tenant. Inert in MVP (not evaluated against live data).

        Attributes:
            signals (list[DetectionSignal] | Unset):
    """

    signals: list[DetectionSignal] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.signals, Unset):
            signals = []
            for signals_item_data in self.signals:
                signals_item = signals_item_data.to_dict()
                signals.append(signals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signals is not UNSET:
            field_dict["signals"] = signals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.detection_signal import DetectionSignal

        d = dict(src_dict)
        _signals = d.pop("signals", UNSET)
        signals: list[DetectionSignal] | Unset = UNSET
        if _signals is not UNSET:
            signals = []
            for signals_item_data in _signals:
                signals_item = DetectionSignal.from_dict(signals_item_data)

                signals.append(signals_item)

        detection = cls(
            signals=signals,
        )

        detection.additional_properties = d
        return detection

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
