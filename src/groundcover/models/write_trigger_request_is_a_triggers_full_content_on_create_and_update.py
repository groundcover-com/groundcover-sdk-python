from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_model_selection import InvestigationModelSelection


T = TypeVar("T", bound="WriteTriggerRequestIsATriggersFullContentOnCreateAndUpdate")


@_attrs_define
class WriteTriggerRequestIsATriggersFullContentOnCreateAndUpdate:
    """
    Attributes:
        name (str):
        query (str): The gcQL issue selector notification routes use.
        cooldown_interval (str | Unset): The same values a notification route's renotificationInterval takes; empty:
            once per firing cycle.
        instructions (str | Unset): Plain text the investigator gets after its statement; empty for none. An update
            saves what it sends,
            so one without instructions clears them.
        max_concurrent (int | Unset): At most this many of the trigger's investigations are open at once; a firing issue
            over the cap waits for
            one to close. Omitted: 100.
        model_selection (InvestigationModelSelection | Unset): ModelSelection is the model agent-service runs an
            investigation's agents on. agent-service decides which
            models and efforts are allowed, and refuses a run whose selection it doesn't allow.
    """

    name: str
    query: str
    cooldown_interval: str | Unset = UNSET
    instructions: str | Unset = UNSET
    max_concurrent: int | Unset = UNSET
    model_selection: InvestigationModelSelection | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        query = self.query

        cooldown_interval = self.cooldown_interval

        instructions = self.instructions

        max_concurrent = self.max_concurrent

        model_selection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_selection, Unset):
            model_selection = self.model_selection.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "query": query,
            }
        )
        if cooldown_interval is not UNSET:
            field_dict["cooldownInterval"] = cooldown_interval
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if max_concurrent is not UNSET:
            field_dict["maxConcurrent"] = max_concurrent
        if model_selection is not UNSET:
            field_dict["modelSelection"] = model_selection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_model_selection import InvestigationModelSelection

        d = dict(src_dict)
        name = d.pop("name")

        query = d.pop("query")

        cooldown_interval = d.pop("cooldownInterval", UNSET)

        instructions = d.pop("instructions", UNSET)

        max_concurrent = d.pop("maxConcurrent", UNSET)

        _model_selection = d.pop("modelSelection", UNSET)
        model_selection: InvestigationModelSelection | Unset
        if isinstance(_model_selection, Unset) or _model_selection is None:
            model_selection = UNSET
        else:
            model_selection = InvestigationModelSelection.from_dict(_model_selection)

        write_trigger_request_is_a_triggers_full_content_on_create_and_update = cls(
            name=name,
            query=query,
            cooldown_interval=cooldown_interval,
            instructions=instructions,
            max_concurrent=max_concurrent,
            model_selection=model_selection,
        )

        write_trigger_request_is_a_triggers_full_content_on_create_and_update.additional_properties = d
        return write_trigger_request_is_a_triggers_full_content_on_create_and_update

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
