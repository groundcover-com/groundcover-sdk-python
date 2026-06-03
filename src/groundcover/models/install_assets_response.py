from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_install_result import AssetInstallResult


T = TypeVar("T", bound="InstallAssetsResponse")


@_attrs_define
class InstallAssetsResponse:
    """
    Attributes:
        already_installed_count (int | Unset): The number of assets that were already installed.
        failed_count (int | Unset): The number of assets that failed to install.
        installed_count (int | Unset): The number of assets successfully installed.
        not_convertible_count (int | Unset): The number of assets that were not convertible.
        not_found_count (int | Unset): The number of assets that were not found.
        results (list[AssetInstallResult] | Unset): Detailed results for each asset.
    """

    already_installed_count: int | Unset = UNSET
    failed_count: int | Unset = UNSET
    installed_count: int | Unset = UNSET
    not_convertible_count: int | Unset = UNSET
    not_found_count: int | Unset = UNSET
    results: list[AssetInstallResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        already_installed_count = self.already_installed_count

        failed_count = self.failed_count

        installed_count = self.installed_count

        not_convertible_count = self.not_convertible_count

        not_found_count = self.not_found_count

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if already_installed_count is not UNSET:
            field_dict["alreadyInstalledCount"] = already_installed_count
        if failed_count is not UNSET:
            field_dict["failedCount"] = failed_count
        if installed_count is not UNSET:
            field_dict["installedCount"] = installed_count
        if not_convertible_count is not UNSET:
            field_dict["notConvertibleCount"] = not_convertible_count
        if not_found_count is not UNSET:
            field_dict["notFoundCount"] = not_found_count
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_install_result import AssetInstallResult

        d = dict(src_dict)
        already_installed_count = d.pop("alreadyInstalledCount", UNSET)

        failed_count = d.pop("failedCount", UNSET)

        installed_count = d.pop("installedCount", UNSET)

        not_convertible_count = d.pop("notConvertibleCount", UNSET)

        not_found_count = d.pop("notFoundCount", UNSET)

        _results = d.pop("results", UNSET)
        results: list[AssetInstallResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = AssetInstallResult.from_dict(results_item_data)

                results.append(results_item)

        install_assets_response = cls(
            already_installed_count=already_installed_count,
            failed_count=failed_count,
            installed_count=installed_count,
            not_convertible_count=not_convertible_count,
            not_found_count=not_found_count,
            results=results,
        )

        install_assets_response.additional_properties = d
        return install_assets_response

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
