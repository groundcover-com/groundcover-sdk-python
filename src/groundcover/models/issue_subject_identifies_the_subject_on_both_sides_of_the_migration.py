from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration")


@_attrs_define
class IssueSubjectIdentifiesTheSubjectOnBothSidesOfTheMigration:
    """
    Attributes:
        name_dd (str):
        name_gc (str):
    """

    name_dd: str
    name_gc: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_dd = self.name_dd

        name_gc = self.name_gc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name_dd": name_dd,
                "name_gc": name_gc,
            }
        )

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
        name_dd = d.pop("name_dd")

        name_gc = d.pop("name_gc")

        issue_subject_identifies_the_subject_on_both_sides_of_the_migration = cls(
            name_dd=name_dd,
            name_gc=name_gc,
        )

        issue_subject_identifies_the_subject_on_both_sides_of_the_migration.additional_properties = d
        return issue_subject_identifies_the_subject_on_both_sides_of_the_migration

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
