from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="IntegrationCountHoldsAnIntegrationNameAndItsCountForSortedOutput")


@_attrs_define
class IntegrationCountHoldsAnIntegrationNameAndItsCountForSortedOutput:
    """
    Attributes:
        count (int | Unset):
        name (str | Unset):
    """

    count: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
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
        count = d.pop("count", UNSET)

        name = d.pop("name", UNSET)

        integration_count_holds_an_integration_name_and_its_count_for_sorted_output = cls(
            count=count,
            name=name,
        )

        integration_count_holds_an_integration_name_and_its_count_for_sorted_output.additional_properties = d
        return integration_count_holds_an_integration_name_and_its_count_for_sorted_output

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
