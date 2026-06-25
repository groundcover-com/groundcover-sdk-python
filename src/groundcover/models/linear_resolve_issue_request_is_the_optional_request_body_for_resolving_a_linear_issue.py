from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="LinearResolveIssueRequestIsTheOptionalRequestBodyForResolvingALinearIssue")


@_attrs_define
class LinearResolveIssueRequestIsTheOptionalRequestBodyForResolvingALinearIssue:
    """
    Attributes:
        state_id (str | Unset):
    """

    state_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state_id = self.state_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state_id is not UNSET:
            field_dict["state_id"] = state_id

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
        state_id = d.pop("state_id", UNSET)

        linear_resolve_issue_request_is_the_optional_request_body_for_resolving_a_linear_issue = cls(
            state_id=state_id,
        )

        linear_resolve_issue_request_is_the_optional_request_body_for_resolving_a_linear_issue.additional_properties = d
        return linear_resolve_issue_request_is_the_optional_request_body_for_resolving_a_linear_issue

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
