from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_tool_policy_batch_delete_request_is_the_delete_group_for_batched_tool_policy_mutations import (
        AgentToolPolicyBatchDeleteRequestIsTheDeleteGroupForBatchedToolPolicyMutations,
    )
    from ..models.agent_tool_policy_batch_upsert_request_is_the_upsert_group_for_batched_tool_policy_mutations import (
        AgentToolPolicyBatchUpsertRequestIsTheUpsertGroupForBatchedToolPolicyMutations,
    )


T = TypeVar("T", bound="AgentToolPolicyBatchRequestIsForwardedToAgentServiceForBatchedToolPolicyMutations")


@_attrs_define
class AgentToolPolicyBatchRequestIsForwardedToAgentServiceForBatchedToolPolicyMutations:
    """
    Attributes:
        resource_id (str):
        resource_type (str):
        delete (AgentToolPolicyBatchDeleteRequestIsTheDeleteGroupForBatchedToolPolicyMutations | Unset):
        resource_subtype (str | Unset): Optional resource subtype.
        upsert (AgentToolPolicyBatchUpsertRequestIsTheUpsertGroupForBatchedToolPolicyMutations | Unset):
    """

    resource_id: str
    resource_type: str
    delete: AgentToolPolicyBatchDeleteRequestIsTheDeleteGroupForBatchedToolPolicyMutations | Unset = UNSET
    resource_subtype: str | Unset = UNSET
    upsert: AgentToolPolicyBatchUpsertRequestIsTheUpsertGroupForBatchedToolPolicyMutations | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        resource_type = self.resource_type

        delete: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        resource_subtype = self.resource_subtype

        upsert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upsert, Unset):
            upsert = self.upsert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceId": resource_id,
                "resourceType": resource_type,
            }
        )
        if delete is not UNSET:
            field_dict["delete"] = delete
        if resource_subtype is not UNSET:
            field_dict["resourceSubtype"] = resource_subtype
        if upsert is not UNSET:
            field_dict["upsert"] = upsert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_tool_policy_batch_delete_request_is_the_delete_group_for_batched_tool_policy_mutations import (
            AgentToolPolicyBatchDeleteRequestIsTheDeleteGroupForBatchedToolPolicyMutations,
        )
        from ..models.agent_tool_policy_batch_upsert_request_is_the_upsert_group_for_batched_tool_policy_mutations import (
            AgentToolPolicyBatchUpsertRequestIsTheUpsertGroupForBatchedToolPolicyMutations,
        )

        d = dict(src_dict)
        resource_id = d.pop("resourceId")

        resource_type = d.pop("resourceType")

        _delete = d.pop("delete", UNSET)
        delete: AgentToolPolicyBatchDeleteRequestIsTheDeleteGroupForBatchedToolPolicyMutations | Unset
        if isinstance(_delete, Unset) or _delete is None:
            delete = UNSET
        else:
            delete = AgentToolPolicyBatchDeleteRequestIsTheDeleteGroupForBatchedToolPolicyMutations.from_dict(_delete)

        resource_subtype = d.pop("resourceSubtype", UNSET)

        _upsert = d.pop("upsert", UNSET)
        upsert: AgentToolPolicyBatchUpsertRequestIsTheUpsertGroupForBatchedToolPolicyMutations | Unset
        if isinstance(_upsert, Unset) or _upsert is None:
            upsert = UNSET
        else:
            upsert = AgentToolPolicyBatchUpsertRequestIsTheUpsertGroupForBatchedToolPolicyMutations.from_dict(_upsert)

        agent_tool_policy_batch_request_is_forwarded_to_agent_service_for_batched_tool_policy_mutations = cls(
            resource_id=resource_id,
            resource_type=resource_type,
            delete=delete,
            resource_subtype=resource_subtype,
            upsert=upsert,
        )

        agent_tool_policy_batch_request_is_forwarded_to_agent_service_for_batched_tool_policy_mutations.additional_properties = d
        return agent_tool_policy_batch_request_is_forwarded_to_agent_service_for_batched_tool_policy_mutations

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
