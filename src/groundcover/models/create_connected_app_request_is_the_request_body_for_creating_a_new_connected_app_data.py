from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppData")


@_attrs_define
class CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppData:
    """The connected app-specific data. Schema depends on the 'type' field:
    For type "slack-webhook": use SlackWebhookData schema
    For type "pagerduty": use PagerDutyData schema
    For type "opsgenie": use OpsGenieData schema
    For type "incidentio": use IncidentIOData schema
    For type "rootly": use RootlyData schema
    For type "webhook": use WebhookData schema ({"url": "https://...", "method": "POST", "headers": {...}, "auth_type":
    "bearer", "api_key": "..."})
    For type "ms-teams": use MSTeamsData schema

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
        create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app_data = cls()

        create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app_data.additional_properties = d
        return create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app_data

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
