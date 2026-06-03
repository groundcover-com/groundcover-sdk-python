from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CreateAssetsResponse")


@_attrs_define
class CreateAssetsResponse:
    """
    Attributes:
        created_asset_count (int | Unset): The number of assets created.
        discovered_at (datetime.datetime | Unset): The discovery timestamp.
            Format: date-time
        discovery_id (str | Unset): The discovery identifier.
    """

    created_asset_count: int | Unset = UNSET
    discovered_at: datetime.datetime | Unset = UNSET
    discovery_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_asset_count = self.created_asset_count

        discovered_at: str | Unset = UNSET
        if not isinstance(self.discovered_at, Unset):
            discovered_at = self.discovered_at.isoformat()

        discovery_id = self.discovery_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_asset_count is not UNSET:
            field_dict["createdAssetCount"] = created_asset_count
        if discovered_at is not UNSET:
            field_dict["discoveredAt"] = discovered_at
        if discovery_id is not UNSET:
            field_dict["discoveryId"] = discovery_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        created_asset_count = d.pop("createdAssetCount", UNSET)

        _discovered_at = d.pop("discoveredAt", UNSET)
        discovered_at: datetime.datetime | Unset
        if isinstance(_discovered_at, Unset) or _discovered_at is None:
            discovered_at = UNSET
        else:
            discovered_at = parse_datetime(_discovered_at)

        discovery_id = d.pop("discoveryId", UNSET)

        create_assets_response = cls(
            created_asset_count=created_asset_count,
            discovered_at=discovered_at,
            discovery_id=discovery_id,
        )

        create_assets_response.additional_properties = d
        return create_assets_response

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
