from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_rule import CustomRule


T = TypeVar("T", bound="StorageManagementPolicyRequest")


@_attrs_define
class StorageManagementPolicyRequest:
    """
    Attributes:
        retention (str):
        version (int):
        cold_move_duration (str | Unset):
        cold_volume (str | Unset):
        created_by (str | Unset):
        custom_rules (list[CustomRule] | Unset):
    """

    retention: str
    version: int
    cold_move_duration: str | Unset = UNSET
    cold_volume: str | Unset = UNSET
    created_by: str | Unset = UNSET
    custom_rules: list[CustomRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retention = self.retention

        version = self.version

        cold_move_duration = self.cold_move_duration

        cold_volume = self.cold_volume

        created_by = self.created_by

        custom_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_rules, Unset):
            custom_rules = []
            for custom_rules_item_data in self.custom_rules:
                custom_rules_item = custom_rules_item_data.to_dict()
                custom_rules.append(custom_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retention": retention,
                "version": version,
            }
        )
        if cold_move_duration is not UNSET:
            field_dict["cold_move_duration"] = cold_move_duration
        if cold_volume is not UNSET:
            field_dict["cold_volume"] = cold_volume
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if custom_rules is not UNSET:
            field_dict["custom_rules"] = custom_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_rule import CustomRule

        d = dict(src_dict)
        retention = d.pop("retention")

        version = d.pop("version")

        cold_move_duration = d.pop("cold_move_duration", UNSET)

        cold_volume = d.pop("cold_volume", UNSET)

        created_by = d.pop("created_by", UNSET)

        _custom_rules = d.pop("custom_rules", UNSET)
        custom_rules: list[CustomRule] | Unset = UNSET
        if _custom_rules is not UNSET:
            custom_rules = []
            for custom_rules_item_data in _custom_rules:
                custom_rules_item = CustomRule.from_dict(custom_rules_item_data)

                custom_rules.append(custom_rules_item)

        storage_management_policy_request = cls(
            retention=retention,
            version=version,
            cold_move_duration=cold_move_duration,
            cold_volume=cold_volume,
            created_by=created_by,
            custom_rules=custom_rules,
        )

        storage_management_policy_request.additional_properties = d
        return storage_management_policy_request

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
