"""E2E tests for synthetics endpoints. Mirrors sdk/tests/e2e/synthetics_test.go."""

from __future__ import annotations

import json
import time

import groundcover
from groundcover.api.synthetics import (
    create_synthetic_test,
    delete_synthetic_test,
    get_synthetic_test,
    list_synthetic_tests,
    update_synthetic_test,
)
from groundcover.models.assertion_defines_model_for_assertion import (
    AssertionDefinesModelForAssertion,
)
from groundcover.models.dns_request_defines_model_for_dns_request import (
    DnsRequestDefinesModelForDnsRequest,
)
from groundcover.models.execution_policy_defines_model_for_execution_policy import (
    ExecutionPolicyDefinesModelForExecutionPolicy,
)
from groundcover.models.http_request_defines_model_for_http_request import (
    HttpRequestDefinesModelForHttpRequest,
)
from groundcover.models.metadata_defines_model_for_metadata import (
    MetadataDefinesModelForMetadata,
)
from groundcover.models.request_check_request_configuration_only_one_field_should_be_set_based_on_the_check_kind import (  # noqa: E501
    RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind,
)
from groundcover.models.ssl_request_defines_model_for_ssl_request import (
    SslRequestDefinesModelForSslRequest,
)
from groundcover.models.synthetic_test_create_request import SyntheticTestCreateRequest
from groundcover.models.tcp_request_defines_model_for_tcp_request import (
    TcpRequestDefinesModelForTcpRequest,
)
from groundcover.models.tracing_defines_model_for_tracing import (
    TracingDefinesModelForTracing,
)
from groundcover.models.worker_request_defines_model_for_worker_request import (
    WorkerRequestDefinesModelForWorkerRequest,
)


def _poll_list_for_synthetic(
    gc_client: groundcover.Client,
    synthetic_id: str,
    *,
    should_exist: bool = True,
    expected_name: str | None = None,
    timeout: float = 120.0,
    interval: float = 2.0,
) -> None:
    """Poll the list endpoint until the synthetic test appears/disappears."""
    deadline = time.monotonic() + timeout
    last_error = ""
    while time.monotonic() < deadline:
        result = list_synthetic_tests.sync_detailed(client=gc_client)
        if result.status_code == 200:
            data = json.loads(result.content)
            synthetics = data.get("synthetics", data) if isinstance(data, dict) else data
            found = False
            for item in synthetics or []:
                item_id = item.get("id", "") if isinstance(item, dict) else getattr(item, "id", "")
                if item_id == synthetic_id:
                    if expected_name is not None:
                        item_name = item.get("name", "") if isinstance(item, dict) else getattr(item, "name", "")
                        if item_name != expected_name:
                            continue
                    found = True
                    break
            if found == should_exist:
                return
            last_error = f"synthetic {synthetic_id} {'not found' if should_exist else 'still present'} in list"
        time.sleep(interval)
    raise AssertionError(f"Timed out: {last_error}")


def _make_http_check(name: str) -> WorkerRequestDefinesModelForWorkerRequest:
    return WorkerRequestDefinesModelForWorkerRequest(
        kind="http",
        metadata=MetadataDefinesModelForMetadata(synthetic_name=name),
        request=RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind(
            http=HttpRequestDefinesModelForHttpRequest(
                kind="http",
                method="GET",
                url="https://httpbin.org/get",
                timeout="30s",
            ),
        ),
        execution_policy=ExecutionPolicyDefinesModelForExecutionPolicy(
            assertions=[
                AssertionDefinesModelForAssertion(source="statusCode", operator="eq", target="200"),
            ],
        ),
        tracing=TracingDefinesModelForTracing(),
    )


class TestHTTPSyntheticsLifecycle:
    """Full CRUD lifecycle for HTTP synthetic tests."""

    def test_http_synthetic_crud(self, gc_client: groundcover.Client) -> None:
        synthetic_name = f"sdk-e2e-test-http-synthetic-{time.time_ns()}"
        created_id = None

        try:
            # Create
            create_result = create_synthetic_test.sync_detailed(
                client=gc_client,
                body=SyntheticTestCreateRequest(
                    name=synthetic_name,
                    version=1,
                    enabled=True,
                    interval="5m",
                    check_config=_make_http_check(synthetic_name),
                ),
            )
            assert create_result.status_code == 201
            create_data = json.loads(create_result.content)
            created_id = create_data["id"]
            assert created_id

            # List - poll until visible
            _poll_list_for_synthetic(gc_client, created_id, should_exist=True)

            # Get
            get_result = get_synthetic_test.sync_detailed(created_id, client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["name"] == synthetic_name

            # Update - change name and interval
            updated_name = synthetic_name + "-updated"
            update_result = update_synthetic_test.sync_detailed(
                created_id,
                client=gc_client,
                body=SyntheticTestCreateRequest(
                    name=updated_name,
                    version=1,
                    enabled=True,
                    interval="10m",
                    check_config=_make_http_check(updated_name),
                ),
            )
            assert update_result.status_code == 200

            # Poll list until updated name visible
            _poll_list_for_synthetic(gc_client, created_id, should_exist=True, expected_name=updated_name)

            # Verify update via Get
            get_result = get_synthetic_test.sync_detailed(created_id, client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["name"] == updated_name
            assert get_data["interval"] == "10m"
            assert get_data["checkConfig"]["kind"] == "http"
            assert get_data["checkConfig"]["request"]["http"]["method"] == "GET"
            assert get_data["checkConfig"]["request"]["http"]["url"] == "https://httpbin.org/get"

            # Delete
            delete_result = delete_synthetic_test.sync_detailed(created_id, client=gc_client)
            assert delete_result.status_code == 204

            # Poll until removed
            _poll_list_for_synthetic(gc_client, created_id, should_exist=False)
            created_id = None

        finally:
            if created_id:
                try:
                    delete_synthetic_test.sync_detailed(created_id, client=gc_client)
                except Exception:
                    pass


class TestTCPSyntheticsLifecycle:
    """CRUD lifecycle for TCP synthetic tests."""

    def test_tcp_synthetic_crud(self, gc_client: groundcover.Client) -> None:
        synthetic_name = f"sdk-e2e-test-tcp-synthetic-{time.time_ns()}"
        created_id = None

        try:
            # Create
            create_result = create_synthetic_test.sync_detailed(
                client=gc_client,
                body=SyntheticTestCreateRequest(
                    name=synthetic_name,
                    version=1,
                    enabled=True,
                    interval="5m",
                    check_config=WorkerRequestDefinesModelForWorkerRequest(
                        kind="tcp",
                        metadata=MetadataDefinesModelForMetadata(synthetic_name=synthetic_name),
                        request=RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind(
                            tcp=TcpRequestDefinesModelForTcpRequest(
                                kind="tcp",
                                host="google.com",
                                port=80,
                            ),
                        ),
                        execution_policy=ExecutionPolicyDefinesModelForExecutionPolicy(
                            assertions=[
                                AssertionDefinesModelForAssertion(source="tcp", operator="exists", target="true"),
                            ],
                        ),
                        tracing=TracingDefinesModelForTracing(),
                    ),
                ),
            )
            assert create_result.status_code == 201
            create_data = json.loads(create_result.content)
            created_id = create_data["id"]
            assert created_id

            # Get - verify TCP config
            get_result = get_synthetic_test.sync_detailed(created_id, client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["name"] == synthetic_name
            assert get_data["checkConfig"]["kind"] == "tcp"
            assert get_data["checkConfig"]["request"]["tcp"]["host"] == "google.com"
            assert get_data["checkConfig"]["request"]["tcp"]["port"] == 80

            # Delete
            delete_result = delete_synthetic_test.sync_detailed(created_id, client=gc_client)
            assert delete_result.status_code == 204
            created_id = None

        finally:
            if created_id:
                try:
                    delete_synthetic_test.sync_detailed(created_id, client=gc_client)
                except Exception:
                    pass


class TestSSLSyntheticsLifecycle:
    """CRUD lifecycle for SSL synthetic tests."""

    def test_ssl_synthetic_crud(self, gc_client: groundcover.Client) -> None:
        synthetic_name = f"sdk-e2e-test-ssl-synthetic-{time.time_ns()}"
        created_id = None

        try:
            # Create
            create_result = create_synthetic_test.sync_detailed(
                client=gc_client,
                body=SyntheticTestCreateRequest(
                    name=synthetic_name,
                    version=1,
                    enabled=True,
                    interval="5m",
                    check_config=WorkerRequestDefinesModelForWorkerRequest(
                        kind="ssl",
                        metadata=MetadataDefinesModelForMetadata(synthetic_name=synthetic_name),
                        request=RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind(
                            ssl=SslRequestDefinesModelForSslRequest(
                                kind="ssl",
                                host="google.com",
                                port=443,
                            ),
                        ),
                        execution_policy=ExecutionPolicyDefinesModelForExecutionPolicy(
                            assertions=[
                                AssertionDefinesModelForAssertion(source="ssl", operator="eq", target="true"),
                            ],
                        ),
                        tracing=TracingDefinesModelForTracing(),
                    ),
                ),
            )
            assert create_result.status_code == 201
            create_data = json.loads(create_result.content)
            created_id = create_data["id"]
            assert created_id

            # Get - verify SSL config
            get_result = get_synthetic_test.sync_detailed(created_id, client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["name"] == synthetic_name
            assert get_data["checkConfig"]["kind"] == "ssl"
            assert get_data["checkConfig"]["request"]["ssl"]["host"] == "google.com"
            assert get_data["checkConfig"]["request"]["ssl"]["port"] == 443

            # Delete
            delete_result = delete_synthetic_test.sync_detailed(created_id, client=gc_client)
            assert delete_result.status_code == 204
            created_id = None

        finally:
            if created_id:
                try:
                    delete_synthetic_test.sync_detailed(created_id, client=gc_client)
                except Exception:
                    pass


class TestDNSSyntheticsLifecycle:
    """CRUD lifecycle for DNS synthetic tests."""

    def test_dns_synthetic_crud(self, gc_client: groundcover.Client) -> None:
        synthetic_name = f"sdk-e2e-test-dns-synthetic-{time.time_ns()}"
        created_id = None

        try:
            # Create
            create_result = create_synthetic_test.sync_detailed(
                client=gc_client,
                body=SyntheticTestCreateRequest(
                    name=synthetic_name,
                    version=1,
                    enabled=True,
                    interval="5m",
                    check_config=WorkerRequestDefinesModelForWorkerRequest(
                        kind="dns",
                        metadata=MetadataDefinesModelForMetadata(synthetic_name=synthetic_name),
                        request=RequestCheckRequestConfigurationOnlyOneFieldShouldBeSetBasedOnTheCheckKind(
                            dns=DnsRequestDefinesModelForDnsRequest(
                                kind="dns",
                                domain="google.com",
                                resolver="8.8.8.8",
                                port=53,
                                record_type="A",
                                timeout="30s",
                            ),
                        ),
                        execution_policy=ExecutionPolicyDefinesModelForExecutionPolicy(
                            assertions=[
                                AssertionDefinesModelForAssertion(source="dnsAnswer", operator="exists", target="true"),
                            ],
                        ),
                        tracing=TracingDefinesModelForTracing(),
                    ),
                ),
            )
            assert create_result.status_code == 201
            create_data = json.loads(create_result.content)
            created_id = create_data["id"]
            assert created_id

            # Get - verify DNS config
            get_result = get_synthetic_test.sync_detailed(created_id, client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["name"] == synthetic_name
            assert get_data["checkConfig"]["kind"] == "dns"
            dns_req = get_data["checkConfig"]["request"]["dns"]
            assert dns_req["domain"] == "google.com"
            assert dns_req["resolver"] == "8.8.8.8"
            assert dns_req["port"] == 53
            assert dns_req["recordType"] == "A"

            # Delete
            delete_result = delete_synthetic_test.sync_detailed(created_id, client=gc_client)
            assert delete_result.status_code == 204
            created_id = None

        finally:
            if created_id:
                try:
                    delete_synthetic_test.sync_detailed(created_id, client=gc_client)
                except Exception:
                    pass
