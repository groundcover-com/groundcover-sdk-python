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


T = TypeVar("T", bound="UpdateSilenceRequest")


@_attrs_define
class UpdateSilenceRequest:
    """
    Attributes:
        backend_id (str | Unset):
        client_id (str | Unset):
        comment (str | Unset): Optional comment for the silence
        ends_at (datetime.datetime | Unset): End time for the silence (must be after StartsAt)
        matchers (list[SilenceMatcher] | Unset): Matchers is a slice of Matchers that is sortable, implements Stringer,
            and
            provides a Matches method to match a LabelSet against all Matchers in the
            slice. Note that some users of Matchers might require it to be sorted.
        starts_at (datetime.datetime | Unset): Start time for the silence
    """

    backend_id: str | Unset = UNSET
    client_id: str | Unset = UNSET
    comment: str | Unset = UNSET
    ends_at: datetime.datetime | Unset = UNSET
    matchers: list[SilenceMatcher] | Unset = UNSET
    starts_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backend_id = self.backend_id

        client_id = self.client_id

        comment = self.comment

        ends_at: str | Unset = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        matchers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matchers, Unset):
            matchers = []
            for componentsschemas_matchers_item_data in self.matchers:
                componentsschemas_matchers_item = componentsschemas_matchers_item_data.to_dict()
                matchers.append(componentsschemas_matchers_item)

        starts_at: str | Unset = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backend_id is not UNSET:
            field_dict["BackendID"] = backend_id
        if client_id is not UNSET:
            field_dict["ClientID"] = client_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at
        if matchers is not UNSET:
            field_dict["matchers"] = matchers
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.silence_matcher import SilenceMatcher

        d = dict(src_dict)
        backend_id = d.pop("BackendID", UNSET)

        client_id = d.pop("ClientID", UNSET)

        comment = d.pop("comment", UNSET)

        _ends_at = d.pop("endsAt", UNSET)
        ends_at: datetime.datetime | Unset
        if isinstance(_ends_at, Unset) or _ends_at is None:
            ends_at = UNSET
        else:
            ends_at = parse_datetime(_ends_at)

        _matchers = d.pop("matchers", UNSET)
        matchers: list[SilenceMatcher] | Unset = UNSET
        if _matchers is not UNSET:
            matchers = []
            for componentsschemas_matchers_item_data in _matchers:
                componentsschemas_matchers_item = SilenceMatcher.from_dict(componentsschemas_matchers_item_data)

                matchers.append(componentsschemas_matchers_item)

        _starts_at = d.pop("startsAt", UNSET)
        starts_at: datetime.datetime | Unset
        if isinstance(_starts_at, Unset) or _starts_at is None:
            starts_at = UNSET
        else:
            starts_at = parse_datetime(_starts_at)

        update_silence_request = cls(
            backend_id=backend_id,
            client_id=client_id,
            comment=comment,
            ends_at=ends_at,
            matchers=matchers,
            starts_at=starts_at,
        )

        update_silence_request.additional_properties = d
        return update_silence_request

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
