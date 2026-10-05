from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_finding_is_one_finding_or_warning_of_an_evaluated_asset import (
        AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset,
    )


T = TypeVar("T", bound="AssetFindingsGroupsAreTheFindingsThatCountTowardNeedsReviewByType")


@_attrs_define
class AssetFindingsGroupsAreTheFindingsThatCountTowardNeedsReviewByType:
    """
    Attributes:
        missing_key (list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset):
        missing_metric (list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset):
        missing_value (list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset):
        not_supported (list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset):
    """

    missing_key: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
    missing_metric: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
    missing_value: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
    not_supported: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        missing_key: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.missing_key, Unset):
            missing_key = []
            for missing_key_item_data in self.missing_key:
                missing_key_item = missing_key_item_data.to_dict()
                missing_key.append(missing_key_item)

        missing_metric: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.missing_metric, Unset):
            missing_metric = []
            for missing_metric_item_data in self.missing_metric:
                missing_metric_item = missing_metric_item_data.to_dict()
                missing_metric.append(missing_metric_item)

        missing_value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.missing_value, Unset):
            missing_value = []
            for missing_value_item_data in self.missing_value:
                missing_value_item = missing_value_item_data.to_dict()
                missing_value.append(missing_value_item)

        not_supported: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.not_supported, Unset):
            not_supported = []
            for not_supported_item_data in self.not_supported:
                not_supported_item = not_supported_item_data.to_dict()
                not_supported.append(not_supported_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if missing_key is not UNSET:
            field_dict["missing_key"] = missing_key
        if missing_metric is not UNSET:
            field_dict["missing_metric"] = missing_metric
        if missing_value is not UNSET:
            field_dict["missing_value"] = missing_value
        if not_supported is not UNSET:
            field_dict["not_supported"] = not_supported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_finding_is_one_finding_or_warning_of_an_evaluated_asset import (
            AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset,
        )

        d = dict(src_dict)
        _missing_key = d.pop("missing_key", UNSET)
        missing_key: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
        if _missing_key is not UNSET:
            missing_key = []
            for missing_key_item_data in _missing_key:
                missing_key_item = AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset.from_dict(missing_key_item_data)

                missing_key.append(missing_key_item)

        _missing_metric = d.pop("missing_metric", UNSET)
        missing_metric: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
        if _missing_metric is not UNSET:
            missing_metric = []
            for missing_metric_item_data in _missing_metric:
                missing_metric_item = AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset.from_dict(
                    missing_metric_item_data
                )

                missing_metric.append(missing_metric_item)

        _missing_value = d.pop("missing_value", UNSET)
        missing_value: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
        if _missing_value is not UNSET:
            missing_value = []
            for missing_value_item_data in _missing_value:
                missing_value_item = AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset.from_dict(
                    missing_value_item_data
                )

                missing_value.append(missing_value_item)

        _not_supported = d.pop("not_supported", UNSET)
        not_supported: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
        if _not_supported is not UNSET:
            not_supported = []
            for not_supported_item_data in _not_supported:
                not_supported_item = AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset.from_dict(
                    not_supported_item_data
                )

                not_supported.append(not_supported_item)

        asset_findings_groups_are_the_findings_that_count_toward_needs_review_by_type = cls(
            missing_key=missing_key,
            missing_metric=missing_metric,
            missing_value=missing_value,
            not_supported=not_supported,
        )

        asset_findings_groups_are_the_findings_that_count_toward_needs_review_by_type.additional_properties = d
        return asset_findings_groups_are_the_findings_that_count_toward_needs_review_by_type

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
