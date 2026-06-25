from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creator import Creator
    from ..models.monitor_options import MonitorOptions
    from ..models.monitor_state import MonitorState


T = TypeVar("T", bound="Monitor")


@_attrs_define
class Monitor:
    """Monitor represents a Datadog monitor

    Attributes:
        classification (str | Unset):
        created (str | Unset):
        creator (Creator | Unset): Creator represents the creator of a resource
        id (int | Unset):
        matching_downtimes (list[Any] | Unset):
        message (str | Unset):
        modified (str | Unset):
        multi (bool | Unset):
        name (str | Unset):
        options (MonitorOptions | Unset): MonitorOptions represents options for a monitor
        overall_state (str | Unset):
        overall_state_ts (int | Unset):
        priority (int | Unset):
        query (str | Unset):
        restricted_roles (list[str] | Unset):
        state (MonitorState | Unset): MonitorState represents the state of a monitor
        tags (list[str] | Unset):
        type_ (str | Unset):
    """

    classification: str | Unset = UNSET
    created: str | Unset = UNSET
    creator: Creator | Unset = UNSET
    id: int | Unset = UNSET
    matching_downtimes: list[Any] | Unset = UNSET
    message: str | Unset = UNSET
    modified: str | Unset = UNSET
    multi: bool | Unset = UNSET
    name: str | Unset = UNSET
    options: MonitorOptions | Unset = UNSET
    overall_state: str | Unset = UNSET
    overall_state_ts: int | Unset = UNSET
    priority: int | Unset = UNSET
    query: str | Unset = UNSET
    restricted_roles: list[str] | Unset = UNSET
    state: MonitorState | Unset = UNSET
    tags: list[str] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classification = self.classification

        created = self.created

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        id = self.id

        matching_downtimes: list[Any] | Unset = UNSET
        if not isinstance(self.matching_downtimes, Unset):
            matching_downtimes = self.matching_downtimes

        message = self.message

        modified = self.modified

        multi = self.multi

        name = self.name

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        overall_state = self.overall_state

        overall_state_ts = self.overall_state_ts

        priority = self.priority

        query = self.query

        restricted_roles: list[str] | Unset = UNSET
        if not isinstance(self.restricted_roles, Unset):
            restricted_roles = self.restricted_roles

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classification is not UNSET:
            field_dict["classification"] = classification
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if id is not UNSET:
            field_dict["id"] = id
        if matching_downtimes is not UNSET:
            field_dict["matching_downtimes"] = matching_downtimes
        if message is not UNSET:
            field_dict["message"] = message
        if modified is not UNSET:
            field_dict["modified"] = modified
        if multi is not UNSET:
            field_dict["multi"] = multi
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options
        if overall_state is not UNSET:
            field_dict["overall_state"] = overall_state
        if overall_state_ts is not UNSET:
            field_dict["overall_state_ts"] = overall_state_ts
        if priority is not UNSET:
            field_dict["priority"] = priority
        if query is not UNSET:
            field_dict["query"] = query
        if restricted_roles is not UNSET:
            field_dict["restricted_roles"] = restricted_roles
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator import Creator
        from ..models.monitor_options import MonitorOptions
        from ..models.monitor_state import MonitorState

        d = dict(src_dict)
        classification = d.pop("classification", UNSET)

        created = d.pop("created", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: Creator | Unset
        if isinstance(_creator, Unset) or _creator is None:
            creator = UNSET
        else:
            creator = Creator.from_dict(_creator)

        id = d.pop("id", UNSET)

        matching_downtimes = cast(list[Any], d.pop("matching_downtimes", UNSET))

        message = d.pop("message", UNSET)

        modified = d.pop("modified", UNSET)

        multi = d.pop("multi", UNSET)

        name = d.pop("name", UNSET)

        _options = d.pop("options", UNSET)
        options: MonitorOptions | Unset
        if isinstance(_options, Unset) or _options is None:
            options = UNSET
        else:
            options = MonitorOptions.from_dict(_options)

        overall_state = d.pop("overall_state", UNSET)

        overall_state_ts = d.pop("overall_state_ts", UNSET)

        priority = d.pop("priority", UNSET)

        query = d.pop("query", UNSET)

        restricted_roles = cast(list[str], d.pop("restricted_roles", UNSET))

        _state = d.pop("state", UNSET)
        state: MonitorState | Unset
        if isinstance(_state, Unset) or _state is None:
            state = UNSET
        else:
            state = MonitorState.from_dict(_state)

        tags = cast(list[str], d.pop("tags", UNSET))

        type_ = d.pop("type", UNSET)

        monitor = cls(
            classification=classification,
            created=created,
            creator=creator,
            id=id,
            matching_downtimes=matching_downtimes,
            message=message,
            modified=modified,
            multi=multi,
            name=name,
            options=options,
            overall_state=overall_state,
            overall_state_ts=overall_state_ts,
            priority=priority,
            query=query,
            restricted_roles=restricted_roles,
            state=state,
            tags=tags,
            type_=type_,
        )

        monitor.additional_properties = d
        return monitor

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
