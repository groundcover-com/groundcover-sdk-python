from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AssetFetchResult")


@_attrs_define
class AssetFetchResult:
    """
    Attributes:
        error_code (str | Unset): Error code if the fetch failed (e.g., "RATE_LIMITED", "UNAUTHORIZED").
        error_message (str | Unset): Error message if the fetch failed.
        fetched_assets (int | Unset): The number of assets fetched.
        required_permissions (list[str] | Unset): Required permissions for this asset type when fetch fails due to
            missing scopes.
        skip_reason (str | Unset): SkipReason explains why the asset type was skipped (status and message).
        skipped (bool | Unset): Skipped is true when the entire asset type was skipped because its list
            endpoint reported the type as absent (404). The run still succeeds. A
            missing scope (403) is reported as a failure with RequiredPermissions
            instead, not as a skip.
        skipped_assets (int | Unset): The number of individual assets skipped during fetch (e.g., a private
            dashboard the Application Key cannot read).
        status (str | Unset): The status of the fetch operation ("success" or "failed").
        type_ (str | Unset): The type of asset (e.g., "monitors").
    """

    error_code: str | Unset = UNSET
    error_message: str | Unset = UNSET
    fetched_assets: int | Unset = UNSET
    required_permissions: list[str] | Unset = UNSET
    skip_reason: str | Unset = UNSET
    skipped: bool | Unset = UNSET
    skipped_assets: int | Unset = UNSET
    status: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        error_message = self.error_message

        fetched_assets = self.fetched_assets

        required_permissions: list[str] | Unset = UNSET
        if not isinstance(self.required_permissions, Unset):
            required_permissions = self.required_permissions

        skip_reason = self.skip_reason

        skipped = self.skipped

        skipped_assets = self.skipped_assets

        status = self.status

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if fetched_assets is not UNSET:
            field_dict["fetchedAssets"] = fetched_assets
        if required_permissions is not UNSET:
            field_dict["requiredPermissions"] = required_permissions
        if skip_reason is not UNSET:
            field_dict["skipReason"] = skip_reason
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if skipped_assets is not UNSET:
            field_dict["skippedAssets"] = skipped_assets
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

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
        error_code = d.pop("errorCode", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        fetched_assets = d.pop("fetchedAssets", UNSET)

        required_permissions = cast(list[str], d.pop("requiredPermissions", UNSET))

        skip_reason = d.pop("skipReason", UNSET)

        skipped = d.pop("skipped", UNSET)

        skipped_assets = d.pop("skippedAssets", UNSET)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        asset_fetch_result = cls(
            error_code=error_code,
            error_message=error_message,
            fetched_assets=fetched_assets,
            required_permissions=required_permissions,
            skip_reason=skip_reason,
            skipped=skipped,
            skipped_assets=skipped_assets,
            status=status,
            type_=type_,
        )

        asset_fetch_result.additional_properties = d
        return asset_fetch_result

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
