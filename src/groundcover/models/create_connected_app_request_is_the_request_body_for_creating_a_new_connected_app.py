from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app_type import (
    CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppType,
)

if TYPE_CHECKING:
    from ..models.create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app_data import (
        CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppData,
    )


T = TypeVar("T", bound="CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp")


@_attrs_define
class CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedApp:
    """
    Attributes:
        data (CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppData): The connected app-specific
            data. Schema depends on the 'type' field:
            For type "slack-webhook": use SlackWebhookData schema
            For type "pagerduty": use PagerDutyData schema
            For type "opsgenie": use OpsGenieData schema
            For type "incidentio": use IncidentIOData schema
            For type "rootly": use RootlyData schema
            For type "webhook": use WebhookData schema ({"url": "https://...", "method": "POST", "headers": {...},
            "auth_type": "bearer", "api_key": "..."})
            For type "ms-teams": use MSTeamsData schema
        name (str): The name of the connected app Example: my-slack-app.
        type_ (CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppType): The type of the connected app
            Example: slack-webhook.
    """

    data: CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppData
    name: str
    type_: CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        name = self.name

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app_data import (
            CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppData,
        )

        d = dict(src_dict)
        data = CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppData.from_dict(d.pop("data"))

        name = d.pop("name")

        type_ = CreateConnectedAppRequestIsTheRequestBodyForCreatingANewConnectedAppType(d.pop("type"))

        create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app = cls(
            data=data,
            name=name,
            type_=type_,
        )

        create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app.additional_properties = d
        return create_connected_app_request_is_the_request_body_for_creating_a_new_connected_app

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
