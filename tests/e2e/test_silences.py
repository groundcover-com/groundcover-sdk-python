"""E2E tests for silences endpoints. Mirrors sdk/tests/e2e/silences_test.go."""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timedelta, timezone

import pytest

import groundcover
from groundcover.api.monitors import (
    create_silence,
    delete_silence,
    get_all_silences,
    get_silence,
    update_silence,
)
from groundcover.exceptions import NotFoundError
from groundcover.models.create_silence_request import CreateSilenceRequest
from groundcover.models.silence_matcher import SilenceMatcher
from groundcover.models.update_silence_request import UpdateSilenceRequest


class TestSilencesLifecycle:
    """CRUD lifecycle for silences."""

    def test_silence_crud(self, gc_client: groundcover.Client) -> None:
        now = datetime.now(timezone.utc)
        silence_comment = f"e2e-test-silence-{uuid.uuid4()}"

        # Create
        create_result = create_silence.sync_detailed(
            client=gc_client,
            body=CreateSilenceRequest(
                starts_at=now + timedelta(minutes=1),
                ends_at=now + timedelta(hours=1, minutes=1),
                matchers=[
                    SilenceMatcher(is_equal=True, is_regex=False, name="service", value="test-equal"),
                    SilenceMatcher(is_equal=False, is_regex=True, name="environment", value="*test-not-equal-regex*"),
                    SilenceMatcher(is_equal=True, is_regex=False, name="workload", value="test-empty-equal"),
                ],
                comment=silence_comment,
            ),
        )
        assert create_result.status_code == 200
        create_data = json.loads(create_result.content)
        silence_id = create_data["id"]
        assert silence_id

        try:
            # Get
            get_result = get_silence.sync_detailed(silence_id, client=gc_client)
            assert get_result.status_code == 200
            get_data = json.loads(get_result.content)
            assert get_data["id"] == silence_id
            assert get_data["comment"] == silence_comment
            assert len(get_data.get("matchers", [])) > 0

            # List all
            list_result = get_all_silences.sync_detailed(client=gc_client)
            assert list_result.status_code == 200
            list_data = json.loads(list_result.content)
            if isinstance(list_data, dict):
                list_data = list_data.get("silences", list_data.get("items", []))
            found = any(s.get("id") == silence_id for s in (list_data or []))
            assert found, f"Created silence {silence_id} not found in list"

            # Update
            updated_comment = "Updated silence comment during E2E testing"
            update_result = update_silence.sync_detailed(
                silence_id,
                client=gc_client,
                body=UpdateSilenceRequest(
                    starts_at=now + timedelta(minutes=2),
                    ends_at=now + timedelta(hours=2, minutes=2),
                    comment=updated_comment,
                    matchers=[
                        SilenceMatcher(is_equal=True, is_regex=False, name="service", value="updated-test-service"),
                        SilenceMatcher(is_equal=True, is_regex=False, name="environment", value="production"),
                    ],
                ),
            )
            assert update_result.status_code == 200

            # Verify update
            get_updated = get_silence.sync_detailed(silence_id, client=gc_client)
            assert get_updated.status_code == 200
            updated_data = json.loads(get_updated.content)
            assert updated_data["comment"] == updated_comment

        finally:
            # Delete
            delete_result = delete_silence.sync_detailed(silence_id, client=gc_client)
            assert delete_result.status_code == 200

        # Verify deletion
        with pytest.raises(NotFoundError):
            get_silence.sync_detailed(silence_id, client=gc_client)
