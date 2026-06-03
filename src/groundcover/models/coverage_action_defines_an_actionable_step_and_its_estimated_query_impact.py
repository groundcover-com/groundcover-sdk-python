from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="CoverageActionDefinesAnActionableStepAndItsEstimatedQueryImpact")


@_attrs_define
class CoverageActionDefinesAnActionableStepAndItsEstimatedQueryImpact:
    """
    Attributes:
        action_type (str | Unset):
        display_name (str | Unset):
        id (str | Unset):
        integration (str | Unset):
        issue_type (str | Unset):
        labels (list[str] | Unset):
        message (str | Unset):
        queries_unblocked (int | Unset):
        queries_unblocked_pct (float | Unset):
    """

    action_type: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    integration: str | Unset = UNSET
    issue_type: str | Unset = UNSET
    labels: list[str] | Unset = UNSET
    message: str | Unset = UNSET
    queries_unblocked: int | Unset = UNSET
    queries_unblocked_pct: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        display_name = self.display_name

        id = self.id

        integration = self.integration

        issue_type = self.issue_type

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        message = self.message

        queries_unblocked = self.queries_unblocked

        queries_unblocked_pct = self.queries_unblocked_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_type is not UNSET:
            field_dict["action_type"] = action_type
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if integration is not UNSET:
            field_dict["integration"] = integration
        if issue_type is not UNSET:
            field_dict["issue_type"] = issue_type
        if labels is not UNSET:
            field_dict["labels"] = labels
        if message is not UNSET:
            field_dict["message"] = message
        if queries_unblocked is not UNSET:
            field_dict["queries_unblocked"] = queries_unblocked
        if queries_unblocked_pct is not UNSET:
            field_dict["queries_unblocked_pct"] = queries_unblocked_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        action_type = d.pop("action_type", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        integration = d.pop("integration", UNSET)

        issue_type = d.pop("issue_type", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        message = d.pop("message", UNSET)

        queries_unblocked = d.pop("queries_unblocked", UNSET)

        queries_unblocked_pct = d.pop("queries_unblocked_pct", UNSET)

        coverage_action_defines_an_actionable_step_and_its_estimated_query_impact = cls(
            action_type=action_type,
            display_name=display_name,
            id=id,
            integration=integration,
            issue_type=issue_type,
            labels=labels,
            message=message,
            queries_unblocked=queries_unblocked,
            queries_unblocked_pct=queries_unblocked_pct,
        )

        coverage_action_defines_an_actionable_step_and_its_estimated_query_impact.additional_properties = d
        return coverage_action_defines_an_actionable_step_and_its_estimated_query_impact

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
