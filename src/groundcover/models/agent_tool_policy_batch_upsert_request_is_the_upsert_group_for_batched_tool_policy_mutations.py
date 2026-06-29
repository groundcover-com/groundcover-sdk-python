from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentToolPolicyBatchUpsertRequestIsTheUpsertGroupForBatchedToolPolicyMutations")


@_attrs_define
class AgentToolPolicyBatchUpsertRequestIsTheUpsertGroupForBatchedToolPolicyMutations:
    """
    Attributes:
        policy (str):
        tool_names (list[str]):
    """

    policy: str
    tool_names: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy = self.policy

        tool_names = self.tool_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy": policy,
                "toolNames": tool_names,
            }
        )

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

        tool_names = cast(list[str], d.pop("toolNames"))

        agent_tool_policy_batch_upsert_request_is_the_upsert_group_for_batched_tool_policy_mutations = cls(
            policy=policy,
            tool_names=tool_names,
        )

        agent_tool_policy_batch_upsert_request_is_the_upsert_group_for_batched_tool_policy_mutations.additional_properties = d
        return agent_tool_policy_batch_upsert_request_is_the_upsert_group_for_batched_tool_policy_mutations

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
