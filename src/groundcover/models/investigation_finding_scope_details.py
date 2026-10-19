from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.investigation_scope_entry import InvestigationScopeEntry


T = TypeVar("T", bound="InvestigationFindingScopeDetails")


@_attrs_define
class InvestigationFindingScopeDetails:
    """FindingScopeDetails are the details of FINDING_OUT_OF_SCOPE: the node's scope entries a
    finding's query must filter on, with one of the values for each key.

        Attributes:
            scope (list[InvestigationScopeEntry]):
    """

    scope: list[InvestigationScopeEntry]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope = []
        for scope_item_data in self.scope:
            scope_item = scope_item_data.to_dict()
            scope.append(scope_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_scope_entry import InvestigationScopeEntry

        d = dict(src_dict)
        scope = []
        _scope = d.pop("scope")
        for scope_item_data in _scope:
            scope_item = InvestigationScopeEntry.from_dict(scope_item_data)

            scope.append(scope_item)

        investigation_finding_scope_details = cls(
            scope=scope,
        )

        investigation_finding_scope_details.additional_properties = d
        return investigation_finding_scope_details

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
