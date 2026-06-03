from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backend_settings import BackendSettings


T = TypeVar("T", bound="GetBackendSettingsResponse")


@_attrs_define
class GetBackendSettingsResponse:
    """
    Attributes:
        settings (BackendSettings | Unset):
    """

    settings: BackendSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backend_settings import BackendSettings

        d = dict(src_dict)
        _settings = d.pop("settings", UNSET)
        settings: BackendSettings | Unset
        if isinstance(_settings, Unset) or _settings is None:
            settings = UNSET
        else:
            settings = BackendSettings.from_dict(_settings)

        get_backend_settings_response = cls(
            settings=settings,
        )

        get_backend_settings_response.additional_properties = d
        return get_backend_settings_response

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
