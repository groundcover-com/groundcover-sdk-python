from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_install_result_status import AssetInstallResultStatus
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AssetInstallResult")


@_attrs_define
class AssetInstallResult:
    """
    Attributes:
        name (str): The name of the asset.
        source_resource_id (str): The source resource ID from the provider.
        status (AssetInstallResultStatus): The status of the installation.
        error (str | Unset): Error message if the installation failed.
        gc_resource_id (str | Unset): The groundcover resource ID if successfully installed.
    """

    name: str
    source_resource_id: str
    status: AssetInstallResultStatus
    error: str | Unset = UNSET
    gc_resource_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        source_resource_id = self.source_resource_id

        status = self.status.value

        error = self.error

        gc_resource_id = self.gc_resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "sourceResourceId": source_resource_id,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if gc_resource_id is not UNSET:
            field_dict["gcResourceId"] = gc_resource_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        name = d.pop("name")

        source_resource_id = d.pop("sourceResourceId")

        status = AssetInstallResultStatus(d.pop("status"))

        error = d.pop("error", UNSET)

        gc_resource_id = d.pop("gcResourceId", UNSET)

        asset_install_result = cls(
            name=name,
            source_resource_id=source_resource_id,
            status=status,
            error=error,
            gc_resource_id=gc_resource_id,
        )

        asset_install_result.additional_properties = d
        return asset_install_result

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
