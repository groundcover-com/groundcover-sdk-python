from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentModelCapabilities")


@_attrs_define
class AgentModelCapabilities:
    """
    Attributes:
        effort_levels (list[str]):
        default_effort (str | Unset):
    """

    effort_levels: list[str]
    default_effort: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effort_levels = self.effort_levels

        default_effort = self.default_effort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effortLevels": effort_levels,
            }
        )
        if default_effort is not UNSET:
            field_dict["defaultEffort"] = default_effort

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
        effort_levels = cast(list[str], d.pop("effortLevels"))

        default_effort = d.pop("defaultEffort", UNSET)

        agent_model_capabilities = cls(
            effort_levels=effort_levels,
            default_effort=default_effort,
        )

        agent_model_capabilities.additional_properties = d
        return agent_model_capabilities

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
