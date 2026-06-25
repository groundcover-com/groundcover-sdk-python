from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.migration_data_source_item import MigrationDataSourceItem


T = TypeVar("T", bound="ListMigrationDataSourcesResponse")


@_attrs_define
class ListMigrationDataSourcesResponse:
    """
    Attributes:
        data_sources (list[MigrationDataSourceItem]): The list of migration data sources.
    """

    data_sources: list[MigrationDataSourceItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_sources = []
        for data_sources_item_data in self.data_sources:
            data_sources_item = data_sources_item_data.to_dict()
            data_sources.append(data_sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataSources": data_sources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_data_source_item import MigrationDataSourceItem

        d = dict(src_dict)
        data_sources = []
        _data_sources = d.pop("dataSources")
        for data_sources_item_data in _data_sources:
            data_sources_item = MigrationDataSourceItem.from_dict(data_sources_item_data)

            data_sources.append(data_sources_item)

        list_migration_data_sources_response = cls(
            data_sources=data_sources,
        )

        list_migration_data_sources_response.additional_properties = d
        return list_migration_data_sources_response

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
