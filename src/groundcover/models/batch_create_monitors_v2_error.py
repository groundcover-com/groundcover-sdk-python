from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="BatchCreateMonitorsV2Error")


@_attrs_define
class BatchCreateMonitorsV2Error:
    """BatchCreateMonitorsV2Error is one failed item, with the single-create error's
    message, code and details.

        Attributes:
            code (str | Unset):
            details (Any | Unset):
            index (int | Unset): Position of the item in the request's monitors list.
            message (str | Unset):
            name (str | Unset):
    """

    code: str | Unset = UNSET
    details: Any | Unset = UNSET
    index: int | Unset = UNSET
    message: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        details = self.details

        index = self.index

        message = self.message

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if details is not UNSET:
            field_dict["details"] = details
        if index is not UNSET:
            field_dict["index"] = index
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name

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
        code = d.pop("code", UNSET)

        details = d.pop("details", UNSET)

        index = d.pop("index", UNSET)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        batch_create_monitors_v2_error = cls(
            code=code,
            details=details,
            index=index,
            message=message,
            name=name,
        )

        batch_create_monitors_v2_error.additional_properties = d
        return batch_create_monitors_v2_error

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
