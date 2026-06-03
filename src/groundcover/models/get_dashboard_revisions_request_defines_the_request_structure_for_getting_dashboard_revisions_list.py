from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="GetDashboardRevisionsRequestDefinesTheRequestStructureForGettingDashboardRevisionsList")


@_attrs_define
class GetDashboardRevisionsRequestDefinesTheRequestStructureForGettingDashboardRevisionsList:
    """
    Attributes:
        limit (int): Maximum number of revisions to return.
        skip (int | Unset): Number of revisions to skip (for pagination).
    """

    limit: int
    skip: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        skip = self.skip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
            }
        )
        if skip is not UNSET:
            field_dict["skip"] = skip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        limit = d.pop("limit")

        skip = d.pop("skip", UNSET)

        get_dashboard_revisions_request_defines_the_request_structure_for_getting_dashboard_revisions_list = cls(
            limit=limit,
            skip=skip,
        )

        get_dashboard_revisions_request_defines_the_request_structure_for_getting_dashboard_revisions_list.additional_properties = d
        return get_dashboard_revisions_request_defines_the_request_structure_for_getting_dashboard_revisions_list

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
