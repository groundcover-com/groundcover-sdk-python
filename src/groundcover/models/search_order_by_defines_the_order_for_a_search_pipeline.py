from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selector import Selector


T = TypeVar("T", bound="SearchOrderByDefinesTheOrderForASearchPipeline")


@_attrs_define
class SearchOrderByDefinesTheOrderForASearchPipeline:
    """
    Attributes:
        direction (str | Unset):
        selector (Selector | Unset):
    """

    direction: str | Unset = UNSET
    selector: Selector | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction = self.direction

        selector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direction is not UNSET:
            field_dict["direction"] = direction
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.selector import Selector

        d = dict(src_dict)
        direction = d.pop("direction", UNSET)

        _selector = d.pop("selector", UNSET)
        selector: Selector | Unset
        if isinstance(_selector, Unset) or _selector is None:
            selector = UNSET
        else:
            selector = Selector.from_dict(_selector)

        search_order_by_defines_the_order_for_a_search_pipeline = cls(
            direction=direction,
            selector=selector,
        )

        search_order_by_defines_the_order_for_a_search_pipeline.additional_properties = d
        return search_order_by_defines_the_order_for_a_search_pipeline

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
