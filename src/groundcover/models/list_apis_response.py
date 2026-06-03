from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_apis_response_item import ListApisResponseItem


T = TypeVar("T", bound="ListApisResponse")


@_attrs_define
class ListApisResponse:
    """
    Attributes:
        apis (list[ListApisResponseItem] | Unset):
        is_limit_reached (bool | Unset):
    """

    apis: list[ListApisResponseItem] | Unset = UNSET
    is_limit_reached: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apis: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.apis, Unset):
            apis = []
            for apis_item_data in self.apis:
                apis_item = apis_item_data.to_dict()
                apis.append(apis_item)

        is_limit_reached = self.is_limit_reached

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apis is not UNSET:
            field_dict["apis"] = apis
        if is_limit_reached is not UNSET:
            field_dict["isLimitReached"] = is_limit_reached

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_apis_response_item import ListApisResponseItem

        d = dict(src_dict)
        _apis = d.pop("apis", UNSET)
        apis: list[ListApisResponseItem] | Unset = UNSET
        if _apis is not UNSET:
            apis = []
            for apis_item_data in _apis:
                apis_item = ListApisResponseItem.from_dict(apis_item_data)

                apis.append(apis_item)

        is_limit_reached = d.pop("isLimitReached", UNSET)

        list_apis_response = cls(
            apis=apis,
            is_limit_reached=is_limit_reached,
        )

        list_apis_response.additional_properties = d
        return list_apis_response

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
