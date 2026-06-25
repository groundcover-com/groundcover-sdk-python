from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.migration_cloud_integration_item import MigrationCloudIntegrationItem


T = TypeVar("T", bound="ListMigrationCloudIntegrationsResponse")


@_attrs_define
class ListMigrationCloudIntegrationsResponse:
    """
    Attributes:
        cloud_integrations (list[MigrationCloudIntegrationItem]): The list of cloud integrations.
    """

    cloud_integrations: list[MigrationCloudIntegrationItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_integrations = []
        for cloud_integrations_item_data in self.cloud_integrations:
            cloud_integrations_item = cloud_integrations_item_data.to_dict()
            cloud_integrations.append(cloud_integrations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloudIntegrations": cloud_integrations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_cloud_integration_item import MigrationCloudIntegrationItem

        d = dict(src_dict)
        cloud_integrations = []
        _cloud_integrations = d.pop("cloudIntegrations")
        for cloud_integrations_item_data in _cloud_integrations:
            cloud_integrations_item = MigrationCloudIntegrationItem.from_dict(cloud_integrations_item_data)

            cloud_integrations.append(cloud_integrations_item)

        list_migration_cloud_integrations_response = cls(
            cloud_integrations=cloud_integrations,
        )

        list_migration_cloud_integrations_response.additional_properties = d
        return list_migration_cloud_integrations_response

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
