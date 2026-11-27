from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="BlockerCount")


@_attrs_define
class BlockerCount:
    """BlockerCount is one named blocker of unresolved goals. None and unknown
    are reported beside this list, not as percentages.

        Attributes:
            blocker (str):
            unresolved_goals (int): UnresolvedGoals counts the unresolved goals this blocker stopped.
            drilldown (str | Unset): Drilldown is the clause of this bucket. To open it, send the same sources and
                (<request query>) AND <clause>, or the clause alone when the request query
                is empty; that selects exactly these goals.
    """

    blocker: str
    unresolved_goals: int
    drilldown: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocker = self.blocker

        unresolved_goals = self.unresolved_goals

        drilldown = self.drilldown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blocker": blocker,
                "unresolvedGoals": unresolved_goals,
            }
        )
        if drilldown is not UNSET:
            field_dict["drilldown"] = drilldown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        blocker = d.pop("blocker")

        unresolved_goals = d.pop("unresolvedGoals")

        drilldown = d.pop("drilldown", UNSET)

        blocker_count = cls(
            blocker=blocker,
            unresolved_goals=unresolved_goals,
            drilldown=drilldown,
        )

        blocker_count.additional_properties = d
        return blocker_count

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
