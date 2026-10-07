from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_data_source_status import AssetDataSourceStatus
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AssetDataSource")


@_attrs_define
class AssetDataSource:
    """
    Attributes:
        connected_at (datetime.datetime | Unset): When the user connected the data source. Absent until then.
            Format: date-time
        id (str | Unset): The data source ID, as listed by the data sources endpoint.
        integration_type (str | Unset): The integration that provides the data.
        name (str | Unset): The data source name.
        status (AssetDataSourceStatus | Unset): Whether live data was observed: todo (none), partial or active.
    """

    connected_at: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    integration_type: str | Unset = UNSET
    name: str | Unset = UNSET
    status: AssetDataSourceStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_at: str | Unset = UNSET
        if not isinstance(self.connected_at, Unset):
            connected_at = self.connected_at.isoformat()

        id = self.id

        integration_type = self.integration_type

        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_at is not UNSET:
            field_dict["connected_at"] = connected_at
        if id is not UNSET:
            field_dict["id"] = id
        if integration_type is not UNSET:
            field_dict["integration_type"] = integration_type
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

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
        _connected_at = d.pop("connected_at", UNSET)
        connected_at: datetime.datetime | Unset
        if isinstance(_connected_at, Unset) or _connected_at is None:
            connected_at = UNSET
        else:
            connected_at = parse_datetime(_connected_at)

        id = d.pop("id", UNSET)

        integration_type = d.pop("integration_type", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: AssetDataSourceStatus | Unset
        if isinstance(_status, Unset) or _status is None:
            status = UNSET
        else:
            status = AssetDataSourceStatus(_status)

        asset_data_source = cls(
            connected_at=connected_at,
            id=id,
            integration_type=integration_type,
            name=name,
            status=status,
        )

        asset_data_source.additional_properties = d
        return asset_data_source

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
