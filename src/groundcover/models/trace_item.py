from __future__ import annotations

import datetime

from .._datetime_compat import parse_datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_details_request_info import TraceDetailsRequestInfo
    from ..models.trace_details_response_info import TraceDetailsResponseInfo
    from ..models.trace_item_additional_columns import TraceItemAdditionalColumns


T = TypeVar("T", bound="TraceItem")


@_attrs_define
class TraceItem:
    """
    Attributes:
        additional_columns (TraceItemAdditionalColumns | Unset):
        client (str | Unset):
        client_namespace (str | Unset):
        cluster (str | Unset):
        container_name (str | Unset):
        env (str | Unset):
        instance_uid (str | Unset):
        is_cross_az (bool | Unset):
        is_encrypted (bool | Unset):
        is_external (bool | Unset):
        is_pii (bool | Unset):
        latency (float | Unset):
        namespace (str | Unset):
        node_name (str | Unset):
        operation_name (str | Unset):
        partner_is_external (bool | Unset):
        partner_namespace (str | Unset):
        partner_workload (str | Unset):
        perspective_entity_resource_id (str | Unset):
        pod_name (str | Unset):
        pod_uid (str | Unset):
        request (TraceDetailsRequestInfo | Unset):
        resource (str | Unset):
        resource_id (str | Unset):
        response (TraceDetailsResponseInfo | Unset):
        role (str | Unset):
        server (str | Unset):
        server_namespace (str | Unset):
        source (str | Unset):
        span_id (str | Unset):
        span_name (str | Unset):
        span_type (str | Unset):
        status (str | Unset):
        status_code (str | Unset):
        status_code_message (str | Unset):
        time (datetime.datetime | Unset):
        trace_id (str | Unset):
        workload (str | Unset):
    """

    additional_columns: TraceItemAdditionalColumns | Unset = UNSET
    client: str | Unset = UNSET
    client_namespace: str | Unset = UNSET
    cluster: str | Unset = UNSET
    container_name: str | Unset = UNSET
    env: str | Unset = UNSET
    instance_uid: str | Unset = UNSET
    is_cross_az: bool | Unset = UNSET
    is_encrypted: bool | Unset = UNSET
    is_external: bool | Unset = UNSET
    is_pii: bool | Unset = UNSET
    latency: float | Unset = UNSET
    namespace: str | Unset = UNSET
    node_name: str | Unset = UNSET
    operation_name: str | Unset = UNSET
    partner_is_external: bool | Unset = UNSET
    partner_namespace: str | Unset = UNSET
    partner_workload: str | Unset = UNSET
    perspective_entity_resource_id: str | Unset = UNSET
    pod_name: str | Unset = UNSET
    pod_uid: str | Unset = UNSET
    request: TraceDetailsRequestInfo | Unset = UNSET
    resource: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    response: TraceDetailsResponseInfo | Unset = UNSET
    role: str | Unset = UNSET
    server: str | Unset = UNSET
    server_namespace: str | Unset = UNSET
    source: str | Unset = UNSET
    span_id: str | Unset = UNSET
    span_name: str | Unset = UNSET
    span_type: str | Unset = UNSET
    status: str | Unset = UNSET
    status_code: str | Unset = UNSET
    status_code_message: str | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    trace_id: str | Unset = UNSET
    workload: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_columns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_columns, Unset):
            additional_columns = self.additional_columns.to_dict()

        client = self.client

        client_namespace = self.client_namespace

        cluster = self.cluster

        container_name = self.container_name

        env = self.env

        instance_uid = self.instance_uid

        is_cross_az = self.is_cross_az

        is_encrypted = self.is_encrypted

        is_external = self.is_external

        is_pii = self.is_pii

        latency = self.latency

        namespace = self.namespace

        node_name = self.node_name

        operation_name = self.operation_name

        partner_is_external = self.partner_is_external

        partner_namespace = self.partner_namespace

        partner_workload = self.partner_workload

        perspective_entity_resource_id = self.perspective_entity_resource_id

        pod_name = self.pod_name

        pod_uid = self.pod_uid

        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        resource = self.resource

        resource_id = self.resource_id

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        role = self.role

        server = self.server

        server_namespace = self.server_namespace

        source = self.source

        span_id = self.span_id

        span_name = self.span_name

        span_type = self.span_type

        status = self.status

        status_code = self.status_code

        status_code_message = self.status_code_message

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        trace_id = self.trace_id

        workload = self.workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_columns is not UNSET:
            field_dict["additionalColumns"] = additional_columns
        if client is not UNSET:
            field_dict["client"] = client
        if client_namespace is not UNSET:
            field_dict["clientNamespace"] = client_namespace
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if container_name is not UNSET:
            field_dict["containerName"] = container_name
        if env is not UNSET:
            field_dict["env"] = env
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if is_cross_az is not UNSET:
            field_dict["isCrossAz"] = is_cross_az
        if is_encrypted is not UNSET:
            field_dict["isEncrypted"] = is_encrypted
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_pii is not UNSET:
            field_dict["isPii"] = is_pii
        if latency is not UNSET:
            field_dict["latency"] = latency
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name
        if partner_is_external is not UNSET:
            field_dict["partnerIsExternal"] = partner_is_external
        if partner_namespace is not UNSET:
            field_dict["partnerNamespace"] = partner_namespace
        if partner_workload is not UNSET:
            field_dict["partnerWorkload"] = partner_workload
        if perspective_entity_resource_id is not UNSET:
            field_dict["perspectiveEntityResourceId"] = perspective_entity_resource_id
        if pod_name is not UNSET:
            field_dict["podName"] = pod_name
        if pod_uid is not UNSET:
            field_dict["podUid"] = pod_uid
        if request is not UNSET:
            field_dict["request"] = request
        if resource is not UNSET:
            field_dict["resource"] = resource
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if response is not UNSET:
            field_dict["response"] = response
        if role is not UNSET:
            field_dict["role"] = role
        if server is not UNSET:
            field_dict["server"] = server
        if server_namespace is not UNSET:
            field_dict["serverNamespace"] = server_namespace
        if source is not UNSET:
            field_dict["source"] = source
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if span_name is not UNSET:
            field_dict["spanName"] = span_name
        if span_type is not UNSET:
            field_dict["spanType"] = span_type
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if status_code_message is not UNSET:
            field_dict["statusCodeMessage"] = status_code_message
        if time is not UNSET:
            field_dict["time"] = time
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_details_request_info import TraceDetailsRequestInfo
        from ..models.trace_details_response_info import TraceDetailsResponseInfo
        from ..models.trace_item_additional_columns import TraceItemAdditionalColumns

        d = dict(src_dict)
        _additional_columns = d.pop("additionalColumns", UNSET)
        additional_columns: TraceItemAdditionalColumns | Unset
        if isinstance(_additional_columns, Unset) or _additional_columns is None:
            additional_columns = UNSET
        else:
            additional_columns = TraceItemAdditionalColumns.from_dict(_additional_columns)

        client = d.pop("client", UNSET)

        client_namespace = d.pop("clientNamespace", UNSET)

        cluster = d.pop("cluster", UNSET)

        container_name = d.pop("containerName", UNSET)

        env = d.pop("env", UNSET)

        instance_uid = d.pop("instanceUid", UNSET)

        is_cross_az = d.pop("isCrossAz", UNSET)

        is_encrypted = d.pop("isEncrypted", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_pii = d.pop("isPii", UNSET)

        latency = d.pop("latency", UNSET)

        namespace = d.pop("namespace", UNSET)

        node_name = d.pop("nodeName", UNSET)

        operation_name = d.pop("operationName", UNSET)

        partner_is_external = d.pop("partnerIsExternal", UNSET)

        partner_namespace = d.pop("partnerNamespace", UNSET)

        partner_workload = d.pop("partnerWorkload", UNSET)

        perspective_entity_resource_id = d.pop("perspectiveEntityResourceId", UNSET)

        pod_name = d.pop("podName", UNSET)

        pod_uid = d.pop("podUid", UNSET)

        _request = d.pop("request", UNSET)
        request: TraceDetailsRequestInfo | Unset
        if isinstance(_request, Unset) or _request is None:
            request = UNSET
        else:
            request = TraceDetailsRequestInfo.from_dict(_request)

        resource = d.pop("resource", UNSET)

        resource_id = d.pop("resourceId", UNSET)

        _response = d.pop("response", UNSET)
        response: TraceDetailsResponseInfo | Unset
        if isinstance(_response, Unset) or _response is None:
            response = UNSET
        else:
            response = TraceDetailsResponseInfo.from_dict(_response)

        role = d.pop("role", UNSET)

        server = d.pop("server", UNSET)

        server_namespace = d.pop("serverNamespace", UNSET)

        source = d.pop("source", UNSET)

        span_id = d.pop("spanId", UNSET)

        span_name = d.pop("spanName", UNSET)

        span_type = d.pop("spanType", UNSET)

        status = d.pop("status", UNSET)

        status_code = d.pop("statusCode", UNSET)

        status_code_message = d.pop("statusCodeMessage", UNSET)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset) or _time is None:
            time = UNSET
        else:
            time = parse_datetime(_time)

        trace_id = d.pop("traceId", UNSET)

        workload = d.pop("workload", UNSET)

        trace_item = cls(
            additional_columns=additional_columns,
            client=client,
            client_namespace=client_namespace,
            cluster=cluster,
            container_name=container_name,
            env=env,
            instance_uid=instance_uid,
            is_cross_az=is_cross_az,
            is_encrypted=is_encrypted,
            is_external=is_external,
            is_pii=is_pii,
            latency=latency,
            namespace=namespace,
            node_name=node_name,
            operation_name=operation_name,
            partner_is_external=partner_is_external,
            partner_namespace=partner_namespace,
            partner_workload=partner_workload,
            perspective_entity_resource_id=perspective_entity_resource_id,
            pod_name=pod_name,
            pod_uid=pod_uid,
            request=request,
            resource=resource,
            resource_id=resource_id,
            response=response,
            role=role,
            server=server,
            server_namespace=server_namespace,
            source=source,
            span_id=span_id,
            span_name=span_name,
            span_type=span_type,
            status=status,
            status_code=status_code,
            status_code_message=status_code_message,
            time=time,
            trace_id=trace_id,
            workload=workload,
        )

        trace_item.additional_properties = d
        return trace_item

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
