from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_pipeline_defines_a_pipeline_for_search_queries import SqlPipelineDefinesAPipelineForSearchQueries


T = TypeVar("T", bound="UnionDefinesAUnionOperationBetweenTwoPipelinesUNIONALL")


@_attrs_define
class UnionDefinesAUnionOperationBetweenTwoPipelinesUNIONALL:
    """
    Attributes:
        left_pipeline (SqlPipelineDefinesAPipelineForSearchQueries | Unset): When Join is set, the pipeline acts as a
            container for the join operation ONLY.
            When Union is set, the pipeline acts as a container for the union operation ONLY.
            In these cases, no other fields should be used.
        right_pipeline (SqlPipelineDefinesAPipelineForSearchQueries | Unset): When Join is set, the pipeline acts as a
            container for the join operation ONLY.
            When Union is set, the pipeline acts as a container for the union operation ONLY.
            In these cases, no other fields should be used.
    """

    left_pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset = UNSET
    right_pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        left_pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.left_pipeline, Unset):
            left_pipeline = self.left_pipeline.to_dict()

        right_pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.right_pipeline, Unset):
            right_pipeline = self.right_pipeline.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left_pipeline is not UNSET:
            field_dict["leftPipeline"] = left_pipeline
        if right_pipeline is not UNSET:
            field_dict["rightPipeline"] = right_pipeline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        _right_pipeline = d.pop("rightPipeline", UNSET)
        right_pipeline: SqlPipelineDefinesAPipelineForSearchQueries | Unset
        if isinstance(_right_pipeline, Unset) or _right_pipeline is None:
            right_pipeline = UNSET
        else:
            right_pipeline = SqlPipelineDefinesAPipelineForSearchQueries.from_dict(_right_pipeline)

        union_defines_a_union_operation_between_two_pipelines_unionall = cls(
            left_pipeline=left_pipeline,
            right_pipeline=right_pipeline,
        )

        union_defines_a_union_operation_between_two_pipelines_unionall.additional_properties = d
        return union_defines_a_union_operation_between_two_pipelines_unionall

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
