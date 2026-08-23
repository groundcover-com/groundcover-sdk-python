from __future__ import annotations

import dataclasses
import re
from typing import Any, Dict, Optional, Pattern, Tuple

# Named rather than inferred from an empty `timestamp_fields`, so sweeping a kind
# the age gate never looked at is something someone had to type.
AGE_FROM_TIMESTAMP = "timestamp"
# What protects an ungated kind is not uniform: service-account has a lastActive
# veto, ingestion-key has nothing time-based at all.
AGE_UNGATED = "ungated"


@dataclasses.dataclass(frozen=True)
class ListRoute:
    method: str
    path: str
    # None => the payload is a bare JSON array. Otherwise the envelope key.
    container: Optional[str] = None
    params: Optional[Dict[str, Any]] = None
    # {} means "send an empty JSON body", which ingestion-keys/list requires and
    # which is not the same as sending none.
    body: Optional[Dict[str, Any]] = None
    page_size: Optional[int] = None
    # For endpoints that cap their response and offer no skip/cursor -- agent
    # skills (agent/controller.go:388) and monitors/summary/query, which hardcodes
    # 5000 (summary_query.go:196). A full response is then indistinguishable from
    # a truncated one, so the sweep refuses to conclude. Excludes page_size.
    hard_cap: Optional[int] = None


@dataclasses.dataclass(frozen=True)
class DeleteRoute:
    # "/api/dashboards/{id}", "/api/integrations/v1/data/config/{type}/{id}"
    path_template: Optional[str] = None
    # Fixed path plus a JSON body naming the resource (ingestion keys).
    path: Optional[str] = None
    body_template: Optional[Dict[str, str]] = None
    method: str = "DELETE"
    # These routes answer 200, 202 or 204. Any 2xx counts, but 202 stays
    # distinguishable -- it means accepted, not done.
    accepted_status: int = 202
    # 404 only. A 400 is a rejection, never "gone".
    gone_statuses: Tuple[int, ...] = (404,)
    # "Did something, but the response does not say what" -- counted apart from
    # `deleted` and resolved by re-listing, like accepted_status.
    unverified_statuses: Tuple[int, ...] = ()


@dataclasses.dataclass(frozen=True)
class Kind:
    kind: str
    list_route: ListRoute
    delete_route: DeleteRoute
    id_field: str
    # Ordered, first non-empty wins: silences carry the unique name in `comment`
    # and monitors in `title`, not `name`.
    name_fields: Tuple[str, ...]
    age_source: str
    # Lower rank deletes first, as a barrier not a sort: a live API key makes its
    # service account's DELETE answer 400.
    rank: int = 50
    # The age gate uses max(created, updated), so a resource someone is actively
    # editing reads as fresh however old it is.
    timestamp_fields: Tuple[str, ...] = ()
    # Holds the SERVICE ACCOUNT'S NAME under API-key auth, not an email
    # (gc_apikey_middleware.go:105). That account is shared with other
    # automation -- on backend-dev it also owns 982 non-e2e monitors -- so this
    # proves "not a human's", not "e2e's". A conjunct with the name, not a
    # substitute.
    creator_field: Optional[str] = None
    # A freshness veto, not an age source. See sweep.py.
    last_active_field: Optional[str] = None
    # {field: (values...)} -- a row is excluded when the field holds any of them.
    exclude_when: Tuple[Tuple[str, Tuple[Any, ...]], ...] = ()
    # The inverse, for two kinds sharing one list route and wanting disjoint
    # slices of it. exclude_when cannot express that without enumerating every
    # value that exists today and swallowing any added later.
    include_only_when: Tuple[Tuple[str, Tuple[Any, ...]], ...] = ()
    # Name of another kind whose listing must NOT contain this row's delete id.
    # Fail-closed: if that listing cannot be obtained completely, no candidate of
    # this kind is deleted, because absence cannot be proved from a partial list.
    #
    # This exists because synthetic-companion-monitor deletes by asking the
    # SYNTHETICS route to remove the synthetic -- so a companion whose synthetic
    # is still live would take the live synthetic with it. Rank ordering is not
    # enough on its own: phase 1 lists every kind before phase 2 deletes anything,
    # so the companion rows are captured while the synthetic still exists.
    requires_absent_from: Optional[str] = None
    # The kind tokens the suites actually put in a name for this kind. They do
    # not all equal `kind`: Go writes "apikey" and "skill" where the registry
    # says "api-key" and "agent-skill". Each becomes an anchored pattern via
    # _suite_pattern(); test_janitor_registry proves the set covers both suites.
    name_tokens: Tuple[str, ...] = ()
    # Whether a sub-kind segment may precede the token. See _suite_pattern.
    allow_name_infix: bool = False
    # Name shapes no generated pattern can reach -- different case, spaces, or
    # no e2e token at all.
    extra_name_patterns: Tuple[Pattern[str], ...] = ()
    # Fields copied verbatim into the delete route's templates.
    extra_delete_fields: Tuple[str, ...] = ()

    @property
    def name_patterns(self) -> Tuple[Pattern[str], ...]:
        generated = tuple(_suite_pattern(t, self.allow_name_infix) for t in self.name_tokens)
        return generated + self.extra_name_patterns


# The five prefixes the suites are observed to mint. The last two are TypeScript
# inconsistencies rather than a convention, kept because their debris exists:
#
#   e2e-test-           Go            e2e-test-dashboard-<uuid>
#   sdk-e2e-test-       Go, Python    sdk-e2e-test-<kind>-<run_id>-p<pid>n<counter>
#   sdk-ts-e2e-test-    TypeScript    most of its kinds
#   ts-sdk-e2e-test-    TypeScript    skills only
#   e2e-ts-test-        TypeScript    silences only
_SUITE_PREFIX = r"(?:(?:[a-z0-9]+-)?sdk-(?:[a-z0-9]+-)?)?e2e-(?:[a-z0-9]+-)?test-"

# The contract a future suite mints against. Derived from the matcher's own
# string so the two cannot disagree.
SUITE_NAME_RE = re.compile("^" + _SUITE_PREFIX)

# Loose, and never used to delete: a name matching this but no strict pattern is
# counted and logged. That count is how the two TypeScript prefixes above were
# found, while every strict pattern reported clean.
LOOKALIKE_RE = re.compile(r"e2e[-_ ]?test", re.IGNORECASE)

_UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

# The machine tail every suite name ends with, and the thing that actually
# separates debris from a human's resource: a prefix test alone accepts
# `e2e-test-dashboard-for-the-demo`. Python mints <run_id>-p<pid>n<counter>
# (tests/e2e/_names.py:121); Go mints a uuid or a unixnano.
_RUN_SUFFIX = r"(?:[0-9a-z]+-p[0-9]+n[0-9]+|" + _UUID + r"|[0-9]{13,20})"

# Segments appended after the machine tail: `-updated`, `-created`, a bare `-2`.
# The gate is the required tail, not the end anchor, so this does not loosen it.
_NAME_SUFFIX = r"(?:-[a-z0-9]+)*"


def _suite_regex(token: str, allow_infix: bool = False) -> str:
    infix = r"(?:[a-z0-9-]+-)?" if allow_infix else ""
    return _SUITE_PREFIX + infix + re.escape(token) + r"-" + _RUN_SUFFIX + _NAME_SUFFIX


def _suite_pattern(token: str, allow_infix: bool = False) -> Pattern[str]:
    return re.compile("^" + _suite_regex(token, allow_infix) + "$")


# Kinds the suites create that we deliberately do not sweep -- a reason, not an
# absence. A test asserts every tracked kind lands here or in KINDS.
UNSWEEPABLE: Dict[str, str] = {
    "secret": (
        "No list route exists -- only create/update/delete/hash "
        "(internal/services/router/api/secret/uris/uris.go), so a leaked secret "
        "cannot be enumerated at all, by name or otherwise. Requested in BE-2717."
    ),
}


KINDS: Dict[str, Kind] = {
    # GET /api/dashboards rather than POST /api/dashboards/list: only the former
    # carries timestamps and `owner` (views_dal.go:34-41).
    "dashboard": Kind(
        kind="dashboard",
        list_route=ListRoute(method="GET", path="/api/dashboards"),
        delete_route=DeleteRoute(path_template="/api/dashboards/{id}"),
        id_field="uuid",
        name_fields=("name",),
        age_source=AGE_FROM_TIMESTAMP,
        timestamp_fields=("updatedTimestamp", "createdTimestamp"),
        creator_field="owner",
        # Deleting either means fighting Terraform or the catalog installer.
        exclude_when=(("isProvisioned", (True,)), ("originType", ("Catalog",))),
        name_tokens=("dashboard",),
    ),
    # POST /api/monitors/list has no timestamp and no creator; summary/query has
    # createdByEmail, createdAt, updatedAt AND originType, so one call satisfies
    # the creator gate, the age gate and the synthetic-owned exclusion together.
    # It hardcodes a 5000 limit and ignores skip (summary_query.go:196), hence
    # hard_cap rather than page_size.
    "monitor": Kind(
        kind="monitor",
        list_route=ListRoute(
            method="POST",
            path="/api/monitors/summary/query",
            container="results",
            body={},
            hard_cap=5000,
        ),
        delete_route=DeleteRoute(path_template="/api/monitors/{id}"),
        id_field="uuid",
        name_fields=("title", "name"),
        age_source=AGE_FROM_TIMESTAMP,
        timestamp_fields=("updatedAt", "createdAt"),
        creator_field="createdByEmail",
        # A companion monitor cannot be deleted through this route at all: the
        # UPDATE carries `origin_type != 'SyntheticTest'` and 0 rows becomes 403
        # (monitors.go:84,1100). synthetic-companion-monitor reclaims them.
        exclude_when=(("originType", ("SyntheticTest",)), ("isProvisioned", (True,))),
        name_tokens=("monitor",),
        extra_name_patterns=(
            # monitors_test.go:51. The trailing int is rng.Intn(10_000_000), not a
            # timestamp. No _NAME_SUFFIX: with no uuid or timestamp this is the one
            # pattern a person could plausibly type, so it must not widen.
            re.compile(r"^E2E Test - K8s Pod Not Healthy Monitor - [0-9]{1,7}$"),
            # Matched only so the originType exclusion above can count companions
            # rather than reporting hundreds of them as unrecognised lookalikes,
            # which would bury the one signal that list carries.
            re.compile(r"^\[synthetic\] - " + _suite_regex("synthetic", allow_infix=True) + r"$"),
        ),
    ),
    # v2, not v1: v1's only time field is the caller-supplied `startsAt`, which is
    # backdatable. Needs backend >= 1.11.750; older ones 404 and report `partial`.
    "silence": Kind(
        kind="silence",
        list_route=ListRoute(
            method="GET",
            path="/api/monitors/v2/silences",
            container="silences",
            page_size=1000,
        ),
        delete_route=DeleteRoute(path_template="/api/monitors/v2/silences/{id}"),
        id_field="id",
        name_fields=("comment",),
        age_source=AGE_FROM_TIMESTAMP,
        timestamp_fields=("updatedAt", "createdAt"),
        creator_field="createdByEmail",
        name_tokens=("silence",),
    ),
    "policy": Kind(
        kind="policy",
        list_route=ListRoute(method="GET", path="/api/rbac/policies/list"),
        delete_route=DeleteRoute(path_template="/api/rbac/policy/{id}"),
        id_field="uuid",
        name_fields=("name",),
        age_source=AGE_FROM_TIMESTAMP,
        timestamp_fields=("updatedTimestamp", "createdTimestamp"),
        creator_field="createdBy",
        rank=30,
        # readOnly policies answer 404 on delete (delete_policy.go:61), which is
        # indistinguishable from "already gone". sweep.py adds an entityCount > 0
        # exclusion, which is what keeps the janitor's own policy safe.
        exclude_when=(("readOnly", (True,)),),
        name_tokens=("policy", "policy-for-apikey", "policy-for-sa"),
        extra_name_patterns=(
            # Historic: the Go suite now mints e2e-test-policy-for-sa-<uuid>, but
            # this shape has no e2e token and its debris still exists.
            re.compile(r"^sa-test-policy-" + _UUID + _NAME_SUFFIX + r"$"),
        ),
    ),
    # No creation timestamp is exposed: the DAL selects creation_date and the HTTP
    # mapper never copies it (list_service_accounts.go:50). Ungated by decision,
    # guarded by the lastActive veto.
    "service-account": Kind(
        kind="service-account",
        list_route=ListRoute(method="GET", path="/api/rbac/service-accounts/list"),
        delete_route=DeleteRoute(path_template="/api/rbac/service-account/{id}"),
        id_field="serviceAccountId",
        name_fields=("name",),
        age_source=AGE_UNGATED,
        last_active_field="lastActive",
        rank=20,
        name_tokens=("service-account", "sa", "sa-for-apikey"),
    ),
    # Deliberately WITHOUT withRevoked/withExpired: DELETE here is a revoke
    # (queries.go:70), so asking for revoked rows resurfaces every key the janitor
    # ever deleted and retries them forever.
    "api-key": Kind(
        kind="api-key",
        list_route=ListRoute(method="GET", path="/api/rbac/apikeys/list"),
        delete_route=DeleteRoute(path_template="/api/rbac/apikey/{id}"),
        id_field="id",
        name_fields=("name",),
        age_source=AGE_FROM_TIMESTAMP,
        timestamp_fields=("creationDate",),
        creator_field="createdBy",
        # The middleware bumps last_used on every authenticated request
        # (gc_apikey_middleware.go:94), so the janitor's own key can never pass
        # this veto.
        last_active_field="lastActive",
        rank=10,
        # Go writes "apikey", Python writes "api-key".
        name_tokens=("api-key", "apikey"),
    ),
    "synthetic": Kind(
        kind="synthetic",
        # hard_cap is a tripwire, not a known server limit: this route takes no
        # paging parameters, so without it every 200 is marked complete by
        # construction and requires_absent_from below would prove absence from a
        # listing that could have been silently truncated.
        list_route=ListRoute(method="GET", path="/api/synthetics/v1/rules", container="synthetics", hard_cap=5000),
        delete_route=DeleteRoute(path_template="/api/synthetics/v1/rules/{id}"),
        id_field="id",
        name_fields=("name",),
        age_source=AGE_FROM_TIMESTAMP,
        # No createdAt exists; modifiedAt moves on every update.
        timestamp_fields=("modifiedAt",),
        creator_field="creator",
        # The only kind needing the infix: Python mints http-/tcp-/ssl-/dns-.
        name_tokens=("synthetic",),
        allow_name_infix=True,
    ),
    # Reclaims companion monitors whose synthetic is already gone -- which nothing
    # else can (BE-2727). DELETE /api/monitors/{id} answers 403 for them by design
    # (monitors.go:84,1100, pinned by TestDeleteMonitorSyntheticTestOrigin), and the
    # only path that removes one is DeleteMonitorByOrigin, reachable solely by
    # deleting the owning synthetic (synthetics/service.go:483).
    #
    # So this deletes a MONITOR through the SYNTHETICS route, and that call's
    # FAILURE is its success signal: it reaps the companion first, then fails on the
    # missing config with 404, or 410 if the config is merely archived -- which is
    # the common case, since a fleet-manager delete IS an archive (manage/v2.go:152).
    # A 500 means the monitor delete itself failed and stays a failure.
    #
    # Both are `unverified`, never `deleted`: the response never says the monitor
    # went, so the re-list is the proof. That is what makes this safe despite
    # depending on undocumented ordering inside a handler. The durable fix is to make
    # the synthetics delete idempotent when its config is gone, mirroring the
    # tolerance it already has for a missing monitor (service.go:484); this kind then
    # keeps working and starts seeing 204s. If these deletes start reporting 500, or
    # confirm starts reporting them still-listed, the ordering changed and this goes.
    "synthetic-companion-monitor": Kind(
        kind="synthetic-companion-monitor",
        # The same listing as `monitor`, sliced the other way.
        list_route=ListRoute(
            method="POST",
            path="/api/monitors/summary/query",
            container="results",
            body={},
            hard_cap=5000,
        ),
        # Addressed by the synthetic's config id, exposed on the monitor listing as
        # originId (api/monitors/monitors.go:141).
        delete_route=DeleteRoute(
            path_template="/api/synthetics/v1/rules/{id}",
            unverified_statuses=(404, 410),
            # No status here proves absence: a 404 means the CONFIG was gone, which
            # says nothing about the monitor.
            gone_statuses=(),
        ),
        # originId rather than uuid: the DELETE and the confirming re-list then use
        # the same identifier. One companion exists per config id.
        id_field="originId",
        name_fields=("title",),
        age_source=AGE_FROM_TIMESTAMP,
        timestamp_fields=("updatedAt", "createdAt"),
        creator_field="createdByEmail",
        # After `synthetic` (50), so this only mops up what that left behind.
        rank=60,
        include_only_when=(("originType", ("SyntheticTest",)),),
        exclude_when=(("isProvisioned", (True,)),),
        # No generated pattern: the title is "[synthetic] - <name>", so the e2e
        # token sits inside rather than at the front.
        name_tokens=(),
        extra_name_patterns=(re.compile(r"^\[synthetic\] - " + _suite_regex("synthetic", allow_infix=True) + r"$"),),
        requires_absent_from="synthetic",
    ),
    "data-integration": Kind(
        kind="data-integration",
        list_route=ListRoute(method="GET", path="/api/integrations/v1/data/config"),
        delete_route=DeleteRoute(
            path_template="/api/integrations/v1/data/config/{type}/{id}",
        ),
        id_field="id",
        name_fields=("name",),
        age_source=AGE_FROM_TIMESTAMP,
        timestamp_fields=("update_timestamp",),
        exclude_when=(("is_archived", (True,)),),
        extra_delete_fields=("type",),
        name_tokens=("data-integration", "cloudwatch", "cloudwatch-tags", "cloudwatch-tags-updated"),
        extra_name_patterns=(
            # Historic: renamed to the convention in this change.
            re.compile(r"^e2e-cloudwatch-" + _UUID + _NAME_SUFFIX + r"$"),
        ),
    ),
    # Addressed by name in a JSON body, never by id (delete_key.go:28), so it is
    # cleanable even when the create response was never seen. Kong's created_at is
    # validated and then discarded (list_keys.go:116), so there is no age signal
    # and no lastActive either -- ungated by decision.
    "ingestion-key": Kind(
        kind="ingestion-key",
        list_route=ListRoute(method="POST", path="/api/rbac/ingestion-keys/list", body={}),
        delete_route=DeleteRoute(
            path="/api/rbac/ingestion-keys/delete",
            body_template={"name": "{name}"},
        ),
        id_field="id",
        name_fields=("name",),
        age_source=AGE_UNGATED,
        name_tokens=("ingestion-key",),
    ),
    # Go-suite only, absent from tests/e2e/_cleanup.SPECS -- one reason this table
    # cannot be derived from SPECS. Under API-key auth the listing only covers
    # service-account-owned and organizational skills, so a human's skill is
    # invisible here rather than protected by a gate.
    "agent-skill": Kind(
        kind="agent-skill",
        list_route=ListRoute(
            method="GET",
            path="/api/agent/skills",
            container="skills",
            params={"limit": 250},
            hard_cap=250,
        ),
        delete_route=DeleteRoute(path_template="/api/agent/skills/{id}"),
        id_field="id",
        name_fields=("name",),
        age_source=AGE_FROM_TIMESTAMP,
        timestamp_fields=("updated_at", "created_at"),
        # Go writes "skill"; the registry key is "agent-skill".
        name_tokens=("agent-skill", "skill"),
    ),
}


class RegistryError(ValueError):
    pass


def _validate() -> None:
    for kind, spec in KINDS.items():
        if kind != spec.kind:
            raise RegistryError("{}: keyed as {} but names itself {}".format(kind, kind, spec.kind))
        if kind in UNSWEEPABLE:
            raise RegistryError("{}: is in both KINDS and UNSWEEPABLE".format(kind))

        lr = spec.list_route
        if lr.page_size is not None and lr.hard_cap is not None:
            raise RegistryError(
                "{}: page_size and hard_cap are mutually exclusive -- a capped endpoint either "
                "pages or refuses to conclude, never both".format(kind)
            )

        dr = spec.delete_route
        if bool(dr.path_template) == bool(dr.path):
            raise RegistryError("{}: delete needs exactly one of path_template or path".format(kind))
        if bool(dr.path) != bool(dr.body_template):
            raise RegistryError("{}: a body-addressed delete needs both path and body_template".format(kind))
        allowed = {"id", "name"} | set(spec.extra_delete_fields)
        for template in (dr.path_template or "", "".join((dr.body_template or {}).values())):
            for field in re.findall(r"{(\w+)}", template):
                if field not in allowed:
                    raise RegistryError(
                        "{}: delete template references {{{}}}, which is not id, name or one of "
                        "extra_delete_fields {}".format(kind, field, spec.extra_delete_fields)
                    )

        if not spec.name_fields:
            raise RegistryError("{}: needs at least one name field".format(kind))
        has_timestamps = bool(spec.timestamp_fields)
        if (spec.age_source == AGE_FROM_TIMESTAMP) != has_timestamps:
            raise RegistryError(
                "{}: age_source={} but timestamp_fields={} -- a timestamp-aged kind must name its "
                "fields, and an ungated kind must not pretend to have them".format(
                    kind, spec.age_source, spec.timestamp_fields
                )
            )
        if spec.age_source not in (AGE_FROM_TIMESTAMP, AGE_UNGATED):
            raise RegistryError("{}: unknown age_source {!r}".format(kind, spec.age_source))

        overlap = set(dr.unverified_statuses) & set(dr.gone_statuses)
        if overlap:
            raise RegistryError(
                "{}: {} is both unverified and gone -- one means 'proved absent', the other means "
                "'no idea', so a status cannot be both".format(kind, sorted(overlap))
            )
        for status in dr.unverified_statuses:
            # delete_one() tests unverified before accepted_status and the generic
            # 2xx branch, so a success code here would be booked as indeterminate.
            if 200 <= status < 300:
                raise RegistryError(
                    "{}: unverified status {} is a success code -- those are already counted as "
                    "deleted or accepted, and listing one here downgrades a completed delete to "
                    "'no idea'".format(kind, status)
                )
            if status == dr.accepted_status:
                raise RegistryError("{}: unverified status {} is also accepted_status".format(kind, status))

        for field, _ in spec.include_only_when:
            if any(field == excluded for excluded, _ in spec.exclude_when):
                raise RegistryError(
                    "{}: {!r} appears in both include_only_when and exclude_when, which is a "
                    "contradiction rather than a narrowing".format(kind, field)
                )

        dep = spec.requires_absent_from
        if dep is not None:
            if dep not in KINDS:
                raise RegistryError("{}: requires_absent_from names unknown kind {!r}".format(kind, dep))
            if dep == kind:
                raise RegistryError("{}: requires_absent_from cannot name itself".format(kind))
            # The gate is what makes this safe, not the ordering -- but a dependency
            # ranked after its dependent means the ordering was a mistake.
            if KINDS[dep].rank >= spec.rank:
                raise RegistryError(
                    "{}: rank {} must be greater than {}'s rank {} so the dependency is already "
                    "swept when this kind runs".format(kind, spec.rank, dep, KINDS[dep].rank)
                )
            dep_route = KINDS[dep].list_route
            if dep_route.page_size is None and dep_route.hard_cap is None:
                # Otherwise _drop_present_in's truncation check is a dead guard:
                # list_rows() marks a capless route complete for any 200.
                raise RegistryError(
                    "{}: depends on {}, whose list route sets neither page_size nor hard_cap, so "
                    "its listing can never report itself incomplete and absence cannot be "
                    "proved".format(kind, dep)
                )

    for kind, reason in UNSWEEPABLE.items():
        if not reason.strip():
            raise RegistryError("{}: UNSWEEPABLE needs a reason".format(kind))


_validate()
