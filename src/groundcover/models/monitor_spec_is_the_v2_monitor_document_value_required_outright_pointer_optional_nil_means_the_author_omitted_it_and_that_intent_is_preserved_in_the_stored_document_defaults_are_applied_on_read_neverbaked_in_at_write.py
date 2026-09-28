from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_display_controls_how_the_resulting_issue_is_rendered import (
        IssueDisplayControlsHowTheResultingIssueIsRendered,
    )
    from ..models.model_wraps_the_single_query_and_the_thresholds_list_capped_at_one_item import (
        ModelWrapsTheSingleQueryAndTheThresholdsListCappedAtOneItem,
    )
    from ..models.monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write_annotations import (
        MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteAnnotations,
    )
    from ..models.monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write_labels import (
        MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteLabels,
    )
    from ..models.notification_settings_requires_exactly_one_mode_block_there_is_no_default import (
        NotificationSettingsRequiresExactlyOneModeBlockThereIsNoDefault,
    )
    from ..models.v2_evaluation_interval import V2EvaluationInterval


T = TypeVar(
    "T",
    bound="MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite",
)


@_attrs_define
class MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWrite:
    """The validate tags include custom ones registered only by this package.
    Validate through ValidateSpec — a bare validator panics.

        Attributes:
            annotations (MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndT
                hatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteAnnotations | Unset):
                Deprecated: workflows-only. Reserved _gc_* keys are rejected.
            auto_resolve (bool | Unset): nil = default (true) applied on read.
            category (str | Unset): Category is free-form — the built-ins use Infrastructure|API|… but custom
                values exist in the fleet, so there is no enum. "" is omitted/no-data.
            evaluation_error_state (str | Unset):
            evaluation_interval (V2EvaluationInterval | Unset): EvaluationInterval carries the evaluation cadence and
                pending window. The
                prom_duration tag param is the example in the error text, not a bound; the
                real bounds are struct-level rules.
            evaluation_no_data_state (str | Unset):
            is_paused (bool | Unset):
            issue_display (IssueDisplayControlsHowTheResultingIssueIsRendered | Unset):
            labels (MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIn
                tentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteLabels | Unset): Reserved _gc_*
                keys are rejected.
            measurement_type (str | Unset): MeasurementType switches the timeline query builder; nil = derived on read.
            model (ModelWrapsTheSingleQueryAndTheThresholdsListCappedAtOneItem | Unset):
            name (str | Unset):
            notification_settings (NotificationSettingsRequiresExactlyOneModeBlockThereIsNoDefault | Unset): The
                renotification knobs apply to any mode.
            severity (str | Unset): Severity is "" when omitted; that intent is preserved, defaults are
                applied on read.
            tags (list[str] | Unset): Tags are free-form; items must not be blank.
            team (str | Unset):
            type_ (str | Unset): Type is the dataType; query language and datasource are inferred from it.
                monitor_type defers to the registry — see registry.go for the set.
    """

    annotations: (
        MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteAnnotations
        | Unset
    ) = UNSET
    auto_resolve: bool | Unset = UNSET
    category: str | Unset = UNSET
    evaluation_error_state: str | Unset = UNSET
    evaluation_interval: V2EvaluationInterval | Unset = UNSET
    evaluation_no_data_state: str | Unset = UNSET
    is_paused: bool | Unset = UNSET
    issue_display: IssueDisplayControlsHowTheResultingIssueIsRendered | Unset = UNSET
    labels: (
        MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteLabels
        | Unset
    ) = UNSET
    measurement_type: str | Unset = UNSET
    model: ModelWrapsTheSingleQueryAndTheThresholdsListCappedAtOneItem | Unset = UNSET
    name: str | Unset = UNSET
    notification_settings: NotificationSettingsRequiresExactlyOneModeBlockThereIsNoDefault | Unset = UNSET
    severity: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    team: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        auto_resolve = self.auto_resolve

        category = self.category

        evaluation_error_state = self.evaluation_error_state

        evaluation_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evaluation_interval, Unset):
            evaluation_interval = self.evaluation_interval.to_dict()

        evaluation_no_data_state = self.evaluation_no_data_state

        is_paused = self.is_paused

        issue_display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_display, Unset):
            issue_display = self.issue_display.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        measurement_type = self.measurement_type

        model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        name = self.name

        notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        severity = self.severity

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        team = self.team

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if auto_resolve is not UNSET:
            field_dict["autoResolve"] = auto_resolve
        if category is not UNSET:
            field_dict["category"] = category
        if evaluation_error_state is not UNSET:
            field_dict["evaluationErrorState"] = evaluation_error_state
        if evaluation_interval is not UNSET:
            field_dict["evaluationInterval"] = evaluation_interval
        if evaluation_no_data_state is not UNSET:
            field_dict["evaluationNoDataState"] = evaluation_no_data_state
        if is_paused is not UNSET:
            field_dict["isPaused"] = is_paused
        if issue_display is not UNSET:
            field_dict["issueDisplay"] = issue_display
        if labels is not UNSET:
            field_dict["labels"] = labels
        if measurement_type is not UNSET:
            field_dict["measurementType"] = measurement_type
        if model is not UNSET:
            field_dict["model"] = model
        if name is not UNSET:
            field_dict["name"] = name
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings
        if severity is not UNSET:
            field_dict["severity"] = severity
        if tags is not UNSET:
            field_dict["tags"] = tags
        if team is not UNSET:
            field_dict["team"] = team
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_display_controls_how_the_resulting_issue_is_rendered import (
            IssueDisplayControlsHowTheResultingIssueIsRendered,
        )
        from ..models.model_wraps_the_single_query_and_the_thresholds_list_capped_at_one_item import (
            ModelWrapsTheSingleQueryAndTheThresholdsListCappedAtOneItem,
        )
        from ..models.monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write_annotations import (
            MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteAnnotations,
        )
        from ..models.monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write_labels import (
            MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteLabels,
        )
        from ..models.notification_settings_requires_exactly_one_mode_block_there_is_no_default import (
            NotificationSettingsRequiresExactlyOneModeBlockThereIsNoDefault,
        )
        from ..models.v2_evaluation_interval import V2EvaluationInterval

        d = dict(src_dict)
        _annotations = d.pop("annotations", UNSET)
        annotations: (
            MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteAnnotations
            | Unset
        )
        if isinstance(_annotations, Unset) or _annotations is None:
            annotations = UNSET
        else:
            annotations = MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteAnnotations.from_dict(
                _annotations
            )

        auto_resolve = d.pop("autoResolve", UNSET)

        category = d.pop("category", UNSET)

        evaluation_error_state = d.pop("evaluationErrorState", UNSET)

        _evaluation_interval = d.pop("evaluationInterval", UNSET)
        evaluation_interval: V2EvaluationInterval | Unset
        if isinstance(_evaluation_interval, Unset) or _evaluation_interval is None:
            evaluation_interval = UNSET
        else:
            evaluation_interval = V2EvaluationInterval.from_dict(_evaluation_interval)

        evaluation_no_data_state = d.pop("evaluationNoDataState", UNSET)

        is_paused = d.pop("isPaused", UNSET)

        _issue_display = d.pop("issueDisplay", UNSET)
        issue_display: IssueDisplayControlsHowTheResultingIssueIsRendered | Unset
        if isinstance(_issue_display, Unset) or _issue_display is None:
            issue_display = UNSET
        else:
            issue_display = IssueDisplayControlsHowTheResultingIssueIsRendered.from_dict(_issue_display)

        _labels = d.pop("labels", UNSET)
        labels: (
            MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteLabels
            | Unset
        )
        if isinstance(_labels, Unset) or _labels is None:
            labels = UNSET
        else:
            labels = MonitorSpecIsTheV2MonitorDocumentValueRequiredOutrightPointerOptionalNilMeansTheAuthorOmittedItAndThatIntentIsPRESERVEDInTheStoredDocumentDefaultsAreAppliedOnReadNeverbakedInAtWriteLabels.from_dict(
                _labels
            )

        measurement_type = d.pop("measurementType", UNSET)

        _model = d.pop("model", UNSET)
        model: ModelWrapsTheSingleQueryAndTheThresholdsListCappedAtOneItem | Unset
        if isinstance(_model, Unset) or _model is None:
            model = UNSET
        else:
            model = ModelWrapsTheSingleQueryAndTheThresholdsListCappedAtOneItem.from_dict(_model)

        name = d.pop("name", UNSET)

        _notification_settings = d.pop("notificationSettings", UNSET)
        notification_settings: NotificationSettingsRequiresExactlyOneModeBlockThereIsNoDefault | Unset
        if isinstance(_notification_settings, Unset) or _notification_settings is None:
            notification_settings = UNSET
        else:
            notification_settings = NotificationSettingsRequiresExactlyOneModeBlockThereIsNoDefault.from_dict(
                _notification_settings
            )

        severity = d.pop("severity", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        team = d.pop("team", UNSET)

        type_ = d.pop("type", UNSET)

        monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write = cls(
            annotations=annotations,
            auto_resolve=auto_resolve,
            category=category,
            evaluation_error_state=evaluation_error_state,
            evaluation_interval=evaluation_interval,
            evaluation_no_data_state=evaluation_no_data_state,
            is_paused=is_paused,
            issue_display=issue_display,
            labels=labels,
            measurement_type=measurement_type,
            model=model,
            name=name,
            notification_settings=notification_settings,
            severity=severity,
            tags=tags,
            team=team,
            type_=type_,
        )

        monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write.additional_properties = d
        return monitor_spec_is_the_v2_monitor_document_value_required_outright_pointer_optional_nil_means_the_author_omitted_it_and_that_intent_is_preserved_in_the_stored_document_defaults_are_applied_on_read_neverbaked_in_at_write

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
