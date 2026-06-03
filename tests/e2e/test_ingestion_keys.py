"""E2E tests for ingestion keys endpoints. Mirrors sdk/tests/e2e/ingestionkeys_test.go."""

from __future__ import annotations

import time

import pytest

import groundcover


def test_ingestion_key_crud(gc_client: groundcover.Client) -> None:
    """Create, list, and delete an ingestion key.

    Uses raw HTTP methods because the generated models require fields (``type_``)
    that the backend treats as optional, and the delete endpoint accepts ``id``
    rather than the ``name`` field expected by the generated model.
    """
    key_name = f"sdk-e2e-test-ingestion-key-{time.time_ns()}"

    # Create
    try:
        create_resp = gc_client.post(
            "/api/rbac/ingestion-keys/create",
            json={"name": key_name},
        )
    except Exception as exc:
        if "inCloud backends" in str(exc):
            pytest.skip("Ingestion keys not supported on inCloud backends")
        raise

    assert create_resp.status_code == 200
    create_payload = create_resp.json()
    key_id = create_payload.get("id") or create_payload.get("keyId")
    assert key_id, "Ingestion key ID should not be empty"

    try:
        # List
        list_resp = gc_client.get("/api/rbac/ingestion-keys/list")
        assert list_resp.status_code == 200
    finally:
        # Delete
        gc_client.post(
            "/api/rbac/ingestion-keys/delete",
            json={"id": key_id},
        )
