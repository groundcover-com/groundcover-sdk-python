"""E2E tests for silences endpoints. Mirrors sdk/tests/e2e/silences_test.go."""

from __future__ import annotations

import json
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

from ._cleanup import ResourceTracker


class TestSilencesLifecycle:
    """CRUD lifecycle for silences."""

    def test_silence_crud(self, gc_client: groundcover.Client, tracker: ResourceTracker) -> None:
        now = datetime.now(timezone.utc)
        # Silences have no name field, so the suite's unique name goes in the
        # comment -- that is what cleanup matches on to recover the id.
        silence = tracker.new("silence")
        silence_comment = silence.name

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
        silence.resource_id = str(create_data["id"])
        silence_id = silence.resource_id
        assert silence_id

        # Get
        get_result = get_silence.sync_detailed(silence_id, client=gc_client)
        assert get_result.status_code == 200
        get_data = json.loads(get_result.content)
        assert str(get_data["id"]) == silence_id
        assert get_data["comment"] == silence_comment
        assert len(get_data.get("matchers", [])) > 0

        # List all
        list_result = get_all_silences.sync_detailed(client=gc_client)
        assert list_result.status_code == 200
        list_data = json.loads(list_result.content)
        if isinstance(list_data, dict):
            list_data = list_data.get("silences", list_data.get("items", []))
        found = any(str(s.get("id")) == silence_id for s in (list_data or []))
        assert found, f"Created silence {silence_id} not found in list"

        # Update
        # Keep the suite's unique name in the comment so the silence stays
        # identifiable as test debris even after the update.
        updated_comment = f"{silence.name}-updated"
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

        # Delete
        delete_result = delete_silence.sync_detailed(silence_id, client=gc_client)
        assert delete_result.status_code == 200
        tracker.forget(silence)

        # Verify deletion
        with pytest.raises(NotFoundError):
            get_silence.sync_detailed(silence_id, client=gc_client)
