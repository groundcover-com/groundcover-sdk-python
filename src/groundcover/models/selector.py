from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.processor import Processor
    from ..models.window_spec import WindowSpec


T = TypeVar("T", bound="Selector")


@_attrs_define
class Selector:
    """
    Attributes:
        additional_filter (str | Unset):
        alias (str | Unset):
        auto_complete (bool | Unset):
        condition_filter (Group | Unset):
        filter_keys (list[str] | Unset):
        is_nullable (bool | Unset):
        key (str | Unset):
        origin (str | Unset):
        processors (list[Processor] | Unset):
        type_ (str | Unset):
        window_spec (WindowSpec | Unset): WindowSpec specifies window function parameters for OVER clause
    """

    additional_filter: str | Unset = UNSET
    alias: str | Unset = UNSET
    auto_complete: bool | Unset = UNSET
    condition_filter: Group | Unset = UNSET
    filter_keys: list[str] | Unset = UNSET
    is_nullable: bool | Unset = UNSET
    key: str | Unset = UNSET
    origin: str | Unset = UNSET
    processors: list[Processor] | Unset = UNSET
    type_: str | Unset = UNSET
    window_spec: WindowSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_filter = self.additional_filter

        alias = self.alias

        auto_complete = self.auto_complete

        condition_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition_filter, Unset):
            condition_filter = self.condition_filter.to_dict()

        filter_keys: list[str] | Unset = UNSET
        if not isinstance(self.filter_keys, Unset):
            filter_keys = self.filter_keys

        is_nullable = self.is_nullable

        key = self.key

        origin = self.origin

        processors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.processors, Unset):
            processors = []
            for processors_item_data in self.processors:
                processors_item = processors_item_data.to_dict()
                processors.append(processors_item)

        type_ = self.type_

        window_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window_spec, Unset):
            window_spec = self.window_spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_filter is not UNSET:
            field_dict["additionalFilter"] = additional_filter
        if alias is not UNSET:
            field_dict["alias"] = alias
        if auto_complete is not UNSET:
            field_dict["autoComplete"] = auto_complete
        if condition_filter is not UNSET:
            field_dict["conditionFilter"] = condition_filter
        if filter_keys is not UNSET:
            field_dict["filterKeys"] = filter_keys
        if is_nullable is not UNSET:
            field_dict["isNullable"] = is_nullable
        if key is not UNSET:
            field_dict["key"] = key
        if origin is not UNSET:
            field_dict["origin"] = origin
        if processors is not UNSET:
            field_dict["processors"] = processors
        if type_ is not UNSET:
            field_dict["type"] = type_
        if window_spec is not UNSET:
            field_dict["windowSpec"] = window_spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group import Group
        from ..models.processor import Processor
        from ..models.window_spec import WindowSpec

        d = dict(src_dict)
        additional_filter = d.pop("additionalFilter", UNSET)

        alias = d.pop("alias", UNSET)

        auto_complete = d.pop("autoComplete", UNSET)

        _condition_filter = d.pop("conditionFilter", UNSET)
        condition_filter: Group | Unset
        if isinstance(_condition_filter, Unset) or _condition_filter is None:
            condition_filter = UNSET
        else:
            condition_filter = Group.from_dict(_condition_filter)

        filter_keys = cast(list[str], d.pop("filterKeys", UNSET))

        is_nullable = d.pop("isNullable", UNSET)

        key = d.pop("key", UNSET)

        origin = d.pop("origin", UNSET)

        _processors = d.pop("processors", UNSET)
        processors: list[Processor] | Unset = UNSET
        if _processors is not UNSET:
            processors = []
            for processors_item_data in _processors:
                processors_item = Processor.from_dict(processors_item_data)

                processors.append(processors_item)

        type_ = d.pop("type", UNSET)

        _window_spec = d.pop("windowSpec", UNSET)
        window_spec: WindowSpec | Unset
        if isinstance(_window_spec, Unset) or _window_spec is None:
            window_spec = UNSET
        else:
            window_spec = WindowSpec.from_dict(_window_spec)

        selector = cls(
            additional_filter=additional_filter,
            alias=alias,
            auto_complete=auto_complete,
            condition_filter=condition_filter,
            filter_keys=filter_keys,
            is_nullable=is_nullable,
            key=key,
            origin=origin,
            processors=processors,
            type_=type_,
            window_spec=window_spec,
        )

        selector.additional_properties = d
        return selector

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
