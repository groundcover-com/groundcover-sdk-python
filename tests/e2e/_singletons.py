"""Snapshot-and-restore for the four tenant-wide singleton configs.

The logs/traces/metrics pipeline configs and the metrics aggregator config have
no resource id -- there is exactly one per tenant. So a test that "cleans up" by
deleting one does not remove *its* resource, it destroys the tenant's real
configuration. On the shared tenant the suite runs against, that is worse than a
leak. These tests must snapshot the config first and put it back afterwards.

The restore rule follows from how the backend implements DELETE:

* ``DeleteConfig`` writes a NEW revision whose value is empty rather than
  removing anything (``pipelines/logs/config.go:121-141``,
  ``aggregations/metrics/config.go``). GET answers 204 only if a config never
  existed at all (``pipelines/common/config_read.go:26``).
* Create/update bodies declare ``Value string `json:"value" binding:"required"```
  (``pipelines/logs/config.go:49``), so an empty value cannot be written back
  with PUT.

Therefore: **snapshot non-empty -> PUT it back; snapshot absent or empty ->
DELETE.** (Once a config has existed, "never existed" is not reachable again; an
empty revision is the closest state and is what these tests already leave.)
"""

from __future__ import annotations

import dataclasses
import json
import logging
from typing import Any, Callable, Dict, Optional, Sequence, Type

import groundcover

logger = logging.getLogger(__name__)

# Type of the `singleton` fixture: (kind, markers=...) -> the snapshotted payload.
SingletonFixture = Callable[..., Optional[Any]]


@dataclasses.dataclass(frozen=True)
class SingletonSpec:
    path: str
    # Response/request field holding the config: a YAML string for three of them,
    # a structured relabel object for the metrics pipeline.
    payload_key: str
    # Expected type of that field. Checked before a restore is registered, because
    # whatever is captured here is what teardown writes back verbatim.
    payload_type: Type[Any]


SINGLETONS: Dict[str, SingletonSpec] = {
    "logs-pipeline": SingletonSpec("/api/pipelines/logs/config", "value", str),
    "traces-pipeline": SingletonSpec("/api/pipelines/traces/config", "value", str),
    "metrics-pipeline": SingletonSpec("/api/pipelines/v1/metrics/config", "rules", dict),
    "metrics-aggregator": SingletonSpec("/api/aggregations/v1/metrics/config", "value", str),
}


def snapshot(client: groundcover.Client, kind: str) -> Optional[Any]:
    """Return the tenant's current config payload, or None if there isn't one.

    Absent means: a documented 204, an empty body, or a config envelope that omits
    the payload key. That last case is real, not defensive -- once a config has been
    deleted, `GET /api/pipelines/v1/metrics/config` answers 200 with only
    ``{uuid, created_by, created_timestamp}`` and no ``rules`` at all.

    A payload that is not an object does raise: mistaking an unreadable response for
    "no config" would make the finalizer DELETE a configuration that exists, which is
    worse than leaking. An error status raises earlier, via the client's response hook.
    """
    spec = SINGLETONS[kind]
    response = client.get(spec.path)
    if response.status_code == 204 or not response.content:
        return None
    payload = response.json()
    if not isinstance(payload, dict):
        raise RuntimeError("unexpected {} config response: {}".format(kind, type(payload).__name__))
    value = payload.get(spec.payload_key)
    if value is not None and not isinstance(value, spec.payload_type):
        # Whatever is captured here is written back verbatim at teardown, so refuse to
        # carry a payload we do not recognise rather than replay it into the config.
        raise RuntimeError(
            "unexpected {} config {!r}: expected {}, got {}".format(
                kind, spec.payload_key, spec.payload_type.__name__, type(value).__name__
            )
        )
    return value


def restore(
    client: groundcover.Client,
    kind: str,
    snapshotted: Optional[Any],
    markers: Sequence[str] = (),
) -> None:
    """Put the tenant's config back to ``snapshotted``.

    ``None`` means there was no config, so DELETE (which the backend implements as
    an empty revision). An empty-but-present payload -- ``""`` or ``{}`` -- is also
    restored by DELETE, since the update endpoint rejects an empty value; anything
    non-empty is PUT back verbatim.

    Re-reads first and stands down if a non-test config is already in place. These
    routes have no compare-and-swap, so a blind write can clobber whatever landed
    while this test ran; if real config is back, a stale snapshot is the wrong thing
    to reinstate. That narrows the race rather than closing it -- closing it needs a
    precondition on the endpoint.
    """
    spec = SINGLETONS[kind]
    current = snapshot(client, kind)
    if current and not looks_like_test_payload(current, markers):
        logger.warning(
            "e2e cleanup: leaving %s config alone -- it no longer holds a test payload, "
            "so restoring this run's snapshot would overwrite it",
            kind,
        )
        return
    if snapshotted:
        client.put(spec.path, json={spec.payload_key: snapshotted})
    else:
        client.delete(spec.path)


# Tokens that identify a *test* payload sitting in a tenant singleton -- this suite's
# and the Go suite's, because both write these same four configs and the two jobs run
# in parallel in the same CI workflow (.github/workflows/sdk-test.yml).
#
# The Go tokens are its literal fixtures (sdk/tests/e2e/logspipeline_test.go:13,
# metricsaggregator_test.go:13, metricspipeline_test.go:19). They are generic enough
# that a real tenant config could contain one and skip the lifecycle test -- that
# tradeoff is deliberate. A skip is visible and recoverable; failing to recognise a
# foreign test payload means the finalizer PUTs it back and it becomes the shared
# tenant's permanent configuration. So this errs toward skipping, never toward
# restoring someone else's test data.
SUITE_MARKERS = (
    # this suite
    "sdk-e2e-test",
    "sdk_e2e_test",
    # Go suite: logs/traces pipelines
    "example-rule",
    "test.key",
    # Go suite: metrics aggregator
    "test_metric_counter",
    "test_metric_latency",
    # Go suite: metrics pipeline relabel rules
    "http_requests_total",
    "process_cpu_seconds_total",
)


def looks_like_test_payload(snapshotted: Optional[Any], markers: Sequence[str]) -> bool:
    """Whether a snapshot appears to be a payload this suite itself writes.

    Used to detect a concurrent suite run holding the singleton: if we snapshot
    another run's test payload we would "restore" it as the tenant's permanent
    config. There is no lock API for these endpoints, so the safe move is to
    detect and skip rather than to coordinate. Heuristic by construction -- it
    matches on strings that only appear in this suite's fixtures.
    """
    if not snapshotted:
        return False
    blob = snapshotted if isinstance(snapshotted, str) else json.dumps(snapshotted)
    return any(marker in blob for marker in markers)
