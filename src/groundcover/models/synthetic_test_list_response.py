from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.synthetic_test_list_item import SyntheticTestListItem


T = TypeVar("T", bound="SyntheticTestListResponse")


@_attrs_define
class SyntheticTestListResponse:
    """
    Attributes:
        synthetics (list[SyntheticTestListItem] | Unset):
    """

    synthetics: list[SyntheticTestListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synthetics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.synthetics, Unset):
            synthetics = []
            for synthetics_item_data in self.synthetics:
                synthetics_item = synthetics_item_data.to_dict()
                synthetics.append(synthetics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if synthetics is not UNSET:
            field_dict["synthetics"] = synthetics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.synthetic_test_list_item import SyntheticTestListItem

        d = dict(src_dict)
        _synthetics = d.pop("synthetics", UNSET)
        synthetics: list[SyntheticTestListItem] | Unset = UNSET
        if _synthetics is not UNSET:
            synthetics = []
            for synthetics_item_data in _synthetics:
                synthetics_item = SyntheticTestListItem.from_dict(synthetics_item_data)

                synthetics.append(synthetics_item)

        synthetic_test_list_response = cls(
            synthetics=synthetics,
        )

        synthetic_test_list_response.additional_properties = d
        return synthetic_test_list_response

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
