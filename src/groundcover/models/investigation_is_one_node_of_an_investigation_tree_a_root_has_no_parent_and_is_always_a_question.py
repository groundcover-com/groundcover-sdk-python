from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
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

if TYPE_CHECKING:
    from ..models.investigation_author import InvestigationAuthor
    from ..models.investigation_scope_entry import InvestigationScopeEntry
    from ..models.investigation_time_range import InvestigationTimeRange
    from ..models.source_is_how_a_root_started_manual_on_the_public_create_route_or_what_a_backend_caller_opened_it_from import (
        SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFrom,
    )
    from ..models.subject_is_what_a_root_investigates_at_most_one_root_per_subject_is_open_at_a_time import (
        SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime,
    )


T = TypeVar("T", bound="InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion")


@_attrs_define
class InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestion:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (InvestigationAuthor):
        id (UUID):
        kind (InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionKind):
        root_id (UUID): Root of the tree; equals id for roots.
        statement (str): The question, or the claim to test.
        status (InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionStatus): Questions use
            open/answered/stopped; hypotheses use open/supported/refuted/stopped.
        close_approved_by (InvestigationAuthor | Unset):
        closed_at (datetime.datetime | Unset):
        closed_by (InvestigationAuthor | Unset):
        instructions (str | Unset): What the backend caller that opened the root asked of its investigator, sent after
            the statement; omitted when none.
        outcome (str | Unset):
        outcome_proposal_id (UUID | Unset): The approved resolve, refute or stop that closed the node; for a node a stop
            closed below it, that stop.
        parent_id (UUID | Unset): Parent node; omitted for roots.
        scope (list[InvestigationScopeEntry] | Unset):
        source (SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFrom | Unset):
        subject (SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime | Unset):
        time_range (InvestigationTimeRange | Unset):
    """

    created_at: datetime.datetime
    created_by: InvestigationAuthor
    id: UUID
    kind: InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionKind
    root_id: UUID
    statement: str
    status: InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionStatus
    close_approved_by: InvestigationAuthor | Unset = UNSET
    closed_at: datetime.datetime | Unset = UNSET
    closed_by: InvestigationAuthor | Unset = UNSET
    instructions: str | Unset = UNSET
    outcome: str | Unset = UNSET
    outcome_proposal_id: UUID | Unset = UNSET
    parent_id: UUID | Unset = UNSET
    scope: list[InvestigationScopeEntry] | Unset = UNSET
    source: SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFrom | Unset = UNSET
    subject: SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime | Unset = UNSET
    time_range: InvestigationTimeRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by.to_dict()

        id = str(self.id)

        kind = self.kind.value

        root_id = str(self.root_id)

        statement = self.statement

        status = self.status.value

        close_approved_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.close_approved_by, Unset):
            close_approved_by = self.close_approved_by.to_dict()

        closed_at: str | Unset = UNSET
        if not isinstance(self.closed_at, Unset):
            closed_at = self.closed_at.isoformat()

        closed_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.closed_by, Unset):
            closed_by = self.closed_by.to_dict()

        instructions = self.instructions

        outcome = self.outcome

        outcome_proposal_id: str | Unset = UNSET
        if not isinstance(self.outcome_proposal_id, Unset):
            outcome_proposal_id = str(self.outcome_proposal_id)

        parent_id: str | Unset = UNSET
        if not isinstance(self.parent_id, Unset):
            parent_id = str(self.parent_id)

        scope: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = []
            for scope_item_data in self.scope:
                scope_item = scope_item_data.to_dict()
                scope.append(scope_item)

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        subject: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "createdBy": created_by,
                "id": id,
                "kind": kind,
                "rootId": root_id,
                "statement": statement,
                "status": status,
            }
        )
        if close_approved_by is not UNSET:
            field_dict["closeApprovedBy"] = close_approved_by
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if closed_by is not UNSET:
            field_dict["closedBy"] = closed_by
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if outcome_proposal_id is not UNSET:
            field_dict["outcomeProposalId"] = outcome_proposal_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if scope is not UNSET:
            field_dict["scope"] = scope
        if source is not UNSET:
            field_dict["source"] = source
        if subject is not UNSET:
            field_dict["subject"] = subject
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_author import InvestigationAuthor
        from ..models.investigation_scope_entry import InvestigationScopeEntry
        from ..models.investigation_time_range import InvestigationTimeRange
        from ..models.source_is_how_a_root_started_manual_on_the_public_create_route_or_what_a_backend_caller_opened_it_from import (
            SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFrom,
        )
        from ..models.subject_is_what_a_root_investigates_at_most_one_root_per_subject_is_open_at_a_time import (
            SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime,
        )

        d = dict(src_dict)
        created_at = parse_datetime(d.pop("createdAt"))

        created_by = InvestigationAuthor.from_dict(d.pop("createdBy"))

        id = UUID(d.pop("id"))

        kind = InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionKind(d.pop("kind"))

        root_id = UUID(d.pop("rootId"))

        statement = d.pop("statement")

        status = InvestigationIsOneNodeOfAnInvestigationTreeARootHasNoParentAndIsAlwaysAQuestionStatus(d.pop("status"))

        _close_approved_by = d.pop("closeApprovedBy", UNSET)
        close_approved_by: InvestigationAuthor | Unset
        if isinstance(_close_approved_by, Unset) or _close_approved_by is None:
            close_approved_by = UNSET
        else:
            close_approved_by = InvestigationAuthor.from_dict(_close_approved_by)

        _closed_at = d.pop("closedAt", UNSET)
        closed_at: datetime.datetime | Unset
        if isinstance(_closed_at, Unset) or _closed_at is None:
            closed_at = UNSET
        else:
            closed_at = parse_datetime(_closed_at)

        _closed_by = d.pop("closedBy", UNSET)
        closed_by: InvestigationAuthor | Unset
        if isinstance(_closed_by, Unset) or _closed_by is None:
            closed_by = UNSET
        else:
            closed_by = InvestigationAuthor.from_dict(_closed_by)

        instructions = d.pop("instructions", UNSET)

        outcome = d.pop("outcome", UNSET)

        _outcome_proposal_id = d.pop("outcomeProposalId", UNSET)
        outcome_proposal_id: UUID | Unset
        if isinstance(_outcome_proposal_id, Unset) or _outcome_proposal_id is None:
            outcome_proposal_id = UNSET
        else:
            outcome_proposal_id = UUID(_outcome_proposal_id)

        _parent_id = d.pop("parentId", UNSET)
        parent_id: UUID | Unset
        if isinstance(_parent_id, Unset) or _parent_id is None:
            parent_id = UNSET
        else:
            parent_id = UUID(_parent_id)

        _scope = d.pop("scope", UNSET)
        scope: list[InvestigationScopeEntry] | Unset = UNSET
        if _scope is not UNSET:
            scope = []
            for scope_item_data in _scope:
                scope_item = InvestigationScopeEntry.from_dict(scope_item_data)

                scope.append(scope_item)

        _source = d.pop("source", UNSET)
        source: SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFrom | Unset
        if isinstance(_source, Unset) or _source is None:
            source = UNSET
        else:
            source = SourceIsHowARootStartedManualOnThePublicCreateRouteOrWhatABackendCallerOpenedItFrom.from_dict(
                _source
            )

        _subject = d.pop("subject", UNSET)
        subject: SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime | Unset
        if isinstance(_subject, Unset) or _subject is None:
            subject = UNSET
        else:
            subject = SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime.from_dict(_subject)

        _time_range = d.pop("timeRange", UNSET)
        time_range: InvestigationTimeRange | Unset
        if isinstance(_time_range, Unset) or _time_range is None:
            time_range = UNSET
        else:
            time_range = InvestigationTimeRange.from_dict(_time_range)

        investigation_is_one_node_of_an_investigation_tree_a_root_has_no_parent_and_is_always_a_question = cls(
            created_at=created_at,
            created_by=created_by,
            id=id,
            kind=kind,
            root_id=root_id,
            statement=statement,
            status=status,
            close_approved_by=close_approved_by,
            closed_at=closed_at,
            closed_by=closed_by,
            instructions=instructions,
            outcome=outcome,
            outcome_proposal_id=outcome_proposal_id,
            parent_id=parent_id,
            scope=scope,
            source=source,
            subject=subject,
            time_range=time_range,
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
