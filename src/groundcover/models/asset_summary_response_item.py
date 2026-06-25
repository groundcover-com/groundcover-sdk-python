from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AssetSummaryResponseItem")


@_attrs_define
class AssetSummaryResponseItem:
    """
    Attributes:
        asset_type (str | Unset): The type of asset (e.g., "monitors").
        installed_total (int | Unset): Total number of installed assets.
        pending_total (int | Unset): Total number of assets pending conversion.
        source_total (int | Unset): Total number of unique assets from the source.
        supported_total (int | Unset): Total number of supported assets (full or partial support).
        unsupported_total (int | Unset): Total number of unsupported assets.
    """

    asset_type: str | Unset = UNSET
    installed_total: int | Unset = UNSET
    pending_total: int | Unset = UNSET
    source_total: int | Unset = UNSET
    supported_total: int | Unset = UNSET
    unsupported_total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_type = self.asset_type

        installed_total = self.installed_total

        pending_total = self.pending_total

        source_total = self.source_total

        supported_total = self.supported_total

        unsupported_total = self.unsupported_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if installed_total is not UNSET:
            field_dict["installed_total"] = installed_total
        if pending_total is not UNSET:
            field_dict["pending_total"] = pending_total
        if source_total is not UNSET:
            field_dict["source_total"] = source_total
        if supported_total is not UNSET:
            field_dict["supported_total"] = supported_total
        if unsupported_total is not UNSET:
            field_dict["unsupported_total"] = unsupported_total

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
        asset_type = d.pop("asset_type", UNSET)

        installed_total = d.pop("installed_total", UNSET)

        pending_total = d.pop("pending_total", UNSET)

        source_total = d.pop("source_total", UNSET)

        supported_total = d.pop("supported_total", UNSET)

        unsupported_total = d.pop("unsupported_total", UNSET)

        asset_summary_response_item = cls(
            asset_type=asset_type,
            installed_total=installed_total,
            pending_total=pending_total,
            source_total=source_total,
            supported_total=supported_total,
            unsupported_total=unsupported_total,
        )

        asset_summary_response_item.additional_properties = d
        return asset_summary_response_item

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
