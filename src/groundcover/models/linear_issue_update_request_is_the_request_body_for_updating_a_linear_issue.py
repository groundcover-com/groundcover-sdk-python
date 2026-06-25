from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="LinearIssueUpdateRequestIsTheRequestBodyForUpdatingALinearIssue")


@_attrs_define
class LinearIssueUpdateRequestIsTheRequestBodyForUpdatingALinearIssue:
    """
    Attributes:
        assignee_id (str | Unset):
        description (str | Unset):
        label_ids (list[str] | Unset):
        priority (int | Unset):
        project_id (str | Unset):
        state_id (str | Unset):
        title (str | Unset):
    """

    assignee_id: str | Unset = UNSET
    description: str | Unset = UNSET
    label_ids: list[str] | Unset = UNSET
    priority: int | Unset = UNSET
    project_id: str | Unset = UNSET
    state_id: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignee_id = self.assignee_id

        description = self.description

        label_ids: list[str] | Unset = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids

        priority = self.priority

        project_id = self.project_id

        state_id = self.state_id

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if description is not UNSET:
            field_dict["description"] = description
        if label_ids is not UNSET:
            field_dict["label_ids"] = label_ids
        if priority is not UNSET:
            field_dict["priority"] = priority
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if state_id is not UNSET:
            field_dict["state_id"] = state_id
        if title is not UNSET:
            field_dict["title"] = title

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
        assignee_id = d.pop("assignee_id", UNSET)

        description = d.pop("description", UNSET)

        label_ids = cast(list[str], d.pop("label_ids", UNSET))

        priority = d.pop("priority", UNSET)

        project_id = d.pop("project_id", UNSET)

        state_id = d.pop("state_id", UNSET)

        title = d.pop("title", UNSET)

        linear_issue_update_request_is_the_request_body_for_updating_a_linear_issue = cls(
            assignee_id=assignee_id,
            description=description,
            label_ids=label_ids,
            priority=priority,
            project_id=project_id,
            state_id=state_id,
            title=title,
        )

        linear_issue_update_request_is_the_request_body_for_updating_a_linear_issue.additional_properties = d
        return linear_issue_update_request_is_the_request_body_for_updating_a_linear_issue

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
