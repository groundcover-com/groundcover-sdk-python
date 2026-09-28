from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteAnnotations",
)


@_attrs_define
class MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteAnnotations:
    """Deprecated: workflows-only. Reserved _gc_* keys are rejected."""

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        if isinstance(src_dict, str):
            if not src_dict.strip():
                src_dict = {}
            else:
                import json

                src_dict = json.loads(src_dict)
        d = dict(src_dict)
        monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write_annotations = cls()

        monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write_annotations.additional_properties = d
        return monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write_annotations

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
