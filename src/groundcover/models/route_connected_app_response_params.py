from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RouteConnectedAppResponseParams")


@_attrs_define
class RouteConnectedAppResponseParams:
    """Route-specific parameters for this connected app.
    Slack App routes may include params.channels with the selected Slack channels
    as {"id":"C123456","name":"#alerts"} objects; name is an optional display name.
    Linear routes may include team_id, project_id, label_ids, assignee_id,
    resolved_status_id, and auto_resolve.
    Connected app types that do not support route params omit this field.

        Example:
            {'channels': [{'id': 'C123456', 'name': '#alerts'}]}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

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
        route_connected_app_response_params = cls()

        route_connected_app_response_params.additional_properties = d
        return route_connected_app_response_params

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
