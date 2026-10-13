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


T = TypeVar("T", bound="RevisionEntry")


@_attrs_define
class RevisionEntry:
    """RevisionEntry is one recorded write as the history read returns it: the spec
    after it, who made it and the stamp it set.

        Attributes:
            operation (str | Unset):
            spec (MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatInte
                ntIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite | Unset): The validate tags include
                custom ones registered only by this package.
                Validate through ValidateSpec — a bare validator panics.
            updated_at (datetime.datetime | Unset):
            updated_by (str | Unset):
    """

    operation: str | Unset = UNSET
    spec: (
        MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite
        | Unset
    ) = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    updated_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation is not UNSET:
            field_dict["operation"] = operation
        if spec is not UNSET:
            field_dict["spec"] = spec
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write import (
            MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite,
        )

        d = dict(src_dict)
        operation = d.pop("operation", UNSET)

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

        updated_by = d.pop("updatedBy", UNSET)

        revision_entry = cls(
            operation=operation,
            spec=spec,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        revision_entry.additional_properties = d
        return revision_entry

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
