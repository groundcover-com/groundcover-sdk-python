from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_monitor_connected_app_channel_identifies_a_slack_channel_for_slack_app_delivery import (
        TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery,
    )


T = TypeVar("T", bound="TestMonitorConnectedAppDeliveryOptions")


@_attrs_define
class TestMonitorConnectedAppDeliveryOptions:
    """TestMonitorConnectedAppDeliveryOptions carries per-app delivery options for a direct
    connected-app test notification. Fields are app-type specific; unrelated fields are ignored.

        Attributes:
            assignee_id (str | Unset): AssigneeID optionally assigns created/updated Linear issues to a user.
            auto_resolve (bool | Unset): AutoResolve controls whether resolved monitor issues transition Linear issues.
            channels (list[TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery] | Unset): Channels
                lists the Slack channels to post to (slack-app connected apps).
                Multiple channels result in one test notification per channel.
            label_ids (list[str] | Unset): LabelIDs optionally assigns Linear labels to created/updated issues.
            project_id (str | Unset): ProjectID optionally assigns created/updated Linear issues to a project.
            resolved_status_id (str | Unset): ResolvedStatusID optionally selects the Linear status used for auto-resolve.
            team_id (str | Unset): TeamID selects the Linear team that receives created issues.
    """

    assignee_id: str | Unset = UNSET
    auto_resolve: bool | Unset = UNSET
    channels: list[TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery] | Unset = UNSET
    label_ids: list[str] | Unset = UNSET
    project_id: str | Unset = UNSET
    resolved_status_id: str | Unset = UNSET
    team_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignee_id = self.assignee_id

        auto_resolve = self.auto_resolve

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        label_ids: list[str] | Unset = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids

        project_id = self.project_id

        resolved_status_id = self.resolved_status_id

        team_id = self.team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if auto_resolve is not UNSET:
            field_dict["auto_resolve"] = auto_resolve
        if channels is not UNSET:
            field_dict["channels"] = channels
        if label_ids is not UNSET:
            field_dict["label_ids"] = label_ids
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if resolved_status_id is not UNSET:
            field_dict["resolved_status_id"] = resolved_status_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_monitor_connected_app_channel_identifies_a_slack_channel_for_slack_app_delivery import (
            TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery,
        )

        d = dict(src_dict)
        assignee_id = d.pop("assignee_id", UNSET)

        auto_resolve = d.pop("auto_resolve", UNSET)

        _channels = d.pop("channels", UNSET)
        channels: list[TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = TestMonitorConnectedAppChannelIdentifiesASlackChannelForSlackAppDelivery.from_dict(
                    channels_item_data
                )

                channels.append(channels_item)

        label_ids = cast(list[str], d.pop("label_ids", UNSET))

        project_id = d.pop("project_id", UNSET)

        resolved_status_id = d.pop("resolved_status_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        test_monitor_connected_app_delivery_options = cls(
            assignee_id=assignee_id,
            auto_resolve=auto_resolve,
            channels=channels,
            label_ids=label_ids,
            project_id=project_id,
            resolved_status_id=resolved_status_id,
            team_id=team_id,
        )

        test_monitor_connected_app_delivery_options.additional_properties = d
        return test_monitor_connected_app_delivery_options

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
