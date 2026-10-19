from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentDiscoveredModel")


@_attrs_define
class AgentDiscoveredModel:
    """
    Attributes:
        display_name (str):
        model_id (str):
        error (None | str | Unset): Nullable: true
        validated_at (None | str | Unset): Nullable: true
    """

    display_name: str
    model_id: str
    error: None | str | Unset = UNSET
    validated_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        model_id = self.model_id

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        validated_at: None | str | Unset
        if isinstance(self.validated_at, Unset):
            validated_at = UNSET
        else:
            validated_at = self.validated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "modelId": model_id,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if validated_at is not UNSET:
            field_dict["validatedAt"] = validated_at

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
        display_name = d.pop("displayName")

        model_id = d.pop("modelId")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_validated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        validated_at = _parse_validated_at(d.pop("validatedAt", UNSET))

        agent_discovered_model = cls(
            display_name=display_name,
            model_id=model_id,
            error=error,
            validated_at=validated_at,
        )

        agent_discovered_model.additional_properties = d
        return agent_discovered_model

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
