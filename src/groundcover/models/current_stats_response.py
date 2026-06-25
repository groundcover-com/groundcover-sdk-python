from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ottl_stats_entry import OttlStatsEntry
    from ..models.total_stats import TotalStats


T = TypeVar("T", bound="CurrentStatsResponse")


@_attrs_define
class CurrentStatsResponse:
    """
    Attributes:
        stats (list[OttlStatsEntry] | Unset):
        total_stats (TotalStats | Unset):
    """

    stats: list[OttlStatsEntry] | Unset = UNSET
    total_stats: TotalStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        total_stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_stats, Unset):
            total_stats = self.total_stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stats is not UNSET:
            field_dict["stats"] = stats
        if total_stats is not UNSET:
            field_dict["totalStats"] = total_stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ottl_stats_entry import OttlStatsEntry
        from ..models.total_stats import TotalStats

        d = dict(src_dict)
        _stats = d.pop("stats", UNSET)
        stats: list[OttlStatsEntry] | Unset = UNSET
        if _stats is not UNSET:
            stats = []
            for stats_item_data in _stats:
                stats_item = OttlStatsEntry.from_dict(stats_item_data)

                stats.append(stats_item)

        _total_stats = d.pop("totalStats", UNSET)
        total_stats: TotalStats | Unset
        if isinstance(_total_stats, Unset) or _total_stats is None:
            total_stats = UNSET
        else:
            total_stats = TotalStats.from_dict(_total_stats)

        current_stats_response = cls(
            stats=stats,
            total_stats=total_stats,
        )

        current_stats_response.additional_properties = d
        return current_stats_response

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
