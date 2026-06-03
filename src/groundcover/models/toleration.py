from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="Toleration")


@_attrs_define
class Toleration:
    """The pod this Toleration is attached to tolerates any taint that matches
    the triple <key,value,effect> using the matching operator <operator>.

        Attributes:
            effect (str | Unset): +enum
            key (str | Unset): Key is the taint key that the toleration applies to. Empty means match all taint keys.
                If the key is empty, operator must be Exists; this combination means to match all values and all keys.
                +optional
            operator (str | Unset): +enum
            toleration_seconds (int | Unset): TolerationSeconds represents the period of time the toleration (which must be
                of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default,
                it is not set, which means tolerate the taint forever (do not evict). Zero and
                negative values will be treated as 0 (evict immediately) by the system.
                +optional
            value (str | Unset): Value is the taint value the toleration matches to.
                If the operator is Exists, the value should be empty, otherwise just a regular string.
                +optional
    """

    effect: str | Unset = UNSET
    key: str | Unset = UNSET
    operator: str | Unset = UNSET
    toleration_seconds: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effect = self.effect

        key = self.key

        operator = self.operator

        toleration_seconds = self.toleration_seconds

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if effect is not UNSET:
            field_dict["effect"] = effect
        if key is not UNSET:
            field_dict["key"] = key
        if operator is not UNSET:
            field_dict["operator"] = operator
        if toleration_seconds is not UNSET:
            field_dict["tolerationSeconds"] = toleration_seconds
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        effect = d.pop("effect", UNSET)

        key = d.pop("key", UNSET)

        operator = d.pop("operator", UNSET)

        toleration_seconds = d.pop("tolerationSeconds", UNSET)

        value = d.pop("value", UNSET)

        toleration = cls(
            effect=effect,
            key=key,
            operator=operator,
            toleration_seconds=toleration_seconds,
            value=value,
        )

        toleration.additional_properties = d
        return toleration

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
