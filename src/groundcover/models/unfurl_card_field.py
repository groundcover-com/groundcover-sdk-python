from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="UnfurlCardField")


@_attrs_define
class UnfurlCardField:
    """UnfurlCardField is one labeled value on an unfurl card. Value is typed per
    ValueType ("string" or "integer") so a provider-side renderer (Slack Work
    Object today) can pick the right field type without inspecting the Go
    value's kind. Link is omitted when the field carries no follow-up URL.

        Attributes:
            key (str | Unset):
            label (str | Unset):
            link (str | Unset):
            value (Any | Unset):
            value_type (str | Unset):
    """

    key: str | Unset = UNSET
    label: str | Unset = UNSET
    link: str | Unset = UNSET
    value: Any | Unset = UNSET
    value_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        link = self.link

        value = self.value

        value_type = self.value_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if link is not UNSET:
            field_dict["link"] = link
        if value is not UNSET:
            field_dict["value"] = value
        if value_type is not UNSET:
            field_dict["valueType"] = value_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        label = d.pop("label", UNSET)

        link = d.pop("link", UNSET)

        value = d.pop("value", UNSET)

        value_type = d.pop("valueType", UNSET)

        unfurl_card_field = cls(
            key=key,
            label=label,
            link=link,
            value=value,
            value_type=value_type,
        )

        unfurl_card_field.additional_properties = d
        return unfurl_card_field

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
