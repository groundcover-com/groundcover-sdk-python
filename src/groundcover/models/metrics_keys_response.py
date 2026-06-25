from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MetricsKeysResponse")


@_attrs_define
class MetricsKeysResponse:
    """
    Attributes:
        is_limit_reached (bool | Unset): IsLimitReached indicates whether the query limit was reached.
        keys (list[str] | Unset): Keys is the list of metric keys.
        name (str | Unset): Name is the metric name.
    """

    is_limit_reached: bool | Unset = UNSET
    keys: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_limit_reached = self.is_limit_reached

        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_limit_reached is not UNSET:
            field_dict["isLimitReached"] = is_limit_reached
        if keys is not UNSET:
            field_dict["keys"] = keys
        if name is not UNSET:
            field_dict["name"] = name

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
        is_limit_reached = d.pop("isLimitReached", UNSET)

        keys = cast(list[str], d.pop("keys", UNSET))

        name = d.pop("name", UNSET)

        metrics_keys_response = cls(
            is_limit_reached=is_limit_reached,
            keys=keys,
            name=name,
        )

        metrics_keys_response.additional_properties = d
        return metrics_keys_response

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
