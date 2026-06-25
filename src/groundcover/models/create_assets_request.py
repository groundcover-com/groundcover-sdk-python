from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_assets_request_source_method import CreateAssetsRequestSourceMethod
from ..models.create_assets_request_source_provider import CreateAssetsRequestSourceProvider

if TYPE_CHECKING:
    from ..models.asset_item import AssetItem


T = TypeVar("T", bound="CreateAssetsRequest")


@_attrs_define
class CreateAssetsRequest:
    """
    Attributes:
        assets (list[AssetItem]): The list of assets to create.
        discovered_at (datetime.datetime): The discovery timestamp.
        discovery_id (str): The discovery identifier for this batch.
        source_method (CreateAssetsRequestSourceMethod): The method of asset acquisition from the source.
        source_provider (CreateAssetsRequestSourceProvider): The source provider.
    """

    assets: list[AssetItem]
    discovered_at: datetime.datetime
    discovery_id: str
    source_method: CreateAssetsRequestSourceMethod
    source_provider: CreateAssetsRequestSourceProvider
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        discovered_at = self.discovered_at.isoformat()

        discovery_id = self.discovery_id

        source_method = self.source_method.value

        source_provider = self.source_provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assets": assets,
                "discoveredAt": discovered_at,
                "discoveryId": discovery_id,
                "sourceMethod": source_method,
                "sourceProvider": source_provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_item import AssetItem

        d = dict(src_dict)
        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = AssetItem.from_dict(assets_item_data)

            assets.append(assets_item)

        discovered_at = parse_datetime(d.pop("discoveredAt"))

        discovery_id = d.pop("discoveryId")

        source_method = CreateAssetsRequestSourceMethod(d.pop("sourceMethod"))

        source_provider = CreateAssetsRequestSourceProvider(d.pop("sourceProvider"))

        create_assets_request = cls(
            assets=assets,
            discovered_at=discovered_at,
            discovery_id=discovery_id,
            source_method=source_method,
            source_provider=source_provider,
        )

        create_assets_request.additional_properties = d
        return create_assets_request

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
