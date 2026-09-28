from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_is_the_whole_expression_in_the_language_monitor_spec_type_implies import (
        QueryIsTheWholeExpressionInTheLanguageMonitorSpecTypeImplies,
    )
    from ..models.threshold_spec_is_one_condition_block_firing_is_its_only_arm_today import (
        ThresholdSpecIsOneConditionBlockFiringIsItsOnlyArmToday,
    )


T = TypeVar("T", bound="ModelWrapsTheSingleQueryAndTheThresholdsListCappedAtOneItem")


@_attrs_define
class ModelWrapsTheSingleQueryAndTheThresholdsListCappedAtOneItem:
    """
    Attributes:
        query (QueryIsTheWholeExpressionInTheLanguageMonitorSpecTypeImplies | Unset):
        thresholds (list[ThresholdSpecIsOneConditionBlockFiringIsItsOnlyArmToday] | Unset):
    """

    query: QueryIsTheWholeExpressionInTheLanguageMonitorSpecTypeImplies | Unset = UNSET
    thresholds: list[ThresholdSpecIsOneConditionBlockFiringIsItsOnlyArmToday] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        thresholds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.thresholds, Unset):
            thresholds = []
            for thresholds_item_data in self.thresholds:
                thresholds_item = thresholds_item_data.to_dict()
                thresholds.append(thresholds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if thresholds is not UNSET:
            field_dict["thresholds"] = thresholds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_is_the_whole_expression_in_the_language_monitor_spec_type_implies import (
            QueryIsTheWholeExpressionInTheLanguageMonitorSpecTypeImplies,
        )
        from ..models.threshold_spec_is_one_condition_block_firing_is_its_only_arm_today import (
            ThresholdSpecIsOneConditionBlockFiringIsItsOnlyArmToday,
        )

        d = dict(src_dict)
        _query = d.pop("query", UNSET)
        query: QueryIsTheWholeExpressionInTheLanguageMonitorSpecTypeImplies | Unset
        if isinstance(_query, Unset) or _query is None:
            query = UNSET
        else:
            query = QueryIsTheWholeExpressionInTheLanguageMonitorSpecTypeImplies.from_dict(_query)

        _thresholds = d.pop("thresholds", UNSET)
        thresholds: list[ThresholdSpecIsOneConditionBlockFiringIsItsOnlyArmToday] | Unset = UNSET
        if _thresholds is not UNSET:
            thresholds = []
            for thresholds_item_data in _thresholds:
                thresholds_item = ThresholdSpecIsOneConditionBlockFiringIsItsOnlyArmToday.from_dict(
                    thresholds_item_data
                )

                thresholds.append(thresholds_item)

        model_wraps_the_single_query_and_the_thresholds_list_capped_at_one_item = cls(
            query=query,
            thresholds=thresholds,
        )

        model_wraps_the_single_query_and_the_thresholds_list_capped_at_one_item.additional_properties = d
        return model_wraps_the_single_query_and_the_thresholds_list_capped_at_one_item

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
