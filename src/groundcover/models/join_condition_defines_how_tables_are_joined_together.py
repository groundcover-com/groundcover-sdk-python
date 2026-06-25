from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_defines_a_searchable_column_and_its_properties import (
        ColumnDefinesASearchableColumnAndItsProperties,
    )


T = TypeVar("T", bound="JoinConditionDefinesHowTablesAreJoinedTogether")


@_attrs_define
class JoinConditionDefinesHowTablesAreJoinedTogether:
    """
    Attributes:
        left_column (ColumnDefinesASearchableColumnAndItsProperties | Unset):
        right_column (ColumnDefinesASearchableColumnAndItsProperties | Unset):
    """

    left_column: ColumnDefinesASearchableColumnAndItsProperties | Unset = UNSET
    right_column: ColumnDefinesASearchableColumnAndItsProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        left_column: dict[str, Any] | Unset = UNSET
        if not isinstance(self.left_column, Unset):
            left_column = self.left_column.to_dict()

        right_column: dict[str, Any] | Unset = UNSET
        if not isinstance(self.right_column, Unset):
            right_column = self.right_column.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left_column is not UNSET:
            field_dict["leftColumn"] = left_column
        if right_column is not UNSET:
            field_dict["rightColumn"] = right_column

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_defines_a_searchable_column_and_its_properties import (
            ColumnDefinesASearchableColumnAndItsProperties,
        )

        d = dict(src_dict)
        _left_column = d.pop("leftColumn", UNSET)
        left_column: ColumnDefinesASearchableColumnAndItsProperties | Unset
        if isinstance(_left_column, Unset) or _left_column is None:
            left_column = UNSET
        else:
            left_column = ColumnDefinesASearchableColumnAndItsProperties.from_dict(_left_column)

        _right_column = d.pop("rightColumn", UNSET)
        right_column: ColumnDefinesASearchableColumnAndItsProperties | Unset
        if isinstance(_right_column, Unset) or _right_column is None:
            right_column = UNSET
        else:
            right_column = ColumnDefinesASearchableColumnAndItsProperties.from_dict(_right_column)

        join_condition_defines_how_tables_are_joined_together = cls(
            left_column=left_column,
            right_column=right_column,
        )

        join_condition_defines_how_tables_are_joined_together.additional_properties = d
        return join_condition_defines_how_tables_are_joined_together

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
