from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route_rule_response import RouteRuleResponse


T = TypeVar("T", bound="NotificationRouteListItemResponse")


@_attrs_define
class NotificationRouteListItemResponse:
    """
    Attributes:
        created_at (datetime.datetime | Unset): The creation timestamp
        created_by (str | Unset): The email of the user who created the route Example: user@example.com.
        id (str | Unset): The route ID Example: route-123.
        modified_at (datetime.datetime | Unset): The last modification timestamp
        modified_by (str | Unset): The email of the user who last modified the route Example: user@example.com.
        name (str | Unset): The route name Example: prod-alerts-route.
        query (str | Unset): The gcQL query Example: env:prod.
        routes (list[RouteRuleResponse] | Unset): The route rules with status and connected apps
    """

    created_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    id: str | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    modified_by: str | Unset = UNSET
    name: str | Unset = UNSET
    query: str | Unset = UNSET
    routes: list[RouteRuleResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        id = self.id

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by = self.modified_by

        name = self.name

        query = self.query

        routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()
                routes.append(routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if id is not UNSET:
            field_dict["id"] = id
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if query is not UNSET:
            field_dict["query"] = query
        if routes is not UNSET:
            field_dict["routes"] = routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.route_rule_response import RouteRuleResponse

        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset) or _created_at is None:
            created_at = UNSET
        else:
            created_at = parse_datetime(_created_at)

        created_by = d.pop("createdBy", UNSET)

        id = d.pop("id", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: datetime.datetime | Unset
        if isinstance(_modified_at, Unset) or _modified_at is None:
            modified_at = UNSET
        else:
            modified_at = parse_datetime(_modified_at)

        modified_by = d.pop("modifiedBy", UNSET)

        name = d.pop("name", UNSET)

        query = d.pop("query", UNSET)

        _routes = d.pop("routes", UNSET)
        routes: list[RouteRuleResponse] | Unset = UNSET
        if _routes is not UNSET:
            routes = []
            for routes_item_data in _routes:
                routes_item = RouteRuleResponse.from_dict(routes_item_data)

                routes.append(routes_item)

        notification_route_list_item_response = cls(
            created_at=created_at,
            created_by=created_by,
            id=id,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            query=query,
            routes=routes,
        )

        notification_route_list_item_response.additional_properties = d
        return notification_route_list_item_response

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
