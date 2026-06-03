from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_data_scope_defines_fine_grained_data_scoping_rules import (
        AdvancedDataScopeDefinesFineGrainedDataScopingRules,
    )
    from ..models.group import Group


T = TypeVar("T", bound="DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions")


@_attrs_define
class DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions:
    """
    Attributes:
        advanced (AdvancedDataScopeDefinesFineGrainedDataScopingRules | Unset):
        simple (Group | Unset):
    """

    advanced: AdvancedDataScopeDefinesFineGrainedDataScopingRules | Unset = UNSET
    simple: Group | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advanced: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced, Unset):
            advanced = self.advanced.to_dict()

        simple: dict[str, Any] | Unset = UNSET
        if not isinstance(self.simple, Unset):
            simple = self.simple.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if simple is not UNSET:
            field_dict["simple"] = simple

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advanced_data_scope_defines_fine_grained_data_scoping_rules import (
            AdvancedDataScopeDefinesFineGrainedDataScopingRules,
        )
        from ..models.group import Group

        d = dict(src_dict)
        _advanced = d.pop("advanced", UNSET)
        advanced: AdvancedDataScopeDefinesFineGrainedDataScopingRules | Unset
        if isinstance(_advanced, Unset) or _advanced is None:
            advanced = UNSET
        else:
            advanced = AdvancedDataScopeDefinesFineGrainedDataScopingRules.from_dict(_advanced)

        _simple = d.pop("simple", UNSET)
        simple: Group | Unset
        if isinstance(_simple, Unset) or _simple is None:
            simple = UNSET
        else:
            simple = Group.from_dict(_simple)

        data_scope_contains_either_simple_or_advanced_scope_definitions = cls(
            advanced=advanced,
            simple=simple,
        )

        data_scope_contains_either_simple_or_advanced_scope_definitions.additional_properties = d
        return data_scope_contains_either_simple_or_advanced_scope_definitions

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
