from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CatalogInstallRequestIsTheOptionalBodyForACatalogInstall")


@_attrs_define
class CatalogInstallRequestIsTheOptionalBodyForACatalogInstall:
    """
    Attributes:
        name (str | Unset): Optional distinct name for an additional named instance; when omitted the
            catalog entry's display name is used.
    """

    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        name = d.pop("name", UNSET)

        catalog_install_request_is_the_optional_body_for_a_catalog_install = cls(
            name=name,
        )

        catalog_install_request_is_the_optional_body_for_a_catalog_install.additional_properties = d
        return catalog_install_request_is_the_optional_body_for_a_catalog_install

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
