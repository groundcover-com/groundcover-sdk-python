from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ConnectedAppResponse")


@_attrs_define
class ConnectedAppResponse:
    """
    Attributes:
        created_at (datetime.datetime | Unset): The creation timestamp
        created_by (str | Unset): The email of the user who created the connected app Example: user@example.com.
        data (Any | Unset): The connected app data. Schema depends on type field:
            For type "slack-app": use SlackAppDataResponse schema
        id (str | Unset): The ID of the connected app Example: 1a2b-3c4d.
        name (str | Unset): The name of the connected app Example: my-slack-app.
        type_ (str | Unset): The type of the connected app Example: slack-webhook.
        updated_at (datetime.datetime | Unset): The last update timestamp
        updated_by (str | Unset): The email of the user who last updated the connected app Example: user@example.com.
    """

    created_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    data: Any | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    updated_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        data = self.data

        id = self.id

        name = self.name

        type_ = self.type_

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if data is not UNSET:
            field_dict["data"] = data
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
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

        data = d.pop("data", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset) or _updated_at is None:
            updated_at = UNSET
        else:
            updated_at = parse_datetime(_updated_at)

        updated_by = d.pop("updated_by", UNSET)

        connected_app_response = cls(
            created_at=created_at,
            created_by=created_by,
            data=data,
            id=id,
            name=name,
            type_=type_,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        connected_app_response.additional_properties = d
        return connected_app_response

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
