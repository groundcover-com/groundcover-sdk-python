from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="EvaluatedAssetIsOneAssetsEvaluationOutcome")


@_attrs_define
class EvaluatedAssetIsOneAssetsEvaluationOutcome:
    """
    Attributes:
        applied_written (int | Unset): Of those, findings a tenant mapping rule had already resolved.
        asset_id (str | Unset):
        asset_type (str | Unset):
        evaluated_units (int | Unset): Units the asset was checked as: 1 for a monitor, the data widgets of a dashboard.
        findings_written (int | Unset): Findings and warnings stored for the asset. Zero when persist is false.
        name (str | Unset):
        source_resource_id (str | Unset):
    """

    applied_written: int | Unset = UNSET
    asset_id: str | Unset = UNSET
    asset_type: str | Unset = UNSET
    evaluated_units: int | Unset = UNSET
    findings_written: int | Unset = UNSET
    name: str | Unset = UNSET
    source_resource_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_written = self.applied_written

        asset_id = self.asset_id

        asset_type = self.asset_type

        evaluated_units = self.evaluated_units

        findings_written = self.findings_written

        name = self.name

        source_resource_id = self.source_resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_written is not UNSET:
            field_dict["applied_written"] = applied_written
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if evaluated_units is not UNSET:
            field_dict["evaluated_units"] = evaluated_units
        if findings_written is not UNSET:
            field_dict["findings_written"] = findings_written
        if name is not UNSET:
            field_dict["name"] = name
        if source_resource_id is not UNSET:
            field_dict["source_resource_id"] = source_resource_id

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
        applied_written = d.pop("applied_written", UNSET)

        asset_id = d.pop("asset_id", UNSET)

        asset_type = d.pop("asset_type", UNSET)

        evaluated_units = d.pop("evaluated_units", UNSET)

        findings_written = d.pop("findings_written", UNSET)

        name = d.pop("name", UNSET)

        source_resource_id = d.pop("source_resource_id", UNSET)

        evaluated_asset_is_one_assets_evaluation_outcome = cls(
            applied_written=applied_written,
            asset_id=asset_id,
            asset_type=asset_type,
            evaluated_units=evaluated_units,
            findings_written=findings_written,
            name=name,
            source_resource_id=source_resource_id,
        )

        evaluated_asset_is_one_assets_evaluation_outcome.additional_properties = d
        return evaluated_asset_is_one_assets_evaluation_outcome

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
