from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.insights_ratio_is_akpi_numerator_and_its_evaluable_count_always_present import (
        InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent,
    )


T = TypeVar("T", bound="SentimentPoint")


@_attrs_define
class SentimentPoint:
    """SentimentPoint is one chart bucket. A ratio has denominator 0 when the bucket
    has nothing to evaluate for it; unknown is counted outside that denominator.
    A bucket without goals has every count 0 and every ratio with denominator 0.

        Attributes:
            bucket (datetime.datetime):
            frustration (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could
                be evaluated, so there is no rate.
            mixed (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could be
                evaluated, so there is no rate.
            negative (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could be
                evaluated, so there is no rate.
            neutral (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could be
                evaluated, so there is no rate.
            positive (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could be
                evaluated, so there is no rate.
            satisfaction (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could
                be evaluated, so there is no rate.
            success (InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent): Denominator 0 means nothing could be
                evaluated, so there is no rate.
            unknown (int):
    """

    bucket: datetime.datetime
    frustration: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    mixed: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    negative: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    neutral: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    positive: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    satisfaction: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    success: InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent
    unknown: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket.isoformat()

        frustration = self.frustration.to_dict()

        mixed = self.mixed.to_dict()

        negative = self.negative.to_dict()

        neutral = self.neutral.to_dict()

        positive = self.positive.to_dict()

        satisfaction = self.satisfaction.to_dict()

        success = self.success.to_dict()

        unknown = self.unknown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "frustration": frustration,
                "mixed": mixed,
                "negative": negative,
                "neutral": neutral,
                "positive": positive,
                "satisfaction": satisfaction,
                "success": success,
                "unknown": unknown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insights_ratio_is_akpi_numerator_and_its_evaluable_count_always_present import (
            InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent,
        )

        d = dict(src_dict)
        bucket = parse_datetime(d.pop("bucket"))

        frustration = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("frustration"))

        mixed = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("mixed"))

        negative = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("negative"))

        neutral = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("neutral"))

        positive = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("positive"))

        satisfaction = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("satisfaction"))

        success = InsightsRatioIsAKPINumeratorAndItsEvaluableCountAlwaysPresent.from_dict(d.pop("success"))

        unknown = d.pop("unknown")

        sentiment_point = cls(
            bucket=bucket,
            frustration=frustration,
            mixed=mixed,
            negative=negative,
            neutral=neutral,
            positive=positive,
            satisfaction=satisfaction,
            success=success,
            unknown=unknown,
        )

        sentiment_point.additional_properties = d
        return sentiment_point

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
