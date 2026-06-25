from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow import Workflow


T = TypeVar("T", bound="WorkflowsResponse")


@_attrs_define
class WorkflowsResponse:
    """
    Attributes:
        workflows (list[Workflow] | Unset): List of workflows
    """

    workflows: list[Workflow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item = workflows_item_data.to_dict()
                workflows.append(workflows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflows is not UNSET:
            field_dict["workflows"] = workflows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow import Workflow

        d = dict(src_dict)
        _workflows = d.pop("workflows", UNSET)
        workflows: list[Workflow] | Unset = UNSET
        if _workflows is not UNSET:
            workflows = []
            for workflows_item_data in _workflows:
                workflows_item = Workflow.from_dict(workflows_item_data)

                workflows.append(workflows_item)

        workflows_response = cls(
            workflows=workflows,
        )

        workflows_response.additional_properties = d
        return workflows_response

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
