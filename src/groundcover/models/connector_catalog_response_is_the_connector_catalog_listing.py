from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_catalog_entry import ConnectorCatalogEntry


T = TypeVar("T", bound="ConnectorCatalogResponseIsTheConnectorCatalogListing")


@_attrs_define
class ConnectorCatalogResponseIsTheConnectorCatalogListing:
    """
    Attributes:
        entries (list[ConnectorCatalogEntry] | Unset):
    """

    entries: list[ConnectorCatalogEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_catalog_entry import ConnectorCatalogEntry

        d = dict(src_dict)
        _entries = d.pop("entries", UNSET)
        entries: list[ConnectorCatalogEntry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = ConnectorCatalogEntry.from_dict(entries_item_data)

                entries.append(entries_item)

        connector_catalog_response_is_the_connector_catalog_listing = cls(
            entries=entries,
        )

        connector_catalog_response_is_the_connector_catalog_listing.additional_properties = d
        return connector_catalog_response_is_the_connector_catalog_listing

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
