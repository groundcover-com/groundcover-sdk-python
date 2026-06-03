from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_rule import CustomRule


T = TypeVar("T", bound="StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation")


@_attrs_define
class StorageManagementPolicyResponseIsTheAPIFacingPolicyRepresentation:
    """
    Attributes:
        cold_move_duration (str | Unset):
        cold_volume (str | Unset):
        created_by (str | Unset):
        created_timestamp (datetime.datetime | Unset):
        custom_rules (list[CustomRule] | Unset):
        data_type (str | Unset):
        retention (str | Unset):
        uuid (str | Unset):
        version (int | Unset):
    """

    cold_move_duration: str | Unset = UNSET
    cold_volume: str | Unset = UNSET
    created_by: str | Unset = UNSET
    created_timestamp: datetime.datetime | Unset = UNSET
    custom_rules: list[CustomRule] | Unset = UNSET
    data_type: str | Unset = UNSET
    retention: str | Unset = UNSET
    uuid: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cold_move_duration = self.cold_move_duration

        cold_volume = self.cold_volume

        created_by = self.created_by

        created_timestamp: str | Unset = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        custom_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_rules, Unset):
            custom_rules = []
            for custom_rules_item_data in self.custom_rules:
                custom_rules_item = custom_rules_item_data.to_dict()
                custom_rules.append(custom_rules_item)

        data_type = self.data_type

        retention = self.retention

        uuid = self.uuid

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cold_move_duration is not UNSET:
            field_dict["cold_move_duration"] = cold_move_duration
        if cold_volume is not UNSET:
            field_dict["cold_volume"] = cold_volume
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_timestamp is not UNSET:
            field_dict["created_timestamp"] = created_timestamp
        if custom_rules is not UNSET:
            field_dict["custom_rules"] = custom_rules
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if retention is not UNSET:
            field_dict["retention"] = retention
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_rule import CustomRule

        d = dict(src_dict)
        cold_move_duration = d.pop("cold_move_duration", UNSET)

        cold_volume = d.pop("cold_volume", UNSET)

        created_by = d.pop("created_by", UNSET)

        _created_timestamp = d.pop("created_timestamp", UNSET)
        created_timestamp: datetime.datetime | Unset
        if isinstance(_created_timestamp, Unset) or _created_timestamp is None:
            created_timestamp = UNSET
        else:
            created_timestamp = parse_datetime(_created_timestamp)

        _custom_rules = d.pop("custom_rules", UNSET)
        custom_rules: list[CustomRule] | Unset = UNSET
        if _custom_rules is not UNSET:
            custom_rules = []
            for custom_rules_item_data in _custom_rules:
                custom_rules_item = CustomRule.from_dict(custom_rules_item_data)

                custom_rules.append(custom_rules_item)

        data_type = d.pop("data_type", UNSET)

        retention = d.pop("retention", UNSET)

        uuid = d.pop("uuid", UNSET)

        version = d.pop("version", UNSET)

        storage_management_policy_response_is_the_api_facing_policy_representation = cls(
            cold_move_duration=cold_move_duration,
            cold_volume=cold_volume,
            created_by=created_by,
            created_timestamp=created_timestamp,
            custom_rules=custom_rules,
            data_type=data_type,
            retention=retention,
            uuid=uuid,
            version=version,
        )

        storage_management_policy_response_is_the_api_facing_policy_representation.additional_properties = d
        return storage_management_policy_response_is_the_api_facing_policy_representation

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
