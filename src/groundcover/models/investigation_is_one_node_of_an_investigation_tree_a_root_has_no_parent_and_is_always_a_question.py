from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question_kind import (
    InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionKind,
)
from ..models.investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question_status import (
    InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionStatus,
)
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion")


@_attrs_define
class InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion:
    """
    Attributes:
        created_at (datetime.datetime):
        id (UUID):
        kind (InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionKind):
        root_id (UUID): Root of the tree; equals id for roots.
        statement (str): The question, or the claim to test.
        status (InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionStatus):
        parent_id (UUID | Unset): Parent node; omitted for roots.
    """

    created_at: datetime.datetime
    id: UUID
    kind: InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionKind
    root_id: UUID
    statement: str
    status: InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionStatus
    parent_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        kind = self.kind.value

        root_id = str(self.root_id)

        statement = self.statement

        status = self.status.value

        parent_id: str | Unset = UNSET
        if not isinstance(self.parent_id, Unset):
            parent_id = str(self.parent_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "kind": kind,
                "rootId": root_id,
                "statement": statement,
                "status": status,
            }
        )
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

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
        created_at = parse_datetime(d.pop("createdAt"))

        id = UUID(d.pop("id"))

        kind = InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionKind(d.pop("kind"))

        root_id = UUID(d.pop("rootId"))

        statement = d.pop("statement")

        status = InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionStatus(d.pop("status"))

        _parent_id = d.pop("parentId", UNSET)
        parent_id: UUID | Unset
        if isinstance(_parent_id, Unset) or _parent_id is None:
            parent_id = UNSET
        else:
            parent_id = UUID(_parent_id)

        investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question = cls(
            created_at=created_at,
            id=id,
            kind=kind,
            root_id=root_id,
            statement=statement,
            status=status,
            parent_id=parent_id,
        )

        investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question.additional_properties = d
        return investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question

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
