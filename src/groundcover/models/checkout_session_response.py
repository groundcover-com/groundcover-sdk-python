from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CheckoutSessionResponse")


@_attrs_define
class CheckoutSessionResponse:
    """
    Attributes:
        checkout_session_id (str | Unset):
        url (str | Unset):
    """

    checkout_session_id: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checkout_session_id = self.checkout_session_id

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checkout_session_id is not UNSET:
            field_dict["checkoutSessionId"] = checkout_session_id
        if url is not UNSET:
            field_dict["url"] = url

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
        checkout_session_id = d.pop("checkoutSessionId", UNSET)

        url = d.pop("url", UNSET)

        checkout_session_response = cls(
            checkout_session_id=checkout_session_id,
            url=url,
        )

        checkout_session_response.additional_properties = d
        return checkout_session_response

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
