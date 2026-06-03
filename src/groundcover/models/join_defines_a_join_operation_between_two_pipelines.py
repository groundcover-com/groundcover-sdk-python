from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.join_condition_defines_how_tables_are_joined_together import (
        JoinConditionDefinesHowTablesAreJoinedTogether,
    )
    from ..models.sql_pipeline_defines_a_pipeline_for_search_queries import SqlPipelineDefinesAPipelineForSearchQueries


T = TypeVar("T", bound="JoinDefinesAJoinOperationBetweenTwoPipelines")


@_attrs_define
class JoinDefinesAJoinOperationBetweenTwoPipelines:
    """
    Attributes:
        left_pipeline (SqlPipelineDefinesAPipelineForSearchQueries | Unset): When Join is set, the pipeline acts as a
            container for the join operation ONLY.
            When Union is set, the pipeline acts as a container for the union operation ONLY.
            In these cases, no other fields should be used.
        on_conditions (list[JoinConditionDefinesHowTablesAreJoinedTogether] | Unset): OnConditions defines the join
            conditions
        prefix (str | Unset): Prefix, when set, disambiguates overlapping non-key columns from the right
            side of a join by prefixing them with the given string (e.g., setting prefix
            to "right" causes a right-side "level" column to appear as "right.level").
            Join key columns are not prefixed; they are coalesced into a single column.
        right_pipeline (SqlPipelineDefinesAPipelineForSearchQueries | Unset): When Join is set, the pipeline acts as a
            container for the join operation ONLY.
            When Union is set, the pipeline acts as a container for the union operation ONLY.
            In these cases, no other fields should be used.
        type_ (str | Unset):
    """

    left_pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset = UNSET
    on_conditions: list[JoinConditionDefinesHowTablesAreJoinedTogether] | Unset = UNSET
    prefix: str | Unset = UNSET
    right_pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        left_pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.left_pipeline, Unset):
            left_pipeline = self.left_pipeline.to_dict()

        on_conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.on_conditions, Unset):
            on_conditions = []
            for on_conditions_item_data in self.on_conditions:
                on_conditions_item = on_conditions_item_data.to_dict()
                on_conditions.append(on_conditions_item)

        prefix = self.prefix

        right_pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.right_pipeline, Unset):
            right_pipeline = self.right_pipeline.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left_pipeline is not UNSET:
            field_dict["leftPipeline"] = left_pipeline
        if on_conditions is not UNSET:
            field_dict["onConditions"] = on_conditions
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if right_pipeline is not UNSET:
            field_dict["rightPipeline"] = right_pipeline
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.join_condition_defines_how_tables_are_joined_together import (
            JoinConditionDefinesHowTablesAreJoinedTogether,
        )
        from ..models.sql_pipeline_defines_a_pipeline_for_search_queries import (
            SqlPipelineDefinesAPipelineForSearchQueries,
        )

        d = dict(src_dict)
        _left_pipeline = d.pop("leftPipeline", UNSET)
        left_pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset
        if isinstance(_left_pipeline, Unset) or _left_pipeline is None:
            left_pipeline = UNSET
        else:
            left_pipeline = SqlPipelineDefinesAPipelineForSearchQueries.from_dict(_left_pipeline)

        _on_conditions = d.pop("onConditions", UNSET)
        on_conditions: list[JoinConditionDefinesHowTablesAreJoinedTogether] | Unset = UNSET
        if _on_conditions is not UNSET:
            on_conditions = []
            for on_conditions_item_data in _on_conditions:
                on_conditions_item = JoinConditionDefinesHowTablesAreJoinedTogether.from_dict(on_conditions_item_data)

                on_conditions.append(on_conditions_item)

        prefix = d.pop("prefix", UNSET)

        _right_pipeline = d.pop("rightPipeline", UNSET)
        right_pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset
        if isinstance(_right_pipeline, Unset) or _right_pipeline is None:
            right_pipeline = UNSET
        else:
            right_pipeline = SqlPipelineDefinesAPipelineForSearchQueries.from_dict(_right_pipeline)

        type_ = d.pop("type", UNSET)

        join_defines_a_join_operation_between_two_pipelines = cls(
            left_pipeline=left_pipeline,
            on_conditions=on_conditions,
            prefix=prefix,
            right_pipeline=right_pipeline,
            type_=type_,
        )

        join_defines_a_join_operation_between_two_pipelines.additional_properties = d
        return join_defines_a_join_operation_between_two_pipelines

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
