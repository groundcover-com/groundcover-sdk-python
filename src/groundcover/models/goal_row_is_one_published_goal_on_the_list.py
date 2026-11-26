from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.goal_row_is_one_published_goal_on_the_list_goal_state import GoalRowIsOnePublishedGoalOnTheListGoalState
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.goal_agent_is_one_participant_attributed_to_the_goal import (
        GoalAgentIsOneParticipantAttributedToTheGoal,
    )
    from ..models.goal_drilldown import GoalDrilldown
    from ..models.goal_row_is_one_published_goal_on_the_list_evals import GoalRowIsOnePublishedGoalOnTheListEvals
    from ..models.subject_step_is_one_node_on_the_current_root_to_assigned_path import (
        SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath,
    )


T = TypeVar("T", bound="GoalRowIsOnePublishedGoalOnTheList")


@_attrs_define
class GoalRowIsOnePublishedGoalOnTheList:
    """
    Attributes:
        agents (list[GoalAgentIsOneParticipantAttributedToTheGoal]):
        blocker (None | str): Blocker is what stopped the goal, when one is known.
        cluster (str):
        conversation_key (str): ConversationKey identifies the conversation the goal was found in.
        drilldown (GoalDrilldown): GoalDrilldown holds the filters the UI runs when a row's subject or blocker
            is opened.
        end_timestamp (datetime.datetime):
        env (str):
        gen_ai_cost_input (float | None): GenAiCostInput is the input cost of the goal's spans in USD.
        gen_ai_cost_output (float | None): GenAiCostOutput is the output cost of the goal's spans in USD.
        gen_ai_cost_total (float | None): GenAiCostTotal is the total cost of the goal's spans in USD.
        gen_ai_usage_input_tokens (int | None): Token and cost fields are null when the spans carry no usage or price.
        gen_ai_usage_output_tokens (int | None):
        goal_id (str):
        goal_state (GoalRowIsOnePublishedGoalOnTheListGoalState): pending GoalStatePending
            complete GoalStateComplete
            unknown GoalStateUnknown  GoalStateUnknown has no current outcome result.
        goal_version (str): GoalVersion identifies this published version of the goal.
        namespace (str):
        outcome (None | str): Outcome is set once the goal has an outcome.
        pending_reason (None | str): PendingReason says why a goal without an outcome is still open.
        sentiment_end (None | str): SentimentEnd is the user's sentiment at the end of the goal.
        start_timestamp (datetime.datetime):
        subject_id (str): SubjectID is the current subject of the goal; the last step of subjectPath.
        subject_path (list[SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath]): SubjectPath is the current root-to-
            subject path, never empty. A goal without
            a current subject has the path of the subject other.
        timestamp (datetime.datetime): Timestamp is the time of the goal's first publication; it does not change
            between versions, and the list sorts on it.
        title (str):
        workloads (list[str]):
        evals (GoalRowIsOnePublishedGoalOnTheListEvals | Unset): Evals holds the current result of each requested
            evalFields reference, keyed by that reference.
    """

    agents: list[GoalAgentIsOneParticipantAttributedToTheGoal]
    blocker: None | str
    cluster: str
    conversation_key: str
    drilldown: GoalDrilldown
    end_timestamp: datetime.datetime
    env: str
    gen_ai_cost_input: float | None
    gen_ai_cost_output: float | None
    gen_ai_cost_total: float | None
    gen_ai_usage_input_tokens: int | None
    gen_ai_usage_output_tokens: int | None
    goal_id: str
    goal_state: GoalRowIsOnePublishedGoalOnTheListGoalState
    goal_version: str
    namespace: str
    outcome: None | str
    pending_reason: None | str
    sentiment_end: None | str
    start_timestamp: datetime.datetime
    subject_id: str
    subject_path: list[SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath]
    timestamp: datetime.datetime
    title: str
    workloads: list[str]
    evals: GoalRowIsOnePublishedGoalOnTheListEvals | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()
            agents.append(agents_item)

        blocker: None | str
        blocker = self.blocker

        cluster = self.cluster

        conversation_key = self.conversation_key

        drilldown = self.drilldown.to_dict()

        end_timestamp = self.end_timestamp.isoformat()

        env = self.env

        gen_ai_cost_input: float | None
        gen_ai_cost_input = self.gen_ai_cost_input

        gen_ai_cost_output: float | None
        gen_ai_cost_output = self.gen_ai_cost_output

        gen_ai_cost_total: float | None
        gen_ai_cost_total = self.gen_ai_cost_total

        gen_ai_usage_input_tokens: int | None
        gen_ai_usage_input_tokens = self.gen_ai_usage_input_tokens

        gen_ai_usage_output_tokens: int | None
        gen_ai_usage_output_tokens = self.gen_ai_usage_output_tokens

        goal_id = self.goal_id

        goal_state = self.goal_state.value

        goal_version = self.goal_version

        namespace = self.namespace

        outcome: None | str
        outcome = self.outcome

        pending_reason: None | str
        pending_reason = self.pending_reason

        sentiment_end: None | str
        sentiment_end = self.sentiment_end

        start_timestamp = self.start_timestamp.isoformat()

        subject_id = self.subject_id

        subject_path = []
        for subject_path_item_data in self.subject_path:
            subject_path_item = subject_path_item_data.to_dict()
            subject_path.append(subject_path_item)

        timestamp = self.timestamp.isoformat()

        title = self.title

        workloads = self.workloads

        evals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evals, Unset):
            evals = self.evals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agents": agents,
                "blocker": blocker,
                "cluster": cluster,
                "conversationKey": conversation_key,
                "drilldown": drilldown,
                "endTimestamp": end_timestamp,
                "env": env,
                "genAiCostInput": gen_ai_cost_input,
                "genAiCostOutput": gen_ai_cost_output,
                "genAiCostTotal": gen_ai_cost_total,
                "genAiUsageInputTokens": gen_ai_usage_input_tokens,
                "genAiUsageOutputTokens": gen_ai_usage_output_tokens,
                "goalId": goal_id,
                "goalState": goal_state,
                "goalVersion": goal_version,
                "namespace": namespace,
                "outcome": outcome,
                "pendingReason": pending_reason,
                "sentimentEnd": sentiment_end,
                "startTimestamp": start_timestamp,
                "subjectId": subject_id,
                "subjectPath": subject_path,
                "timestamp": timestamp,
                "title": title,
                "workloads": workloads,
            }
        )
        if evals is not UNSET:
            field_dict["evals"] = evals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.goal_agent_is_one_participant_attributed_to_the_goal import (
            GoalAgentIsOneParticipantAttributedToTheGoal,
        )
        from ..models.goal_drilldown import GoalDrilldown
        from ..models.goal_row_is_one_published_goal_on_the_list_evals import GoalRowIsOnePublishedGoalOnTheListEvals
        from ..models.subject_step_is_one_node_on_the_current_root_to_assigned_path import (
            SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath,
        )

        d = dict(src_dict)
        agents = []
        _agents = d.pop("agents")
        for agents_item_data in _agents:
            agents_item = GoalAgentIsOneParticipantAttributedToTheGoal.from_dict(agents_item_data)

            agents.append(agents_item)

        def _parse_blocker(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        blocker = _parse_blocker(d.pop("blocker"))

        cluster = d.pop("cluster")

        conversation_key = d.pop("conversationKey")

        drilldown = GoalDrilldown.from_dict(d.pop("drilldown"))

        end_timestamp = parse_datetime(d.pop("endTimestamp"))

        env = d.pop("env")

        def _parse_gen_ai_cost_input(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        gen_ai_cost_input = _parse_gen_ai_cost_input(d.pop("genAiCostInput"))

        def _parse_gen_ai_cost_output(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        gen_ai_cost_output = _parse_gen_ai_cost_output(d.pop("genAiCostOutput"))

        def _parse_gen_ai_cost_total(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        gen_ai_cost_total = _parse_gen_ai_cost_total(d.pop("genAiCostTotal"))

        def _parse_gen_ai_usage_input_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        gen_ai_usage_input_tokens = _parse_gen_ai_usage_input_tokens(d.pop("genAiUsageInputTokens"))

        def _parse_gen_ai_usage_output_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        gen_ai_usage_output_tokens = _parse_gen_ai_usage_output_tokens(d.pop("genAiUsageOutputTokens"))

        goal_id = d.pop("goalId")

        goal_state = GoalRowIsOnePublishedGoalOnTheListGoalState(d.pop("goalState"))

        goal_version = d.pop("goalVersion")

        namespace = d.pop("namespace")

        def _parse_outcome(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome = _parse_outcome(d.pop("outcome"))

        def _parse_pending_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pending_reason = _parse_pending_reason(d.pop("pendingReason"))

        def _parse_sentiment_end(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sentiment_end = _parse_sentiment_end(d.pop("sentimentEnd"))

        start_timestamp = parse_datetime(d.pop("startTimestamp"))

        subject_id = d.pop("subjectId")

        subject_path = []
        _subject_path = d.pop("subjectPath")
        for subject_path_item_data in _subject_path:
            subject_path_item = SubjectStepIsOneNodeOnTheCurrentRootToAssignedPath.from_dict(subject_path_item_data)

            subject_path.append(subject_path_item)

        timestamp = parse_datetime(d.pop("timestamp"))

        title = d.pop("title")

        workloads = cast(list[str], d.pop("workloads"))

        _evals = d.pop("evals", UNSET)
        evals: GoalRowIsOnePublishedGoalOnTheListEvals | Unset
        if isinstance(_evals, Unset) or _evals is None:
            evals = UNSET
        else:
            evals = GoalRowIsOnePublishedGoalOnTheListEvals.from_dict(_evals)

        goal_row_is_one_published_goal_on_the_list = cls(
            agents=agents,
            blocker=blocker,
            cluster=cluster,
            conversation_key=conversation_key,
            drilldown=drilldown,
            end_timestamp=end_timestamp,
            env=env,
            gen_ai_cost_input=gen_ai_cost_input,
            gen_ai_cost_output=gen_ai_cost_output,
            gen_ai_cost_total=gen_ai_cost_total,
            gen_ai_usage_input_tokens=gen_ai_usage_input_tokens,
            gen_ai_usage_output_tokens=gen_ai_usage_output_tokens,
            goal_id=goal_id,
            goal_state=goal_state,
            goal_version=goal_version,
            namespace=namespace,
            outcome=outcome,
            pending_reason=pending_reason,
            sentiment_end=sentiment_end,
            start_timestamp=start_timestamp,
            subject_id=subject_id,
            subject_path=subject_path,
            timestamp=timestamp,
            title=title,
            workloads=workloads,
            evals=evals,
        )

        goal_row_is_one_published_goal_on_the_list.additional_properties = d
        return goal_row_is_one_published_goal_on_the_list

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
