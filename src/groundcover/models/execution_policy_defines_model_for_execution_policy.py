from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assertion_defines_model_for_assertion import AssertionDefinesModelForAssertion
    from ..models.execution_policy_defines_model_for_execution_policy_retries import (
        ExecutionPolicyDefinesModelForExecutionPolicyRetries,
    )


T = TypeVar("T", bound="ExecutionPolicyDefinesModelForExecutionPolicy")


@_attrs_define
class ExecutionPolicyDefinesModelForExecutionPolicy:
    """
    Attributes:
        assertions (list[AssertionDefinesModelForAssertion] | Unset):
        retries (ExecutionPolicyDefinesModelForExecutionPolicyRetries | Unset):
    """

    assertions: list[AssertionDefinesModelForAssertion] | Unset = UNSET
    retries: ExecutionPolicyDefinesModelForExecutionPolicyRetries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assertions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assertions, Unset):
            assertions = []
            for assertions_item_data in self.assertions:
                assertions_item = assertions_item_data.to_dict()
                assertions.append(assertions_item)

        retries: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retries, Unset):
            retries = self.retries.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assertions is not UNSET:
            field_dict["assertions"] = assertions
        if retries is not UNSET:
            field_dict["retries"] = retries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assertion_defines_model_for_assertion import AssertionDefinesModelForAssertion
        from ..models.execution_policy_defines_model_for_execution_policy_retries import (
            ExecutionPolicyDefinesModelForExecutionPolicyRetries,
        )

        d = dict(src_dict)
        _assertions = d.pop("assertions", UNSET)
        assertions: list[AssertionDefinesModelForAssertion] | Unset = UNSET
        if _assertions is not UNSET:
            assertions = []
            for assertions_item_data in _assertions:
                assertions_item = AssertionDefinesModelForAssertion.from_dict(assertions_item_data)

                assertions.append(assertions_item)

        _retries = d.pop("retries", UNSET)
        retries: ExecutionPolicyDefinesModelForExecutionPolicyRetries | Unset
        if isinstance(_retries, Unset) or _retries is None:
            retries = UNSET
        else:
            retries = ExecutionPolicyDefinesModelForExecutionPolicyRetries.from_dict(_retries)

        execution_policy_defines_model_for_execution_policy = cls(
            assertions=assertions,
            retries=retries,
        )

        execution_policy_defines_model_for_execution_policy.additional_properties = d
        return execution_policy_defines_model_for_execution_policy

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
