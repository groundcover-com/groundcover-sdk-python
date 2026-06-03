from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transform_represents_a_column_transform_that_registers_in_the_alias_registry_transforms_dont_create_subqueries_they_register_handlers_that_resolve_aliases_to_sql_expressions_type import (
    TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressionsType,
)
from .._generated_types import UNSET, Unset

T = TypeVar(
    "T",
    bound="TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressions",
)


@_attrs_define
class TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressions:
    """Requirements by transform type:
    json_unpack: Args is optional (not used)

        Attributes:
            alias (str): Alias is the name used to reference the transform result in subsequent pipes.
            source_column (str): SourceColumn is the column to transform.
            type_ (TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegis
                terHandlersThatResolveAliasesToSQLExpressionsType): Type specifies the kind of transform to apply.
                json_unpack TransformTypeJsonUnpack  TransformTypeJsonUnpack unpacks JSON fields with prefix matching
                datetime_extract TransformTypeDatetimeExtract  TransformTypeDatetimeExtract extracts date/time parts from
                timestamps
            args (list[str] | Unset): Args contains transform-specific arguments.
    """

    alias: str
    source_column: str
    type_: TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressionsType
    args: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        source_column = self.source_column

        type_ = self.type_.value

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias": alias,
                "sourceColumn": source_column,
                "type": type_,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        alias = d.pop("alias")

        source_column = d.pop("sourceColumn")

        type_ = TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressionsType(
            d.pop("type")
        )

        args = cast(list[str], d.pop("args", UNSET))

        transform_represents_a_column_transform_that_registers_in_the_alias_registry_transforms_dont_create_subqueries_they_register_handlers_that_resolve_aliases_to_sql_expressions = cls(
            alias=alias,
            source_column=source_column,
            type_=type_,
            args=args,
        )

        transform_represents_a_column_transform_that_registers_in_the_alias_registry_transforms_dont_create_subqueries_they_register_handlers_that_resolve_aliases_to_sql_expressions.additional_properties = d
        return transform_represents_a_column_transform_that_registers_in_the_alias_registry_transforms_dont_create_subqueries_they_register_handlers_that_resolve_aliases_to_sql_expressions

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
