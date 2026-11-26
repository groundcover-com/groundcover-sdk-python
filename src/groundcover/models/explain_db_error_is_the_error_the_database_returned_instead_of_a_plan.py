from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ExplainDBErrorIsTheErrorTheDatabaseReturnedInsteadOfAPlan")


@_attrs_define
class ExplainDBErrorIsTheErrorTheDatabaseReturnedInsteadOfAPlan:
    """
    Attributes:
        code (str): The engine's own code: for PostgreSQL the SQLSTATE, such as 42501 for a missing privilege.
        message (str):
        detail (str | Unset):
        hint (str | Unset):
    """

    code: str
    message: str
    detail: str | Unset = UNSET
    hint: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        detail = self.detail

        hint = self.hint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if hint is not UNSET:
            field_dict["hint"] = hint

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
        code = d.pop("code")

        message = d.pop("message")

        detail = d.pop("detail", UNSET)

        hint = d.pop("hint", UNSET)

        explain_db_error_is_the_error_the_database_returned_instead_of_a_plan = cls(
            code=code,
            message=message,
            detail=detail,
            hint=hint,
        )

        explain_db_error_is_the_error_the_database_returned_instead_of_a_plan.additional_properties = d
        return explain_db_error_is_the_error_the_database_returned_instead_of_a_plan

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
