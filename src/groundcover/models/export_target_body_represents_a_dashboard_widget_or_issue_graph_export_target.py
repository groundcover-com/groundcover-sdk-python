from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_target_body_represents_a_dashboard_widget_or_issue_graph_export_target_mode import (
    ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetMode,
)
from ..models.export_target_body_represents_a_dashboard_widget_or_issue_graph_export_target_type import (
    ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetType,
)
from .._generated_types import UNSET, Unset

T = TypeVar("T", bound="ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTarget")


@_attrs_define
class ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTarget:
    """
    Attributes:
        type_ (ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetType): Target type.
        dashboard_id (UUID | Unset): Dashboard ID for dashboard and widget targets.
            Format: uuid
        height (int | Unset): Issue graph height in pixels.
        issue_id (str | Unset): Issue ID for issue graph targets.
        mode (ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetMode | Unset): Issue graph rendering
            mode.
        widget_id (str | Unset): Widget ID for widget targets.
        width (int | Unset): Issue graph width in pixels.
    """

    type_: ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetType
    dashboard_id: UUID | Unset = UNSET
    height: int | Unset = UNSET
    issue_id: str | Unset = UNSET
    mode: ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetMode | Unset = UNSET
    widget_id: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        dashboard_id: str | Unset = UNSET
        if not isinstance(self.dashboard_id, Unset):
            dashboard_id = str(self.dashboard_id)

        height = self.height

        issue_id = self.issue_id

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        widget_id = self.widget_id

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if dashboard_id is not UNSET:
            field_dict["dashboardId"] = dashboard_id
        if height is not UNSET:
            field_dict["height"] = height
        if issue_id is not UNSET:
            field_dict["issueId"] = issue_id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if widget_id is not UNSET:
            field_dict["widgetId"] = widget_id
        if width is not UNSET:
            field_dict["width"] = width

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
        type_ = ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetType(d.pop("type"))

        _dashboard_id = d.pop("dashboardId", UNSET)
        dashboard_id: UUID | Unset
        if isinstance(_dashboard_id, Unset) or _dashboard_id is None:
            dashboard_id = UNSET
        else:
            dashboard_id = UUID(_dashboard_id)

        height = d.pop("height", UNSET)

        issue_id = d.pop("issueId", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetMode | Unset
        if isinstance(_mode, Unset) or _mode is None:
            mode = UNSET
        else:
            mode = ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTargetMode(_mode)

        widget_id = d.pop("widgetId", UNSET)

        width = d.pop("width", UNSET)

        export_target_body_represents_a_dashboard_widget_or_issue_graph_export_target = cls(
            type_=type_,
            dashboard_id=dashboard_id,
            height=height,
            issue_id=issue_id,
            mode=mode,
            widget_id=widget_id,
            width=width,
        )

        export_target_body_represents_a_dashboard_widget_or_issue_graph_export_target.additional_properties = d
        return export_target_body_represents_a_dashboard_widget_or_issue_graph_export_target

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
