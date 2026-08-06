"""E2E tests for API keys endpoints. Mirrors sdk/tests/e2e/apikeys_test.go."""

from __future__ import annotations

import json

import groundcover
from groundcover.api.apikeys import create_api_key, delete_api_key, list_api_keys
from groundcover.api.policies import create_policy
from groundcover.api.serviceaccounts import create_service_account
from groundcover.models.create_api_key_request import CreateApiKeyRequest
from groundcover.models.create_policy_request import CreatePolicyRequest
from groundcover.models.create_service_account_request import CreateServiceAccountRequest
from groundcover.models.data_scope_contains_either_simple_or_advanced_scope_definitions import (
    DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions,
)
from groundcover.models.role_map_defines_the_mapping_of_roles_to_permissions import (
    RoleMapDefinesTheMappingOfRolesToPermissions,
)

from ._cleanup import ResourceTracker


def _make_role(mapping: dict[str, str]) -> RoleMapDefinesTheMappingOfRolesToPermissions:
    role = RoleMapDefinesTheMappingOfRolesToPermissions()
    for k, v in mapping.items():
        role[k] = v
    return role


class TestAPIKeysLifecycle:
    """CRUD lifecycle for API keys (requires policy + service account as prerequisites)."""

    def test_apikey_crud(self, gc_client: groundcover.Client, tracker: ResourceTracker) -> None:
        # Step 1: Create policy prerequisite
        policy = tracker.new("policy")
        policy_result = create_policy.sync_detailed(
            client=gc_client,
            body=CreatePolicyRequest(
                name=policy.name,
                description="Policy for API Keys E2E testing",
                role=_make_role({"admin": "admin"}),
                data_scope=DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions(),
            ),
        )
        assert policy_result.status_code == 201
        policy_data = json.loads(policy_result.content)
        policy.resource_id = policy_data["uuid"]

        # Step 2: Create service account prerequisite
        service_account = tracker.new("service-account")
        sa_result = create_service_account.sync_detailed(
            client=gc_client,
            body=CreateServiceAccountRequest(
                name=service_account.name,
                email=f"{service_account.name}@groundcover.com",
                policy_uui_ds=[policy.resource_id],
            ),
        )
        assert sa_result.status_code == 200
        sa_data = json.loads(sa_result.content)
        service_account.resource_id = sa_data["serviceAccountId"]

        # Create API key
        api_key = tracker.new("api-key")
        create_result = create_api_key.sync_detailed(
            client=gc_client,
            body=CreateApiKeyRequest(
                name=api_key.name,
                service_account_id=service_account.resource_id,
                description="Created by SDK E2E test",
            ),
        )
        assert create_result.status_code == 200
        create_data = json.loads(create_result.content)
        api_key.resource_id = create_data["id"]
        assert api_key.resource_id
        assert create_data.get("apiKey"), "API Key token should not be empty"

        # List and verify
        list_result = list_api_keys.sync_detailed(client=gc_client)
        list_data = json.loads(list_result.content)
        if isinstance(list_data, dict):
            list_data = list_data.get("apiKeys", list_data.get("items", []))
        found = any(k.get("id") == api_key.resource_id for k in (list_data or []))
        assert found, f"API Key {api_key.resource_id} not found in list"

        # Delete API key
        delete_api_key.sync_detailed(api_key.resource_id, client=gc_client)
        tracker.forget(api_key)

        # Verify deletion (should be revoked, not in default list)
        list_after = list_api_keys.sync_detailed(client=gc_client)
        list_after_data = json.loads(list_after.content)
        if isinstance(list_after_data, dict):
            list_after_data = list_after_data.get("apiKeys", list_after_data.get("items", []))
        found_after = any(k.get("id") == api_key.resource_id for k in (list_after_data or []))
        assert not found_after, "Deleted API key should not appear in default list"
