from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SlackChannelPickerChannelIsASlackChannelReturnedByTheChannelPickerAPI")


@_attrs_define
class SlackChannelPickerChannelIsASlackChannelReturnedByTheChannelPickerAPI:
    """
    Attributes:
        id (str | Unset):
        is_archived (bool | Unset):
        is_private (bool | Unset):
        name (str | Unset):
    """

    id: str | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_private: bool | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_archived = self.is_archived

        is_private = self.is_private

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_archived is not UNSET:
            field_dict["is_archived"] = is_archived
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_archived = d.pop("is_archived", UNSET)

        is_private = d.pop("is_private", UNSET)

        name = d.pop("name", UNSET)

        slack_channel_picker_channel_is_a_slack_channel_returned_by_the_channel_picker_api = cls(
            id=id,
            is_archived=is_archived,
            is_private=is_private,
            name=name,
        )

        slack_channel_picker_channel_is_a_slack_channel_returned_by_the_channel_picker_api.additional_properties = d
        return slack_channel_picker_channel_is_a_slack_channel_returned_by_the_channel_picker_api

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
