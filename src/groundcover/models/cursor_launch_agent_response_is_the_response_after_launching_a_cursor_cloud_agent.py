from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursor_source_response_is_the_source_info_returned_in_agent_responses import (
        CursorSourceResponseIsTheSourceInfoReturnedInAgentResponses,
    )
    from ..models.cursor_target_response_is_the_target_info_returned_in_agent_responses import (
        CursorTargetResponseIsTheTargetInfoReturnedInAgentResponses,
    )


T = TypeVar("T", bound="CursorLaunchAgentResponseIsTheResponseAfterLaunchingACursorCloudAgent")


@_attrs_define
class CursorLaunchAgentResponseIsTheResponseAfterLaunchingACursorCloudAgent:
    """
    Attributes:
        created_at (str | Unset):
        id (str | Unset):
        name (str | Unset):
        source (CursorSourceResponseIsTheSourceInfoReturnedInAgentResponses | Unset):
        status (str | Unset):
        target (CursorTargetResponseIsTheTargetInfoReturnedInAgentResponses | Unset):
    """

    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    source: CursorSourceResponseIsTheSourceInfoReturnedInAgentResponses | Unset = UNSET
    status: str | Unset = UNSET
    target: CursorTargetResponseIsTheTargetInfoReturnedInAgentResponses | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        name = self.name

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        status = self.status

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_source_response_is_the_source_info_returned_in_agent_responses import (
            CursorSourceResponseIsTheSourceInfoReturnedInAgentResponses,
        )
        from ..models.cursor_target_response_is_the_target_info_returned_in_agent_responses import (
            CursorTargetResponseIsTheTargetInfoReturnedInAgentResponses,
        )

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _source = d.pop("source", UNSET)
        source: CursorSourceResponseIsTheSourceInfoReturnedInAgentResponses | Unset
        if isinstance(_source, Unset) or _source is None:
            source = UNSET
        else:
            source = CursorSourceResponseIsTheSourceInfoReturnedInAgentResponses.from_dict(_source)

        status = d.pop("status", UNSET)

        _target = d.pop("target", UNSET)
        target: CursorTargetResponseIsTheTargetInfoReturnedInAgentResponses | Unset
        if isinstance(_target, Unset) or _target is None:
            target = UNSET
        else:
            target = CursorTargetResponseIsTheTargetInfoReturnedInAgentResponses.from_dict(_target)

        cursor_launch_agent_response_is_the_response_after_launching_a_cursor_cloud_agent = cls(
            created_at=created_at,
            id=id,
            name=name,
            source=source,
            status=status,
            target=target,
        )

        cursor_launch_agent_response_is_the_response_after_launching_a_cursor_cloud_agent.additional_properties = d
        return cursor_launch_agent_response_is_the_response_after_launching_a_cursor_cloud_agent

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
