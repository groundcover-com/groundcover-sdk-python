from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_create_monitors_v2_error import BatchCreateMonitorsV2Error


T = TypeVar("T", bound="BatchCreateMonitorsV2Response")


@_attrs_define
class BatchCreateMonitorsV2Response:
    """
    Attributes:
        created_count (int | Unset):
        created_uuids (list[str] | Unset): UUIDs minted for the created monitors, in request order.
        errors (list[BatchCreateMonitorsV2Error] | Unset):
        failed_count (int | Unset):
    """

    created_count: int | Unset = UNSET
    created_uuids: list[str] | Unset = UNSET
    errors: list[BatchCreateMonitorsV2Error] | Unset = UNSET
    failed_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_count = self.created_count

        created_uuids: list[str] | Unset = UNSET
        if not isinstance(self.created_uuids, Unset):
            created_uuids = self.created_uuids

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        failed_count = self.failed_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_count is not UNSET:
            field_dict["createdCount"] = created_count
        if created_uuids is not UNSET:
            field_dict["createdUuids"] = created_uuids
        if errors is not UNSET:
            field_dict["errors"] = errors
        if failed_count is not UNSET:
            field_dict["failedCount"] = failed_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_create_monitors_v2_error import BatchCreateMonitorsV2Error

        d = dict(src_dict)
        created_count = d.pop("createdCount", UNSET)

        created_uuids = cast(list[str], d.pop("createdUuids", UNSET))

        _errors = d.pop("errors", UNSET)
        errors: list[BatchCreateMonitorsV2Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BatchCreateMonitorsV2Error.from_dict(errors_item_data)

                errors.append(errors_item)

        failed_count = d.pop("failedCount", UNSET)

        batch_create_monitors_v2_response = cls(
            created_count=created_count,
            created_uuids=created_uuids,
            errors=errors,
            failed_count=failed_count,
        )

        batch_create_monitors_v2_response.additional_properties = d
        return batch_create_monitors_v2_response

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
