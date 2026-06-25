from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_monitor_request_execution_error_state import CreateMonitorRequestExecutionErrorState
from ..models.create_monitor_request_measurement_type import CreateMonitorRequestMeasurementType
from ..models.create_monitor_request_no_data_state import CreateMonitorRequestNoDataState
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_model_holds_metadata_if_the_monitor_originated_from_a_catalog import (
        CatalogModelHoldsMetadataIfTheMonitorOriginatedFromACatalog,
    )
    from ..models.create_monitor_request_annotations import CreateMonitorRequestAnnotations
    from ..models.create_monitor_request_labels import CreateMonitorRequestLabels
    from ..models.display_model_controls_how_the_monitor_is_presented import (
        DisplayModelControlsHowTheMonitorIsPresented,
    )
    from ..models.evaluation_interval_defines_the_evaluation_frequency_and_pending_duration import (
        EvaluationIntervalDefinesTheEvaluationFrequencyAndPendingDuration,
    )
    from ..models.notification_settings_defines_the_notification_settings_for_the_monitor import (
        NotificationSettingsDefinesTheNotificationSettingsForTheMonitor,
    )
    from ..models.threshold_definitions import ThresholdDefinitions


T = TypeVar("T", bound="CreateMonitorRequest")


@_attrs_define
class CreateMonitorRequest:
    """
    Attributes:
        title (str): Title of the monitor.
        annotations (CreateMonitorRequestAnnotations | Unset): Annotations to attach to the alert.
        auto_resolve (bool | Unset): Whether the alert should auto-resolve.
        catalog (CatalogModelHoldsMetadataIfTheMonitorOriginatedFromACatalog | Unset):
        category (str | Unset): Category of the monitor.
        display (DisplayModelControlsHowTheMonitorIsPresented | Unset):
        evaluation_interval (EvaluationIntervalDefinesTheEvaluationFrequencyAndPendingDuration | Unset):
        execution_error_state (CreateMonitorRequestExecutionErrorState | Unset): State to enter if execution fails.
        is_paused (bool | Unset): Whether the monitor is paused.
        labels (CreateMonitorRequestLabels | Unset): Labels to attach to the monitor/alert.
        measurement_type (CreateMonitorRequestMeasurementType | Unset): Type of measurement (state or event).
        model (ThresholdDefinitions | Unset):
        no_data_state (CreateMonitorRequestNoDataState | Unset): State to enter if no data is returned.
        notification_settings (NotificationSettingsDefinesTheNotificationSettingsForTheMonitor | Unset):
        routing (list[str] | Unset): Routing information.
        severity (str | Unset): Severity level (free-form; used as a notification/display label, not validated).
        team (str | Unset): Team associated with the monitor.
        is_provisioned (bool | Unset): Whether the monitor is provisioned by IaC.
    """

    title: str
    annotations: CreateMonitorRequestAnnotations | Unset = UNSET
    auto_resolve: bool | Unset = UNSET
    catalog: CatalogModelHoldsMetadataIfTheMonitorOriginatedFromACatalog | Unset = UNSET
    category: str | Unset = UNSET
    display: DisplayModelControlsHowTheMonitorIsPresented | Unset = UNSET
    evaluation_interval: EvaluationIntervalDefinesTheEvaluationFrequencyAndPendingDuration | Unset = UNSET
    execution_error_state: CreateMonitorRequestExecutionErrorState | Unset = UNSET
    is_paused: bool | Unset = UNSET
    labels: CreateMonitorRequestLabels | Unset = UNSET
    measurement_type: CreateMonitorRequestMeasurementType | Unset = UNSET
    model: ThresholdDefinitions | Unset = UNSET
    no_data_state: CreateMonitorRequestNoDataState | Unset = UNSET
    notification_settings: NotificationSettingsDefinesTheNotificationSettingsForTheMonitor | Unset = UNSET
    routing: list[str] | Unset = UNSET
    severity: str | Unset = UNSET
    team: str | Unset = UNSET
    is_provisioned: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        auto_resolve = self.auto_resolve

        catalog: dict[str, Any] | Unset = UNSET
        if not isinstance(self.catalog, Unset):
            catalog = self.catalog.to_dict()

        category = self.category

        display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display, Unset):
            display = self.display.to_dict()

        evaluation_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evaluation_interval, Unset):
            evaluation_interval = self.evaluation_interval.to_dict()

        execution_error_state: str | Unset = UNSET
        if not isinstance(self.execution_error_state, Unset):
            execution_error_state = self.execution_error_state.value

        is_paused = self.is_paused

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        measurement_type: str | Unset = UNSET
        if not isinstance(self.measurement_type, Unset):
            measurement_type = self.measurement_type.value

        model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        no_data_state: str | Unset = UNSET
        if not isinstance(self.no_data_state, Unset):
            no_data_state = self.no_data_state.value

        notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        routing: list[str] | Unset = UNSET
        if not isinstance(self.routing, Unset):
            routing = self.routing

        severity = self.severity

        team = self.team

        is_provisioned = self.is_provisioned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if auto_resolve is not UNSET:
            field_dict["autoResolve"] = auto_resolve
        if catalog is not UNSET:
            field_dict["catalog"] = catalog
        if category is not UNSET:
            field_dict["category"] = category
        if display is not UNSET:
            field_dict["display"] = display
        if evaluation_interval is not UNSET:
            field_dict["evaluationInterval"] = evaluation_interval
        if execution_error_state is not UNSET:
            field_dict["executionErrorState"] = execution_error_state
        if is_paused is not UNSET:
            field_dict["isPaused"] = is_paused
        if labels is not UNSET:
            field_dict["labels"] = labels
        if measurement_type is not UNSET:
            field_dict["measurementType"] = measurement_type
        if model is not UNSET:
            field_dict["model"] = model
        if no_data_state is not UNSET:
            field_dict["noDataState"] = no_data_state
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings
        if routing is not UNSET:
            field_dict["routing"] = routing
        if severity is not UNSET:
            field_dict["severity"] = severity
        if team is not UNSET:
            field_dict["team"] = team
        if is_provisioned is not UNSET:
            field_dict["isProvisioned"] = is_provisioned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_model_holds_metadata_if_the_monitor_originated_from_a_catalog import (
            CatalogModelHoldsMetadataIfTheMonitorOriginatedFromACatalog,
        )
        from ..models.create_monitor_request_annotations import CreateMonitorRequestAnnotations
        from ..models.create_monitor_request_labels import CreateMonitorRequestLabels
        from ..models.display_model_controls_how_the_monitor_is_presented import (
            DisplayModelControlsHowTheMonitorIsPresented,
        )
        from ..models.evaluation_interval_defines_the_evaluation_frequency_and_pending_duration import (
            EvaluationIntervalDefinesTheEvaluationFrequencyAndPendingDuration,
        )
        from ..models.notification_settings_defines_the_notification_settings_for_the_monitor import (
            NotificationSettingsDefinesTheNotificationSettingsForTheMonitor,
        )
        from ..models.threshold_definitions import ThresholdDefinitions

        d = dict(src_dict)
        title = d.pop("title")

        _annotations = d.pop("annotations", UNSET)
        annotations: CreateMonitorRequestAnnotations | Unset
        if isinstance(_annotations, Unset) or _annotations is None:
            annotations = UNSET
        else:
            annotations = CreateMonitorRequestAnnotations.from_dict(_annotations)

        auto_resolve = d.pop("autoResolve", UNSET)

        _catalog = d.pop("catalog", UNSET)
        catalog: CatalogModelHoldsMetadataIfTheMonitorOriginatedFromACatalog | Unset
        if isinstance(_catalog, Unset) or _catalog is None:
            catalog = UNSET
        else:
            catalog = CatalogModelHoldsMetadataIfTheMonitorOriginatedFromACatalog.from_dict(_catalog)

        category = d.pop("category", UNSET)

        _display = d.pop("display", UNSET)
        display: DisplayModelControlsHowTheMonitorIsPresented | Unset
        if isinstance(_display, Unset) or _display is None:
            display = UNSET
        else:
            display = DisplayModelControlsHowTheMonitorIsPresented.from_dict(_display)

        _evaluation_interval = d.pop("evaluationInterval", UNSET)
        evaluation_interval: EvaluationIntervalDefinesTheEvaluationFrequencyAndPendingDuration | Unset
        if isinstance(_evaluation_interval, Unset) or _evaluation_interval is None:
            evaluation_interval = UNSET
        else:
            evaluation_interval = EvaluationIntervalDefinesTheEvaluationFrequencyAndPendingDuration.from_dict(
                _evaluation_interval
            )

        _execution_error_state = d.pop("executionErrorState", UNSET)
        execution_error_state: CreateMonitorRequestExecutionErrorState | Unset
        if isinstance(_execution_error_state, Unset) or _execution_error_state is None:
            execution_error_state = UNSET
        else:
            execution_error_state = CreateMonitorRequestExecutionErrorState(_execution_error_state)

        is_paused = d.pop("isPaused", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: CreateMonitorRequestLabels | Unset
        if isinstance(_labels, Unset) or _labels is None:
            labels = UNSET
        else:
            labels = CreateMonitorRequestLabels.from_dict(_labels)

        _measurement_type = d.pop("measurementType", UNSET)
        measurement_type: CreateMonitorRequestMeasurementType | Unset
        if isinstance(_measurement_type, Unset) or _measurement_type is None:
            measurement_type = UNSET
        else:
            measurement_type = CreateMonitorRequestMeasurementType(_measurement_type)

        _model = d.pop("model", UNSET)
        model: ThresholdDefinitions | Unset
        if isinstance(_model, Unset) or _model is None:
            model = UNSET
        else:
            model = ThresholdDefinitions.from_dict(_model)

        _no_data_state = d.pop("noDataState", UNSET)
        no_data_state: CreateMonitorRequestNoDataState | Unset
        if isinstance(_no_data_state, Unset) or _no_data_state is None:
            no_data_state = UNSET
        else:
            no_data_state = CreateMonitorRequestNoDataState(_no_data_state)

        _notification_settings = d.pop("notificationSettings", UNSET)
        notification_settings: NotificationSettingsDefinesTheNotificationSettingsForTheMonitor | Unset
        if isinstance(_notification_settings, Unset) or _notification_settings is None:
            notification_settings = UNSET
        else:
            notification_settings = NotificationSettingsDefinesTheNotificationSettingsForTheMonitor.from_dict(
                _notification_settings
            )

        routing = cast(list[str], d.pop("routing", UNSET))

        severity = d.pop("severity", UNSET)

        team = d.pop("team", UNSET)

        is_provisioned = d.pop("isProvisioned", UNSET)

        create_monitor_request = cls(
            title=title,
            annotations=annotations,
            auto_resolve=auto_resolve,
            catalog=catalog,
            category=category,
            display=display,
            evaluation_interval=evaluation_interval,
            execution_error_state=execution_error_state,
            is_paused=is_paused,
            labels=labels,
            measurement_type=measurement_type,
            model=model,
            no_data_state=no_data_state,
            notification_settings=notification_settings,
            routing=routing,
            severity=severity,
            team=team,
            is_provisioned=is_provisioned,
        )

        create_monitor_request.additional_properties = d
        return create_monitor_request

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
