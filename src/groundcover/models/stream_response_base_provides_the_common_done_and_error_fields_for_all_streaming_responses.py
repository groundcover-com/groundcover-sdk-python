from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="StreamResponseBaseProvidesTheCommonDoneAndErrorFieldsForAllStreamingResponses")


@_attrs_define
class StreamResponseBaseProvidesTheCommonDoneAndErrorFieldsForAllStreamingResponses:
    """Embed this struct in your streaming response types to automatically implement StreamResponse.

    Attributes:
        done (bool | Unset):
        error (str | Unset):
    """

    done: bool | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if done is not UNSET:
            field_dict["done"] = done
        if error is not UNSET:
            field_dict["error"] = error

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
        done = d.pop("done", UNSET)

        error = d.pop("error", UNSET)

        stream_response_base_provides_the_common_done_and_error_fields_for_all_streaming_responses = cls(
            done=done,
            error=error,
        )

        stream_response_base_provides_the_common_done_and_error_fields_for_all_streaming_responses.additional_properties = d
        return stream_response_base_provides_the_common_done_and_error_fields_for_all_streaming_responses

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
