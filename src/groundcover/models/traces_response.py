from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_item import TraceItem


T = TypeVar("T", bound="TracesResponse")


@_attrs_define
class TracesResponse:
    """
    Attributes:
        done (bool | Unset):
        is_limit_reached (bool | Unset):
        optimized_keys (list[str] | Unset):
        partial_result (bool | Unset):
        traces (list[TraceItem] | Unset):
    """

    done: bool | Unset = UNSET
    is_limit_reached: bool | Unset = UNSET
    optimized_keys: list[str] | Unset = UNSET
    partial_result: bool | Unset = UNSET
    traces: list[TraceItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        is_limit_reached = self.is_limit_reached

        optimized_keys: list[str] | Unset = UNSET
        if not isinstance(self.optimized_keys, Unset):
            optimized_keys = self.optimized_keys

        partial_result = self.partial_result

        traces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.traces, Unset):
            traces = []
            for traces_item_data in self.traces:
                traces_item = traces_item_data.to_dict()
                traces.append(traces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if done is not UNSET:
            field_dict["done"] = done
        if is_limit_reached is not UNSET:
            field_dict["isLimitReached"] = is_limit_reached
        if optimized_keys is not UNSET:
            field_dict["optimizedKeys"] = optimized_keys
        if partial_result is not UNSET:
            field_dict["partialResult"] = partial_result
        if traces is not UNSET:
            field_dict["traces"] = traces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_item import TraceItem

        d = dict(src_dict)
        done = d.pop("done", UNSET)

        is_limit_reached = d.pop("isLimitReached", UNSET)

        optimized_keys = cast(list[str], d.pop("optimizedKeys", UNSET))

        partial_result = d.pop("partialResult", UNSET)

        _traces = d.pop("traces", UNSET)
        traces: list[TraceItem] | Unset = UNSET
        if _traces is not UNSET:
            traces = []
            for traces_item_data in _traces:
                traces_item = TraceItem.from_dict(traces_item_data)

                traces.append(traces_item)

        traces_response = cls(
            done=done,
            is_limit_reached=is_limit_reached,
            optimized_keys=optimized_keys,
            partial_result=partial_result,
            traces=traces,
        )

        traces_response.additional_properties = d
        return traces_response

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
