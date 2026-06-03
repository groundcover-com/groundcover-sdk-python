from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.migration_data_source_item_status import MigrationDataSourceItemStatus
from ..models.migration_data_source_item_support_type import MigrationDataSourceItemSupportType
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="MigrationDataSourceItem")


@_attrs_define
class MigrationDataSourceItem:
    """
    Attributes:
        datasource_name (str): The data source display name. For cloud integrations
            (AWS / GCP / Azure) this is prefixed with the cloud label and a
            space, e.g. "AWS 123456789012", "GCP sa@my-prod.iam.gserviceaccount.com",
            "Azure prod-azure-tenant". For non-cloud integrations it is the raw
            source-provider integration name (e.g. "redis", "kubelet").
        id (str): The stable unique identifier for this data source.
        impacted_dashboards_count (int): Number of dashboards impacted by this data source.
        impacted_metrics_count (int): Number of metrics impacted by this data source.
        impacted_monitors_count (int): Number of monitors impacted by this data source.
        referenced_resources (list[str]): Cloud or external resources referenced by this data source.
        status (MigrationDataSourceItemStatus): The current migration status for this data source.
        support_type (MigrationDataSourceItemSupportType): Whether this data source is supported by migration.
        integration_type (None | str | Unset): The matching groundcover integration type, or null when unsupported or
            unmapped.
    """

    datasource_name: str
    id: str
    impacted_dashboards_count: int
    impacted_metrics_count: int
    impacted_monitors_count: int
    referenced_resources: list[str]
    status: MigrationDataSourceItemStatus
    support_type: MigrationDataSourceItemSupportType
    integration_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasource_name = self.datasource_name

        id = self.id

        impacted_dashboards_count = self.impacted_dashboards_count

        impacted_metrics_count = self.impacted_metrics_count

        impacted_monitors_count = self.impacted_monitors_count

        referenced_resources = self.referenced_resources

        status = self.status.value

        support_type = self.support_type.value

        integration_type: None | str | Unset
        if isinstance(self.integration_type, Unset):
            integration_type = UNSET
        else:
            integration_type = self.integration_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasourceName": datasource_name,
                "id": id,
                "impactedDashboardsCount": impacted_dashboards_count,
                "impactedMetricsCount": impacted_metrics_count,
                "impactedMonitorsCount": impacted_monitors_count,
                "referencedResources": referenced_resources,
                "status": status,
                "supportType": support_type,
            }
        )
        if integration_type is not UNSET:
            field_dict["integrationType"] = integration_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            import json

            src_dict = json.loads(src_dict)
        d = dict(src_dict)
        datasource_name = d.pop("datasourceName")

        id = d.pop("id")

        impacted_dashboards_count = d.pop("impactedDashboardsCount")

        impacted_metrics_count = d.pop("impactedMetricsCount")

        impacted_monitors_count = d.pop("impactedMonitorsCount")

        referenced_resources = cast(list[str], d.pop("referencedResources"))

        status = MigrationDataSourceItemStatus(d.pop("status"))

        support_type = MigrationDataSourceItemSupportType(d.pop("supportType"))

        def _parse_integration_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        integration_type = _parse_integration_type(d.pop("integrationType", UNSET))

        migration_data_source_item = cls(
            datasource_name=datasource_name,
            id=id,
            impacted_dashboards_count=impacted_dashboards_count,
            impacted_metrics_count=impacted_metrics_count,
            impacted_monitors_count=impacted_monitors_count,
            referenced_resources=referenced_resources,
            status=status,
            support_type=support_type,
            integration_type=integration_type,
        )

        migration_data_source_item.additional_properties = d
        return migration_data_source_item

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
