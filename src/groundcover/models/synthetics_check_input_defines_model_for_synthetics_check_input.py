from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.worker_request_defines_model_for_worker_request import WorkerRequestDefinesModelForWorkerRequest


T = TypeVar("T", bound="SyntheticsCheckInputDefinesModelForSyntheticsCheckInput")


@_attrs_define
class SyntheticsCheckInputDefinesModelForSyntheticsCheckInput:
    """
    Attributes:
        check_config (WorkerRequestDefinesModelForWorkerRequest | Unset):
        interval (str | Unset):
    """

    check_config: WorkerRequestDefinesModelForWorkerRequest | Unset = UNSET
    interval: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_config, Unset):
            check_config = self.check_config.to_dict()

        interval = self.interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_config is not UNSET:
            field_dict["checkConfig"] = check_config
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worker_request_defines_model_for_worker_request import WorkerRequestDefinesModelForWorkerRequest

        d = dict(src_dict)
        _check_config = d.pop("checkConfig", UNSET)
        check_config: WorkerRequestDefinesModelForWorkerRequest | Unset
        if isinstance(_check_config, Unset) or _check_config is None:
            check_config = UNSET
        else:
            check_config = WorkerRequestDefinesModelForWorkerRequest.from_dict(_check_config)

        interval = d.pop("interval", UNSET)

        synthetics_check_input_defines_model_for_synthetics_check_input = cls(
            check_config=check_config,
            interval=interval,
        )

        synthetics_check_input_defines_model_for_synthetics_check_input.additional_properties = d
        return synthetics_check_input_defines_model_for_synthetics_check_input

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
