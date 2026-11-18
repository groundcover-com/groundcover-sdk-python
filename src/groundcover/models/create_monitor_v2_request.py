from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write import (
        MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite,
    )


T = TypeVar("T", bound="CreateMonitorV2Request")


@_attrs_define
class CreateMonitorV2Request:
    """CreateMonitorV2Request is the POST /api/v2/monitors body; the uuid is
    minted server-side (a client-owned identity uses PUT /{uuid}).

        Attributes:
            is_provisioned (bool | Unset):
            origin_id (str | Unset):
            origin_type (str | Unset): Origin has server-side behaviour (synthetics, migrations), so only
                Catalog with a known catalog entry id is accepted from clients.
            spec (MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatInte
                ntIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite | Unset): The validate tags include
                custom ones registered only by this package.
                Validate through ValidateSpec — a bare validator panics.
    """

    is_provisioned: bool | Unset = UNSET
    origin_id: str | Unset = UNSET
    origin_type: str | Unset = UNSET
    spec: (
        MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_provisioned = self.is_provisioned

        origin_id = self.origin_id

        origin_type = self.origin_type

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_provisioned is not UNSET:
            field_dict["isProvisioned"] = is_provisioned
        if origin_id is not UNSET:
            field_dict["originId"] = origin_id
        if origin_type is not UNSET:
            field_dict["originType"] = origin_type
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write import (
            MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite,
        )

        d = dict(src_dict)
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

        create_monitor_v2_request = cls(
            is_provisioned=is_provisioned,
            origin_id=origin_id,
            origin_type=origin_type,
            spec=spec,
        )

        create_monitor_v2_request.additional_properties = d
        return create_monitor_v2_request

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
