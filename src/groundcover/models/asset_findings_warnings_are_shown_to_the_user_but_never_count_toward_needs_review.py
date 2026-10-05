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


T = TypeVar("T", bound="AssetFindingsWarningsAreShownToTheUserButNeverCountTowardNeedsReview")


@_attrs_define
class AssetFindingsWarningsAreShownToTheUserButNeverCountTowardNeedsReview:
    """
    Attributes:
        no_data (list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset):
    """

    no_data: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.no_data, Unset):
            no_data = []
            for no_data_item_data in self.no_data:
                no_data_item = no_data_item_data.to_dict()
                no_data.append(no_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_data is not UNSET:
            field_dict["no_data"] = no_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_finding_is_one_finding_or_warning_of_an_evaluated_asset import (
            AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset,
        )

        d = dict(src_dict)
        _no_data = d.pop("no_data", UNSET)
        no_data: list[AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset] | Unset = UNSET
        if _no_data is not UNSET:
            no_data = []
            for no_data_item_data in _no_data:
                no_data_item = AssetFindingIsOneFindingOrWarningOfAnEvaluatedAsset.from_dict(no_data_item_data)

                no_data.append(no_data_item)

        asset_findings_warnings_are_shown_to_the_user_but_never_count_toward_needs_review = cls(
            no_data=no_data,
        )

        asset_findings_warnings_are_shown_to_the_user_but_never_count_toward_needs_review.additional_properties = d
        return asset_findings_warnings_are_shown_to_the_user_but_never_count_toward_needs_review

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
