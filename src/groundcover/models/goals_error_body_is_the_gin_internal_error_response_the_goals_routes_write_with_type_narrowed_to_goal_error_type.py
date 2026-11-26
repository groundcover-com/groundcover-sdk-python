from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.goals_error_body_is_the_gin_internal_error_response_the_goals_routes_write_with_type_narrowed_to_goal_error_type_code import (
    GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeCode,
)
from ..models.goals_error_body_is_the_gin_internal_error_response_the_goals_routes_write_with_type_narrowed_to_goal_error_type_type import (
    GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeType,
)
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorType")


@_attrs_define
class GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorType:
    """
    Attributes:
        code (GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeCode |
            Unset): SEMANTIC_INTELLIGENCE_DISABLED on 409 when the switch is off;
            EXCEEDED_MAX_ROWS_TO_GROUP_BY on 400 when a read hits a group or result cap.
            EXCEEDED_MAX_ROWS_TO_GROUP_BY ErrCodeExceededMaxRowsToGroupBy  ErrCodeExceededMaxRowsToGroupBy is returned when
            a ClickHouse query  hits the `max_rows_to_group_by` cap under `group_by_overflow_mode='throw'`  (exception 158,
            mapped from `clickhouse.ErrTooManyRows`). Paired with  HTTP 400 and a hint to narrow filters or reduce group-by
            cardinality.
            SEMANTIC_INTELLIGENCE_DISABLED ErrCodeSemanticIntelligenceDisabled  ErrCodeSemanticIntelligenceDisabled: the
            backend's Semantic Intelligence  switch is off, or account-level AI features are, so AI goal data is not
            served. HTTP 409; clients render the disabled state instead of empty data.
            MONITOR_EVAL_FAILED ErrCodeMonitorEvalFailed  ErrCodeMonitorEvalFailed: the monitor's queries/condition failed
            live  evaluation — details.evalErrors carries [{query, message, raw}] per  failing node. HTTP 400.
            MONITOR_VALIDATION_FAILED ErrCodeMonitorValidationFailed  ErrCodeMonitorValidationFailed: the monitor definition
            failed schema or  model validation — details carries a field→message map. HTTP 400/422.
            MONITOR_DUPLICATE_TITLE ErrCodeMonitorDuplicateTitle  ErrCodeMonitorDuplicateTitle: a monitor with this title
            already exists.  HTTP 409.
            CONNECTED_APP_IN_USE ErrCodeConnectedAppInUse  ErrCodeConnectedAppInUse: a connected app or connector cannot be
            deleted  because notification routes or monitors still reference it. HTTP 409.
            VIEW_REVISION_CONFLICT ErrCodeViewRevisionConflict  ErrCodeViewRevisionConflict: a view/dashboard update carried
            a  currentRevision that has since been superseded, so nothing was written.  The message names the revision that
            won and who wrote it. Clients branch  on this to offer reload/overwrite/save-as-new. Distinct from HTTP 404 on
            the same endpoint, which means the view is gone. HTTP 409.
            CONNECTED_APP_ORPHANED_SECRET ErrCodeConnectedAppOrphanedSecret  ErrCodeConnectedAppOrphanedSecret: a connected
            app's usage could not be  checked because its backing secret no longer exists (deleted out-of-band),  so a
            provider-disable/delete guard fails closed on the corruption. Distinct  from CONNECTED_APP_IN_USE (also HTTP
            409) so clients can tell "still  referenced, expected" apart from "corrupted, needs cleanup". HTTP 409.
            INVALID_ARGUMENT ErrCodeInvalidArgument  ErrCodeInvalidArgument: a request parameter is malformed or outside its
            allowed values.
            INVESTIGATION_EXISTS ErrCodeInvestigationExists  ErrCodeInvestigationExists: an investigation root was opened
            for an issue  that already has an open root; details.investigationId names the root to  join. HTTP 409.
            SYNC_TARGET_TAKEN ErrCodeSyncTargetTaken  ErrCodeSyncTargetTaken: an investigation root was opened from a Slack
            thread that another root, open or closed, already follows, so nothing  was opened; details.ownerInvestigationId
            names that root. HTTP 409.
            TRIGGER_AT_CAPACITY ErrCodeTriggerAtCapacity  ErrCodeTriggerAtCapacity: an automation trigger already has its
            maxConcurrent  open investigation roots, so it may open another only after one closes; the  Retry-After header
            says when to try again. HTTP 429.
            TRIGGER_IN_COOLDOWN ErrCodeTriggerInCooldown  ErrCodeTriggerInCooldown: an automation trigger opened a root of
            the issue  within its cooldown, so nothing was opened; details.investigationId names  that root. HTTP 409.
            RUN_IDENTITY_REQUIRED ErrCodeRunIdentityRequired  ErrCodeRunIdentityRequired: an investigation root needs a user
            to act for:  its opener must be a user, or an agent acting for one, and a trigger that  opens roots must be
            saved by a user. HTTP 403.
            INVESTIGATIONS_DISABLED ErrCodeInvestigationsDisabled  ErrCodeInvestigationsDisabled: the organization has
            Investigations turned  off, so its investigation and trigger APIs are refused. HTTP 403.
            INVESTIGATION_CLOSED ErrCodeInvestigationClosed  ErrCodeInvestigationClosed: a write targets an investigation
            node that is  closed, or has a closed ancestor. HTTP 409.
            FINDING_OUT_OF_SCOPE ErrCodeFindingOutOfScope  ErrCodeFindingOutOfScope: a finding's query doesn't filter on the
            scope of  the node it is recorded on; details.scope names the entries to filter on.  HTTP 400.
            FINDING_RETRACTED ErrCodeFindingRetracted  ErrCodeFindingRetracted: a finding is already retracted, or a
            citation  names a retracted finding. HTTP 409.
            NOT_AUTHOR ErrCodeNotAuthor  ErrCodeNotAuthor: only a finding's author may retract it, since retraction  applies
            without moderation. HTTP 403.
            INVESTIGATION_GRAMMAR ErrCodeInvestigationGrammar  ErrCodeInvestigationGrammar: a create_child proposal asks for
            a kind the  node can't have as a child. HTTP 400.
            EVIDENCE_REQUIRED ErrCodeEvidenceRequired  ErrCodeEvidenceRequired: a resolve or refute proposal lacks the live
            evidence its kind needs. HTTP 400.
            REFUTE_REQUIRES_HYPOTHESIS ErrCodeRefuteRequiresHypothesis  ErrCodeRefuteRequiresHypothesis: a refute proposal
            targets a question;  only hypotheses are refuted. HTTP 400.
            HYPOTHESIS_REQUIRED ErrCodeHypothesisRequired  ErrCodeHypothesisRequired: a resolve proposal on a root question
            has no  settled (supported or refuted) hypothesis child; a person deciding  directly is exempt. HTTP 409.
        message (str | Unset): Human-readable error message.
        trace_id (str | Unset): Trace ID of the request.
        type_ (GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeType |
            Unset):
    """

    code: GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeCode | Unset = (
        UNSET
    )
    message: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    type_: GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeType | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        message = self.message

        trace_id = self.trace_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if type_ is not UNSET:
            field_dict["type"] = type_

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
        _code = d.pop("code", UNSET)
        code: GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeCode | Unset
        if isinstance(_code, Unset) or _code is None:
            code = UNSET
        else:
            code = GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeCode(
                _code
            )

        message = d.pop("message", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeType | Unset
        if isinstance(_type_, Unset) or _type_ is None:
            type_ = UNSET
        else:
            type_ = GoalsErrorBodyIsTheGinInternalErrorResponseTheGoalsRoutesWriteWithTypeNarrowedToGoalErrorTypeType(
                _type_
            )

        goals_error_body_is_the_gin_internal_error_response_the_goals_routes_write_with_type_narrowed_to_goal_error_type = cls(
            code=code,
            message=message,
            trace_id=trace_id,
            type_=type_,
        )

        goals_error_body_is_the_gin_internal_error_response_the_goals_routes_write_with_type_narrowed_to_goal_error_type.additional_properties = d
        return goals_error_body_is_the_gin_internal_error_response_the_goals_routes_write_with_type_narrowed_to_goal_error_type

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
