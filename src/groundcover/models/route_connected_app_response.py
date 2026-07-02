from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route_connected_app_response_params import RouteConnectedAppResponseParams


T = TypeVar("T", bound="RouteConnectedAppResponse")


@_attrs_define
class RouteConnectedAppResponse:
    """
    Attributes:
        id (str | Unset): The connected app ID Example: app-123.
        name (str | Unset): The connected app name (resolved) Example: My Slack App.
        params (RouteConnectedAppResponseParams | Unset): Route-specific parameters for this connected app.
            Slack App routes may include params.channels with the selected Slack channels
            as {"id":"C123456","name":"#alerts"} objects; name is an optional display name.
            Linear routes may include team_id, project_id, label_ids, assignee_id,
            delegate_id, resolved_status_id, and auto_resolve.
            Connected app types that do not support route params omit this field. Example: {'channels': [{'id': 'C123456',
            'name': '#alerts'}]}.
        type_ (str | Unset): The type of the connected app. Example: slack-app.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    params: RouteConnectedAppResponseParams | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if params is not UNSET:
            field_dict["params"] = params
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.route_connected_app_response_params import RouteConnectedAppResponseParams

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _params = d.pop("params", UNSET)
        params: RouteConnectedAppResponseParams | Unset
        if isinstance(_params, Unset) or _params is None:
            params = UNSET
        else:
            params = RouteConnectedAppResponseParams.from_dict(_params)

        type_ = d.pop("type", UNSET)

        route_connected_app_response = cls(
            id=id,
            name=name,
            params=params,
            type_=type_,
        )

        route_connected_app_response.additional_properties = d
        return route_connected_app_response

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
