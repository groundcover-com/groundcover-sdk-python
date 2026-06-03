from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="Endpoint")


@_attrs_define
class Endpoint:
    """
    Attributes:
        domain (str | Unset):
        is_public (bool | Unset):
        vpc_service_name (str | Unset):
    """

    domain: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    vpc_service_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        is_public = self.is_public

        vpc_service_name = self.vpc_service_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if vpc_service_name is not UNSET:
            field_dict["vpc_service_name"] = vpc_service_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        domain = d.pop("domain", UNSET)

        is_public = d.pop("is_public", UNSET)

        vpc_service_name = d.pop("vpc_service_name", UNSET)

        endpoint = cls(
            domain=domain,
            is_public=is_public,
            vpc_service_name=vpc_service_name,
        )

        endpoint.additional_properties = d
        return endpoint

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
