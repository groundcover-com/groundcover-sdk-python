from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_target_attachment_answers_an_attach_the_root_and_what_became_of_the_thread_outcome import (
    SyncTargetAttachmentAnswersAnAttachTheRootAndWhatBecameOfTheThreadOutcome,
)
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="SyncTargetAttachmentAnswersAnAttachTheRootAndWhatBecameOfTheThread")


@_attrs_define
class SyncTargetAttachmentAnswersAnAttachTheRootAndWhatBecameOfTheThread:
    """
    Attributes:
        investigation_id (UUID):
        outcome (SyncTargetAttachmentAnswersAnAttachTheRootAndWhatBecameOfTheThreadOutcome): attached: the thread is now
            the root's target, and catches up from the root's first event.
            already_attached: it already was. attached_to_another_root: another root, such as an earlier, closed
            root of the issue, owns the thread and keeps it, so this root does not sync there.
            attached SyncTargetAttached  SyncTargetAttached added a new target to the root.
            already_attached SyncTargetAlreadyAttached  SyncTargetAlreadyAttached found the destination attached to this
            root already.
            attached_to_another_root SyncTargetAttachedToAnotherRoot  SyncTargetAttachedToAnotherRoot found the destination
            attached to another root, where it stays.
        owner_investigation_id (UUID | Unset): The root that owns the thread; set with attached_to_another_root.
    """

    investigation_id: UUID
    outcome: SyncTargetAttachmentAnswersAnAttachTheRootAndWhatBecameOfTheThreadOutcome
    owner_investigation_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investigation_id = str(self.investigation_id)

        outcome = self.outcome.value

        owner_investigation_id: str | Unset = UNSET
        if not isinstance(self.owner_investigation_id, Unset):
            owner_investigation_id = str(self.owner_investigation_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "investigationId": investigation_id,
                "outcome": outcome,
            }
        )
        if owner_investigation_id is not UNSET:
            field_dict["ownerInvestigationId"] = owner_investigation_id

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
        investigation_id = UUID(d.pop("investigationId"))

        outcome = SyncTargetAttachmentAnswersAnAttachTheRootAndWhatBecameOfTheThreadOutcome(d.pop("outcome"))

        _owner_investigation_id = d.pop("ownerInvestigationId", UNSET)
        owner_investigation_id: UUID | Unset
        if isinstance(_owner_investigation_id, Unset) or _owner_investigation_id is None:
            owner_investigation_id = UNSET
        else:
            owner_investigation_id = UUID(_owner_investigation_id)

        sync_target_attachment_answers_an_attach_the_root_and_what_became_of_the_thread = cls(
            investigation_id=investigation_id,
            outcome=outcome,
            owner_investigation_id=owner_investigation_id,
        )

        sync_target_attachment_answers_an_attach_the_root_and_what_became_of_the_thread.additional_properties = d
        return sync_target_attachment_answers_an_attach_the_root_and_what_became_of_the_thread

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
