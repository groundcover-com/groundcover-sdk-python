from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SlackAppDataResponse")


@_attrs_define
class SlackAppDataResponse:
    """
    Attributes:
        connector_id (str | Unset): Comm-hub Slack org connector ID used by dispatch-center. Example:
            550e8400-e29b-41d4-a716-446655440000.
        team_id (str | Unset): Slack workspace team ID. Example: T123456.
        team_name (str | Unset): Slack workspace team name. Example: Engineering.
    """

    connector_id: str | Unset = UNSET
    team_id: str | Unset = UNSET
    team_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_id = self.connector_id

        team_id = self.team_id

        team_name = self.team_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connector_id is not UNSET:
            field_dict["connector_id"] = connector_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if team_name is not UNSET:
            field_dict["team_name"] = team_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        connector_id = d.pop("connector_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        team_name = d.pop("team_name", UNSET)

        slack_app_data_response = cls(
            connector_id=connector_id,
            team_id=team_id,
            team_name=team_name,
        )

        slack_app_data_response.additional_properties = d
        return slack_app_data_response

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
