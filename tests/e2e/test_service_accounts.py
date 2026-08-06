"""E2E tests for service accounts endpoints. Mirrors sdk/tests/e2e/serviceaccounts_test.go."""

from __future__ import annotations

import json

import groundcover
from groundcover.api.policies import create_policy
from groundcover.api.serviceaccounts import (
    create_service_account,
    delete_service_account,
    list_service_accounts,
    update_service_account,
)
from groundcover.models.create_policy_request import CreatePolicyRequest
from groundcover.models.create_service_account_request import CreateServiceAccountRequest
from groundcover.models.data_scope_contains_either_simple_or_advanced_scope_definitions import (
    DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions,
)
from groundcover.models.role_map_defines_the_mapping_of_roles_to_permissions import (
    RoleMapDefinesTheMappingOfRolesToPermissions,
)
from groundcover.models.update_service_account_request import UpdateServiceAccountRequest

from ._cleanup import ResourceTracker


def _make_role(mapping: dict[str, str]) -> RoleMapDefinesTheMappingOfRolesToPermissions:
    role = RoleMapDefinesTheMappingOfRolesToPermissions()
    for k, v in mapping.items():
        role[k] = v
    return role


def _create_test_policy(gc_client: groundcover.Client, tracker: ResourceTracker) -> str:
    """Create a temporary policy and return its UUID."""
    policy = tracker.new("policy")
    policy_result = create_policy.sync_detailed(
        client=gc_client,
        body=CreatePolicyRequest(
            name=policy.name,
            description="Policy for SA E2E testing",
            role=_make_role({"write": ""}),
            data_scope=DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions(),
        ),
    )
    assert policy_result.status_code == 201
    policy_data = json.loads(policy_result.content)
    policy.resource_id = policy_data["uuid"]
    return policy.resource_id


def test_service_account_crud(gc_client: groundcover.Client, tracker: ResourceTracker) -> None:
    """Create, list, update (with verification), and delete a service account."""
    # Create two policies: one for initial assignment, one for update
    policy_uuid = _create_test_policy(gc_client, tracker)
    second_policy_uuid = _create_test_policy(gc_client, tracker)

    # Create service account
    service_account = tracker.new("service-account")
    sa_result = create_service_account.sync_detailed(
        client=gc_client,
        body=CreateServiceAccountRequest(
            name=service_account.name,
            email=f"{service_account.name}@groundcover.com",
            policy_uui_ds=[policy_uuid],
        ),
    )
    assert sa_result.status_code == 200
    sa_data = json.loads(sa_result.content)
    service_account.resource_id = sa_data["serviceAccountId"]
    sa_id = service_account.resource_id

    # List - verify presence
    list_result = list_service_accounts.sync_detailed(client=gc_client)
    assert list_result.status_code == 200
    list_data = json.loads(list_result.content)
    if isinstance(list_data, dict):
        list_data = list_data.get("serviceAccounts", list_data.get("items", []))
    found = any(sa.get("serviceAccountId") == sa_id for sa in (list_data or []))
    assert found, f"Service account {sa_id} not found in list"

    # Update - change email and add second policy
    updated_email = f"{service_account.name}-updated@groundcover.com"
    update_service_account.sync_detailed(
        client=gc_client,
        body=UpdateServiceAccountRequest(
            service_account_id=sa_id,
            email=updated_email,
            policy_uui_ds=[second_policy_uuid],
        ),
    )

    # Verify update via List
    list_result = list_service_accounts.sync_detailed(client=gc_client)
    assert list_result.status_code == 200
    list_data = json.loads(list_result.content)
    if isinstance(list_data, dict):
        list_data = list_data.get("serviceAccounts", list_data.get("items", []))
    found_updated = False
    for sa in list_data or []:
        if sa.get("serviceAccountId") == sa_id:
            found_updated = True
            assert sa.get("email") == updated_email, f"Expected email {updated_email}, got {sa.get('email')}"
            # Verify policies include the second policy
            policy_uuids = {p.get("uuid") for p in sa.get("policies", []) if isinstance(p, dict)}
            assert second_policy_uuid in policy_uuids, f"Second policy {second_policy_uuid} missing after update"
            break
    assert found_updated, f"Updated service account {sa_id} not found in list"

    # Delete service account
    delete_service_account.sync_detailed(sa_id, client=gc_client)
    tracker.forget(service_account)
