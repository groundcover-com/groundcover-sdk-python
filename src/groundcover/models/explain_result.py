from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.explain_result_plan_kind import ExplainResultPlanKind
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.explain_db_error_is_the_error_the_database_returned_instead_of_a_plan import (
        ExplainDBErrorIsTheErrorTheDatabaseReturnedInsteadOfAPlan,
    )


T = TypeVar("T", bound="ExplainResult")


@_attrs_define
class ExplainResult:
    """ExplainResult is the database's answer as it gave it: a plan, or the error it returned instead. Every engine's
    explain answers with it.

        Attributes:
            db_error (ExplainDBErrorIsTheErrorTheDatabaseReturnedInsteadOfAPlan | Unset):
            plan (Any | Unset): The engine's own JSON plan as the database wrote it, such as PostgreSQL's EXPLAIN (FORMAT
                JSON) output. Its
                shape is the engine's: PostgreSQL's is a list, MySQL's an object.
            plan_kind (ExplainResultPlanKind | Unset): PostgreSQL only. custom: planned for the query's params. generic: it
                had none, so the plan holds for any value
                (PostgreSQL 16+).
    """

    db_error: ExplainDBErrorIsTheErrorTheDatabaseReturnedInsteadOfAPlan | Unset = UNSET
    plan: Any | Unset = UNSET
    plan_kind: ExplainResultPlanKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        db_error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.db_error, Unset):
            db_error = self.db_error.to_dict()

        plan = self.plan

        plan_kind: str | Unset = UNSET
        if not isinstance(self.plan_kind, Unset):
            plan_kind = self.plan_kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if db_error is not UNSET:
            field_dict["db_error"] = db_error
        if plan is not UNSET:
            field_dict["plan"] = plan
        if plan_kind is not UNSET:
            field_dict["plan_kind"] = plan_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.explain_db_error_is_the_error_the_database_returned_instead_of_a_plan import (
            ExplainDBErrorIsTheErrorTheDatabaseReturnedInsteadOfAPlan,
        )

        d = dict(src_dict)
        _db_error = d.pop("db_error", UNSET)
        db_error: ExplainDBErrorIsTheErrorTheDatabaseReturnedInsteadOfAPlan | Unset
        if isinstance(_db_error, Unset) or _db_error is None:
            db_error = UNSET
        else:
            db_error = ExplainDBErrorIsTheErrorTheDatabaseReturnedInsteadOfAPlan.from_dict(_db_error)

        plan = d.pop("plan", UNSET)

        _plan_kind = d.pop("plan_kind", UNSET)
        plan_kind: ExplainResultPlanKind | Unset
        if isinstance(_plan_kind, Unset) or _plan_kind is None:
            plan_kind = UNSET
        else:
            plan_kind = ExplainResultPlanKind(_plan_kind)

        explain_result = cls(
            db_error=db_error,
            plan=plan,
            plan_kind=plan_kind,
        )

        explain_result.additional_properties = d
        return explain_result

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
