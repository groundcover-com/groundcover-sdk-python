from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.revision_entry import RevisionEntry


T = TypeVar("T", bound="MonitorRevisionsResponseIsAPageOfRevisionsNewestFirst")


@_attrs_define
class MonitorRevisionsResponseIsAPageOfRevisionsNewestFirst:
    """
    Attributes:
        has_next_page (bool | Unset):
        revisions (list[RevisionEntry] | Unset):
    """

    has_next_page: bool | Unset = UNSET
    revisions: list[RevisionEntry] | Unset = UNSET
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
        from ..models.revision_entry import RevisionEntry

        d = dict(src_dict)
        has_next_page = d.pop("hasNextPage", UNSET)

        _revisions = d.pop("revisions", UNSET)
        revisions: list[RevisionEntry] | Unset = UNSET
        if _revisions is not UNSET:
            revisions = []
            for revisions_item_data in _revisions:
                revisions_item = RevisionEntry.from_dict(revisions_item_data)

                revisions.append(revisions_item)

        monitor_revisions_response_is_a_page_of_revisions_newest_first = cls(
            has_next_page=has_next_page,
            revisions=revisions,
        )

        monitor_revisions_response_is_a_page_of_revisions_newest_first.additional_properties = d
        return monitor_revisions_response_is_a_page_of_revisions_newest_first

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
