from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evaluate_assets_summary_is_the_responses_top_level_rollup import (
        EvaluateAssetsSummaryIsTheResponsesTopLevelRollup,
    )
    from ..models.evaluated_asset_is_one_assets_evaluation_outcome import EvaluatedAssetIsOneAssetsEvaluationOutcome


T = TypeVar("T", bound="EvaluateAssetsResponseIsTheFullResponseOfTheEvaluateAssetsEndpoint")


@_attrs_define
class EvaluateAssetsResponseIsTheFullResponseOfTheEvaluateAssetsEndpoint:
    """
    Attributes:
        assets (list[EvaluatedAssetIsOneAssetsEvaluationOutcome] | Unset):
        evaluated_at (datetime.datetime | Unset):
        summary (EvaluateAssetsSummaryIsTheResponsesTopLevelRollup | Unset):
    """

    assets: list[EvaluatedAssetIsOneAssetsEvaluationOutcome] | Unset = UNSET
    evaluated_at: datetime.datetime | Unset = UNSET
    summary: EvaluateAssetsSummaryIsTheResponsesTopLevelRollup | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = assets_item_data.to_dict()
                assets.append(assets_item)

        evaluated_at: str | Unset = UNSET
        if not isinstance(self.evaluated_at, Unset):
            evaluated_at = self.evaluated_at.isoformat()

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if evaluated_at is not UNSET:
            field_dict["evaluated_at"] = evaluated_at
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evaluate_assets_summary_is_the_responses_top_level_rollup import (
            EvaluateAssetsSummaryIsTheResponsesTopLevelRollup,
        )
        from ..models.evaluated_asset_is_one_assets_evaluation_outcome import EvaluatedAssetIsOneAssetsEvaluationOutcome

        d = dict(src_dict)
        _assets = d.pop("assets", UNSET)
        assets: list[EvaluatedAssetIsOneAssetsEvaluationOutcome] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for assets_item_data in _assets:
                assets_item = EvaluatedAssetIsOneAssetsEvaluationOutcome.from_dict(assets_item_data)

                assets.append(assets_item)

        _evaluated_at = d.pop("evaluated_at", UNSET)
        evaluated_at: datetime.datetime | Unset
        if isinstance(_evaluated_at, Unset) or _evaluated_at is None:
            evaluated_at = UNSET
        else:
            evaluated_at = parse_datetime(_evaluated_at)

        _summary = d.pop("summary", UNSET)
        summary: EvaluateAssetsSummaryIsTheResponsesTopLevelRollup | Unset
        if isinstance(_summary, Unset) or _summary is None:
            summary = UNSET
        else:
            summary = EvaluateAssetsSummaryIsTheResponsesTopLevelRollup.from_dict(_summary)

        evaluate_assets_response_is_the_full_response_of_the_evaluate_assets_endpoint = cls(
            assets=assets,
            evaluated_at=evaluated_at,
            summary=summary,
        )

        evaluate_assets_response_is_the_full_response_of_the_evaluate_assets_endpoint.additional_properties = d
        return evaluate_assets_response_is_the_full_response_of_the_evaluate_assets_endpoint

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
