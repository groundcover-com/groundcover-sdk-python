from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
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
        discovered_at (datetime.datetime | Unset): The timestamp when this asset was discovered.
            Format: date-time
        gc_resource_id (str | Unset): The groundcover resource ID if installed.
        install_state (str | Unset): The installation state of the asset.
        metadata (AssetMetadata | Unset):
        missing_data_sources (list[str] | Unset): Names of data sources referenced by this asset that are not yet
            migrated.
            Populated for monitors and dashboards only. Matches DataSourceItem.DatasourceName values.
        missing_reqs (AssetListItemMissingReqs | Unset): Missing requirements for full conversion.
        name (str | Unset): The name of the asset.
        raw_payload (AssetListItemRawPayload | Unset): The verbatim provider object payload.
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
    discovered_at: datetime.datetime | Unset = UNSET
    gc_resource_id: str | Unset = UNSET
    install_state: str | Unset = UNSET
    metadata: AssetMetadata | Unset = UNSET
    missing_data_sources: list[str] | Unset = UNSET
    missing_reqs: AssetListItemMissingReqs | Unset = UNSET
    name: str | Unset = UNSET
    raw_payload: AssetListItemRawPayload | Unset = UNSET
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

        discovered_at: str | Unset = UNSET
        if not isinstance(self.discovered_at, Unset):
            discovered_at = self.discovered_at.isoformat()

        gc_resource_id = self.gc_resource_id

        install_state = self.install_state

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        missing_data_sources: list[str] | Unset = UNSET
        if not isinstance(self.missing_data_sources, Unset):
            missing_data_sources = self.missing_data_sources

        missing_reqs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.missing_reqs, Unset):
            missing_reqs = self.missing_reqs.to_dict()

        name = self.name

        raw_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.raw_payload, Unset):
            raw_payload = self.raw_payload.to_dict()

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
        if discovered_at is not UNSET:
            field_dict["discovered_at"] = discovered_at
        if gc_resource_id is not UNSET:
            field_dict["gc_resource_id"] = gc_resource_id
        if install_state is not UNSET:
            field_dict["install_state"] = install_state
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if missing_data_sources is not UNSET:
            field_dict["missing_data_sources"] = missing_data_sources
        if missing_reqs is not UNSET:
            field_dict["missing_reqs"] = missing_reqs
        if name is not UNSET:
            field_dict["name"] = name
        if raw_payload is not UNSET:
            field_dict["raw_payload"] = raw_payload
        if source_created_at is not UNSET:
            field_dict["source_created_at"] = source_created_at
        if source_resource_id is not UNSET:
            field_dict["source_resource_id"] = source_resource_id
        if support_level is not UNSET:
            field_dict["support_level"] = support_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        _discovered_at = d.pop("discovered_at", UNSET)
        discovered_at: datetime.datetime | Unset
        if isinstance(_discovered_at, Unset) or _discovered_at is None:
            discovered_at = UNSET
        else:
            discovered_at = parse_datetime(_discovered_at)

        gc_resource_id = d.pop("gc_resource_id", UNSET)

        install_state = d.pop("install_state", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AssetMetadata | Unset
        if isinstance(_metadata, Unset) or _metadata is None:
            metadata = UNSET
        else:
            metadata = AssetMetadata.from_dict(_metadata)

        missing_data_sources = cast(list[str], d.pop("missing_data_sources", UNSET))

        _missing_reqs = d.pop("missing_reqs", UNSET)
        missing_reqs: AssetListItemMissingReqs | Unset
        if isinstance(_missing_reqs, Unset) or _missing_reqs is None:
            missing_reqs = UNSET
        else:
            missing_reqs = AssetListItemMissingReqs.from_dict(_missing_reqs)

        name = d.pop("name", UNSET)

        _raw_payload = d.pop("raw_payload", UNSET)
        raw_payload: AssetListItemRawPayload | Unset
        if isinstance(_raw_payload, Unset) or _raw_payload is None:
            raw_payload = UNSET
        else:
            raw_payload = AssetListItemRawPayload.from_dict(_raw_payload)

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
            discovered_at=discovered_at,
            gc_resource_id=gc_resource_id,
            install_state=install_state,
            metadata=metadata,
            missing_data_sources=missing_data_sources,
            missing_reqs=missing_reqs,
            name=name,
            raw_payload=raw_payload,
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
