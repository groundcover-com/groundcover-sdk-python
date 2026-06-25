from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="DashboardListRequest")


@_attrs_define
class DashboardListRequest:
    """
    Attributes:
        description (str | Unset): Case-insensitive substring filter on dashboard description. Empty = no description
            filter.
        limit (int | Unset): Maximum number of dashboards to return (default 1000).
        name (str | Unset): Case-insensitive substring filter on dashboard name. Empty = no name filter.
        skip (int | Unset): Number of dashboards to skip for pagination.
        sort (str | Unset): Field to sort by: "name" (default) or "description".
    """

    description: str | Unset = UNSET
    limit: int | Unset = UNSET
    name: str | Unset = UNSET
    skip: int | Unset = UNSET
    sort: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        limit = self.limit

        name = self.name

        skip = self.skip

        sort = self.sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if limit is not UNSET:
            field_dict["limit"] = limit
        if name is not UNSET:
            field_dict["name"] = name
        if skip is not UNSET:
            field_dict["skip"] = skip
        if sort is not UNSET:
            field_dict["sort"] = sort

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
        description = d.pop("description", UNSET)

        limit = d.pop("limit", UNSET)

        name = d.pop("name", UNSET)

        skip = d.pop("skip", UNSET)

        sort = d.pop("sort", UNSET)

        dashboard_list_request = cls(
            description=description,
            limit=limit,
            name=name,
            skip=skip,
            sort=sort,
        )

        dashboard_list_request.additional_properties = d
        return dashboard_list_request

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
