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


T = TypeVar("T", bound="MathExpression")


@_attrs_define
class MathExpression:
    """
    Attributes:
        alias (str | Unset):
        args (list[MathExpression] | Unset):
        column (ColumnDefinesASearchableColumnAndItsProperties | Unset):
        keep_existing (bool | Unset):
        math_operator (str | Unset):
        scalar (str | Unset):
    """

    alias: str | Unset = UNSET
    args: list[MathExpression] | Unset = UNSET
    column: ColumnDefinesASearchableColumnAndItsProperties | Unset = UNSET
    keep_existing: bool | Unset = UNSET
    math_operator: str | Unset = UNSET
    scalar: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        args: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = []
            for args_item_data in self.args:
                args_item = args_item_data.to_dict()
                args.append(args_item)

        column: dict[str, Any] | Unset = UNSET
        if not isinstance(self.column, Unset):
            column = self.column.to_dict()

        keep_existing = self.keep_existing

        math_operator = self.math_operator

        scalar = self.scalar

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if args is not UNSET:
            field_dict["args"] = args
        if column is not UNSET:
            field_dict["column"] = column
        if keep_existing is not UNSET:
            field_dict["keepExisting"] = keep_existing
        if math_operator is not UNSET:
            field_dict["math_operator"] = math_operator
        if scalar is not UNSET:
            field_dict["scalar"] = scalar

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_defines_a_searchable_column_and_its_properties import (
            ColumnDefinesASearchableColumnAndItsProperties,
        )

        d = dict(src_dict)
        alias = d.pop("alias", UNSET)

        _args = d.pop("args", UNSET)
        args: list[MathExpression] | Unset = UNSET
        if _args is not UNSET:
            args = []
            for args_item_data in _args:
                args_item = MathExpression.from_dict(args_item_data)

                args.append(args_item)

        _column = d.pop("column", UNSET)
        column: ColumnDefinesASearchableColumnAndItsProperties | Unset
        if isinstance(_column, Unset) or _column is None:
            column = UNSET
        else:
            column = ColumnDefinesASearchableColumnAndItsProperties.from_dict(_column)

        keep_existing = d.pop("keepExisting", UNSET)

        math_operator = d.pop("math_operator", UNSET)

        scalar = d.pop("scalar", UNSET)

        math_expression = cls(
            alias=alias,
            args=args,
            column=column,
            keep_existing=keep_existing,
            math_operator=math_operator,
            scalar=scalar,
        )

        math_expression.additional_properties = d
        return math_expression

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
