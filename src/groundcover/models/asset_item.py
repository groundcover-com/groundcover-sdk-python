from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_item_raw_payload import AssetItemRawPayload


T = TypeVar("T", bound="AssetItem")


@_attrs_define
class AssetItem:
    """
    Attributes:
        name (str): The name of the asset.
        raw_hash (str): Hash of the raw payload.
        raw_payload (AssetItemRawPayload): The verbatim provider object.
        source_created_at (datetime.datetime): The timestamp when the asset was created in the source provider.
        source_resource_id (str): The provider's asset identifier.
        popularity (float | Unset): Usage metric from provider.
    """

    name: str
    raw_hash: str
    raw_payload: AssetItemRawPayload
    source_created_at: datetime.datetime
    source_resource_id: str
    popularity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        raw_hash = self.raw_hash

        raw_payload = self.raw_payload.to_dict()

        source_created_at = self.source_created_at.isoformat()

        source_resource_id = self.source_resource_id

        popularity = self.popularity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "rawHash": raw_hash,
                "rawPayload": raw_payload,
                "sourceCreatedAt": source_created_at,
                "sourceResourceId": source_resource_id,
            }
        )
        if popularity is not UNSET:
            field_dict["popularity"] = popularity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_item_raw_payload import AssetItemRawPayload

        d = dict(src_dict)
        name = d.pop("name")

        raw_hash = d.pop("rawHash")

        raw_payload = AssetItemRawPayload.from_dict(d.pop("rawPayload"))

        source_created_at = parse_datetime(d.pop("sourceCreatedAt"))

        source_resource_id = d.pop("sourceResourceId")

        popularity = d.pop("popularity", UNSET)

        asset_item = cls(
            name=name,
            raw_hash=raw_hash,
            raw_payload=raw_payload,
            source_created_at=source_created_at,
            source_resource_id=source_resource_id,
            popularity=popularity,
        )

        asset_item.additional_properties = d
        return asset_item

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
