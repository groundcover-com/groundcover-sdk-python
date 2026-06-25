from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_action_defines_an_actionable_step_and_its_estimated_query_impact import (
        CoverageActionDefinesAnActionableStepAndItsEstimatedQueryImpact,
    )
    from ..models.coverage_step_is_a_selected_action_with_cumulative_projection_metadata import (
        CoverageStepIsASelectedActionWithCumulativeProjectionMetadata,
    )


T = TypeVar("T", bound="CoveragePlanProvidesAPrioritizedPathToImproveQuerySuccessRate")


@_attrs_define
class CoveragePlanProvidesAPrioritizedPathToImproveQuerySuccessRate:
    """
    Attributes:
        baseline_success_pct (float | Unset):
        blocking_queries (int | Unset):
        excluded_issue_types (list[str] | Unset):
        max_reachable_queries (int | Unset):
        max_reachable_success_pct (float | Unset):
        queries_needed_to_target (int | Unset):
        ranked_actions (list[CoverageActionDefinesAnActionableStepAndItsEstimatedQueryImpact] | Unset):
        recommended_path (list[CoverageStepIsASelectedActionWithCumulativeProjectionMetadata] | Unset):
        successful_queries (int | Unset):
        target_reachable (bool | Unset):
        target_success_pct (float | Unset):
        total_queries (int | Unset):
    """

    baseline_success_pct: float | Unset = UNSET
    blocking_queries: int | Unset = UNSET
    excluded_issue_types: list[str] | Unset = UNSET
    max_reachable_queries: int | Unset = UNSET
    max_reachable_success_pct: float | Unset = UNSET
    queries_needed_to_target: int | Unset = UNSET
    ranked_actions: list[CoverageActionDefinesAnActionableStepAndItsEstimatedQueryImpact] | Unset = UNSET
    recommended_path: list[CoverageStepIsASelectedActionWithCumulativeProjectionMetadata] | Unset = UNSET
    successful_queries: int | Unset = UNSET
    target_reachable: bool | Unset = UNSET
    target_success_pct: float | Unset = UNSET
    total_queries: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        baseline_success_pct = self.baseline_success_pct

        blocking_queries = self.blocking_queries

        excluded_issue_types: list[str] | Unset = UNSET
        if not isinstance(self.excluded_issue_types, Unset):
            excluded_issue_types = self.excluded_issue_types

        max_reachable_queries = self.max_reachable_queries

        max_reachable_success_pct = self.max_reachable_success_pct

        queries_needed_to_target = self.queries_needed_to_target

        ranked_actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranked_actions, Unset):
            ranked_actions = []
            for ranked_actions_item_data in self.ranked_actions:
                ranked_actions_item = ranked_actions_item_data.to_dict()
                ranked_actions.append(ranked_actions_item)

        recommended_path: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recommended_path, Unset):
            recommended_path = []
            for recommended_path_item_data in self.recommended_path:
                recommended_path_item = recommended_path_item_data.to_dict()
                recommended_path.append(recommended_path_item)

        successful_queries = self.successful_queries

        target_reachable = self.target_reachable

        target_success_pct = self.target_success_pct

        total_queries = self.total_queries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if baseline_success_pct is not UNSET:
            field_dict["baseline_success_pct"] = baseline_success_pct
        if blocking_queries is not UNSET:
            field_dict["blocking_queries"] = blocking_queries
        if excluded_issue_types is not UNSET:
            field_dict["excluded_issue_types"] = excluded_issue_types
        if max_reachable_queries is not UNSET:
            field_dict["max_reachable_queries"] = max_reachable_queries
        if max_reachable_success_pct is not UNSET:
            field_dict["max_reachable_success_pct"] = max_reachable_success_pct
        if queries_needed_to_target is not UNSET:
            field_dict["queries_needed_to_target"] = queries_needed_to_target
        if ranked_actions is not UNSET:
            field_dict["ranked_actions"] = ranked_actions
        if recommended_path is not UNSET:
            field_dict["recommended_path"] = recommended_path
        if successful_queries is not UNSET:
            field_dict["successful_queries"] = successful_queries
        if target_reachable is not UNSET:
            field_dict["target_reachable"] = target_reachable
        if target_success_pct is not UNSET:
            field_dict["target_success_pct"] = target_success_pct
        if total_queries is not UNSET:
            field_dict["total_queries"] = total_queries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coverage_action_defines_an_actionable_step_and_its_estimated_query_impact import (
            CoverageActionDefinesAnActionableStepAndItsEstimatedQueryImpact,
        )
        from ..models.coverage_step_is_a_selected_action_with_cumulative_projection_metadata import (
            CoverageStepIsASelectedActionWithCumulativeProjectionMetadata,
        )

        d = dict(src_dict)
        baseline_success_pct = d.pop("baseline_success_pct", UNSET)

        blocking_queries = d.pop("blocking_queries", UNSET)

        excluded_issue_types = cast(list[str], d.pop("excluded_issue_types", UNSET))

        max_reachable_queries = d.pop("max_reachable_queries", UNSET)

        max_reachable_success_pct = d.pop("max_reachable_success_pct", UNSET)

        queries_needed_to_target = d.pop("queries_needed_to_target", UNSET)

        _ranked_actions = d.pop("ranked_actions", UNSET)
        ranked_actions: list[CoverageActionDefinesAnActionableStepAndItsEstimatedQueryImpact] | Unset = UNSET
        if _ranked_actions is not UNSET:
            ranked_actions = []
            for ranked_actions_item_data in _ranked_actions:
                ranked_actions_item = CoverageActionDefinesAnActionableStepAndItsEstimatedQueryImpact.from_dict(
                    ranked_actions_item_data
                )

                ranked_actions.append(ranked_actions_item)

        _recommended_path = d.pop("recommended_path", UNSET)
        recommended_path: list[CoverageStepIsASelectedActionWithCumulativeProjectionMetadata] | Unset = UNSET
        if _recommended_path is not UNSET:
            recommended_path = []
            for recommended_path_item_data in _recommended_path:
                recommended_path_item = CoverageStepIsASelectedActionWithCumulativeProjectionMetadata.from_dict(
                    recommended_path_item_data
                )

                recommended_path.append(recommended_path_item)

        successful_queries = d.pop("successful_queries", UNSET)

        target_reachable = d.pop("target_reachable", UNSET)

        target_success_pct = d.pop("target_success_pct", UNSET)

        total_queries = d.pop("total_queries", UNSET)

        coverage_plan_provides_a_prioritized_path_to_improve_query_success_rate = cls(
            baseline_success_pct=baseline_success_pct,
            blocking_queries=blocking_queries,
            excluded_issue_types=excluded_issue_types,
            max_reachable_queries=max_reachable_queries,
            max_reachable_success_pct=max_reachable_success_pct,
            queries_needed_to_target=queries_needed_to_target,
            ranked_actions=ranked_actions,
            recommended_path=recommended_path,
            successful_queries=successful_queries,
            target_reachable=target_reachable,
            target_success_pct=target_success_pct,
            total_queries=total_queries,
        )

        coverage_plan_provides_a_prioritized_path_to_improve_query_success_rate.additional_properties = d
        return coverage_plan_provides_a_prioritized_path_to_improve_query_success_rate

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
