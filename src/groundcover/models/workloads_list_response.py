from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workloads_list_item import WorkloadsListItem


T = TypeVar("T", bound="WorkloadsListResponse")


@_attrs_define
class WorkloadsListResponse:
    """
    Attributes:
        total (int | Unset):
        workloads (list[WorkloadsListItem] | Unset):
    """

    total: int | Unset = UNSET
    workloads: list[WorkloadsListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        workloads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workloads, Unset):
            workloads = []
            for workloads_item_data in self.workloads:
                workloads_item = workloads_item_data.to_dict()
                workloads.append(workloads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if workloads is not UNSET:
            field_dict["workloads"] = workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workloads_list_item import WorkloadsListItem

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        _workloads = d.pop("workloads", UNSET)
        workloads: list[WorkloadsListItem] | Unset = UNSET
        if _workloads is not UNSET:
            workloads = []
            for workloads_item_data in _workloads:
                workloads_item = WorkloadsListItem.from_dict(workloads_item_data)

                workloads.append(workloads_item)

        workloads_list_response = cls(
            total=total,
            workloads=workloads,
        )

        workloads_list_response.additional_properties = d
        return workloads_list_response

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
