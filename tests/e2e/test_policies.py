"""E2E tests for policies endpoints. Mirrors sdk/tests/e2e/policies_test.go."""

from __future__ import annotations

import json
import time

import groundcover
from groundcover.api.policies import (
    apply_policy,
    create_policy,
    delete_policy,
    get_policy,
    get_policy_audit_trail,
    list_policies,
    update_policy,
)
from groundcover.models.apply_policy_request import ApplyPolicyRequest
from groundcover.models.create_policy_request import CreatePolicyRequest
from groundcover.models.data_scope_contains_either_simple_or_advanced_scope_definitions import (
    DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions,
)
from groundcover.models.role_map_defines_the_mapping_of_roles_to_permissions import (
    RoleMapDefinesTheMappingOfRolesToPermissions,
)
from groundcover.models.update_policy_request import UpdatePolicyRequest


def _make_role(mapping: dict[str, str]) -> RoleMapDefinesTheMappingOfRolesToPermissions:
    role = RoleMapDefinesTheMappingOfRolesToPermissions()
    for k, v in mapping.items():
        role[k] = v
    return role


def test_policy_crud(gc_client: groundcover.Client) -> None:
    """Create, list, get, update, apply, audit trail, and delete a policy."""
    policy_name = f"sdk-e2e-test-policy-{time.time_ns()}"

    # Create
    create_result = create_policy.sync_detailed(
        client=gc_client,
        body=CreatePolicyRequest(
            name=policy_name,
            description="E2E test policy",
            role=_make_role({"write": ""}),
            data_scope=DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions(),
        ),
    )
    assert create_result.status_code == 201
    create_data = json.loads(create_result.content)
    policy_uuid = create_data["uuid"]
    assert policy_uuid

    try:
        # List
        list_result = list_policies.sync_detailed(client=gc_client)
        assert list_result.status_code == 200
        list_data = json.loads(list_result.content)
        if isinstance(list_data, dict):
            list_data = list_data.get("policies", list_data.get("items", []))
        found = any(p.get("uuid") == policy_uuid for p in (list_data or []))
        assert found, f"Policy {policy_uuid} not found in list"

        # Get
        get_result = get_policy.sync_detailed(policy_uuid, client=gc_client)
        assert get_result.status_code == 200
        get_data = json.loads(get_result.content)
        assert get_data["uuid"] == policy_uuid
        assert get_data["name"] == policy_name

        # Update - change description and role
        updated_desc = "E2E test policy - updated"
        update_result = update_policy.sync_detailed(
            policy_uuid,
            client=gc_client,
            body=UpdatePolicyRequest(
                name=policy_name,
                description=updated_desc,
                role=_make_role({"admin": ""}),
                data_scope=DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions(),
                current_revision=1,
            ),
        )
        assert update_result.status_code in (200, 202)

        # Verify update via Get
        get_result = get_policy.sync_detailed(policy_uuid, client=gc_client)
        assert get_result.status_code == 200
        get_data = json.loads(get_result.content)
        assert get_data["uuid"] == policy_uuid
        assert get_data["name"] == policy_name

        # Apply policy to a test email
        apply_result = apply_policy.sync_detailed(
            client=gc_client,
            body=ApplyPolicyRequest(
                policy_uui_ds=[policy_uuid],
                emails=["e2e-test@example.com"],
                override=False,
            ),
        )
        assert apply_result.status_code == 200

        # Get audit trail
        audit_result = get_policy_audit_trail.sync_detailed(policy_uuid, client=gc_client)
        assert audit_result.status_code == 200
        audit_data = json.loads(audit_result.content)
        if isinstance(audit_data, list):
            assert len(audit_data) > 0, "Audit trail should not be empty"
        else:
            # May be wrapped in a dict
            assert audit_data, "Audit trail response should not be empty"

    finally:
        # Delete
        delete_policy.sync_detailed(policy_uuid, client=gc_client)
