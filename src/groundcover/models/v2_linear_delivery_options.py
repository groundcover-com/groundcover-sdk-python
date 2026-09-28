from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="V2LinearDeliveryOptions")


@_attrs_define
class V2LinearDeliveryOptions:
    """LinearDeliveryOptions requires TeamID when present. Delivery treats an
    omitted ResolveTicket as true, so ResolvedStatusID is required unless it is
    explicitly false.

        Attributes:
            assignee_id (str | Unset):
            delegate_id (str | Unset):
            label_ids (list[str] | Unset):
            project_id (str | Unset):
            resolve_ticket (bool | Unset):
            resolved_status_id (str | Unset):
            team_id (str | Unset):
    """

    assignee_id: str | Unset = UNSET
    delegate_id: str | Unset = UNSET
    label_ids: list[str] | Unset = UNSET
    project_id: str | Unset = UNSET
    resolve_ticket: bool | Unset = UNSET
    resolved_status_id: str | Unset = UNSET
    team_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignee_id = self.assignee_id

        delegate_id = self.delegate_id

        label_ids: list[str] | Unset = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids

        project_id = self.project_id

        resolve_ticket = self.resolve_ticket

        resolved_status_id = self.resolved_status_id

        team_id = self.team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if delegate_id is not UNSET:
            field_dict["delegateId"] = delegate_id
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if resolve_ticket is not UNSET:
            field_dict["resolveTicket"] = resolve_ticket
        if resolved_status_id is not UNSET:
            field_dict["resolvedStatusId"] = resolved_status_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id

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
        assignee_id = d.pop("assigneeId", UNSET)

        delegate_id = d.pop("delegateId", UNSET)

        label_ids = cast(list[str], d.pop("labelIds", UNSET))

        project_id = d.pop("projectId", UNSET)

        resolve_ticket = d.pop("resolveTicket", UNSET)

        resolved_status_id = d.pop("resolvedStatusId", UNSET)

        team_id = d.pop("teamId", UNSET)

        v2_linear_delivery_options = cls(
            assignee_id=assignee_id,
            delegate_id=delegate_id,
            label_ids=label_ids,
            project_id=project_id,
            resolve_ticket=resolve_ticket,
            resolved_status_id=resolved_status_id,
            team_id=team_id,
        )

        v2_linear_delivery_options.additional_properties = d
        return v2_linear_delivery_options

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
