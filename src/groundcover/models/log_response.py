from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_entry import LogEntry


T = TypeVar("T", bound="LogResponse")


@_attrs_define
class LogResponse:
    """
    Attributes:
        done (bool | Unset):
        levels (list[str] | Unset):
        limit_reached (bool | Unset):
        logs (list[LogEntry] | Unset):
        optimized_keys (list[str] | Unset):
        raise_alert (bool | Unset):
    """

    done: bool | Unset = UNSET
    levels: list[str] | Unset = UNSET
    limit_reached: bool | Unset = UNSET
    logs: list[LogEntry] | Unset = UNSET
    optimized_keys: list[str] | Unset = UNSET
    raise_alert: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        levels: list[str] | Unset = UNSET
        if not isinstance(self.levels, Unset):
            levels = self.levels

        limit_reached = self.limit_reached

        logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        optimized_keys: list[str] | Unset = UNSET
        if not isinstance(self.optimized_keys, Unset):
            optimized_keys = self.optimized_keys

        raise_alert = self.raise_alert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if done is not UNSET:
            field_dict["done"] = done
        if levels is not UNSET:
            field_dict["levels"] = levels
        if limit_reached is not UNSET:
            field_dict["limitReached"] = limit_reached
        if logs is not UNSET:
            field_dict["logs"] = logs
        if optimized_keys is not UNSET:
            field_dict["optimizedKeys"] = optimized_keys
        if raise_alert is not UNSET:
            field_dict["raiseAlert"] = raise_alert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_entry import LogEntry

        d = dict(src_dict)
        done = d.pop("done", UNSET)

        levels = cast(list[str], d.pop("levels", UNSET))

        limit_reached = d.pop("limitReached", UNSET)

        _logs = d.pop("logs", UNSET)
        logs: list[LogEntry] | Unset = UNSET
        if _logs is not UNSET:
            logs = []
            for logs_item_data in _logs:
                logs_item = LogEntry.from_dict(logs_item_data)

                logs.append(logs_item)

        optimized_keys = cast(list[str], d.pop("optimizedKeys", UNSET))

        raise_alert = d.pop("raiseAlert", UNSET)

        log_response = cls(
            done=done,
            levels=levels,
            limit_reached=limit_reached,
            logs=logs,
            optimized_keys=optimized_keys,
            raise_alert=raise_alert,
        )

        log_response.additional_properties = d
        return log_response

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
