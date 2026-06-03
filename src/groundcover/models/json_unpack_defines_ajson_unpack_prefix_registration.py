from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="JsonUnpackDefinesAJSONUnpackPrefixRegistration")


@_attrs_define
class JsonUnpackDefinesAJSONUnpackPrefixRegistration:
    """
    Attributes:
        prefix (str | Unset):
        source_column (str | Unset):
    """

    prefix: str | Unset = UNSET
    source_column: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix = self.prefix

        source_column = self.source_column

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if source_column is not UNSET:
            field_dict["sourceColumn"] = source_column

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        prefix = d.pop("prefix", UNSET)

        source_column = d.pop("sourceColumn", UNSET)

        json_unpack_defines_ajson_unpack_prefix_registration = cls(
            prefix=prefix,
            source_column=source_column,
        )

        json_unpack_defines_ajson_unpack_prefix_registration.additional_properties = d
        return json_unpack_defines_ajson_unpack_prefix_registration

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
