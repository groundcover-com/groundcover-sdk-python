from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AssetMetadata")


@_attrs_define
class AssetMetadata:
    """
    Attributes:
        creator_email (str | Unset): Monitor-specific: the email of the creator.
        creator_name (str | Unset): The name of the creator (monitors) or author (dashboards).
        last_modified (datetime.datetime | Unset): The timestamp when the asset was last modified.
            Format: date-time
        popularity (float | Unset): Dashboard-specific: popularity metric.
        status (str | Unset): Monitor-specific: the overall state of the monitor.
        tags (list[str] | Unset): Tags associated with the asset.
        type_ (str | Unset): Monitor-specific: the beautified type of the monitor.
    """

    creator_email: str | Unset = UNSET
    creator_name: str | Unset = UNSET
    last_modified: datetime.datetime | Unset = UNSET
    popularity: float | Unset = UNSET
    status: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator_email = self.creator_email

        creator_name = self.creator_name

        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        popularity = self.popularity

        status = self.status

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator_email is not UNSET:
            field_dict["creatorEmail"] = creator_email
        if creator_name is not UNSET:
            field_dict["creatorName"] = creator_name
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if popularity is not UNSET:
            field_dict["popularity"] = popularity
        if status is not UNSET:
            field_dict["status"] = status
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_

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
        creator_email = d.pop("creatorEmail", UNSET)

        creator_name = d.pop("creatorName", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: datetime.datetime | Unset
        if isinstance(_last_modified, Unset) or _last_modified is None:
            last_modified = UNSET
        else:
            last_modified = parse_datetime(_last_modified)

        popularity = d.pop("popularity", UNSET)

        status = d.pop("status", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        type_ = d.pop("type", UNSET)

        asset_metadata = cls(
            creator_email=creator_email,
            creator_name=creator_name,
            last_modified=last_modified,
            popularity=popularity,
            status=status,
            tags=tags,
            type_=type_,
        )

        asset_metadata.additional_properties = d
        return asset_metadata

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
