from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distributed_trace_node import DistributedTraceNode


T = TypeVar("T", bound="DistibutedTraceResponse")


@_attrs_define
class DistibutedTraceResponse:
    """
    Attributes:
        count (int | Unset):
        limit_reached (bool | Unset):
        nodes (list[DistributedTraceNode] | Unset):
    """

    count: int | Unset = UNSET
    limit_reached: bool | Unset = UNSET
    nodes: list[DistributedTraceNode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        limit_reached = self.limit_reached

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if limit_reached is not UNSET:
            field_dict["limitReached"] = limit_reached
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.distributed_trace_node import DistributedTraceNode

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        limit_reached = d.pop("limitReached", UNSET)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[DistributedTraceNode] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = DistributedTraceNode.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        distibuted_trace_response = cls(
            count=count,
            limit_reached=limit_reached,
            nodes=nodes,
        )

        distibuted_trace_response.additional_properties = d
        return distibuted_trace_response

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
