from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_finding import InvestigationFinding
    from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question import (
        InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion,
    )


T = TypeVar("T", bound="GetInvestigationResponse")


@_attrs_define
class GetInvestigationResponse:
    """
    Attributes:
        children (list[InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion]):
        events_after (int): Tree events after afterTimestamp, or all events when it is omitted.
        findings (list[InvestigationFinding]): Findings belonging to this node, included for all callers; an empty
            collection is [].
        investigation (InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion):
        next_after_timestamp (datetime.datetime | Unset): Timestamp of the latest tree event in this snapshot.
    """

    children: list[InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion]
    events_after: int
    findings: list[InvestigationFinding]
    investigation: InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion
    next_after_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        events_after = self.events_after

        findings = []
        for findings_item_data in self.findings:
            findings_item = findings_item_data.to_dict()
            findings.append(findings_item)

        investigation = self.investigation.to_dict()

        next_after_timestamp: str | Unset = UNSET
        if not isinstance(self.next_after_timestamp, Unset):
            next_after_timestamp = self.next_after_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "children": children,
                "eventsAfter": events_after,
                "findings": findings,
                "investigation": investigation,
            }
        )
        if next_after_timestamp is not UNSET:
            field_dict["nextAfterTimestamp"] = next_after_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_finding import InvestigationFinding
        from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question import (
            InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion,
        )

        d = dict(src_dict)
        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion.from_dict(
                children_item_data
            )

            children.append(children_item)

        events_after = d.pop("eventsAfter")

        findings = []
        _findings = d.pop("findings")
        for findings_item_data in _findings:
            findings_item = InvestigationFinding.from_dict(findings_item_data)

            findings.append(findings_item)

        investigation = InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion.from_dict(
            d.pop("investigation")
        )

        _next_after_timestamp = d.pop("nextAfterTimestamp", UNSET)
        next_after_timestamp: datetime.datetime | Unset
        if isinstance(_next_after_timestamp, Unset) or _next_after_timestamp is None:
            next_after_timestamp = UNSET
        else:
            next_after_timestamp = parse_datetime(_next_after_timestamp)

        get_investigation_response = cls(
            children=children,
            events_after=events_after,
            findings=findings,
            investigation=investigation,
            next_after_timestamp=next_after_timestamp,
        )

        get_investigation_response.additional_properties = d
        return get_investigation_response

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
