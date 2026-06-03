from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_group_parse_response import LogGroupParseResponse


T = TypeVar("T", bound="LogParseGroupsResponse")


@_attrs_define
class LogParseGroupsResponse:
    """
    Attributes:
        log_group_parses (list[LogGroupParseResponse] | Unset):
    """

    log_group_parses: list[LogGroupParseResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log_group_parses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.log_group_parses, Unset):
            log_group_parses = []
            for log_group_parses_item_data in self.log_group_parses:
                log_group_parses_item = log_group_parses_item_data.to_dict()
                log_group_parses.append(log_group_parses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if log_group_parses is not UNSET:
            field_dict["logGroupParses"] = log_group_parses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_group_parse_response import LogGroupParseResponse

        d = dict(src_dict)
        _log_group_parses = d.pop("logGroupParses", UNSET)
        log_group_parses: list[LogGroupParseResponse] | Unset = UNSET
        if _log_group_parses is not UNSET:
            log_group_parses = []
            for log_group_parses_item_data in _log_group_parses:
                log_group_parses_item = LogGroupParseResponse.from_dict(log_group_parses_item_data)

                log_group_parses.append(log_group_parses_item)

        log_parse_groups_response = cls(
            log_group_parses=log_group_parses,
        )

        log_parse_groups_response.additional_properties = d
        return log_parse_groups_response

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
