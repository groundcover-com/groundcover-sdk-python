from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CursorListModelsResponseIsTheResponseForTheListModelsEndpoint")


@_attrs_define
class CursorListModelsResponseIsTheResponseForTheListModelsEndpoint:
    """
    Attributes:
        models (list[str] | Unset):
    """

    models: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        models: list[str] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if models is not UNSET:
            field_dict["models"] = models

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
        models = cast(list[str], d.pop("models", UNSET))

        cursor_list_models_response_is_the_response_for_the_list_models_endpoint = cls(
            models=models,
        )

        cursor_list_models_response_is_the_response_for_the_list_models_endpoint.additional_properties = d
        return cursor_list_models_response_is_the_response_for_the_list_models_endpoint

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
