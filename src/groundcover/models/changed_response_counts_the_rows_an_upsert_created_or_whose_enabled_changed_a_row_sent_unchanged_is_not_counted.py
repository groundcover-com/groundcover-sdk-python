from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ChangedResponseCountsTheRowsAnUpsertCreatedOrWhoseEnabledChangedARowSentUnchangedIsNotCounted")


@_attrs_define
class ChangedResponseCountsTheRowsAnUpsertCreatedOrWhoseEnabledChangedARowSentUnchangedIsNotCounted:
    """
    Attributes:
        changed (int | Unset):
    """

    changed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed is not UNSET:
            field_dict["changed"] = changed

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
        changed = d.pop("changed", UNSET)

        changed_response_counts_the_rows_an_upsert_created_or_whose_enabled_changed_a_row_sent_unchanged_is_not_counted = cls(
            changed=changed,
        )

        changed_response_counts_the_rows_an_upsert_created_or_whose_enabled_changed_a_row_sent_unchanged_is_not_counted.additional_properties = d
        return changed_response_counts_the_rows_an_upsert_created_or_whose_enabled_changed_a_row_sent_unchanged_is_not_counted

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
