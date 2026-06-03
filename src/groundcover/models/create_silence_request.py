from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.silence_matcher import SilenceMatcher


T = TypeVar("T", bound="CreateSilenceRequest")


@_attrs_define
class CreateSilenceRequest:
    """
    Attributes:
        ends_at (datetime.datetime): End time for the silence (must be after StartsAt)
        matchers (list[SilenceMatcher]): Matchers is a slice of Matchers that is sortable, implements Stringer, and
            provides a Matches method to match a LabelSet against all Matchers in the
            slice. Note that some users of Matchers might require it to be sorted.
        starts_at (datetime.datetime): Start time for the silence
        backend_id (str | Unset):
        client_id (str | Unset):
        comment (str | Unset): Optional comment for the silence
    """

    ends_at: datetime.datetime
    matchers: list[SilenceMatcher]
    starts_at: datetime.datetime
    backend_id: str | Unset = UNSET
    client_id: str | Unset = UNSET
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ends_at = self.ends_at.isoformat()

        matchers = []
        for componentsschemas_matchers_item_data in self.matchers:
            componentsschemas_matchers_item = componentsschemas_matchers_item_data.to_dict()
            matchers.append(componentsschemas_matchers_item)

        starts_at = self.starts_at.isoformat()

        backend_id = self.backend_id

        client_id = self.client_id

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endsAt": ends_at,
                "matchers": matchers,
                "startsAt": starts_at,
            }
        )
        if backend_id is not UNSET:
            field_dict["BackendID"] = backend_id
        if client_id is not UNSET:
            field_dict["ClientID"] = client_id
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.silence_matcher import SilenceMatcher

        d = dict(src_dict)
        ends_at = parse_datetime(d.pop("endsAt"))

        matchers = []
        _matchers = d.pop("matchers")
        for componentsschemas_matchers_item_data in _matchers:
            componentsschemas_matchers_item = SilenceMatcher.from_dict(componentsschemas_matchers_item_data)

            matchers.append(componentsschemas_matchers_item)

        starts_at = parse_datetime(d.pop("startsAt"))

        backend_id = d.pop("BackendID", UNSET)

        client_id = d.pop("ClientID", UNSET)

        comment = d.pop("comment", UNSET)

        create_silence_request = cls(
            ends_at=ends_at,
            matchers=matchers,
            starts_at=starts_at,
            backend_id=backend_id,
            client_id=client_id,
            comment=comment,
        )

        create_silence_request.additional_properties = d
        return create_silence_request

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
