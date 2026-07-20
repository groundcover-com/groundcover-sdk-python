from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_request_body_represents_the_request_body_proxied_to_export_service_format import (
    ExportRequestBodyRepresentsTheRequestBodyProxiedToExportServiceFormat,
)
from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_auth_body_represents_the_auth_mode_sent_to_export_service import (
        ExportAuthBodyRepresentsTheAuthModeSentToExportService,
    )
    from ..models.export_capture_body_represents_export_capture_options import (
        ExportCaptureBodyRepresentsExportCaptureOptions,
    )
    from ..models.export_target_body_represents_a_dashboard_widget_or_issue_graph_export_target import (
        ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTarget,
    )
    from ..models.export_time_range_body_represents_the_export_time_range import (
        ExportTimeRangeBodyRepresentsTheExportTimeRange,
    )


T = TypeVar("T", bound="ExportRequestBodyRepresentsTheRequestBodyProxiedToExportService")


@_attrs_define
class ExportRequestBodyRepresentsTheRequestBodyProxiedToExportService:
    """
    Attributes:
        auth (ExportAuthBodyRepresentsTheAuthModeSentToExportService):
        format_ (ExportRequestBodyRepresentsTheRequestBodyProxiedToExportServiceFormat): Export output format.
        target (ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTarget):
        capture (ExportCaptureBodyRepresentsExportCaptureOptions | Unset):
        time_range (ExportTimeRangeBodyRepresentsTheExportTimeRange | Unset):
    """

    auth: ExportAuthBodyRepresentsTheAuthModeSentToExportService
    format_: ExportRequestBodyRepresentsTheRequestBodyProxiedToExportServiceFormat
    target: ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTarget
    capture: ExportCaptureBodyRepresentsExportCaptureOptions | Unset = UNSET
    time_range: ExportTimeRangeBodyRepresentsTheExportTimeRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth = self.auth.to_dict()

        format_ = self.format_.value

        target = self.target.to_dict()

        capture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capture, Unset):
            capture = self.capture.to_dict()

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth": auth,
                "format": format_,
                "target": target,
            }
        )
        if capture is not UNSET:
            field_dict["capture"] = capture
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_auth_body_represents_the_auth_mode_sent_to_export_service import (
            ExportAuthBodyRepresentsTheAuthModeSentToExportService,
        )
        from ..models.export_capture_body_represents_export_capture_options import (
            ExportCaptureBodyRepresentsExportCaptureOptions,
        )
        from ..models.export_target_body_represents_a_dashboard_widget_or_issue_graph_export_target import (
            ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTarget,
        )
        from ..models.export_time_range_body_represents_the_export_time_range import (
            ExportTimeRangeBodyRepresentsTheExportTimeRange,
        )

        d = dict(src_dict)
        auth = ExportAuthBodyRepresentsTheAuthModeSentToExportService.from_dict(d.pop("auth"))

        format_ = ExportRequestBodyRepresentsTheRequestBodyProxiedToExportServiceFormat(d.pop("format"))

        target = ExportTargetBodyRepresentsADashboardWidgetOrIssueGraphExportTarget.from_dict(d.pop("target"))

        _capture = d.pop("capture", UNSET)
        capture: ExportCaptureBodyRepresentsExportCaptureOptions | Unset
        if isinstance(_capture, Unset) or _capture is None:
            capture = UNSET
        else:
            capture = ExportCaptureBodyRepresentsExportCaptureOptions.from_dict(_capture)

        _time_range = d.pop("timeRange", UNSET)
        time_range: ExportTimeRangeBodyRepresentsTheExportTimeRange | Unset
        if isinstance(_time_range, Unset) or _time_range is None:
            time_range = UNSET
        else:
            time_range = ExportTimeRangeBodyRepresentsTheExportTimeRange.from_dict(_time_range)

        export_request_body_represents_the_request_body_proxied_to_export_service = cls(
            auth=auth,
            format_=format_,
            target=target,
            capture=capture,
            time_range=time_range,
        )

        export_request_body_represents_the_request_body_proxied_to_export_service.additional_properties = d
        return export_request_body_represents_the_request_body_proxied_to_export_service

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
