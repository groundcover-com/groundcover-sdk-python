from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SourceRefHoldsTheFieldsOfEverySourceTypeEachTypeRequiresItsOwnAndRefusesTheOthers")


@_attrs_define
class SourceRefHoldsTheFieldsOfEverySourceTypeEachTypeRequiresItsOwnAndRefusesTheOthers:
    """
    Attributes:
        channel_id (str | Unset): slack: the channel of the alert thread whose Investigate button opened the root.
        connector_id (str | Unset): slack: the comm-hub org connector the alert was posted with.
        thread_ts (str | Unset): slack: the ts of that thread's alert message.
        trigger_id (str | Unset): automation: the trigger that opened the root.
    """

    channel_id: str | Unset = UNSET
    connector_id: str | Unset = UNSET
    thread_ts: str | Unset = UNSET
    trigger_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        connector_id = self.connector_id

        thread_ts = self.thread_ts

        trigger_id = self.trigger_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if thread_ts is not UNSET:
            field_dict["threadTs"] = thread_ts
        if trigger_id is not UNSET:
            field_dict["triggerId"] = trigger_id

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
        channel_id = d.pop("channelId", UNSET)

        connector_id = d.pop("connectorId", UNSET)

        thread_ts = d.pop("threadTs", UNSET)

        trigger_id = d.pop("triggerId", UNSET)

        source_ref_holds_the_fields_of_every_source_type_each_type_requires_its_own_and_refuses_the_others = cls(
            channel_id=channel_id,
            connector_id=connector_id,
            thread_ts=thread_ts,
            trigger_id=trigger_id,
        )

        source_ref_holds_the_fields_of_every_source_type_each_type_requires_its_own_and_refuses_the_others.additional_properties = d
        return source_ref_holds_the_fields_of_every_source_type_each_type_requires_its_own_and_refuses_the_others

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
