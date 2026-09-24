from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit")


@_attrs_define
class FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit:
    """
    Attributes:
        children (list[FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit] | Unset):
        name (str | Unset):
        omitted (bool | Unset): Omitted identifies a synthetic bucket, distinct from a real frame named other.
        self_ (float | Unset):
        value (float | Unset):
    """

    children: list[FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit] | Unset = UNSET
    name: str | Unset = UNSET
    omitted: bool | Unset = UNSET
    self_: float | Unset = UNSET
    value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        _children = d.pop("children", UNSET)
        children: list[FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit.from_dict(
                    children_item_data
                )

                children.append(children_item)

        name = d.pop("name", UNSET)

        omitted = d.pop("omitted", UNSET)

        self_ = d.pop("self", UNSET)

        value = d.pop("value", UNSET)

        flame_node_contains_inclusive_and_self_weight_in_the_selected_sample_unit = cls(
            children=children,
            name=name,
            omitted=omitted,
            self_=self_,
            value=value,
        )

        flame_node_contains_inclusive_and_self_weight_in_the_selected_sample_unit.additional_properties = d
        return flame_node_contains_inclusive_and_self_weight_in_the_selected_sample_unit

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
