from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_fetch_result import AssetFetchResult


T = TypeVar("T", bound="FetchAssetsResponse")


@_attrs_define
class FetchAssetsResponse:
    """
    Attributes:
        assets (list[AssetFetchResult] | Unset): Results for each asset type fetched.
    """

    assets: list[AssetFetchResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_fetch_result import AssetFetchResult

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: list[AssetFetchResult] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = AssetFetchResult.from_dict(assets_item_data)

                assets.append(assets_item)

        fetch_assets_response = cls(
            assets=assets,
        )

        fetch_assets_response.additional_properties = d
        return fetch_assets_response

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
