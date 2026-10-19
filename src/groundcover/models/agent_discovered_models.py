from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_discovered_model import AgentDiscoveredModel


T = TypeVar("T", bound="AgentDiscoveredModels")


@_attrs_define
class AgentDiscoveredModels:
    """
    Attributes:
        available (bool):
        models (list[AgentDiscoveredModel]):
        draft (bool | Unset):
        refreshing (bool | Unset):
    """

    available: bool
    models: list[AgentDiscoveredModel]
    draft: bool | Unset = UNSET
    refreshing: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        draft = self.draft

        refreshing = self.refreshing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available": available,
                "models": models,
            }
        )
        if draft is not UNSET:
            field_dict["draft"] = draft
        if refreshing is not UNSET:
            field_dict["refreshing"] = refreshing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_discovered_model import AgentDiscoveredModel

        d = dict(src_dict)
        available = d.pop("available")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = AgentDiscoveredModel.from_dict(models_item_data)

            models.append(models_item)

        draft = d.pop("draft", UNSET)

        refreshing = d.pop("refreshing", UNSET)

        agent_discovered_models = cls(
            available=available,
            models=models,
            draft=draft,
            refreshing=refreshing,
        )

        agent_discovered_models.additional_properties = d
        return agent_discovered_models

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
