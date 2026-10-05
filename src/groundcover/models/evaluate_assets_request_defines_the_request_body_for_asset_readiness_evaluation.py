from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="EvaluateAssetsRequestDefinesTheRequestBodyForAssetReadinessEvaluation")


@_attrs_define
class EvaluateAssetsRequestDefinesTheRequestBodyForAssetReadinessEvaluation:
    """
    Attributes:
        asset_ids (list[str] | Unset): Restrict evaluation to these source_resource_id values. Optional: empty means all
            assets.
        asset_types (list[str] | Unset): Asset types to evaluate. Optional: defaults to ["monitors", "dashboards"].
        limit (int | Unset): Caps the number of assets evaluated (after asset_ids filtering): converted assets first,
            then
            skipped ones fill what is left. 0 means unlimited.
        monitor_lookback (str | Unset): Lookback window for monitor wet queries, as a Go duration string. Optional:
            defaults to "168h".
        persist (bool | Unset): Stores each asset's findings and evaluation. When false nothing is written and the
            response
            only reports what was evaluated. Optional: defaults to true.
        wet (bool | Unset): Executes every converted query against the tenant's data and stores the no-data
            warnings. Readiness does not depend on it. Optional: defaults to false.
    """

    asset_ids: list[str] | Unset = UNSET
    asset_types: list[str] | Unset = UNSET
    limit: int | Unset = UNSET
    monitor_lookback: str | Unset = UNSET
    persist: bool | Unset = UNSET
    wet: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids: list[str] | Unset = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        asset_types: list[str] | Unset = UNSET
        if not isinstance(self.asset_types, Unset):
            asset_types = self.asset_types

        limit = self.limit

        monitor_lookback = self.monitor_lookback

        persist = self.persist

        wet = self.wet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_ids is not UNSET:
            field_dict["asset_ids"] = asset_ids
        if asset_types is not UNSET:
            field_dict["asset_types"] = asset_types
        if limit is not UNSET:
            field_dict["limit"] = limit
        if monitor_lookback is not UNSET:
            field_dict["monitor_lookback"] = monitor_lookback
        if persist is not UNSET:
            field_dict["persist"] = persist
        if wet is not UNSET:
            field_dict["wet"] = wet

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
        asset_ids = cast(list[str], d.pop("asset_ids", UNSET))

        asset_types = cast(list[str], d.pop("asset_types", UNSET))

        limit = d.pop("limit", UNSET)

        monitor_lookback = d.pop("monitor_lookback", UNSET)

        persist = d.pop("persist", UNSET)

        wet = d.pop("wet", UNSET)

        evaluate_assets_request_defines_the_request_body_for_asset_readiness_evaluation = cls(
            asset_ids=asset_ids,
            asset_types=asset_types,
            limit=limit,
            monitor_lookback=monitor_lookback,
            persist=persist,
            wet=wet,
        )

        evaluate_assets_request_defines_the_request_body_for_asset_readiness_evaluation.additional_properties = d
        return evaluate_assets_request_defines_the_request_body_for_asset_readiness_evaluation

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
