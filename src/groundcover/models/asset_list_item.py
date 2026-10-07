from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_list_item_readiness import AssetListItemReadiness
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_data_source import AssetDataSource
    from ..models.asset_list_item_convert_errors import AssetListItemConvertErrors
    from ..models.asset_list_item_convert_warnings import AssetListItemConvertWarnings
    from ..models.asset_list_item_missing_reqs import AssetListItemMissingReqs
    from ..models.asset_list_item_raw_payload import AssetListItemRawPayload
    from ..models.asset_metadata import AssetMetadata


T = TypeVar("T", bound="AssetListItem")


@_attrs_define
class AssetListItem:
    """
    Attributes:
        conversion_status (str | Unset): The conversion status of the asset.
        convert_errors (AssetListItemConvertErrors | Unset): Conversion errors encountered during processing.
        convert_warnings (AssetListItemConvertWarnings | Unset): Conversion warnings encountered during processing.
        converted_format (str | Unset): The format of the converted payload.
        converted_payload (str | Unset): The converted groundcover resource payload.
        data_sources (list[AssetDataSource] | Unset): Data sources this asset depends on. A todo one that is not
            connected puts the
            asset in missing_data; a connected todo one keeps it in needs_review.
            Populated by the list endpoint for monitors and dashboards.
        discovered_at (datetime.datetime | Unset): The timestamp when this asset was discovered.
            Format: date-time
        evaluated_at (datetime.datetime | Unset): When the current conversion was last evaluated. Absent when it has not
            been.
            Format: date-time
        evaluated_units (int | Unset): Number of units (data widgets for a dashboard, 1 for a monitor) the last
            evaluation checked.
        excluded_at (datetime.datetime | Unset): When the asset was excluded. Absent when not excluded.
        excluded_by (str | Unset): Email of the user who excluded this asset from the migration. Absent when not
            excluded.
        gc_resource_id (str | Unset): The groundcover resource ID if installed.
        install_state (str | Unset): The installation state of the asset.
        metadata (AssetMetadata | Unset):
        missing_metrics (list[str] | None | Unset): Metric names used by this data source that are not currently live in
            groundcover.
            Populated for synthesized metrics items returned with dataSourceId. Null means
            coverage has not been computed because the migration predates this field.
        missing_reqs (AssetListItemMissingReqs | Unset): Missing requirements for full conversion.
        name (str | Unset): The name of the asset.
        open_units (int | Unset): Number of units with an open finding (widgets to review). Populated by the list
            endpoint.
        raw_payload (AssetListItemRawPayload | Unset): The verbatim provider object payload.
        readiness (AssetListItemReadiness | Unset): Where the asset stands on the way to migration, derived at read time
            from
            conversion, install state, data sources and evaluation.
            Populated by the list endpoint.
        source_created_at (datetime.datetime | Unset): The timestamp when the asset was created in the source provider.
            Format: date-time
        source_resource_id (str | Unset): The provider's asset identifier.
        support_level (str | Unset): The support level for this asset type.
    """

    conversion_status: str | Unset = UNSET
    convert_errors: AssetListItemConvertErrors | Unset = UNSET
    convert_warnings: AssetListItemConvertWarnings | Unset = UNSET
    converted_format: str | Unset = UNSET
    converted_payload: str | Unset = UNSET
    data_sources: list[AssetDataSource] | Unset = UNSET
    discovered_at: datetime.datetime | Unset = UNSET
    evaluated_at: datetime.datetime | Unset = UNSET
    evaluated_units: int | Unset = UNSET
    excluded_at: datetime.datetime | Unset = UNSET
    excluded_by: str | Unset = UNSET
    gc_resource_id: str | Unset = UNSET
    install_state: str | Unset = UNSET
    metadata: AssetMetadata | Unset = UNSET
    missing_metrics: list[str] | None | Unset = UNSET
    missing_reqs: AssetListItemMissingReqs | Unset = UNSET
    name: str | Unset = UNSET
    open_units: int | Unset = UNSET
    raw_payload: AssetListItemRawPayload | Unset = UNSET
    readiness: AssetListItemReadiness | Unset = UNSET
    source_created_at: datetime.datetime | Unset = UNSET
    source_resource_id: str | Unset = UNSET
    support_level: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversion_status = self.conversion_status

        convert_errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.convert_errors, Unset):
            convert_errors = self.convert_errors.to_dict()

        convert_warnings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.convert_warnings, Unset):
            convert_warnings = self.convert_warnings.to_dict()

        converted_format = self.converted_format

        converted_payload = self.converted_payload

        data_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_sources, Unset):
            data_sources = []
            for data_sources_item_data in self.data_sources:
                data_sources_item = data_sources_item_data.to_dict()
                data_sources.append(data_sources_item)

        discovered_at: str | Unset = UNSET
        if not isinstance(self.discovered_at, Unset):
            discovered_at = self.discovered_at.isoformat()

        evaluated_at: str | Unset = UNSET
        if not isinstance(self.evaluated_at, Unset):
            evaluated_at = self.evaluated_at.isoformat()

        evaluated_units = self.evaluated_units

        excluded_at: str | Unset = UNSET
        if not isinstance(self.excluded_at, Unset):
            excluded_at = self.excluded_at.isoformat()

        excluded_by = self.excluded_by

        gc_resource_id = self.gc_resource_id

        install_state = self.install_state

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        missing_metrics: list[str] | None | Unset
        if isinstance(self.missing_metrics, Unset):
            missing_metrics = UNSET
        elif isinstance(self.missing_metrics, list):
            missing_metrics = self.missing_metrics

        else:
            missing_metrics = self.missing_metrics

        missing_reqs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.missing_reqs, Unset):
            missing_reqs = self.missing_reqs.to_dict()

        name = self.name

        open_units = self.open_units

        raw_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.raw_payload, Unset):
            raw_payload = self.raw_payload.to_dict()

        readiness: str | Unset = UNSET
        if not isinstance(self.readiness, Unset):
            readiness = self.readiness.value

        source_created_at: str | Unset = UNSET
        if not isinstance(self.source_created_at, Unset):
            source_created_at = self.source_created_at.isoformat()

        source_resource_id = self.source_resource_id

        support_level = self.support_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversion_status is not UNSET:
            field_dict["conversion_status"] = conversion_status
        if convert_errors is not UNSET:
            field_dict["convert_errors"] = convert_errors
        if convert_warnings is not UNSET:
            field_dict["convert_warnings"] = convert_warnings
        if converted_format is not UNSET:
            field_dict["converted_format"] = converted_format
        if converted_payload is not UNSET:
            field_dict["converted_payload"] = converted_payload
        if data_sources is not UNSET:
            field_dict["data_sources"] = data_sources
        if discovered_at is not UNSET:
            field_dict["discovered_at"] = discovered_at
        if evaluated_at is not UNSET:
            field_dict["evaluated_at"] = evaluated_at
        if evaluated_units is not UNSET:
            field_dict["evaluated_units"] = evaluated_units
        if excluded_at is not UNSET:
            field_dict["excluded_at"] = excluded_at
        if excluded_by is not UNSET:
            field_dict["excluded_by"] = excluded_by
        if gc_resource_id is not UNSET:
            field_dict["gc_resource_id"] = gc_resource_id
        if install_state is not UNSET:
            field_dict["install_state"] = install_state
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if missing_metrics is not UNSET:
            field_dict["missing_metrics"] = missing_metrics
        if missing_reqs is not UNSET:
            field_dict["missing_reqs"] = missing_reqs
        if name is not UNSET:
            field_dict["name"] = name
        if open_units is not UNSET:
            field_dict["open_units"] = open_units
        if raw_payload is not UNSET:
            field_dict["raw_payload"] = raw_payload
        if readiness is not UNSET:
            field_dict["readiness"] = readiness
        if source_created_at is not UNSET:
            field_dict["source_created_at"] = source_created_at
        if source_resource_id is not UNSET:
            field_dict["source_resource_id"] = source_resource_id
        if support_level is not UNSET:
            field_dict["support_level"] = support_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_data_source import AssetDataSource
        from ..models.asset_list_item_convert_errors import AssetListItemConvertErrors
        from ..models.asset_list_item_convert_warnings import AssetListItemConvertWarnings
        from ..models.asset_list_item_missing_reqs import AssetListItemMissingReqs
        from ..models.asset_list_item_raw_payload import AssetListItemRawPayload
        from ..models.asset_metadata import AssetMetadata

        d = dict(src_dict)
        conversion_status = d.pop("conversion_status", UNSET)

        _convert_errors = d.pop("convert_errors", UNSET)
        convert_errors: AssetListItemConvertErrors | Unset
        if isinstance(_convert_errors, Unset) or _convert_errors is None:
            convert_errors = UNSET
        else:
            convert_errors = AssetListItemConvertErrors.from_dict(_convert_errors)

        _convert_warnings = d.pop("convert_warnings", UNSET)
        convert_warnings: AssetListItemConvertWarnings | Unset
        if isinstance(_convert_warnings, Unset) or _convert_warnings is None:
            convert_warnings = UNSET
        else:
            convert_warnings = AssetListItemConvertWarnings.from_dict(_convert_warnings)

        converted_format = d.pop("converted_format", UNSET)

        converted_payload = d.pop("converted_payload", UNSET)

        _data_sources = d.pop("data_sources", UNSET)
        data_sources: list[AssetDataSource] | Unset = UNSET
        if _data_sources is not UNSET:
            data_sources = []
            for data_sources_item_data in _data_sources:
                data_sources_item = AssetDataSource.from_dict(data_sources_item_data)

                data_sources.append(data_sources_item)

        _discovered_at = d.pop("discovered_at", UNSET)
        discovered_at: datetime.datetime | Unset
        if isinstance(_discovered_at, Unset) or _discovered_at is None:
            discovered_at = UNSET
        else:
            discovered_at = parse_datetime(_discovered_at)

        _evaluated_at = d.pop("evaluated_at", UNSET)
        evaluated_at: datetime.datetime | Unset
        if isinstance(_evaluated_at, Unset) or _evaluated_at is None:
            evaluated_at = UNSET
        else:
            evaluated_at = parse_datetime(_evaluated_at)

        evaluated_units = d.pop("evaluated_units", UNSET)

        _excluded_at = d.pop("excluded_at", UNSET)
        excluded_at: datetime.datetime | Unset
        if isinstance(_excluded_at, Unset) or _excluded_at is None:
            excluded_at = UNSET
        else:
            excluded_at = parse_datetime(_excluded_at)

        excluded_by = d.pop("excluded_by", UNSET)

        gc_resource_id = d.pop("gc_resource_id", UNSET)

        install_state = d.pop("install_state", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AssetMetadata | Unset
        if isinstance(_metadata, Unset) or _metadata is None:
            metadata = UNSET
        else:
            metadata = AssetMetadata.from_dict(_metadata)

        def _parse_missing_metrics(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_metrics_type_0 = cast(list[str], data)

                return missing_metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        missing_metrics = _parse_missing_metrics(d.pop("missing_metrics", UNSET))

        _missing_reqs = d.pop("missing_reqs", UNSET)
        missing_reqs: AssetListItemMissingReqs | Unset
        if isinstance(_missing_reqs, Unset) or _missing_reqs is None:
            missing_reqs = UNSET
        else:
            missing_reqs = AssetListItemMissingReqs.from_dict(_missing_reqs)

        name = d.pop("name", UNSET)

        open_units = d.pop("open_units", UNSET)

        _raw_payload = d.pop("raw_payload", UNSET)
        raw_payload: AssetListItemRawPayload | Unset
        if isinstance(_raw_payload, Unset) or _raw_payload is None:
            raw_payload = UNSET
        else:
            raw_payload = AssetListItemRawPayload.from_dict(_raw_payload)

        _readiness = d.pop("readiness", UNSET)
        readiness: AssetListItemReadiness | Unset
        if isinstance(_readiness, Unset) or _readiness is None:
            readiness = UNSET
        else:
            readiness = AssetListItemReadiness(_readiness)

        _source_created_at = d.pop("source_created_at", UNSET)
        source_created_at: datetime.datetime | Unset
        if isinstance(_source_created_at, Unset) or _source_created_at is None:
            source_created_at = UNSET
        else:
            source_created_at = parse_datetime(_source_created_at)

        source_resource_id = d.pop("source_resource_id", UNSET)

        support_level = d.pop("support_level", UNSET)

        asset_list_item = cls(
            conversion_status=conversion_status,
            convert_errors=convert_errors,
            convert_warnings=convert_warnings,
            converted_format=converted_format,
            converted_payload=converted_payload,
            data_sources=data_sources,
            discovered_at=discovered_at,
            evaluated_at=evaluated_at,
            evaluated_units=evaluated_units,
            excluded_at=excluded_at,
            excluded_by=excluded_by,
            gc_resource_id=gc_resource_id,
            install_state=install_state,
            metadata=metadata,
            missing_metrics=missing_metrics,
            missing_reqs=missing_reqs,
            name=name,
            open_units=open_units,
            raw_payload=raw_payload,
            readiness=readiness,
            source_created_at=source_created_at,
            source_resource_id=source_resource_id,
            support_level=support_level,
        )

        asset_list_item.additional_properties = d
        return asset_list_item

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
