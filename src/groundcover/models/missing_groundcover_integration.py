from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.missing_groundcover_integration_kind import MissingGroundcoverIntegrationKind
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MissingGroundcoverIntegration")


@_attrs_define
class MissingGroundcoverIntegration:
    """
    Attributes:
        id (str): Opaque offering ID supplied by the caller.
        kind (MissingGroundcoverIntegrationKind): connector MissingGroundcoverIntegrationConnector
            data_source MissingGroundcoverIntegrationDataSource
        reason (str | Unset): Additional evidence or telemetry that would help complete the assessment.
    """

    id: str
    kind: MissingGroundcoverIntegrationKind
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

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
        id = d.pop("id")

        kind = MissingGroundcoverIntegrationKind(d.pop("kind"))

        reason = d.pop("reason", UNSET)

        missing_groundcover_integration = cls(
            id=id,
            kind=kind,
            reason=reason,
        )

        missing_groundcover_integration.additional_properties = d
        return missing_groundcover_integration

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
