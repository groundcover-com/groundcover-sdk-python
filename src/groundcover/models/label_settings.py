from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_settings_extra_labels import LabelSettingsExtraLabels


T = TypeVar("T", bound="LabelSettings")


@_attrs_define
class LabelSettings:
    """
    Attributes:
        drop_labels (list[str] | Unset):
        extra_labels (LabelSettingsExtraLabels | Unset):
    """

    drop_labels: list[str] | Unset = UNSET
    extra_labels: LabelSettingsExtraLabels | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        drop_labels: list[str] | Unset = UNSET
        if not isinstance(self.drop_labels, Unset):
            drop_labels = self.drop_labels

        extra_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_labels, Unset):
            extra_labels = self.extra_labels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if drop_labels is not UNSET:
            field_dict["dropLabels"] = drop_labels
        if extra_labels is not UNSET:
            field_dict["extraLabels"] = extra_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_settings_extra_labels import LabelSettingsExtraLabels

        d = dict(src_dict)
        drop_labels = cast(list[str], d.pop("dropLabels", UNSET))

        _extra_labels = d.pop("extraLabels", UNSET)
        extra_labels: LabelSettingsExtraLabels | Unset
        if isinstance(_extra_labels, Unset) or _extra_labels is None:
            extra_labels = UNSET
        else:
            extra_labels = LabelSettingsExtraLabels.from_dict(_extra_labels)

        label_settings = cls(
            drop_labels=drop_labels,
            extra_labels=extra_labels,
        )

        label_settings.additional_properties = d
        return label_settings

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
