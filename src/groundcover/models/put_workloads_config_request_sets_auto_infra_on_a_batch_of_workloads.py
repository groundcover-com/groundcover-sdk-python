from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.auto_infra_workload_config import AutoInfraWorkloadConfig


T = TypeVar("T", bound="PutWorkloadsConfigRequestSetsAutoInfraOnABatchOfWorkloads")


@_attrs_define
class PutWorkloadsConfigRequestSetsAutoInfraOnABatchOfWorkloads:
    """
    Attributes:
        configs (list[AutoInfraWorkloadConfig]):
    """

    configs: list[AutoInfraWorkloadConfig]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configs = []
        for configs_item_data in self.configs:
            configs_item = configs_item_data.to_dict()
            configs.append(configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configs": configs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_infra_workload_config import AutoInfraWorkloadConfig

        d = dict(src_dict)
        configs = []
        _configs = d.pop("configs")
        for configs_item_data in _configs:
            configs_item = AutoInfraWorkloadConfig.from_dict(configs_item_data)

            configs.append(configs_item)

        put_workloads_config_request_sets_auto_infra_on_a_batch_of_workloads = cls(
            configs=configs,
        )

        put_workloads_config_request_sets_auto_infra_on_a_batch_of_workloads.additional_properties = d
        return put_workloads_config_request_sets_auto_infra_on_a_batch_of_workloads

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
