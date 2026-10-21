from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ProfilingDiffFlameNode")


@_attrs_define
class ProfilingDiffFlameNode:
    """DiffFlameNode contains inclusive and self weight per side in the selected
    sample unit. A frame present on one side only has zero weight on the other.

        Attributes:
            base_self (float | Unset):
            base_value (float | Unset):
            children (list[ProfilingDiffFlameNode] | Unset):
            name (str | Unset):
            omitted (bool | Unset): Omitted identifies a synthetic bucket, distinct from a real frame named other.
            self_ (float | Unset): Weight sampled directly in this function. In inverted trees, caller
                children partition the same weight and have zero self weight.
            value (float | Unset):
    """

    base_self: float | Unset = UNSET
    base_value: float | Unset = UNSET
    children: list[ProfilingDiffFlameNode] | Unset = UNSET
    name: str | Unset = UNSET
    omitted: bool | Unset = UNSET
    self_: float | Unset = UNSET
    value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_self = self.base_self

        base_value = self.base_value

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        name = self.name

        omitted = self.omitted

        self_ = self.self_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_self is not UNSET:
            field_dict["baseSelf"] = base_self
        if base_value is not UNSET:
            field_dict["baseValue"] = base_value
        if children is not UNSET:
            field_dict["children"] = children
        if name is not UNSET:
            field_dict["name"] = name
        if omitted is not UNSET:
            field_dict["omitted"] = omitted
        if self_ is not UNSET:
            field_dict["self"] = self_
        if value is not UNSET:
            field_dict["value"] = value

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
        base_self = d.pop("baseSelf", UNSET)

        base_value = d.pop("baseValue", UNSET)

        _children = d.pop("children", UNSET)
        children: list[ProfilingDiffFlameNode] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = ProfilingDiffFlameNode.from_dict(children_item_data)

                children.append(children_item)

        name = d.pop("name", UNSET)

        omitted = d.pop("omitted", UNSET)

        self_ = d.pop("self", UNSET)

        value = d.pop("value", UNSET)

        profiling_diff_flame_node = cls(
            base_self=base_self,
            base_value=base_value,
            children=children,
            name=name,
            omitted=omitted,
            self_=self_,
            value=value,
        )

        profiling_diff_flame_node.additional_properties = d
        return profiling_diff_flame_node

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
