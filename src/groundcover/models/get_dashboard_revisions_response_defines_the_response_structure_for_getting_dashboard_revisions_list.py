from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.view import View


T = TypeVar("T", bound="GetDashboardRevisionsResponseDefinesTheResponseStructureForGettingDashboardRevisionsList")


@_attrs_define
class GetDashboardRevisionsResponseDefinesTheResponseStructureForGettingDashboardRevisionsList:
    """
    Attributes:
        has_next_page (bool | Unset):
        revisions (list[View] | Unset): The list of all dashboard revisions.
    """

    has_next_page: bool | Unset = UNSET
    revisions: list[View] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_next_page = self.has_next_page

        revisions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.revisions, Unset):
            revisions = []
            for revisions_item_data in self.revisions:
                revisions_item = revisions_item_data.to_dict()
                revisions.append(revisions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_next_page is not UNSET:
            field_dict["hasNextPage"] = has_next_page
        if revisions is not UNSET:
            field_dict["revisions"] = revisions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view import View

        d = dict(src_dict)
        has_next_page = d.pop("hasNextPage", UNSET)

        _revisions = d.pop("revisions", UNSET)
        revisions: list[View] | Unset = UNSET
        if _revisions is not UNSET:
            revisions = []
            for revisions_item_data in _revisions:
                revisions_item = View.from_dict(revisions_item_data)

                revisions.append(revisions_item)

        get_dashboard_revisions_response_defines_the_response_structure_for_getting_dashboard_revisions_list = cls(
            has_next_page=has_next_page,
            revisions=revisions,
        )

        get_dashboard_revisions_response_defines_the_response_structure_for_getting_dashboard_revisions_list.additional_properties = d
        return get_dashboard_revisions_response_defines_the_response_structure_for_getting_dashboard_revisions_list

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
