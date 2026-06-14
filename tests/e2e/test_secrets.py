"""E2E tests for secrets endpoints. Mirrors sdk/tests/e2e/secrets_test.go."""

from __future__ import annotations

import json
import time

import pytest

import groundcover
from groundcover.api.secret import create_secret, delete_secret, get_secret_hash, update_secret
from groundcover.exceptions import APIError
from groundcover.models.create_secret_request import CreateSecretRequest
from groundcover.models.create_secret_request_managed_by_provider import (
    CreateSecretRequestManagedByProvider,
)
from groundcover.models.update_secret_request import UpdateSecretRequest


class TestSecretsLifecycle:
    """CRUD lifecycle for secrets."""

    def test_secret_crud(self, gc_client: groundcover.Client) -> None:
        secret_name = f"sdk-e2e-test-secret-{time.time_ns()}"

        # Create
        create_result = create_secret.sync_detailed(
            client=gc_client,
            body=CreateSecretRequest(
                name=secret_name,
                type_="api_key",
                content="test-secret-content",
            ),
        )
        assert create_result.status_code == 201
        create_data = json.loads(create_result.content)
        secret_id = create_data["id"]
        assert secret_id
        assert create_data["name"] == secret_name
        assert create_data["type"] == "api_key"

        try:
            # Update
            update_result = update_secret.sync_detailed(
                secret_id,
                client=gc_client,
                body=UpdateSecretRequest(
                    name=secret_name,
                    type_="api_key",
                    content="updated-secret-content",
                ),
            )
            assert update_result.status_code == 200
            update_data = json.loads(update_result.content)
            assert update_data["id"] == secret_id

            # Get hash
            try:
                hash_result = get_secret_hash.sync_detailed(secret_id, client=gc_client)
                hash_data = json.loads(hash_result.content)
                assert hash_data["id"] == secret_id
                assert hash_data.get("contentHash"), "ContentHash should not be empty"
            except groundcover.NotFoundError:
                pytest.skip("GetSecretHash endpoint not available yet")

        finally:
            # Delete
            delete_secret.sync_detailed(secret_id, client=gc_client)

    def test_secret_types(self, gc_client: groundcover.Client) -> None:
        """Test creating secrets with different types."""
        created_ids = []

        try:
            for secret_type in ("api_key", "password", "basic_auth"):
                name = f"sdk-e2e-test-secret-{time.time_ns()}-{secret_type}"
                result = create_secret.sync_detailed(
                    client=gc_client,
                    body=CreateSecretRequest(
                        name=name,
                        type_=secret_type,
                        content="test-content",
                    ),
                )
                assert result.status_code == 201
                data = json.loads(result.content)
                assert data["type"] == secret_type
                created_ids.append(data["id"])
        finally:
            for sid in created_ids:
                try:
                    delete_secret.sync_detailed(sid, client=gc_client)
                except Exception:
                    pass

    def test_create_secret_with_managed_provider(self, gc_client: groundcover.Client) -> None:
        """Test creating a secret with a managed-by provider."""
        secret_name = f"sdk-e2e-test-secret-{time.time_ns()}-terraform"
        created_id = None

        try:
            create_result = create_secret.sync_detailed(
                client=gc_client,
                body=CreateSecretRequest(
                    name=secret_name,
                    type_="api_key",
                    content="terraform-managed-secret",
                    managed_by_provider=CreateSecretRequestManagedByProvider.TERRAFORM,
                ),
            )
            assert create_result.status_code == 201
            create_data = json.loads(create_result.content)
            created_id = create_data["id"]
            assert created_id
        finally:
            if created_id:
                try:
                    delete_secret.sync_detailed(created_id, client=gc_client)
                except Exception:
                    pass

    def test_update_nonexistent_secret(self, gc_client: groundcover.Client) -> None:
        with pytest.raises(APIError):
            update_secret.sync_detailed(
                "secretRef::store::00000000-0000-0000-0000-000000000000",
                client=gc_client,
                body=UpdateSecretRequest(
                    name="non-existent",
                    type_="api_key",
                    content="test",
                ),
            )

    def test_delete_nonexistent_secret(self, gc_client: groundcover.Client) -> None:
        with pytest.raises(APIError):
            delete_secret.sync_detailed(
                "secretRef::store::00000000-0000-0000-0000-000000000000",
                client=gc_client,
            )

    def test_get_hash_nonexistent_secret(self, gc_client: groundcover.Client) -> None:
        """Get hash of a non-existent secret should fail."""
        try:
            result = get_secret_hash.sync_detailed(
                "secretRef::store::00000000-0000-0000-0000-000000000000",
                client=gc_client,
            )
            # If no exception raised, the endpoint returned an error status
            assert result.status_code >= 400, (
                f"Expected error status for non-existent secret hash, got {result.status_code}"
            )
        except (APIError, groundcover.NotFoundError):
            pass  # Expected
