from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MemberViewsRequest")


@_attrs_define
class MemberViewsRequest:
    """
    Attributes:
        favorites_only (bool | Unset):
        filter_ (str | Unset):
        self_owned_only (bool | Unset):
        type_ (str | Unset):
    """

    favorites_only: bool | Unset = UNSET
    filter_: str | Unset = UNSET
    self_owned_only: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        favorites_only = self.favorites_only

        filter_ = self.filter_

        self_owned_only = self.self_owned_only

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if favorites_only is not UNSET:
            field_dict["favoritesOnly"] = favorites_only
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if self_owned_only is not UNSET:
            field_dict["selfOwnedOnly"] = self_owned_only
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
        favorites_only = d.pop("favoritesOnly", UNSET)

        filter_ = d.pop("filter", UNSET)

        self_owned_only = d.pop("selfOwnedOnly", UNSET)

        type_ = d.pop("type", UNSET)

        member_views_request = cls(
            favorites_only=favorites_only,
            filter_=filter_,
            self_owned_only=self_owned_only,
            type_=type_,
        )

        member_views_request.additional_properties = d
        return member_views_request

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
