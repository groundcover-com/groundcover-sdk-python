from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_summary_response_item import AssetSummaryResponseItem


T = TypeVar("T", bound="AssetsSummaryResponse")


@_attrs_define
class AssetsSummaryResponse:
    """
    Attributes:
        summary (list[AssetSummaryResponseItem] | Unset): Summary statistics grouped by asset type.
    """

    summary: list[AssetSummaryResponseItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = []
            for summary_item_data in self.summary:
                summary_item = summary_item_data.to_dict()
                summary.append(summary_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_summary_response_item import AssetSummaryResponseItem

        d = dict(src_dict)
        _summary = d.pop("summary", UNSET)
        summary: list[AssetSummaryResponseItem] | Unset = UNSET
        if _summary is not UNSET:
            summary = []
            for summary_item_data in _summary:
                summary_item = AssetSummaryResponseItem.from_dict(summary_item_data)

                summary.append(summary_item)

        assets_summary_response = cls(
            summary=summary,
        )

        assets_summary_response.additional_properties = d
        return assets_summary_response

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
