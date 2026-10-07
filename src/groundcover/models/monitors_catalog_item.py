from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MonitorsCatalogItem")


@_attrs_define
class MonitorsCatalogItem:
    """
    Attributes:
        catalog_id (str | Unset):
        category (str | Unset):
        condition_description (str | Unset):
        created_at (datetime.datetime | Unset):
        description (str | Unset):
        integration (None | str | Unset): Integration is the technology family, or null for native monitors.
            Same shape as the dashboards catalog so both feed one card component.
        last_updated (datetime.datetime | Unset):
        monitor_type (str | Unset):
        tags (list[str] | Unset):
        title (str | Unset):
        version (int | Unset):
    """

    catalog_id: str | Unset = UNSET
    category: str | Unset = UNSET
    condition_description: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    integration: None | str | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    monitor_type: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_id = self.catalog_id

        category = self.category

        condition_description = self.condition_description

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        integration: None | str | Unset
        if isinstance(self.integration, Unset):
            integration = UNSET
        else:
            integration = self.integration

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        monitor_type = self.monitor_type

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        title = self.title

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog_id is not UNSET:
            field_dict["catalogId"] = catalog_id
        if category is not UNSET:
            field_dict["category"] = category
        if condition_description is not UNSET:
            field_dict["conditionDescription"] = condition_description
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if integration is not UNSET:
            field_dict["integration"] = integration
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if monitor_type is not UNSET:
            field_dict["monitorType"] = monitor_type
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if version is not UNSET:
            field_dict["version"] = version

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
        catalog_id = d.pop("catalogId", UNSET)

        category = d.pop("category", UNSET)

        condition_description = d.pop("conditionDescription", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset) or _created_at is None:
            created_at = UNSET
        else:
            created_at = parse_datetime(_created_at)

        description = d.pop("description", UNSET)

        def _parse_integration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        integration = _parse_integration(d.pop("integration", UNSET))

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset) or _last_updated is None:
            last_updated = UNSET
        else:
            last_updated = parse_datetime(_last_updated)

        monitor_type = d.pop("monitorType", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        title = d.pop("title", UNSET)

        version = d.pop("version", UNSET)

        monitors_catalog_item = cls(
            catalog_id=catalog_id,
            category=category,
            condition_description=condition_description,
            created_at=created_at,
            description=description,
            integration=integration,
            last_updated=last_updated,
            monitor_type=monitor_type,
            tags=tags,
            title=title,
            version=version,
        )

        monitors_catalog_item.additional_properties = d
        return monitors_catalog_item

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
