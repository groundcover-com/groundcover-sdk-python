from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.investigation_author import InvestigationAuthor


T = TypeVar("T", bound="ProposalDecisionRecordsWhoDecidedAProposalAndWhy")


@_attrs_define
class ProposalDecisionRecordsWhoDecidedAProposalAndWhy:
    """
    Attributes:
        at (datetime.datetime):
        by (InvestigationAuthor):
        reason (str):
    """

    at: datetime.datetime
    by: InvestigationAuthor
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        by = self.by.to_dict()

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "at": at,
                "by": by,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_author import InvestigationAuthor

        d = dict(src_dict)
        at = parse_datetime(d.pop("at"))

        by = InvestigationAuthor.from_dict(d.pop("by"))

        reason = d.pop("reason")

        proposal_decision_records_who_decided_a_proposal_and_why = cls(
            at=at,
            by=by,
            reason=reason,
        )

        proposal_decision_records_who_decided_a_proposal_and_why.additional_properties = d
        return proposal_decision_records_who_decided_a_proposal_and_why

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
