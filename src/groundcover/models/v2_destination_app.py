from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slack_delivery_options_requires_a_non_empty_channels_when_present import (
        SlackDeliveryOptionsRequiresANonEmptyChannelsWhenPresent,
    )
    from ..models.v2_linear_delivery_options import V2LinearDeliveryOptions


T = TypeVar("T", bound="V2DestinationApp")


@_attrs_define
class V2DestinationApp:
    """DestinationApp carries at most one delivery-options block. The spec cannot
    check the block against the app id's integration type; the write service does.

        Attributes:
            id (str | Unset):
            linear (V2LinearDeliveryOptions | Unset): LinearDeliveryOptions requires TeamID when present. Delivery treats an
                omitted ResolveTicket as true, so ResolvedStatusID is required unless it is
                explicitly false.
            slack (SlackDeliveryOptionsRequiresANonEmptyChannelsWhenPresent | Unset):
    """

    id: str | Unset = UNSET
    linear: V2LinearDeliveryOptions | Unset = UNSET
    slack: SlackDeliveryOptionsRequiresANonEmptyChannelsWhenPresent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        linear: dict[str, Any] | Unset = UNSET
        if not isinstance(self.linear, Unset):
            linear = self.linear.to_dict()

        slack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slack, Unset):
            slack = self.slack.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if linear is not UNSET:
            field_dict["linear"] = linear
        if slack is not UNSET:
            field_dict["slack"] = slack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slack_delivery_options_requires_a_non_empty_channels_when_present import (
            SlackDeliveryOptionsRequiresANonEmptyChannelsWhenPresent,
        )
        from ..models.v2_linear_delivery_options import V2LinearDeliveryOptions

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _linear = d.pop("linear", UNSET)
        linear: V2LinearDeliveryOptions | Unset
        if isinstance(_linear, Unset) or _linear is None:
            linear = UNSET
        else:
            linear = V2LinearDeliveryOptions.from_dict(_linear)

        _slack = d.pop("slack", UNSET)
        slack: SlackDeliveryOptionsRequiresANonEmptyChannelsWhenPresent | Unset
        if isinstance(_slack, Unset) or _slack is None:
            slack = UNSET
        else:
            slack = SlackDeliveryOptionsRequiresANonEmptyChannelsWhenPresent.from_dict(_slack)

        v2_destination_app = cls(
            id=id,
            linear=linear,
            slack=slack,
        )

        v2_destination_app.additional_properties = d
        return v2_destination_app

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
