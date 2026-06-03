from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route_connected_app_request_params import RouteConnectedAppRequestParams


T = TypeVar("T", bound="RouteConnectedAppRequest")


@_attrs_define
class RouteConnectedAppRequest:
    """
    Attributes:
        id (str): The connected app ID Example: app-123.
        type_ (str): The type of the connected app. Example: slack-app.
        params (RouteConnectedAppRequestParams | Unset): Route-specific parameters for this connected app.
            Slack App routes require params.channels with at least one channel ID.
            Connected app types that do not support route params must omit this field. Example: {'channels': ['C123456']}.
    """

    id: str
    type_: str
    params: RouteConnectedAppRequestParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.route_connected_app_request_params import RouteConnectedAppRequestParams

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        _params = d.pop("params", UNSET)
        params: RouteConnectedAppRequestParams | Unset
        if isinstance(_params, Unset) or _params is None:
            params = UNSET
        else:
            params = RouteConnectedAppRequestParams.from_dict(_params)

        route_connected_app_request = cls(
            id=id,
            type_=type_,
            params=params,
        )

        route_connected_app_request.additional_properties = d
        return route_connected_app_request

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
