from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.migration import Migration


T = TypeVar("T", bound="ListMigrationsResponse")


@_attrs_define
class ListMigrationsResponse:
    """
    Attributes:
        migrations (list[Migration] | Unset): List of migrations
    """

    migrations: list[Migration] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        migrations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.migrations, Unset):
            migrations = []
            for migrations_item_data in self.migrations:
                migrations_item = migrations_item_data.to_dict()
                migrations.append(migrations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if migrations is not UNSET:
            field_dict["migrations"] = migrations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration import Migration

        d = dict(src_dict)
        _migrations = d.pop("migrations", UNSET)
        migrations: list[Migration] | Unset = UNSET
        if _migrations is not UNSET:
            migrations = []
            for migrations_item_data in _migrations:
                migrations_item = Migration.from_dict(migrations_item_data)

                migrations.append(migrations_item)

        list_migrations_response = cls(
            migrations=migrations,
        )

        list_migrations_response.additional_properties = d
        return list_migrations_response

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
