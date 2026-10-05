from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wet_summary_counts_summarizes_the_wet_mode_execution_pass_if_any import (
        WetSummaryCountsSummarizesTheWetModeExecutionPassIfAny,
    )


T = TypeVar("T", bound="EvaluateAssetsSummaryIsTheResponsesTopLevelRollup")


@_attrs_define
class EvaluateAssetsSummaryIsTheResponsesTopLevelRollup:
    """
    Attributes:
        assets_evaluated (int | Unset):
        wet (WetSummaryCountsSummarizesTheWetModeExecutionPassIfAny | Unset):
    """

    assets_evaluated: int | Unset = UNSET
    wet: WetSummaryCountsSummarizesTheWetModeExecutionPassIfAny | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets_evaluated = self.assets_evaluated

        wet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wet, Unset):
            wet = self.wet.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets_evaluated is not UNSET:
            field_dict["assets_evaluated"] = assets_evaluated
        if wet is not UNSET:
            field_dict["wet"] = wet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wet_summary_counts_summarizes_the_wet_mode_execution_pass_if_any import (
            WetSummaryCountsSummarizesTheWetModeExecutionPassIfAny,
        )

        d = dict(src_dict)
        assets_evaluated = d.pop("assets_evaluated", UNSET)

        _wet = d.pop("wet", UNSET)
        wet: WetSummaryCountsSummarizesTheWetModeExecutionPassIfAny | Unset
        if isinstance(_wet, Unset) or _wet is None:
            wet = UNSET
        else:
            wet = WetSummaryCountsSummarizesTheWetModeExecutionPassIfAny.from_dict(_wet)

        evaluate_assets_summary_is_the_responses_top_level_rollup = cls(
            assets_evaluated=assets_evaluated,
            wet=wet,
        )

        evaluate_assets_summary_is_the_responses_top_level_rollup.additional_properties = d
        return evaluate_assets_summary_is_the_responses_top_level_rollup

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
