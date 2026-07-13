from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnectorCatalogEntry")


@_attrs_define
class ConnectorCatalogEntry:
    """ConnectorCatalogEntry is a single declarative connector-catalog entry (a
    first-class MCP-backed preset identified by catalog id).

        Attributes:
            auth_mode (str | Unset):
            description (str | Unset):
            display_name (str | Unset):
            icon_domain (str | Unset):
            icon_url (str | Unset):
            id (str | Unset):
            setup_help (str | Unset):
    """

    auth_mode: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    icon_domain: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    id: str | Unset = UNSET
    setup_help: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_mode = self.auth_mode

        description = self.description

        display_name = self.display_name

        icon_domain = self.icon_domain

        icon_url = self.icon_url

        id = self.id

        setup_help = self.setup_help

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_mode is not UNSET:
            field_dict["auth_mode"] = auth_mode
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if icon_domain is not UNSET:
            field_dict["icon_domain"] = icon_domain
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if id is not UNSET:
            field_dict["id"] = id
        if setup_help is not UNSET:
            field_dict["setup_help"] = setup_help

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
        auth_mode = d.pop("auth_mode", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        icon_domain = d.pop("icon_domain", UNSET)

        icon_url = d.pop("icon_url", UNSET)

        id = d.pop("id", UNSET)

        setup_help = d.pop("setup_help", UNSET)

        connector_catalog_entry = cls(
            auth_mode=auth_mode,
            description=description,
            display_name=display_name,
            icon_domain=icon_domain,
            icon_url=icon_url,
            id=id,
            setup_help=setup_help,
        )

        connector_catalog_entry.additional_properties = d
        return connector_catalog_entry

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
