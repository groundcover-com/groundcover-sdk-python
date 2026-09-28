from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write import (
        MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite,
    )


T = TypeVar("T", bound="V2MonitorEntity")


@_attrs_define
class V2MonitorEntity:
    """V2MonitorEntity is the wire shape of one monitor in the batch-read
    response: the envelope fields callers use, plus the spec. A type of its
    own, not model.Monitor — a column added to that storage row does not
    automatically reach this response.

        Attributes:
            backend_id (str | Unset):
            created_at (datetime.datetime | Unset):
            created_by_email (str | Unset):
            grafana_monitor_id (str | Unset):
            is_provisioned (bool | Unset):
            origin_id (str | Unset):
            origin_type (str | Unset):
            spec (MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatInte
                ntIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite | Unset): The validate tags include
                custom ones registered only by this package.
                Validate through ValidateSpec — a bare validator panics.
            updated_at (datetime.datetime | Unset):
            uuid (str | Unset):
    """

    backend_id: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by_email: str | Unset = UNSET
    grafana_monitor_id: str | Unset = UNSET
    is_provisioned: bool | Unset = UNSET
    origin_id: str | Unset = UNSET
    origin_type: str | Unset = UNSET
    spec: (
        MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite
        | Unset
    ) = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backend_id = self.backend_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by_email = self.created_by_email

        grafana_monitor_id = self.grafana_monitor_id

        is_provisioned = self.is_provisioned

        origin_id = self.origin_id

        origin_type = self.origin_type

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backend_id is not UNSET:
            field_dict["backendId"] = backend_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by_email is not UNSET:
            field_dict["createdByEmail"] = created_by_email
        if grafana_monitor_id is not UNSET:
            field_dict["grafanaMonitorId"] = grafana_monitor_id
        if is_provisioned is not UNSET:
            field_dict["isProvisioned"] = is_provisioned
        if origin_id is not UNSET:
            field_dict["originId"] = origin_id
        if origin_type is not UNSET:
            field_dict["originType"] = origin_type
        if spec is not UNSET:
            field_dict["spec"] = spec
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write import (
            MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite,
        )

        d = dict(src_dict)
        backend_id = d.pop("backendId", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset) or _created_at is None:
            created_at = UNSET
        else:
            created_at = parse_datetime(_created_at)

        created_by_email = d.pop("createdByEmail", UNSET)

        grafana_monitor_id = d.pop("grafanaMonitorId", UNSET)

        is_provisioned = d.pop("isProvisioned", UNSET)

        origin_id = d.pop("originId", UNSET)

        origin_type = d.pop("originType", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: (
            MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite
            | Unset
        )
        if isinstance(_spec, Unset) or _spec is None:
            spec = UNSET
        else:
            spec = MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite.from_dict(
                _spec
            )

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset) or _updated_at is None:
            updated_at = UNSET
        else:
            updated_at = parse_datetime(_updated_at)

        uuid = d.pop("uuid", UNSET)

        v2_monitor_entity = cls(
            backend_id=backend_id,
            created_at=created_at,
            created_by_email=created_by_email,
            grafana_monitor_id=grafana_monitor_id,
            is_provisioned=is_provisioned,
            origin_id=origin_id,
            origin_type=origin_type,
            spec=spec,
            updated_at=updated_at,
            uuid=uuid,
        )

        v2_monitor_entity.additional_properties = d
        return v2_monitor_entity

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
