from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="QuerySourceIsAQueryTheCallerWritesItNeedNotHaveRun")


@_attrs_define
class QuerySourceIsAQueryTheCallerWritesItNeedNotHaveRun:
    """
    Attributes:
        text (str): One SQL statement, without EXPLAIN.
        params (list[str] | Unset): Text values bound to $1, $2…, in that order; null is NULL. Without params, a query
            with placeholders gets
            a generic plan.
    """

    text: str
    params: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        params: list[str] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

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
        text = d.pop("text")

        params = cast(list[str], d.pop("params", UNSET))

        query_source_is_a_query_the_caller_writes_it_need_not_have_run = cls(
            text=text,
            params=params,
        )

        query_source_is_a_query_the_caller_writes_it_need_not_have_run.additional_properties = d
        return query_source_is_a_query_the_caller_writes_it_need_not_have_run

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
