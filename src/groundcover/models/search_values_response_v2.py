from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.value_item import ValueItem


T = TypeVar("T", bound="SearchValuesResponseV2")


@_attrs_define
class SearchValuesResponseV2:
    """
    Attributes:
        done (bool | Unset):
        error (str | Unset):
        is_limit_reached (bool | Unset):
        key (str | Unset):
        values (list[ValueItem] | Unset):
    """

    done: bool | Unset = UNSET
    error: str | Unset = UNSET
    is_limit_reached: bool | Unset = UNSET
    key: str | Unset = UNSET
    values: list[ValueItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        error = self.error

        is_limit_reached = self.is_limit_reached

        key = self.key

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if done is not UNSET:
            field_dict["done"] = done
        if error is not UNSET:
            field_dict["error"] = error
        if is_limit_reached is not UNSET:
            field_dict["isLimitReached"] = is_limit_reached
        if key is not UNSET:
            field_dict["key"] = key
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.value_item import ValueItem

        d = dict(src_dict)
        done = d.pop("done", UNSET)

        error = d.pop("error", UNSET)

        is_limit_reached = d.pop("isLimitReached", UNSET)

        key = d.pop("key", UNSET)

        _values = d.pop("values", UNSET)
        values: list[ValueItem] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = ValueItem.from_dict(values_item_data)

                values.append(values_item)

        search_values_response_v2 = cls(
            done=done,
            error=error,
            is_limit_reached=is_limit_reached,
            key=key,
            values=values,
        )

        search_values_response_v2.additional_properties = d
        return search_values_response_v2

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
