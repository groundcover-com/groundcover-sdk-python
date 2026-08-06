"""E2E tests for ingestion keys endpoints. Mirrors sdk/tests/e2e/ingestionkeys_test.go."""

from __future__ import annotations

import json
import time

import groundcover
from groundcover.api.ingestionkeys import create_ingestion_key, delete_ingestion_key, list_ingestion_keys
from groundcover.models.create_ingestion_key_request import CreateIngestionKeyRequest
from groundcover.models.create_ingestion_key_request_type import CreateIngestionKeyRequestType
from groundcover.models.delete_ingestion_key_request import DeleteIngestionKeyRequest
from groundcover.models.list_ingestion_keys_request import ListIngestionKeysRequest

from ._cleanup import ResourceTracker

INGESTION_KEY_TYPE = CreateIngestionKeyRequestType.SENSOR
LIST_TIMEOUT_SECONDS = 10.0


def test_ingestion_key_crud(gc_incloud_client: groundcover.Client, incloud_tracker: ResourceTracker) -> None:
    """Create, list, and delete an ingestion key.

    Runs against an inCloud backend rather than skipping, matching the Go suite
    (``sdk/tests/e2e/ingestionkeys_test.go``) -- these endpoints sit behind
    ``VerifyIncloudBackend`` and are rejected on ``backend-dev``.

    Ingestion keys are addressed by name rather than by id, which is why the tracker
    can clean one up even when the create response is never seen.
    """
    key = incloud_tracker.new("ingestion-key")

    create_result = create_ingestion_key.sync_detailed(
        client=gc_incloud_client,
        body=CreateIngestionKeyRequest(name=key.name, type_=INGESTION_KEY_TYPE),
    )
    assert create_result.status_code == 201
    create_payload = json.loads(create_result.content)
    created_key = create_payload.get("key")
    assert created_key, "Created ingestion key value should not be empty"
    assert create_payload.get("name") == key.name

    # List, filtered by name, polling until it shows up.
    deadline = time.monotonic() + LIST_TIMEOUT_SECONDS
    listed: list = []
    while True:
        list_result = list_ingestion_keys.sync_detailed(
            client=gc_incloud_client,
            body=ListIngestionKeysRequest(name=key.name),
        )
        assert list_result.status_code == 200
        assert list_result.content, "list response body should not be empty"
        listed = json.loads(list_result.content)
        assert isinstance(listed, list), f"expected a list of keys, got {type(listed).__name__}"
        assert all(isinstance(item, dict) for item in listed), "list entries should be objects"
        if listed or time.monotonic() > deadline:
            break
        time.sleep(1)

    assert len(listed) == 1, f"Expected exactly one ingestion key named {key.name}, found {len(listed)}"
    assert listed[0].get("name") == key.name
    assert listed[0].get("type") == INGESTION_KEY_TYPE.value
    assert listed[0].get("key") == created_key

    # Delete by name, the only identifier this endpoint accepts.
    delete_result = delete_ingestion_key.sync_detailed(
        client=gc_incloud_client,
        body=DeleteIngestionKeyRequest(name=key.name),
    )
    # DeleteKey answers 202 and only 202 (ingestionkeys/delete_key.go:87).
    assert delete_result.status_code == 202
    incloud_tracker.forget(key)
