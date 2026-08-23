"""Per-test resource cleanup for the E2E suite.

Every resource these tests create lands on a shared live tenant, so it has to be
removed even when the test aborts before its own delete step. The Go suite gets
this from ``TestClient.Cleanup()`` plus ``Track*``/``Untrack*`` and a kind-enum
switch (``sdk/tests/e2e/setup.go``). This is the same guarantee with one
primitive: a registry of resources, drained on fixture teardown.

Four deliberate departures from the Go harness:

* **Register before the create, not after.** ``tracker.new()`` mints the name and
  registers the resource *before* the create request is sent, so a create that
  commits server-side while the client sees a 502 is still cleaned up: teardown
  recovers the id by listing and matching the unique name. Registering after the
  create (Go's ``Track*``) structurally cannot catch that case -- it is the
  orphan class ``sdk-python/tools/gc_e2e_janitor`` exists to mop up.
* **No ``untrack``.** "Already gone" is swallowed, so a test deleting its own
  resource needs no bookkeeping and a redundant delete is a no-op.
* **LIFO within a dependency rank, not FIFO.** Go drains in creation order
  (``setup.go:232``), which deletes a policy before the service account that
  references it. Lower ``rank`` tears down first.
* **Cleanup failures fail the test.** Go only ``t.Logf``s them (``setup.go:234``),
  which makes a leak invisible. A resource we could not delete raises out of
  teardown as an ERROR.
"""

from __future__ import annotations

import dataclasses
import logging
from typing import Any, Callable, Dict, List, Optional, Set

import groundcover
from groundcover.api.apikeys import delete_api_key
from groundcover.api.dashboards import delete_dashboard
from groundcover.api.ingestionkeys import delete_ingestion_key
from groundcover.api.integrations import delete_data_integration_config
from groundcover.api.monitors import delete_monitor, delete_silence
from groundcover.api.policies import delete_policy
from groundcover.api.secret import delete_secret
from groundcover.api.serviceaccounts import delete_service_account
from groundcover.api.synthetics import delete_synthetic_test
from groundcover.exceptions import APIError
from groundcover.models.delete_ingestion_key_request import DeleteIngestionKeyRequest

from ._names import unique_name

logger = logging.getLogger(__name__)

# 404 means the resource is not there any more, which is a cleanup success: the
# normal case when the test deleted it itself.
GONE_STATUSES = (404,)

# Nothing else counts as "gone". 400 in particular does not: it is how a request gets
# rejected outright, and the one kind that appeared to need it (ingestion keys) only
# answered 400 because the test was hitting a non-inCloud backend. Against a real
# inCloud backend that delete answers 404 like everything else, so the special case is
# gone -- and a 400 now surfaces, which is what should happen if cleanup ever targets
# the wrong backend again.


@dataclasses.dataclass
class ResourceHandle:
    """A resource this test is responsible for deleting.

    ``name`` is minted before the create request; ``resource_id`` is filled in by
    the test from the create response. Teardown deletes by id when it has one and
    falls back to resolving the id from ``name`` when it does not.
    """

    kind: str
    name: str
    resource_id: Optional[str] = None
    extra: Dict[str, Any] = dataclasses.field(default_factory=dict)


@dataclasses.dataclass(frozen=True)
class _Lister:
    """How to find a resource's id from its name, for the ID-less sad path."""

    method: str
    path: str
    id_field: str
    name_field: str
    container: Optional[str] = None
    params: Optional[Dict[str, Any]] = None
    body: Optional[Dict[str, Any]] = None
    # Set for endpoints that cap their response: the lister then pages with
    # skip/limit until a short page comes back. Without this, a resource beyond
    # the cap is invisible to recovery -- backend-dev already holds more monitors
    # than one page (`done: false` at limit 1000), and silences default to
    # `SilencesDefaultLimit = 1000` (internal/monitors/monitors.go:139).
    # Paging goes in the query string for GET and in the body otherwise.
    page_size: Optional[int] = None


# A paginated lister will not fetch more than this many pages, so a server that
# ignores `skip` cannot spin here forever.
_MAX_PAGES = 100


@dataclasses.dataclass(frozen=True)
class _Spec:
    delete: Callable[[groundcover.Client, ResourceHandle], None]
    # Lower rank is torn down first. Dependents rank below what they reference so
    # ordering holds even if a test creates them in an odd order:
    #   api key -> service account -> policy, and everything -> secret.
    rank: int = 50
    lister: Optional[_Lister] = None
    # False when the delete addresses the resource by name, so no id is needed and
    # cleanup can run even if the create response was never seen (ingestion keys).
    id_required: bool = True


def _delete_data_integration(client: groundcover.Client, handle: ResourceHandle) -> None:
    delete_data_integration_config.sync_detailed(handle.extra["type"], handle.resource_id, client=client)


def _delete_ingestion_key(client: groundcover.Client, handle: ResourceHandle) -> None:
    # Ingestion keys are addressed by name, never by id -- the one kind that is
    # fully cleanable even when the create response was never seen.
    delete_ingestion_key.sync_detailed(client=client, body=DeleteIngestionKeyRequest(name=handle.name))


_SYNTHETIC_SPEC = _Spec(
    delete=lambda client, h: delete_synthetic_test.sync_detailed(h.resource_id, client=client),
    lister=_Lister(
        method="GET",
        path="/api/synthetics/v1/rules",
        container="synthetics",
        id_field="id",
        name_field="name",
    ),
)

SPECS: Dict[str, _Spec] = {
    "dashboard": _Spec(
        delete=lambda client, h: delete_dashboard.sync_detailed(h.resource_id, client=client),
        lister=_Lister(method="GET", path="/api/dashboards", id_field="uuid", name_field="name"),
    ),
    "monitor": _Spec(
        delete=lambda client, h: delete_monitor.sync_detailed(h.resource_id, client=client),
        lister=_Lister(
            method="POST",
            path="/api/monitors/list",
            container="monitors",
            id_field="uuid",
            name_field="title",
            page_size=1000,
        ),
    ),
    "silence": _Spec(
        delete=lambda client, h: delete_silence.sync_detailed(h.resource_id, client=client),
        # Silences have no name; the suite puts its unique name in `comment`.
        # The endpoint defaults to SilencesDefaultLimit = 1000
        # (internal/monitors/monitors.go:139), so it has to be paged like monitors.
        lister=_Lister(
            method="GET",
            path="/api/monitors/silences",
            id_field="id",
            name_field="comment",
            page_size=1000,
        ),
    ),
    "policy": _Spec(
        delete=lambda client, h: delete_policy.sync_detailed(h.resource_id, client=client),
        rank=30,
        lister=_Lister(method="GET", path="/api/rbac/policies/list", id_field="uuid", name_field="name"),
    ),
    "service-account": _Spec(
        delete=lambda client, h: delete_service_account.sync_detailed(h.resource_id, client=client),
        rank=20,
        lister=_Lister(
            method="GET",
            path="/api/rbac/service-accounts/list",
            id_field="serviceAccountId",
            name_field="name",
        ),
    ),
    "api-key": _Spec(
        delete=lambda client, h: delete_api_key.sync_detailed(h.resource_id, client=client),
        rank=10,
        # Deleting an API key revokes it, so a revoked key is still a row: ask for
        # revoked ones too or recovery cannot see what it is looking for.
        lister=_Lister(
            method="GET",
            path="/api/rbac/apikeys/list",
            params={"withRevoked": "true", "withExpired": "true"},
            id_field="id",
            name_field="name",
        ),
    ),
    "secret": _Spec(
        delete=lambda client, h: delete_secret.sync_detailed(h.resource_id, client=client),
        rank=60,
        # No list route exists for secrets (only create/update/delete/hash), so a
        # secret whose create response was lost cannot be recovered by name. Known
        # hole, not an oversight; a list route is requested in BE-2717.
        lister=None,
    ),
    "data-integration": _Spec(
        delete=_delete_data_integration,
        lister=_Lister(method="GET", path="/api/integrations/v1/data/config", id_field="id", name_field="name"),
    ),
    "ingestion-key": _Spec(delete=_delete_ingestion_key, id_required=False),
    "http-synthetic": _SYNTHETIC_SPEC,
    "tcp-synthetic": _SYNTHETIC_SPEC,
    "ssl-synthetic": _SYNTHETIC_SPEC,
    "dns-synthetic": _SYNTHETIC_SPEC,
}

# Runs after every resource delete; see ResourceTracker.add_finalizer.
_FINALIZER_RANK = 90


def _is_gone(exc: Exception) -> bool:
    """Whether this delete error means the resource is already gone."""
    return isinstance(exc, APIError) and exc.status_code in GONE_STATUSES


def _page_args(lister: _Lister, page: int) -> Dict[str, Optional[Dict[str, Any]]]:
    """Build the request body/params for one page of a listing."""
    # `is not None` rather than truthiness: a lister that explicitly configures an
    # empty body means "send {}", which is not the same as sending no body.
    body = dict(lister.body) if lister.body is not None else None
    params = dict(lister.params) if lister.params is not None else None
    if lister.page_size is not None:
        window = {"limit": lister.page_size, "skip": page * lister.page_size}
        if lister.method.upper() == "GET":
            params = dict(params or {})
            params.update(window)
        else:
            body = dict(body or {})
            body.update(window)
    return {"body": body, "params": params}


def _fetch_page(
    client: groundcover.Client,
    lister: _Lister,
    body: Optional[Dict[str, Any]],
    params: Optional[Dict[str, Any]] = None,
) -> List[Any]:
    """Return one page of listed resources, or raise if the shape is not what we expect.

    Shape surprises must not be swallowed: an unexpected payload previously became
    an empty list, so "the response did not parse" was indistinguishable from "the
    resource is not there" and a live resource could be silently left behind.
    """
    response = client.request(lister.method, lister.path, json=body, params=params)
    if not response.content:
        # These endpoints spell an empty collection "[]", so a zero-byte body is a
        # truncated or unexpected response. Reading it as an empty collection would
        # make a live resource look absent and skip its delete.
        raise RuntimeError("unexpected empty response from {} (status {})".format(lister.path, response.status_code))
    payload = response.json()
    if isinstance(payload, dict):
        key = lister.container or "items"
        if key not in payload:
            raise RuntimeError(
                "unexpected response from {}: object without a {!r} key (got {})".format(
                    lister.path, key, sorted(payload)[:8]
                )
            )
        items = payload[key]
    else:
        items = payload
    if items is None:
        return []
    if not isinstance(items, list):
        raise RuntimeError("unexpected response from {}: {} is not a list".format(lister.path, type(items).__name__))
    return items


def _find_by_field(
    client: groundcover.Client,
    lister: _Lister,
    field: str,
    value: str,
    exclude_ids: Optional[Set[str]] = None,
) -> Optional[Dict[str, Any]]:
    """Return the listed item whose ``field`` equals ``value``, or None.

    ``exclude_ids`` skips rows already claimed by another handle, which matters when
    two resources deliberately share a name (test_monitors creates a duplicate title
    to assert a 409): without it, recovery could resolve to the original row and
    leave the duplicate behind.
    """
    for page in range(_MAX_PAGES):
        args = _page_args(lister, page)
        items = _fetch_page(client, lister, args["body"], args["params"])
        for item in items:
            if not isinstance(item, dict) or str(item.get(field)) != value:
                continue
            if exclude_ids and str(item.get(lister.id_field)) in exclude_ids:
                continue
            return item

        # Unpaginated listers return everything in one response; paginated ones
        # are exhausted once a page comes back short.
        if lister.page_size is None or len(items) < lister.page_size:
            return None
    # Never report "gave up" as "not there": both callers read None as a definite
    # answer -- recovery as "the create never committed", the presence check as
    # "it is gone" -- so exhausting the page cap has to surface, not be logged.
    raise RuntimeError(
        "could not finish listing {}: still paging for {}={} after {} pages".format(
            lister.path, field, value, _MAX_PAGES
        )
    )


def _find_id_by_name(
    client: groundcover.Client,
    lister: _Lister,
    name: str,
    exclude_ids: Optional[Set[str]] = None,
) -> Optional[str]:
    """Resolve a resource id from its unique name, or None if it is not there.

    None means "no row carries this name". A row that matches but has no usable id
    raises instead: the resource exists and we cannot address it, which is a leak we
    must report rather than fold into "the create never committed".
    """
    item = _find_by_field(client, lister, lister.name_field, name, exclude_ids=exclude_ids)
    if item is None:
        return None
    found = item.get(lister.id_field)
    if found is None:
        raise RuntimeError(
            "found {} {!r} in {} but it has no {!r}, so it cannot be deleted".format(
                lister.name_field, name, lister.path, lister.id_field
            )
        )
    return str(found)


def _still_exists(client: groundcover.Client, lister: _Lister, resource_id: str) -> bool:
    """Whether a resource with this id is still listed.

    Checked by id rather than by name so a test that renames its resource before
    cleanup (test_silences updates the comment it is matched on) is handled. If the
    list request itself fails we cannot prove the resource is gone, so we assume it
    is still there and let the original delete failure stand.
    """
    try:
        return _find_by_field(client, lister, lister.id_field, resource_id) is not None
    except APIError:
        return True


class ResourceTracker:
    """Registry of resources one test is responsible for cleaning up."""

    def __init__(self, client: groundcover.Client) -> None:
        self._client = client
        self._entries: List[Any] = []
        self._handles: List[ResourceHandle] = []

    def new(self, kind: str, *, name: Optional[str] = None, **extra: Any) -> ResourceHandle:
        """Mint a unique name for a ``kind`` resource and register its cleanup.

        Call this immediately *above* the create request and pass ``handle.name``
        as the resource's name, then set ``handle.resource_id`` from the create
        response. Registering first is what makes a create that commits but
        errors recoverable.

        Pass ``name`` to register a resource whose name is already decided (e.g.
        a second create that reuses a name on purpose).
        """
        if kind not in SPECS:
            raise KeyError("unknown resource kind {!r}; add it to _cleanup.SPECS".format(kind))
        handle = ResourceHandle(kind=kind, name=name or unique_name(kind), extra=extra)
        self._entries.append((SPECS[kind].rank, len(self._entries), handle))
        self._handles.append(handle)
        return handle

    def forget(self, handle: ResourceHandle) -> None:
        """Stop tracking a resource the test has already deleted itself.

        The redundant delete this avoids is not free. A second destructive call can
        disturb state the first one is still settling -- for synthetics, deleting the
        config also deletes its companion Grafana alert, and re-issuing that made the
        *next* create fail with "Failed to create monitor". Go carries the same idea
        as ``Untrack*`` (``sdk/tests/e2e/setup.go``), which turns out to be load
        bearing rather than mere bookkeeping.
        """
        self._entries = [e for e in self._entries if e[2] is not handle]
        self._handles = [h for h in self._handles if h is not handle]

    def add_finalizer(self, label: str, restore: Callable[[], None]) -> None:
        """Register a non-delete teardown step, e.g. a singleton config restore.

        Runs after every resource delete, through the same error aggregation.
        """
        self._entries.append((_FINALIZER_RANK, len(self._entries), (label, restore)))

    def drain(self) -> None:
        """Delete everything registered, then raise if anything survived."""
        # Lower rank first; within a rank, reverse registration order (LIFO).
        pending = [entry for _, _, entry in sorted(self._entries, key=lambda e: (e[0], -e[1]))]
        self._entries = []

        failures: List[str] = []
        for attempt in (1, 2):
            retry: List[Any] = []
            for entry in pending:
                try:
                    self._run(entry)
                except Exception as exc:  # noqa: BLE001 - reported, not silenced
                    if attempt == 1:
                        # A 409 "still referenced" usually clears once the thing
                        # referencing it is gone, so give the whole batch a
                        # second pass before calling it a leak.
                        retry.append(entry)
                    else:
                        failures.append("{}: {}".format(_describe(entry), exc))
            pending = retry
            if not pending:
                break

        if failures:
            raise RuntimeError(
                "E2E cleanup failed, {} resource(s) may have leaked:\n  {}".format(len(failures), "\n  ".join(failures))
            )

    def _run(self, entry: Any) -> None:
        if isinstance(entry, tuple):
            label, restore = entry
            restore()
            logger.info("e2e cleanup: ran %s", label)
            return

        handle: ResourceHandle = entry
        spec = SPECS[handle.kind]
        if handle.resource_id is None and spec.id_required:
            if spec.lister is None:
                # Nothing to go on: no id from the create, no way to look it up.
                logger.warning(
                    "e2e cleanup: cannot clean %s %s -- no id was captured and this kind has no list route",
                    handle.kind,
                    handle.name,
                )
                return
            # Never resolve to a row another handle already owns: two resources can
            # share a name on purpose (test_monitors' duplicate-title 409 check).
            claimed = {
                str(other.resource_id)
                for other in self._handles
                if other is not handle and other.resource_id is not None
            }
            try:
                handle.resource_id = _find_id_by_name(self._client, spec.lister, handle.name, exclude_ids=claimed)
            except APIError as exc:
                # The lookup failed, so whether the create committed is unknowable.
                # Warn rather than fail: reaching here means no id was ever captured,
                # which means the test itself already failed -- and it failed against
                # the same broken endpoint, so raising adds a second red mark for one
                # fault and no new information. Claiming a leak would be as wrong as
                # claiming success. Observed live before workflows were removed from
                # the SDK (AI-461): when a list endpoint answers 500 the test fails on
                # its own create, and every tracked resource of that kind then added a
                # teardown ERROR on top of it.
                logger.warning(
                    "e2e cleanup: cannot determine whether %s %s leaked -- listing %s failed with %s",
                    handle.kind,
                    handle.name,
                    spec.lister.path,
                    exc,
                )
                return
            if handle.resource_id is None and spec.id_required:
                # The create never committed; nothing to clean.
                return
            logger.warning(
                "e2e cleanup: recovered %s %s by name (id %s) -- the create committed but the test never saw it",
                handle.kind,
                handle.name,
                handle.resource_id,
            )
        try:
            spec.delete(self._client, handle)
        except Exception as exc:  # noqa: BLE001 - classified below
            if _is_gone(exc):
                return
            # Not every endpoint answers 404 for a resource that is already gone:
            # DELETE /api/monitors/silences/{id} answers 500. So before calling
            # this a leak, confirm the resource really is still listed. Costs a
            # request only on the failure path.
            if (
                spec.lister is not None
                and handle.resource_id is not None
                and not _still_exists(self._client, spec.lister, handle.resource_id)
            ):
                logger.info(
                    "e2e cleanup: %s %s is already gone; its delete answered %s",
                    handle.kind,
                    handle.name,
                    exc,
                )
                return
            raise
        logger.info("e2e cleanup: deleted %s %s (%s)", handle.kind, handle.name, handle.resource_id)


def _describe(entry: Any) -> str:
    if isinstance(entry, tuple):
        return str(entry[0])
    return "{} {} (id {})".format(entry.kind, entry.name, entry.resource_id)
