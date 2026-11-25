from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investigation_exists_error_is_the_409_body_of_create_investigation_the_issues_firing_cycle_has_an_open_root_to_join_code import (
    InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssuesFiringCycleHasAnOpenRootToJoinCode,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_exists_details import InvestigationExistsDetails


T = TypeVar(
    "T", bound="InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssuesFiringCycleHasAnOpenRootToJoin"
)


@_attrs_define
class InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssuesFiringCycleHasAnOpenRootToJoin:
    """
    Attributes:
        code (InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssuesFiringCycleHasAnOpenRootToJoinCode):
        details (InvestigationExistsDetails): InvestigationExistsDetails is the details of a 409 INVESTIGATION_EXISTS,
            the root to join, or of a 409
            TRIGGER_IN_COOLDOWN, the trigger's root of the issue from within its cooldown.
        message (str):
        trace_id (str | Unset):
    """

    code: InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssuesFiringCycleHasAnOpenRootToJoinCode
    details: InvestigationExistsDetails
    message: str
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        details = self.details.to_dict()

        message = self.message

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "details": details,
                "message": message,
            }
        )
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_exists_details import InvestigationExistsDetails

        d = dict(src_dict)
        code = InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssuesFiringCycleHasAnOpenRootToJoinCode(
            d.pop("code")
        )

        details = InvestigationExistsDetails.from_dict(d.pop("details"))

        message = d.pop("message")

        trace_id = d.pop("trace_id", UNSET)

        investigation_exists_error_is_the_409_body_of_create_investigation_the_issues_firing_cycle_has_an_open_root_to_join = cls(
            code=code,
            details=details,
            message=message,
            trace_id=trace_id,
        )

        investigation_exists_error_is_the_409_body_of_create_investigation_the_issues_firing_cycle_has_an_open_root_to_join.additional_properties = d
        return investigation_exists_error_is_the_409_body_of_create_investigation_the_issues_firing_cycle_has_an_open_root_to_join

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
