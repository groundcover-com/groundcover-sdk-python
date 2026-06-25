from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider import Provider
    from ..models.trigger import Trigger


T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """
    Attributes:
        created_by (str | Unset): User who created the workflow
        creation_time (datetime.datetime | Unset): Timestamp when the workflow was created
        description (str | Unset): Description of the workflow
        id (str | Unset): Unique identifier of the workflow
        interval (int | Unset): Execution interval in seconds
        invalid (bool | Unset): Whether the workflow configuration is invalid
        last_execution_started (datetime.datetime | Unset): Timestamp when the last execution started
        last_execution_status (str | Unset): Status of the last execution
        last_execution_time (datetime.datetime | Unset): Timestamp of the last execution
        last_updated (datetime.datetime | Unset): Timestamp when the workflow was last updated
        name (str | Unset): Human-readable name of the workflow
        providers (list[Provider] | Unset): List of providers used by the workflow
        revision (int | Unset): Current revision number of the workflow
        triggers (list[Trigger] | Unset): List of triggers associated with the workflow
        workflow_raw (str | Unset): Raw workflow definition
        workflow_raw_id (str | Unset): Raw workflow identifier
    """

    created_by: str | Unset = UNSET
    creation_time: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    interval: int | Unset = UNSET
    invalid: bool | Unset = UNSET
    last_execution_started: datetime.datetime | Unset = UNSET
    last_execution_status: str | Unset = UNSET
    last_execution_time: datetime.datetime | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    providers: list[Provider] | Unset = UNSET
    revision: int | Unset = UNSET
    triggers: list[Trigger] | Unset = UNSET
    workflow_raw: str | Unset = UNSET
    workflow_raw_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by

        creation_time: str | Unset = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

        description = self.description

        id = self.id

        interval = self.interval

        invalid = self.invalid

        last_execution_started: str | Unset = UNSET
        if not isinstance(self.last_execution_started, Unset):
            last_execution_started = self.last_execution_started.isoformat()

        last_execution_status = self.last_execution_status

        last_execution_time: str | Unset = UNSET
        if not isinstance(self.last_execution_time, Unset):
            last_execution_time = self.last_execution_time.isoformat()

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        name = self.name

        providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()
                providers.append(providers_item)

        revision = self.revision

        triggers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = []
            for triggers_item_data in self.triggers:
                triggers_item = triggers_item_data.to_dict()
                triggers.append(triggers_item)

        workflow_raw = self.workflow_raw

        workflow_raw_id = self.workflow_raw_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if creation_time is not UNSET:
            field_dict["creation_time"] = creation_time
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if interval is not UNSET:
            field_dict["interval"] = interval
        if invalid is not UNSET:
            field_dict["invalid"] = invalid
        if last_execution_started is not UNSET:
            field_dict["last_execution_started"] = last_execution_started
        if last_execution_status is not UNSET:
            field_dict["last_execution_status"] = last_execution_status
        if last_execution_time is not UNSET:
            field_dict["last_execution_time"] = last_execution_time
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if name is not UNSET:
            field_dict["name"] = name
        if providers is not UNSET:
            field_dict["providers"] = providers
        if revision is not UNSET:
            field_dict["revision"] = revision
        if triggers is not UNSET:
            field_dict["triggers"] = triggers
        if workflow_raw is not UNSET:
            field_dict["workflow_raw"] = workflow_raw
        if workflow_raw_id is not UNSET:
            field_dict["workflow_raw_id"] = workflow_raw_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider import Provider
        from ..models.trigger import Trigger

        d = dict(src_dict)
        created_by = d.pop("created_by", UNSET)

        _creation_time = d.pop("creation_time", UNSET)
        creation_time: datetime.datetime | Unset
        if isinstance(_creation_time, Unset) or _creation_time is None:
            creation_time = UNSET
        else:
            creation_time = parse_datetime(_creation_time)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        interval = d.pop("interval", UNSET)

        invalid = d.pop("invalid", UNSET)

        _last_execution_started = d.pop("last_execution_started", UNSET)
        last_execution_started: datetime.datetime | Unset
        if isinstance(_last_execution_started, Unset) or _last_execution_started is None:
            last_execution_started = UNSET
        else:
            last_execution_started = parse_datetime(_last_execution_started)

        last_execution_status = d.pop("last_execution_status", UNSET)

        _last_execution_time = d.pop("last_execution_time", UNSET)
        last_execution_time: datetime.datetime | Unset
        if isinstance(_last_execution_time, Unset) or _last_execution_time is None:
            last_execution_time = UNSET
        else:
            last_execution_time = parse_datetime(_last_execution_time)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset) or _last_updated is None:
            last_updated = UNSET
        else:
            last_updated = parse_datetime(_last_updated)

        name = d.pop("name", UNSET)

        _providers = d.pop("providers", UNSET)
        providers: list[Provider] | Unset = UNSET
        if _providers is not UNSET:
            providers = []
            for providers_item_data in _providers:
                providers_item = Provider.from_dict(providers_item_data)

                providers.append(providers_item)

        revision = d.pop("revision", UNSET)

        _triggers = d.pop("triggers", UNSET)
        triggers: list[Trigger] | Unset = UNSET
        if _triggers is not UNSET:
            triggers = []
            for triggers_item_data in _triggers:
                triggers_item = Trigger.from_dict(triggers_item_data)

                triggers.append(triggers_item)

        workflow_raw = d.pop("workflow_raw", UNSET)

        workflow_raw_id = d.pop("workflow_raw_id", UNSET)

        workflow = cls(
            created_by=created_by,
            creation_time=creation_time,
            description=description,
            id=id,
            interval=interval,
            invalid=invalid,
            last_execution_started=last_execution_started,
            last_execution_status=last_execution_status,
            last_execution_time=last_execution_time,
            last_updated=last_updated,
            name=name,
            providers=providers,
            revision=revision,
            triggers=triggers,
            workflow_raw=workflow_raw,
            workflow_raw_id=workflow_raw_id,
        )

        workflow.additional_properties = d
        return workflow

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
