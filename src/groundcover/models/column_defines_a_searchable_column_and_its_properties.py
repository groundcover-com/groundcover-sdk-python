from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ColumnDefinesASearchableColumnAndItsProperties")


@_attrs_define
class ColumnDefinesASearchableColumnAndItsProperties:
    """
    Attributes:
        additional_filter (str | Unset):
        auto_complete (bool | Unset):
        filter_keys (list[str] | Unset):
        is_nullable (bool | Unset):
        key (str | Unset):
        origin (str | Unset):
        type_ (str | Unset):
    """

    additional_filter: str | Unset = UNSET
    auto_complete: bool | Unset = UNSET
    filter_keys: list[str] | Unset = UNSET
    is_nullable: bool | Unset = UNSET
    key: str | Unset = UNSET
    origin: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_filter = self.additional_filter

        auto_complete = self.auto_complete

        filter_keys: list[str] | Unset = UNSET
        if not isinstance(self.filter_keys, Unset):
            filter_keys = self.filter_keys

        is_nullable = self.is_nullable

        key = self.key

        origin = self.origin

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_filter is not UNSET:
            field_dict["additionalFilter"] = additional_filter
        if auto_complete is not UNSET:
            field_dict["autoComplete"] = auto_complete
        if filter_keys is not UNSET:
            field_dict["filterKeys"] = filter_keys
        if is_nullable is not UNSET:
            field_dict["isNullable"] = is_nullable
        if key is not UNSET:
            field_dict["key"] = key
        if origin is not UNSET:
            field_dict["origin"] = origin
        if type_ is not UNSET:
            field_dict["type"] = type_

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
        additional_filter = d.pop("additionalFilter", UNSET)

        auto_complete = d.pop("autoComplete", UNSET)

        filter_keys = cast(list[str], d.pop("filterKeys", UNSET))

        is_nullable = d.pop("isNullable", UNSET)

        key = d.pop("key", UNSET)

        origin = d.pop("origin", UNSET)

        type_ = d.pop("type", UNSET)

        column_defines_a_searchable_column_and_its_properties = cls(
            additional_filter=additional_filter,
            auto_complete=auto_complete,
            filter_keys=filter_keys,
            is_nullable=is_nullable,
            key=key,
            origin=origin,
            type_=type_,
        )

        column_defines_a_searchable_column_and_its_properties.additional_properties = d
        return column_defines_a_searchable_column_and_its_properties

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
