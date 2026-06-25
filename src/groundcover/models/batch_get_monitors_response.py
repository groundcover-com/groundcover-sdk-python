from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_get_monitors_error import BatchGetMonitorsError
    from ..models.batch_get_monitors_response_monitors import BatchGetMonitorsResponseMonitors


T = TypeVar("T", bound="BatchGetMonitorsResponse")


@_attrs_define
class BatchGetMonitorsResponse:
    """
    Attributes:
        errors (list[BatchGetMonitorsError] | Unset):
        failed_count (int | Unset):
        fetched_count (int | Unset):
        monitors (BatchGetMonitorsResponseMonitors | Unset):
    """

    errors: list[BatchGetMonitorsError] | Unset = UNSET
    failed_count: int | Unset = UNSET
    fetched_count: int | Unset = UNSET
    monitors: BatchGetMonitorsResponseMonitors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        failed_count = self.failed_count

        fetched_count = self.fetched_count

        monitors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitors, Unset):
            monitors = self.monitors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if failed_count is not UNSET:
            field_dict["failedCount"] = failed_count
        if fetched_count is not UNSET:
            field_dict["fetchedCount"] = fetched_count
        if monitors is not UNSET:
            field_dict["monitors"] = monitors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_get_monitors_error import BatchGetMonitorsError
        from ..models.batch_get_monitors_response_monitors import BatchGetMonitorsResponseMonitors

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[BatchGetMonitorsError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BatchGetMonitorsError.from_dict(errors_item_data)

                errors.append(errors_item)

        failed_count = d.pop("failedCount", UNSET)

        fetched_count = d.pop("fetchedCount", UNSET)

        _monitors = d.pop("monitors", UNSET)
        monitors: BatchGetMonitorsResponseMonitors | Unset
        if isinstance(_monitors, Unset) or _monitors is None:
            monitors = UNSET
        else:
            monitors = BatchGetMonitorsResponseMonitors.from_dict(_monitors)

        batch_get_monitors_response = cls(
            errors=errors,
            failed_count=failed_count,
            fetched_count=fetched_count,
            monitors=monitors,
        )

        batch_get_monitors_response.additional_properties = d
        return batch_get_monitors_response

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
