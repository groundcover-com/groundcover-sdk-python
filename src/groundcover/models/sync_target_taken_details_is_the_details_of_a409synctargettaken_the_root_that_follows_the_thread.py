from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SyncTargetTakenDetailsIsTheDetailsOfA409SYNCTARGETTAKENTheRootThatFollowsTheThread")


@_attrs_define
class SyncTargetTakenDetailsIsTheDetailsOfA409SYNCTARGETTAKENTheRootThatFollowsTheThread:
    """
    Attributes:
        owner_investigation_id (UUID):
    """

    owner_investigation_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_investigation_id = str(self.owner_investigation_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ownerInvestigationId": owner_investigation_id,
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
        owner_investigation_id = UUID(d.pop("ownerInvestigationId"))

        sync_target_taken_details_is_the_details_of_a409synctargettaken_the_root_that_follows_the_thread = cls(
            owner_investigation_id=owner_investigation_id,
        )

        sync_target_taken_details_is_the_details_of_a409synctargettaken_the_root_that_follows_the_thread.additional_properties = d
        return sync_target_taken_details_is_the_details_of_a409synctargettaken_the_root_that_follows_the_thread

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
