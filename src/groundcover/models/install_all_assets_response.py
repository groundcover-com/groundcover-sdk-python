from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.install_assets_response import InstallAssetsResponse


T = TypeVar("T", bound="InstallAllAssetsResponse")


@_attrs_define
class InstallAllAssetsResponse:
    """
    Attributes:
        dashboards (InstallAssetsResponse | Unset):
        monitors (InstallAssetsResponse | Unset):
    """

    dashboards: InstallAssetsResponse | Unset = UNSET
    monitors: InstallAssetsResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dashboards: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dashboards, Unset):
            dashboards = self.dashboards.to_dict()

        monitors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitors, Unset):
            monitors = self.monitors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dashboards is not UNSET:
            field_dict["dashboards"] = dashboards
        if monitors is not UNSET:
            field_dict["monitors"] = monitors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.install_assets_response import InstallAssetsResponse

        d = dict(src_dict)
        _dashboards = d.pop("dashboards", UNSET)
        dashboards: InstallAssetsResponse | Unset
        if isinstance(_dashboards, Unset) or _dashboards is None:
            dashboards = UNSET
        else:
            dashboards = InstallAssetsResponse.from_dict(_dashboards)

        _monitors = d.pop("monitors", UNSET)
        monitors: InstallAssetsResponse | Unset
        if isinstance(_monitors, Unset) or _monitors is None:
            monitors = UNSET
        else:
            monitors = InstallAssetsResponse.from_dict(_monitors)

        install_all_assets_response = cls(
            dashboards=dashboards,
            monitors=monitors,
        )

        install_all_assets_response.additional_properties = d
        return install_all_assets_response

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
