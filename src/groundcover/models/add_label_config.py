from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_label_config_add_label import AddLabelConfigAddLabel


T = TypeVar("T", bound="AddLabelConfig")


@_attrs_define
class AddLabelConfig:
    """
    Attributes:
        add_label (AddLabelConfigAddLabel | Unset):
    """

    add_label: AddLabelConfigAddLabel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_label, Unset):
            add_label = self.add_label.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_label is not UNSET:
            field_dict["addLabel"] = add_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_label_config_add_label import AddLabelConfigAddLabel

        d = dict(src_dict)
        _add_label = d.pop("addLabel", UNSET)
        add_label: AddLabelConfigAddLabel | Unset
        if isinstance(_add_label, Unset) or _add_label is None:
            add_label = UNSET
        else:
            add_label = AddLabelConfigAddLabel.from_dict(_add_label)

        add_label_config = cls(
            add_label=add_label,
        )

        add_label_config.additional_properties = d
        return add_label_config

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
