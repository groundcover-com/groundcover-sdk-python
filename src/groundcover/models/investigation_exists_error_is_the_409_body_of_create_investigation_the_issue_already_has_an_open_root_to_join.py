from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investigation_exists_error_is_the_409_body_of_create_investigation_the_issue_already_has_an_open_root_to_join_code import (
    InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssueAlreadyHasAnOpenRootToJoinCode,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_exists_details_is_the_details_of_a409investigationexists_the_root_to_join import (
        InvestigationExistsDetailsIsTheDetailsOfA409INVESTIGATIONEXISTSTheRootToJoin,
    )


T = TypeVar("T", bound="InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssueAlreadyHasAnOpenRootToJoin")


@_attrs_define
class InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssueAlreadyHasAnOpenRootToJoin:
    """
    Attributes:
        code (InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssueAlreadyHasAnOpenRootToJoinCode):
        details (InvestigationExistsDetailsIsTheDetailsOfA409INVESTIGATIONEXISTSTheRootToJoin):
        message (str):
        trace_id (str | Unset):
    """

    code: InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssueAlreadyHasAnOpenRootToJoinCode
    details: InvestigationExistsDetailsIsTheDetailsOfA409INVESTIGATIONEXISTSTheRootToJoin
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
        from ..models.investigation_exists_details_is_the_details_of_a409investigationexists_the_root_to_join import (
            InvestigationExistsDetailsIsTheDetailsOfA409INVESTIGATIONEXISTSTheRootToJoin,
        )

        d = dict(src_dict)
        code = InvestigationExistsErrorIsThe409BodyOfCreateInvestigationTheIssueAlreadyHasAnOpenRootToJoinCode(
            d.pop("code")
        )

        details = InvestigationExistsDetailsIsTheDetailsOfA409INVESTIGATIONEXISTSTheRootToJoin.from_dict(
            d.pop("details")
        )

        message = d.pop("message")

        trace_id = d.pop("trace_id", UNSET)

        investigation_exists_error_is_the_409_body_of_create_investigation_the_issue_already_has_an_open_root_to_join = cls(
            code=code,
            details=details,
            message=message,
            trace_id=trace_id,
        )

        investigation_exists_error_is_the_409_body_of_create_investigation_the_issue_already_has_an_open_root_to_join.additional_properties = d
        return investigation_exists_error_is_the_409_body_of_create_investigation_the_issue_already_has_an_open_root_to_join

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
