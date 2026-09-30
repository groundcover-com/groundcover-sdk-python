from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetExclusion")


@_attrs_define
class AssetExclusion:
    """
    Attributes:
        asset_type (str): The type of the excluded asset.
        excluded_at (datetime.datetime): When the asset was excluded.
        excluded_by (str): Email of the user who excluded the asset.
        source_resource_id (str): The provider's asset identifier.
    """

    asset_type: str
    excluded_at: datetime.datetime
    excluded_by: str
    source_resource_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_type = self.asset_type

        excluded_at = self.excluded_at.isoformat()

        excluded_by = self.excluded_by

        source_resource_id = self.source_resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_type": asset_type,
                "excluded_at": excluded_at,
                "excluded_by": excluded_by,
                "source_resource_id": source_resource_id,
            }
        )

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
        asset_type = d.pop("asset_type")

        excluded_at = parse_datetime(d.pop("excluded_at"))

        excluded_by = d.pop("excluded_by")

        source_resource_id = d.pop("source_resource_id")

        asset_exclusion = cls(
            asset_type=asset_type,
            excluded_at=excluded_at,
            excluded_by=excluded_by,
            source_resource_id=source_resource_id,
        )

        asset_exclusion.additional_properties = d
        return asset_exclusion

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
