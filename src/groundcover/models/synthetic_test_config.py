from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_settings import LabelSettings
    from ..models.worker_request_defines_model_for_worker_request import WorkerRequestDefinesModelForWorkerRequest


T = TypeVar("T", bound="SyntheticTestConfig")


@_attrs_define
class SyntheticTestConfig:
    """
    Attributes:
        check_config (WorkerRequestDefinesModelForWorkerRequest | Unset):
        enabled (bool | Unset):
        exporters (list[str] | Unset): Deprecated: Exporters field is no longer used but kept for backward compatibility
            to prevent parsing errors from clients that still send it.
        interval (str | Unset):
        label_settings (LabelSettings | Unset):
        name (str | Unset):
        version (int | Unset):
    """

    check_config: WorkerRequestDefinesModelForWorkerRequest | Unset = UNSET
    enabled: bool | Unset = UNSET
    exporters: list[str] | Unset = UNSET
    interval: str | Unset = UNSET
    label_settings: LabelSettings | Unset = UNSET
    name: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_config, Unset):
            check_config = self.check_config.to_dict()

        enabled = self.enabled

        exporters: list[str] | Unset = UNSET
        if not isinstance(self.exporters, Unset):
            exporters = self.exporters

        interval = self.interval

        label_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_settings, Unset):
            label_settings = self.label_settings.to_dict()

        name = self.name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_config is not UNSET:
            field_dict["checkConfig"] = check_config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if exporters is not UNSET:
            field_dict["exporters"] = exporters
        if interval is not UNSET:
            field_dict["interval"] = interval
        if label_settings is not UNSET:
            field_dict["labelSettings"] = label_settings
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_settings import LabelSettings
        from ..models.worker_request_defines_model_for_worker_request import WorkerRequestDefinesModelForWorkerRequest

        d = dict(src_dict)
        _check_config = d.pop("checkConfig", UNSET)
        check_config: WorkerRequestDefinesModelForWorkerRequest | Unset
        if isinstance(_check_config, Unset) or _check_config is None:
            check_config = UNSET
        else:
            check_config = WorkerRequestDefinesModelForWorkerRequest.from_dict(_check_config)

        enabled = d.pop("enabled", UNSET)

        exporters = cast(list[str], d.pop("exporters", UNSET))

        interval = d.pop("interval", UNSET)

        _label_settings = d.pop("labelSettings", UNSET)
        label_settings: LabelSettings | Unset
        if isinstance(_label_settings, Unset) or _label_settings is None:
            label_settings = UNSET
        else:
            label_settings = LabelSettings.from_dict(_label_settings)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        synthetic_test_config = cls(
            check_config=check_config,
            enabled=enabled,
            exporters=exporters,
            interval=interval,
            label_settings=label_settings,
            name=name,
            version=version,
        )

        synthetic_test_config.additional_properties = d
        return synthetic_test_config

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
