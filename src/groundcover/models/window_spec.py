from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selector import Selector


T = TypeVar("T", bound="WindowSpec")


@_attrs_define
class WindowSpec:
    """WindowSpec specifies window function parameters for OVER clause

    Attributes:
        partition_by (list[Selector] | Unset):
    """

    partition_by: list[Selector] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partition_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.partition_by, Unset):
            partition_by = []
            for partition_by_item_data in self.partition_by:
                partition_by_item = partition_by_item_data.to_dict()
                partition_by.append(partition_by_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partition_by is not UNSET:
            field_dict["partitionBy"] = partition_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.selector import Selector

        d = dict(src_dict)
        _partition_by = d.pop("partitionBy", UNSET)
        partition_by: list[Selector] | Unset = UNSET
        if _partition_by is not UNSET:
            partition_by = []
            for partition_by_item_data in _partition_by:
                partition_by_item = Selector.from_dict(partition_by_item_data)

                partition_by.append(partition_by_item)

        window_spec = cls(
            partition_by=partition_by,
        )

        window_spec.additional_properties = d
        return window_spec

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
