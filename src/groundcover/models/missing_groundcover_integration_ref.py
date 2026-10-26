from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.missing_groundcover_integration_ref_kind import MissingGroundcoverIntegrationRefKind

T = TypeVar("T", bound="MissingGroundcoverIntegrationRef")


@_attrs_define
class MissingGroundcoverIntegrationRef:
    """
    Attributes:
        id (str):
        kind (MissingGroundcoverIntegrationRefKind): connector MissingGroundcoverIntegrationConnector
            data_source MissingGroundcoverIntegrationDataSource
    """

    id: str
    kind: MissingGroundcoverIntegrationRefKind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
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
        id = d.pop("id")

        kind = MissingGroundcoverIntegrationRefKind(d.pop("kind"))

        missing_groundcover_integration_ref = cls(
            id=id,
            kind=kind,
        )

        missing_groundcover_integration_ref.additional_properties = d
        return missing_groundcover_integration_ref

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
