from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_author import InvestigationAuthor
    from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question import (
        InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion,
    )


T = TypeVar("T", bound="GetInvestigationTreeResponseIsOneConsistentSnapshotOfTheCompleteTree")


@_attrs_define
class GetInvestigationTreeResponseIsOneConsistentSnapshotOfTheCompleteTree:
    """
    Attributes:
        events_after (int): Tree events after afterTimestamp, or all events when it is omitted.
        nodes (list[InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion]): Root first, then
            remaining nodes by createdAt and id.
        participants (list[InvestigationAuthor]):
        next_after_timestamp (datetime.datetime | Unset): Timestamp of the latest event in this snapshot; omitted when
            no event exists.
    """

    events_after: int
    nodes: list[InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion]
    participants: list[InvestigationAuthor]
    next_after_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events_after = self.events_after

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()
            participants.append(participants_item)

        next_after_timestamp: str | Unset = UNSET
        if not isinstance(self.next_after_timestamp, Unset):
            next_after_timestamp = self.next_after_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventsAfter": events_after,
                "nodes": nodes,
                "participants": participants,
            }
        )
        if next_after_timestamp is not UNSET:
            field_dict["nextAfterTimestamp"] = next_after_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_author import InvestigationAuthor
        from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question import (
            InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion,
        )

        d = dict(src_dict)
        events_after = d.pop("eventsAfter")

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion.from_dict(
                nodes_item_data
            )

            nodes.append(nodes_item)

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = InvestigationAuthor.from_dict(participants_item_data)

            participants.append(participants_item)

        _next_after_timestamp = d.pop("nextAfterTimestamp", UNSET)
        next_after_timestamp: datetime.datetime | Unset
        if isinstance(_next_after_timestamp, Unset) or _next_after_timestamp is None:
            next_after_timestamp = UNSET
        else:
            next_after_timestamp = parse_datetime(_next_after_timestamp)

        get_investigation_tree_response_is_one_consistent_snapshot_of_the_complete_tree = cls(
            events_after=events_after,
            nodes=nodes,
            participants=participants,
            next_after_timestamp=next_after_timestamp,
        )

        get_investigation_tree_response_is_one_consistent_snapshot_of_the_complete_tree.additional_properties = d
        return get_investigation_tree_response_is_one_consistent_snapshot_of_the_complete_tree

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
