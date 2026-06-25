from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="AgentToolPolicyRequestIsForwardedToAgentServiceForToolPolicyUpserts")


@_attrs_define
class AgentToolPolicyRequestIsForwardedToAgentServiceForToolPolicyUpserts:
    """
    Attributes:
        policy (str):
        resource_id (str):
        resource_type (str):
        tool_name (str):
        resource_subtype (str | Unset): Optional resource subtype.
    """

    policy: str
    resource_id: str
    resource_type: str
    tool_name: str
    resource_subtype: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy = self.policy

        resource_id = self.resource_id

        resource_type = self.resource_type

        tool_name = self.tool_name

        resource_subtype = self.resource_subtype

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy": policy,
                "resourceId": resource_id,
                "resourceType": resource_type,
                "toolName": tool_name,
            }
        )
        if resource_subtype is not UNSET:
            field_dict["resourceSubtype"] = resource_subtype

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
        policy = d.pop("policy")

        resource_id = d.pop("resourceId")

        resource_type = d.pop("resourceType")

        tool_name = d.pop("toolName")

        resource_subtype = d.pop("resourceSubtype", UNSET)

        agent_tool_policy_request_is_forwarded_to_agent_service_for_tool_policy_upserts = cls(
            policy=policy,
            resource_id=resource_id,
            resource_type=resource_type,
            tool_name=tool_name,
            resource_subtype=resource_subtype,
        )

        agent_tool_policy_request_is_forwarded_to_agent_service_for_tool_policy_upserts.additional_properties = d
        return agent_tool_policy_request_is_forwarded_to_agent_service_for_tool_policy_upserts

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
