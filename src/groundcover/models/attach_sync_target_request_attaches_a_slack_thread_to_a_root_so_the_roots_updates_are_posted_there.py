from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attach_sync_target_request_attaches_a_slack_thread_to_a_root_so_the_roots_updates_are_posted_there_provider import (
    AttachSyncTargetRequestAttachesASlackThreadToARootSoTheRootsUpdatesArePostedThereProvider,
)

if TYPE_CHECKING:
    from ..models.slack_destination_is_a_slack_thread_the_alert_messages_channel_and_ts import (
        SlackDestinationIsASlackThreadTheAlertMessagesChannelAndTs,
    )


T = TypeVar("T", bound="AttachSyncTargetRequestAttachesASlackThreadToARootSoTheRootsUpdatesArePostedThere")


@_attrs_define
class AttachSyncTargetRequestAttachesASlackThreadToARootSoTheRootsUpdatesArePostedThere:
    """
    Attributes:
        connector_id (str): The comm-hub org connector that posts to the thread.
        destination (SlackDestinationIsASlackThreadTheAlertMessagesChannelAndTs):
        provider (AttachSyncTargetRequestAttachesASlackThreadToARootSoTheRootsUpdatesArePostedThereProvider): slack
            SyncTargetProviderSlack
    """

    connector_id: str
    destination: SlackDestinationIsASlackThreadTheAlertMessagesChannelAndTs
    provider: AttachSyncTargetRequestAttachesASlackThreadToARootSoTheRootsUpdatesArePostedThereProvider
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_id = self.connector_id

        destination = self.destination.to_dict()

        provider = self.provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorId": connector_id,
                "destination": destination,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slack_destination_is_a_slack_thread_the_alert_messages_channel_and_ts import (
            SlackDestinationIsASlackThreadTheAlertMessagesChannelAndTs,
        )

        d = dict(src_dict)
        connector_id = d.pop("connectorId")

        destination = SlackDestinationIsASlackThreadTheAlertMessagesChannelAndTs.from_dict(d.pop("destination"))

        provider = AttachSyncTargetRequestAttachesASlackThreadToARootSoTheRootsUpdatesArePostedThereProvider(
            d.pop("provider")
        )

        attach_sync_target_request_attaches_a_slack_thread_to_a_root_so_the_roots_updates_are_posted_there = cls(
            connector_id=connector_id,
            destination=destination,
            provider=provider,
        )

        attach_sync_target_request_attaches_a_slack_thread_to_a_root_so_the_roots_updates_are_posted_there.additional_properties = d
        return attach_sync_target_request_attaches_a_slack_thread_to_a_root_so_the_roots_updates_are_posted_there

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
