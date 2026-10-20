from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node import (
        ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode,
    )


T = TypeVar("T", bound="ListInvestigationProposalsResponse")


@_attrs_define
class ListInvestigationProposalsResponse:
    """
    Attributes:
        done (bool): Whether this page exhausts the pending proposals currently stored.
        proposals (list[ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode]): Pending proposals across the
            root investigation, each with its reviewState, ordered by createdAt, ascending.
        next_after_timestamp (datetime.datetime | Unset): Last returned proposal's createdAt, to send as afterTimestamp;
            an empty page retains afterTimestamp.
    """

    done: bool
    proposals: list[ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode]
    next_after_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        proposals = []
        for proposals_item_data in self.proposals:
            proposals_item = proposals_item_data.to_dict()
            proposals.append(proposals_item)

        next_after_timestamp: str | Unset = UNSET
        if not isinstance(self.next_after_timestamp, Unset):
            next_after_timestamp = self.next_after_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "done": done,
                "proposals": proposals,
            }
        )
        if next_after_timestamp is not UNSET:
            field_dict["nextAfterTimestamp"] = next_after_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_is_an_immutable_request_for_a_decision_on_one_investigation_node import (
            ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode,
        )

        d = dict(src_dict)
        done = d.pop("done")

        proposals = []
        _proposals = d.pop("proposals")
        for proposals_item_data in _proposals:
            proposals_item = ProposalIsAnImmutableRequestForADecisionOnOneInvestigationNode.from_dict(
                proposals_item_data
            )

            proposals.append(proposals_item)

        _next_after_timestamp = d.pop("nextAfterTimestamp", UNSET)
        next_after_timestamp: datetime.datetime | Unset
        if isinstance(_next_after_timestamp, Unset) or _next_after_timestamp is None:
            next_after_timestamp = UNSET
        else:
            next_after_timestamp = parse_datetime(_next_after_timestamp)

        list_investigation_proposals_response = cls(
            done=done,
            proposals=proposals,
            next_after_timestamp=next_after_timestamp,
        )

        list_investigation_proposals_response.additional_properties = d
        return list_investigation_proposals_response

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
