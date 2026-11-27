from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.blocker_count import BlockerCount
    from ..models.sentiment_point import SentimentPoint


T = TypeVar("T", bound="InsightsCharts")


@_attrs_define
class InsightsCharts:
    """InsightsCharts is blockers and end sentiment over time. Sentiment has one
    point for each bucket of the window, in time order, also for a bucket
    without goals.

        Attributes:
            blockers (list[BlockerCount]):
            sentiment (list[SentimentPoint]):
            unresolved_none (int):
            unresolved_unknown (int):
    """

    blockers: list[BlockerCount]
    sentiment: list[SentimentPoint]
    unresolved_none: int
    unresolved_unknown: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blockers = []
        for blockers_item_data in self.blockers:
            blockers_item = blockers_item_data.to_dict()
            blockers.append(blockers_item)

        sentiment = []
        for sentiment_item_data in self.sentiment:
            sentiment_item = sentiment_item_data.to_dict()
            sentiment.append(sentiment_item)

        unresolved_none = self.unresolved_none

        unresolved_unknown = self.unresolved_unknown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blockers": blockers,
                "sentiment": sentiment,
                "unresolvedNone": unresolved_none,
                "unresolvedUnknown": unresolved_unknown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blocker_count import BlockerCount
        from ..models.sentiment_point import SentimentPoint

        d = dict(src_dict)
        blockers = []
        _blockers = d.pop("blockers")
        for blockers_item_data in _blockers:
            blockers_item = BlockerCount.from_dict(blockers_item_data)

            blockers.append(blockers_item)

        sentiment = []
        _sentiment = d.pop("sentiment")
        for sentiment_item_data in _sentiment:
            sentiment_item = SentimentPoint.from_dict(sentiment_item_data)

            sentiment.append(sentiment_item)

        unresolved_none = d.pop("unresolvedNone")

        unresolved_unknown = d.pop("unresolvedUnknown")

        insights_charts = cls(
            blockers=blockers,
            sentiment=sentiment,
            unresolved_none=unresolved_none,
            unresolved_unknown=unresolved_unknown,
        )

        insights_charts.additional_properties = d
        return insights_charts

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
