from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relabel_config_add_label import RelabelConfigAddLabel


T = TypeVar("T", bound="RelabelConfig")


@_attrs_define
class RelabelConfig:
    """
    Attributes:
        add_label (RelabelConfigAddLabel | Unset):
        drop_regex (list[str] | Unset):
        keep_regex (list[str] | Unset):
        raw (str | Unset):
        remove_label (list[str] | Unset):
    """

    add_label: RelabelConfigAddLabel | Unset = UNSET
    drop_regex: list[str] | Unset = UNSET
    keep_regex: list[str] | Unset = UNSET
    raw: str | Unset = UNSET
    remove_label: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_label, Unset):
            add_label = self.add_label.to_dict()

        drop_regex: list[str] | Unset = UNSET
        if not isinstance(self.drop_regex, Unset):
            drop_regex = self.drop_regex

        keep_regex: list[str] | Unset = UNSET
        if not isinstance(self.keep_regex, Unset):
            keep_regex = self.keep_regex

        raw = self.raw

        remove_label: list[str] | Unset = UNSET
        if not isinstance(self.remove_label, Unset):
            remove_label = self.remove_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_label is not UNSET:
            field_dict["addLabel"] = add_label
        if drop_regex is not UNSET:
            field_dict["dropRegex"] = drop_regex
        if keep_regex is not UNSET:
            field_dict["keepRegex"] = keep_regex
        if raw is not UNSET:
            field_dict["raw"] = raw
        if remove_label is not UNSET:
            field_dict["removeLabel"] = remove_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relabel_config_add_label import RelabelConfigAddLabel

        d = dict(src_dict)
        _add_label = d.pop("addLabel", UNSET)
        add_label: RelabelConfigAddLabel | Unset
        if isinstance(_add_label, Unset) or _add_label is None:
            add_label = UNSET
        else:
            add_label = RelabelConfigAddLabel.from_dict(_add_label)

        drop_regex = cast(list[str], d.pop("dropRegex", UNSET))

        keep_regex = cast(list[str], d.pop("keepRegex", UNSET))

        raw = d.pop("raw", UNSET)

        remove_label = cast(list[str], d.pop("removeLabel", UNSET))

        relabel_config = cls(
            add_label=add_label,
            drop_regex=drop_regex,
            keep_regex=keep_regex,
            raw=raw,
            remove_label=remove_label,
        )

        relabel_config.additional_properties = d
        return relabel_config

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
