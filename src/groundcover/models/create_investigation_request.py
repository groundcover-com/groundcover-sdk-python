from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investigation_model_selection import InvestigationModelSelection
    from ..models.investigation_scope_entry import InvestigationScopeEntry
    from ..models.investigation_time_range import InvestigationTimeRange
    from ..models.subject_is_what_a_root_investigates_at_most_one_root_per_subject_is_open_at_a_time import (
        SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime,
    )


T = TypeVar("T", bound="CreateInvestigationRequest")


@_attrs_define
class CreateInvestigationRequest:
    """
    Attributes:
        statement (str):
        subject (SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime):
        model_selection (InvestigationModelSelection | Unset): ModelSelection is the model agent-service runs an
            investigation's agents on. agent-service decides which
            models and efforts are allowed, and refuses a run whose selection it doesn't allow.
        scope (list[InvestigationScopeEntry] | Unset):
        skip_investigator (bool | Unset): true opens the root without starting groundcover's investigator; start it
            later with startInvestigator.
        time_range (InvestigationTimeRange | Unset):
    """

    statement: str
    subject: SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime
    model_selection: InvestigationModelSelection | Unset = UNSET
    scope: list[InvestigationScopeEntry] | Unset = UNSET
    skip_investigator: bool | Unset = UNSET
    time_range: InvestigationTimeRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statement = self.statement

        subject = self.subject.to_dict()

        model_selection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_selection, Unset):
            model_selection = self.model_selection.to_dict()

        scope: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = []
            for scope_item_data in self.scope:
                scope_item = scope_item_data.to_dict()
                scope.append(scope_item)

        skip_investigator = self.skip_investigator

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statement": statement,
                "subject": subject,
            }
        )
        if model_selection is not UNSET:
            field_dict["modelSelection"] = model_selection
        if scope is not UNSET:
            field_dict["scope"] = scope
        if skip_investigator is not UNSET:
            field_dict["skipInvestigator"] = skip_investigator
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investigation_model_selection import InvestigationModelSelection
        from ..models.investigation_scope_entry import InvestigationScopeEntry
        from ..models.investigation_time_range import InvestigationTimeRange
        from ..models.subject_is_what_a_root_investigates_at_most_one_root_per_subject_is_open_at_a_time import (
            SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime,
        )

        d = dict(src_dict)
        statement = d.pop("statement")

        subject = SubjectIsWhatARootInvestigatesAtMostOneRootPerSubjectIsOpenAtATime.from_dict(d.pop("subject"))

        _model_selection = d.pop("modelSelection", UNSET)
        model_selection: InvestigationModelSelection | Unset
        if isinstance(_model_selection, Unset) or _model_selection is None:
            model_selection = UNSET
        else:
            model_selection = InvestigationModelSelection.from_dict(_model_selection)

        _scope = d.pop("scope", UNSET)
        scope: list[InvestigationScopeEntry] | Unset = UNSET
        if _scope is not UNSET:
            scope = []
            for scope_item_data in _scope:
                scope_item = InvestigationScopeEntry.from_dict(scope_item_data)

                scope.append(scope_item)

        skip_investigator = d.pop("skipInvestigator", UNSET)

        _time_range = d.pop("timeRange", UNSET)
        time_range: InvestigationTimeRange | Unset
        if isinstance(_time_range, Unset) or _time_range is None:
            time_range = UNSET
        else:
            time_range = InvestigationTimeRange.from_dict(_time_range)

        create_investigation_request = cls(
            statement=statement,
            subject=subject,
            model_selection=model_selection,
            scope=scope,
            skip_investigator=skip_investigator,
            time_range=time_range,
        )

        create_investigation_request.additional_properties = d
        return create_investigation_request

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
