from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fetch_assets_request_asset_types_item import FetchAssetsRequestAssetTypesItem
from ..models.fetch_assets_request_provider import FetchAssetsRequestProvider
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_configuration import ConnectionConfiguration


T = TypeVar("T", bound="FetchAssetsRequest")


@_attrs_define
class FetchAssetsRequest:
    """
    Attributes:
        connection_configuration (ConnectionConfiguration):
        provider (FetchAssetsRequestProvider): The provider to fetch assets from.
        asset_types (list[FetchAssetsRequestAssetTypesItem] | Unset): The types of assets to fetch. If empty, all asset
            types will be fetched.
    """

    connection_configuration: ConnectionConfiguration
    provider: FetchAssetsRequestProvider
    asset_types: list[FetchAssetsRequestAssetTypesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_configuration = self.connection_configuration.to_dict()

        provider = self.provider.value

        asset_types: list[str] | Unset = UNSET
        if not isinstance(self.asset_types, Unset):
            asset_types = []
            for asset_types_item_data in self.asset_types:
                asset_types_item = asset_types_item_data.value
                asset_types.append(asset_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionConfiguration": connection_configuration,
                "provider": provider,
            }
        )
        if asset_types is not UNSET:
            field_dict["assetTypes"] = asset_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_configuration import ConnectionConfiguration

        d = dict(src_dict)
        connection_configuration = ConnectionConfiguration.from_dict(d.pop("connectionConfiguration"))

        provider = FetchAssetsRequestProvider(d.pop("provider"))

        _asset_types = d.pop("assetTypes", UNSET)
        asset_types: list[FetchAssetsRequestAssetTypesItem] | Unset = UNSET
        if _asset_types is not UNSET:
            asset_types = []
            for asset_types_item_data in _asset_types:
                asset_types_item = FetchAssetsRequestAssetTypesItem(asset_types_item_data)

                asset_types.append(asset_types_item)

        fetch_assets_request = cls(
            connection_configuration=connection_configuration,
            provider=provider,
            asset_types=asset_types,
        )

        fetch_assets_request.additional_properties = d
        return fetch_assets_request

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
