from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pattern_data_additional_columns import PatternDataAdditionalColumns
    from ..models.sample_pair import SamplePair


T = TypeVar("T", bound="PatternData")


@_attrs_define
class PatternData:
    """
    Attributes:
        additional_columns (PatternDataAdditionalColumns | Unset):
        count (int | Unset):
        level (str | Unset):
        pattern (str | Unset):
        pattern_id (int | Unset):
        trend (list[SamplePair] | Unset):
        workload (str | Unset):
    """

    additional_columns: PatternDataAdditionalColumns | Unset = UNSET
    count: int | Unset = UNSET
    level: str | Unset = UNSET
    pattern: str | Unset = UNSET
    pattern_id: int | Unset = UNSET
    trend: list[SamplePair] | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_columns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_columns, Unset):
            additional_columns = self.additional_columns.to_dict()

        count = self.count

        level = self.level

        pattern = self.pattern

        pattern_id = self.pattern_id

        trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.trend, Unset):
            trend = []
            for trend_item_data in self.trend:
                trend_item = trend_item_data.to_dict()
                trend.append(trend_item)

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_columns is not UNSET:
            field_dict["additionalColumns"] = additional_columns
        if count is not UNSET:
            field_dict["count"] = count
        if level is not UNSET:
            field_dict["level"] = level
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if pattern_id is not UNSET:
            field_dict["patternId"] = pattern_id
        if trend is not UNSET:
            field_dict["trend"] = trend
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pattern_data_additional_columns import PatternDataAdditionalColumns
        from ..models.sample_pair import SamplePair

        d = dict(src_dict)
        _additional_columns = d.pop("additionalColumns", UNSET)
        additional_columns: PatternDataAdditionalColumns | Unset
        if isinstance(_additional_columns, Unset) or _additional_columns is None:
            additional_columns = UNSET
        else:
            additional_columns = PatternDataAdditionalColumns.from_dict(_additional_columns)

        count = d.pop("count", UNSET)

        level = d.pop("level", UNSET)

        pattern = d.pop("pattern", UNSET)

        pattern_id = d.pop("patternId", UNSET)

        _trend = d.pop("trend", UNSET)
        trend: list[SamplePair] | Unset = UNSET
        if _trend is not UNSET:
            trend = []
            for trend_item_data in _trend:
                trend_item = SamplePair.from_dict(trend_item_data)

                trend.append(trend_item)

        workload = d.pop("workload", UNSET)

        pattern_data = cls(
            additional_columns=additional_columns,
            count=count,
            level=level,
            pattern=pattern,
            pattern_id=pattern_id,
            trend=trend,
            workload=workload,
        )

        pattern_data.additional_properties = d
        return pattern_data

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
