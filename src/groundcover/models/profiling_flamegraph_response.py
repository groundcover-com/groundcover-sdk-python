from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flame_node_contains_inclusive_and_self_weight_in_the_selected_sample_unit import (
        FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit,
    )
    from ..models.profiling_period import ProfilingPeriod
    from ..models.stack_counts_counts_aggregated_stacks_not_samples_or_rendered_tree_nodes import (
        StackCountsCountsAggregatedStacksNotSamplesOrRenderedTreeNodes,
    )


T = TypeVar("T", bound="ProfilingFlamegraphResponse")


@_attrs_define
class ProfilingFlamegraphResponse:
    """
    Attributes:
        filtered_value (float | Unset):
        period (ProfilingPeriod | Unset):
        profile_type (str | Unset):
        root (FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit | Unset):
        sample_type (str | Unset):
        stacks (StackCountsCountsAggregatedStacksNotSamplesOrRenderedTreeNodes | Unset):
        total (float | Unset):
        truncated (bool | Unset):
        unit (str | Unset):
    """

    filtered_value: float | Unset = UNSET
    period: ProfilingPeriod | Unset = UNSET
    profile_type: str | Unset = UNSET
    root: FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit | Unset = UNSET
    sample_type: str | Unset = UNSET
    stacks: StackCountsCountsAggregatedStacksNotSamplesOrRenderedTreeNodes | Unset = UNSET
    total: float | Unset = UNSET
    truncated: bool | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filtered_value = self.filtered_value

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        profile_type = self.profile_type

        root: dict[str, Any] | Unset = UNSET
        if not isinstance(self.root, Unset):
            root = self.root.to_dict()

        sample_type = self.sample_type

        stacks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stacks, Unset):
            stacks = self.stacks.to_dict()

        total = self.total

        truncated = self.truncated

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filtered_value is not UNSET:
            field_dict["filteredValue"] = filtered_value
        if period is not UNSET:
            field_dict["period"] = period
        if profile_type is not UNSET:
            field_dict["profileType"] = profile_type
        if root is not UNSET:
            field_dict["root"] = root
        if sample_type is not UNSET:
            field_dict["sampleType"] = sample_type
        if stacks is not UNSET:
            field_dict["stacks"] = stacks
        if total is not UNSET:
            field_dict["total"] = total
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flame_node_contains_inclusive_and_self_weight_in_the_selected_sample_unit import (
            FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit,
        )
        from ..models.profiling_period import ProfilingPeriod
        from ..models.stack_counts_counts_aggregated_stacks_not_samples_or_rendered_tree_nodes import (
            StackCountsCountsAggregatedStacksNotSamplesOrRenderedTreeNodes,
        )

        d = dict(src_dict)
        filtered_value = d.pop("filteredValue", UNSET)

        _period = d.pop("period", UNSET)
        period: ProfilingPeriod | Unset
        if isinstance(_period, Unset) or _period is None:
            period = UNSET
        else:
            period = ProfilingPeriod.from_dict(_period)

        profile_type = d.pop("profileType", UNSET)

        _root = d.pop("root", UNSET)
        root: FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit | Unset
        if isinstance(_root, Unset) or _root is None:
            root = UNSET
        else:
            root = FlameNodeContainsInclusiveAndSelfWeightInTheSelectedSampleUnit.from_dict(_root)

        sample_type = d.pop("sampleType", UNSET)

        _stacks = d.pop("stacks", UNSET)
        stacks: StackCountsCountsAggregatedStacksNotSamplesOrRenderedTreeNodes | Unset
        if isinstance(_stacks, Unset) or _stacks is None:
            stacks = UNSET
        else:
            stacks = StackCountsCountsAggregatedStacksNotSamplesOrRenderedTreeNodes.from_dict(_stacks)

        total = d.pop("total", UNSET)

        truncated = d.pop("truncated", UNSET)

        unit = d.pop("unit", UNSET)

        profiling_flamegraph_response = cls(
            filtered_value=filtered_value,
            period=period,
            profile_type=profile_type,
            root=root,
            sample_type=sample_type,
            stacks=stacks,
            total=total,
            truncated=truncated,
            unit=unit,
        )

        profiling_flamegraph_response.additional_properties = d
        return profiling_flamegraph_response

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
