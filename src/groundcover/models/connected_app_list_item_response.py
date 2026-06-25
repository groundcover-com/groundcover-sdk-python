from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnectedAppListItemResponse")


@_attrs_define
class ConnectedAppListItemResponse:
    """
    Attributes:
        created_at (datetime.datetime | Unset): The creation timestamp
        created_by (str | Unset): The email of the user who created the connected app Example: user@example.com.
        data_hash (str | Unset): SHA-256 hash of the stored connected app data, including secret fields Example:
            20b3664454f5b36a20da19805802a369a9f30793fb646a1de9e39b21a004df4e.
        id (str | Unset): The ID of the connected app Example: 1a2b-3c4d.
        name (str | Unset): The name of the connected app Example: my-slack-app.
        type_ (str | Unset): The type of the connected app Example: slack-webhook.
    """

    created_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    data_hash: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        data_hash = self.data_hash

        id = self.id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if data_hash is not UNSET:
            field_dict["data_hash"] = data_hash
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
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
        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset) or _created_at is None:
            created_at = UNSET
        else:
            created_at = parse_datetime(_created_at)

        created_by = d.pop("created_by", UNSET)

        data_hash = d.pop("data_hash", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        connected_app_list_item_response = cls(
            created_at=created_at,
            created_by=created_by,
            data_hash=data_hash,
            id=id,
            name=name,
            type_=type_,
        )

        connected_app_list_item_response.additional_properties = d
        return connected_app_list_item_response

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
