from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v2_silence_response import V2SilenceResponse


T = TypeVar("T", bound="V2SilencesListResponse")


@_attrs_define
class V2SilencesListResponse:
    """
    Attributes:
        done (bool | Unset): Whether all matching results have been returned (no more pages after this one).
        silences (list[V2SilenceResponse] | Unset): Page of silences matching the request.
    """

    done: bool | Unset = UNSET
    silences: list[V2SilenceResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        silences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.silences, Unset):
            silences = []
            for silences_item_data in self.silences:
                silences_item = silences_item_data.to_dict()
                silences.append(silences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if done is not UNSET:
            field_dict["done"] = done
        if silences is not UNSET:
            field_dict["silences"] = silences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_silence_response import V2SilenceResponse

        d = dict(src_dict)
        done = d.pop("done", UNSET)

        _silences = d.pop("silences", UNSET)
        silences: list[V2SilenceResponse] | Unset = UNSET
        if _silences is not UNSET:
            silences = []
            for silences_item_data in _silences:
                silences_item = V2SilenceResponse.from_dict(silences_item_data)

                silences.append(silences_item)

        v2_silences_list_response = cls(
            done=done,
            silences=silences,
        )

        v2_silences_list_response.additional_properties = d
        return v2_silences_list_response

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
