from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="OttlStatsEntry")


@_attrs_define
class OttlStatsEntry:
    """
    Attributes:
        avg_processing_time_seconds (float | Unset):
        cluster (str | Unset):
        condition_eval_error_percentage (float | Unset):
        condition_met_percentage (float | Unset):
        configuration_id (str | Unset):
        context_type (str | Unset):
        env (str | Unset):
        is_rule_disabled (bool | Unset):
        is_rule_valid (bool | Unset):
        logs_condition_met_rate (float | Unset):
        logs_dropped_percentage (float | Unset):
        logs_dropped_rate (float | Unset):
        logs_seen_rate (float | Unset): Calculated rate and percentage metrics
        logs_transformed_rate (float | Unset):
        max_processing_time_seconds (float | Unset):
        min_processing_time_seconds (float | Unset):
        rule_index (int | Unset):
        rule_name (str | Unset):
        rule_source (str | Unset):
        statement_exec_error_percentage (float | Unset):
        total_condition_eval_errors_count (int | Unset):
        total_condition_met_count (int | Unset):
        total_logs_dropped (int | Unset):
        total_logs_seen (int | Unset): Aggregated count metrics
        total_logs_transformed (int | Unset):
        total_processing_time_seconds (float | Unset): Time-based metrics
        total_statement_exec_errors_count (int | Unset):
    """

    avg_processing_time_seconds: float | Unset = UNSET
    cluster: str | Unset = UNSET
    condition_eval_error_percentage: float | Unset = UNSET
    condition_met_percentage: float | Unset = UNSET
    configuration_id: str | Unset = UNSET
    context_type: str | Unset = UNSET
    env: str | Unset = UNSET
    is_rule_disabled: bool | Unset = UNSET
    is_rule_valid: bool | Unset = UNSET
    logs_condition_met_rate: float | Unset = UNSET
    logs_dropped_percentage: float | Unset = UNSET
    logs_dropped_rate: float | Unset = UNSET
    logs_seen_rate: float | Unset = UNSET
    logs_transformed_rate: float | Unset = UNSET
    max_processing_time_seconds: float | Unset = UNSET
    min_processing_time_seconds: float | Unset = UNSET
    rule_index: int | Unset = UNSET
    rule_name: str | Unset = UNSET
    rule_source: str | Unset = UNSET
    statement_exec_error_percentage: float | Unset = UNSET
    total_condition_eval_errors_count: int | Unset = UNSET
    total_condition_met_count: int | Unset = UNSET
    total_logs_dropped: int | Unset = UNSET
    total_logs_seen: int | Unset = UNSET
    total_logs_transformed: int | Unset = UNSET
    total_processing_time_seconds: float | Unset = UNSET
    total_statement_exec_errors_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_processing_time_seconds = self.avg_processing_time_seconds

        cluster = self.cluster

        condition_eval_error_percentage = self.condition_eval_error_percentage

        condition_met_percentage = self.condition_met_percentage

        configuration_id = self.configuration_id

        context_type = self.context_type

        env = self.env

        is_rule_disabled = self.is_rule_disabled

        is_rule_valid = self.is_rule_valid

        logs_condition_met_rate = self.logs_condition_met_rate

        logs_dropped_percentage = self.logs_dropped_percentage

        logs_dropped_rate = self.logs_dropped_rate

        logs_seen_rate = self.logs_seen_rate

        logs_transformed_rate = self.logs_transformed_rate

        max_processing_time_seconds = self.max_processing_time_seconds

        min_processing_time_seconds = self.min_processing_time_seconds

        rule_index = self.rule_index

        rule_name = self.rule_name

        rule_source = self.rule_source

        statement_exec_error_percentage = self.statement_exec_error_percentage

        total_condition_eval_errors_count = self.total_condition_eval_errors_count

        total_condition_met_count = self.total_condition_met_count

        total_logs_dropped = self.total_logs_dropped

        total_logs_seen = self.total_logs_seen

        total_logs_transformed = self.total_logs_transformed

        total_processing_time_seconds = self.total_processing_time_seconds

        total_statement_exec_errors_count = self.total_statement_exec_errors_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_processing_time_seconds is not UNSET:
            field_dict["avgProcessingTimeSeconds"] = avg_processing_time_seconds
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if condition_eval_error_percentage is not UNSET:
            field_dict["conditionEvalErrorPercentage"] = condition_eval_error_percentage
        if condition_met_percentage is not UNSET:
            field_dict["conditionMetPercentage"] = condition_met_percentage
        if configuration_id is not UNSET:
            field_dict["configurationID"] = configuration_id
        if context_type is not UNSET:
            field_dict["contextType"] = context_type
        if env is not UNSET:
            field_dict["env"] = env
        if is_rule_disabled is not UNSET:
            field_dict["isRuleDisabled"] = is_rule_disabled
        if is_rule_valid is not UNSET:
            field_dict["isRuleValid"] = is_rule_valid
        if logs_condition_met_rate is not UNSET:
            field_dict["logsConditionMetRate"] = logs_condition_met_rate
        if logs_dropped_percentage is not UNSET:
            field_dict["logsDroppedPercentage"] = logs_dropped_percentage
        if logs_dropped_rate is not UNSET:
            field_dict["logsDroppedRate"] = logs_dropped_rate
        if logs_seen_rate is not UNSET:
            field_dict["logsSeenRate"] = logs_seen_rate
        if logs_transformed_rate is not UNSET:
            field_dict["logsTransformedRate"] = logs_transformed_rate
        if max_processing_time_seconds is not UNSET:
            field_dict["maxProcessingTimeSeconds"] = max_processing_time_seconds
        if min_processing_time_seconds is not UNSET:
            field_dict["minProcessingTimeSeconds"] = min_processing_time_seconds
        if rule_index is not UNSET:
            field_dict["ruleIndex"] = rule_index
        if rule_name is not UNSET:
            field_dict["ruleName"] = rule_name
        if rule_source is not UNSET:
            field_dict["ruleSource"] = rule_source
        if statement_exec_error_percentage is not UNSET:
            field_dict["statementExecErrorPercentage"] = statement_exec_error_percentage
        if total_condition_eval_errors_count is not UNSET:
            field_dict["totalConditionEvalErrorsCount"] = total_condition_eval_errors_count
        if total_condition_met_count is not UNSET:
            field_dict["totalConditionMetCount"] = total_condition_met_count
        if total_logs_dropped is not UNSET:
            field_dict["totalLogsDropped"] = total_logs_dropped
        if total_logs_seen is not UNSET:
            field_dict["totalLogsSeen"] = total_logs_seen
        if total_logs_transformed is not UNSET:
            field_dict["totalLogsTransformed"] = total_logs_transformed
        if total_processing_time_seconds is not UNSET:
            field_dict["totalProcessingTimeSeconds"] = total_processing_time_seconds
        if total_statement_exec_errors_count is not UNSET:
            field_dict["totalStatementExecErrorsCount"] = total_statement_exec_errors_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        avg_processing_time_seconds = d.pop("avgProcessingTimeSeconds", UNSET)

        cluster = d.pop("cluster", UNSET)

        condition_eval_error_percentage = d.pop("conditionEvalErrorPercentage", UNSET)

        condition_met_percentage = d.pop("conditionMetPercentage", UNSET)

        configuration_id = d.pop("configurationID", UNSET)

        context_type = d.pop("contextType", UNSET)

        env = d.pop("env", UNSET)

        is_rule_disabled = d.pop("isRuleDisabled", UNSET)

        is_rule_valid = d.pop("isRuleValid", UNSET)

        logs_condition_met_rate = d.pop("logsConditionMetRate", UNSET)

        logs_dropped_percentage = d.pop("logsDroppedPercentage", UNSET)

        logs_dropped_rate = d.pop("logsDroppedRate", UNSET)

        logs_seen_rate = d.pop("logsSeenRate", UNSET)

        logs_transformed_rate = d.pop("logsTransformedRate", UNSET)

        max_processing_time_seconds = d.pop("maxProcessingTimeSeconds", UNSET)

        min_processing_time_seconds = d.pop("minProcessingTimeSeconds", UNSET)

        rule_index = d.pop("ruleIndex", UNSET)

        rule_name = d.pop("ruleName", UNSET)

        rule_source = d.pop("ruleSource", UNSET)

        statement_exec_error_percentage = d.pop("statementExecErrorPercentage", UNSET)

        total_condition_eval_errors_count = d.pop("totalConditionEvalErrorsCount", UNSET)

        total_condition_met_count = d.pop("totalConditionMetCount", UNSET)

        total_logs_dropped = d.pop("totalLogsDropped", UNSET)

        total_logs_seen = d.pop("totalLogsSeen", UNSET)

        total_logs_transformed = d.pop("totalLogsTransformed", UNSET)

        total_processing_time_seconds = d.pop("totalProcessingTimeSeconds", UNSET)

        total_statement_exec_errors_count = d.pop("totalStatementExecErrorsCount", UNSET)

        ottl_stats_entry = cls(
            avg_processing_time_seconds=avg_processing_time_seconds,
            cluster=cluster,
            condition_eval_error_percentage=condition_eval_error_percentage,
            condition_met_percentage=condition_met_percentage,
            configuration_id=configuration_id,
            context_type=context_type,
            env=env,
            is_rule_disabled=is_rule_disabled,
            is_rule_valid=is_rule_valid,
            logs_condition_met_rate=logs_condition_met_rate,
            logs_dropped_percentage=logs_dropped_percentage,
            logs_dropped_rate=logs_dropped_rate,
            logs_seen_rate=logs_seen_rate,
            logs_transformed_rate=logs_transformed_rate,
            max_processing_time_seconds=max_processing_time_seconds,
            min_processing_time_seconds=min_processing_time_seconds,
            rule_index=rule_index,
            rule_name=rule_name,
            rule_source=rule_source,
            statement_exec_error_percentage=statement_exec_error_percentage,
            total_condition_eval_errors_count=total_condition_eval_errors_count,
            total_condition_met_count=total_condition_met_count,
            total_logs_dropped=total_logs_dropped,
            total_logs_seen=total_logs_seen,
            total_logs_transformed=total_logs_transformed,
            total_processing_time_seconds=total_processing_time_seconds,
            total_statement_exec_errors_count=total_statement_exec_errors_count,
        )

        ottl_stats_entry.additional_properties = d
        return ottl_stats_entry

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
