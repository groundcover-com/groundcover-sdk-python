from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selector import Selector


T = TypeVar("T", bound="LimitByDefinesPerGroupLimitingForSQLQueriesEGLIMITBY")


@_attrs_define
class LimitByDefinesPerGroupLimitingForSQLQueriesEGLIMITBY:
    """
    Attributes:
        limit (int | Unset):
        offset (int | Unset):
        selectors (list[Selector] | Unset):
    """

    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    selectors: list[Selector] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        selectors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.selectors, Unset):
            selectors = []
            for selectors_item_data in self.selectors:
                selectors_item = selectors_item_data.to_dict()
                selectors.append(selectors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if selectors is not UNSET:
            field_dict["selectors"] = selectors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.selector import Selector

        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        _selectors = d.pop("selectors", UNSET)
        selectors: list[Selector] | Unset = UNSET
        if _selectors is not UNSET:
            selectors = []
            for selectors_item_data in _selectors:
                selectors_item = Selector.from_dict(selectors_item_data)

                selectors.append(selectors_item)

        limit_by_defines_per_group_limiting_for_sql_queries_eglimitby = cls(
            limit=limit,
            offset=offset,
            selectors=selectors,
        )

        limit_by_defines_per_group_limiting_for_sql_queries_eglimitby.additional_properties = d
        return limit_by_defines_per_group_limiting_for_sql_queries_eglimitby

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
