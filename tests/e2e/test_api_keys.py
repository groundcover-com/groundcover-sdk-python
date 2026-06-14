"""E2E tests for API keys endpoints. Mirrors sdk/tests/e2e/apikeys_test.go."""

from __future__ import annotations

import json
import time

import groundcover
from groundcover.api.apikeys import create_api_key, delete_api_key, list_api_keys
from groundcover.api.policies import create_policy, delete_policy
from groundcover.api.serviceaccounts import create_service_account, delete_service_account
from groundcover.models.create_api_key_request import CreateApiKeyRequest
from groundcover.models.create_policy_request import CreatePolicyRequest
from groundcover.models.create_service_account_request import CreateServiceAccountRequest
from groundcover.models.data_scope_contains_either_simple_or_advanced_scope_definitions import (
    DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions,
)
from groundcover.models.role_map_defines_the_mapping_of_roles_to_permissions import (
    RoleMapDefinesTheMappingOfRolesToPermissions,
)


def _make_role(mapping: dict[str, str]) -> RoleMapDefinesTheMappingOfRolesToPermissions:
    role = RoleMapDefinesTheMappingOfRolesToPermissions()
    for k, v in mapping.items():
        role[k] = v
    return role


class TestAPIKeysLifecycle:
    """CRUD lifecycle for API keys (requires policy + service account as prerequisites)."""

    def test_apikey_crud(self, gc_client: groundcover.Client) -> None:
        ts = time.time_ns()

        # Step 1: Create policy prerequisite
        policy_name = f"sdk-e2e-test-policy-for-apikey-{ts}"
        policy_result = create_policy.sync_detailed(
            client=gc_client,
            body=CreatePolicyRequest(
                name=policy_name,
                description="Policy for API Keys E2E testing",
                role=_make_role({"admin": "admin"}),
                data_scope=DataScopeContainsEitherSimpleOrAdvancedScopeDefinitions(),
            ),
        )
        assert policy_result.status_code == 201
        policy_data = json.loads(policy_result.content)
        policy_uuid = policy_data["uuid"]

        try:
            # Step 2: Create service account prerequisite
            sa_name = f"sdk-e2e-test-sa-for-apikey-{ts}"
            sa_result = create_service_account.sync_detailed(
                client=gc_client,
                body=CreateServiceAccountRequest(
                    name=sa_name,
                    email="sdk-e2e-test@groundcover.com",
                    policy_uui_ds=[policy_uuid],
                ),
            )
            assert sa_result.status_code == 200
            sa_data = json.loads(sa_result.content)
            sa_id = sa_data["serviceAccountId"]

            try:
                # Create API key
                apikey_name = f"sdk-e2e-test-apikey-{ts}"
                create_result = create_api_key.sync_detailed(
                    client=gc_client,
                    body=CreateApiKeyRequest(
                        name=apikey_name,
                        service_account_id=sa_id,
                        description="Created by SDK E2E test",
                    ),
                )
                assert create_result.status_code == 200
                create_data = json.loads(create_result.content)
                apikey_id = create_data["id"]
                assert apikey_id
                assert create_data.get("apiKey"), "API Key token should not be empty"

                # List and verify
                list_result = list_api_keys.sync_detailed(client=gc_client)
                list_data = json.loads(list_result.content)
                if isinstance(list_data, dict):
                    list_data = list_data.get("apiKeys", list_data.get("items", []))
                found = any(k.get("id") == apikey_id for k in (list_data or []))
                assert found, f"API Key {apikey_id} not found in list"

                # Delete API key
                delete_api_key.sync_detailed(apikey_id, client=gc_client)

                # Verify deletion (should be revoked, not in default list)
                list_after = list_api_keys.sync_detailed(client=gc_client)
                list_after_data = json.loads(list_after.content)
                if isinstance(list_after_data, dict):
                    list_after_data = list_after_data.get("apiKeys", list_after_data.get("items", []))
                found_after = any(k.get("id") == apikey_id for k in (list_after_data or []))
                assert not found_after, "Deleted API key should not appear in default list"

            finally:
                # Cleanup: delete service account
                try:
                    delete_service_account.sync_detailed(sa_id, client=gc_client)
                except Exception:
                    pass
        finally:
            # Cleanup: delete policy
            try:
                delete_policy.sync_detailed(policy_uuid, client=gc_client)
            except Exception:
                pass
