from __future__ import annotations

import dataclasses
import json as jsonlib
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Mapping, Optional

logger = logging.getLogger(__name__)

# Retried on 5xx, because those are transient often enough to be worth it. 4xx is
# never retried: it is an answer, not a failure to answer.
_MAX_ATTEMPTS = 3
_BACKOFF_SECONDS = 1.5

# A DELETE is never retried even on a timeout. These deletes are not all
# idempotent -- re-deleting a synthetic re-triggers companion-monitor deletion,
# which is the operation that intermittently fails -- and a timed-out DELETE has
# very likely committed. Re-issuing it turns one uncertain outcome into two.
_RETRYABLE_METHODS = frozenset({"GET", "POST"})


class TransportError(RuntimeError):
    pass


class _NoCrossOriginRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        old_origin = urllib.parse.urlparse(req.full_url)
        new_origin = urllib.parse.urlparse(newurl)
        if (new_origin.scheme, new_origin.netloc) != (old_origin.scheme, old_origin.netloc):
            raise TransportError(
                "refusing a cross-origin redirect from {}://{} to {}://{}: it would forward the API key".format(
                    old_origin.scheme, old_origin.netloc, new_origin.scheme, new_origin.netloc
                )
            )
        return super().redirect_request(req, fp, code, msg, headers, newurl)


@dataclasses.dataclass(frozen=True)
class Response:
    status: int
    content: bytes

    def json(self) -> Any:
        if not self.content.strip():
            raise TransportError(
                "HTTP {} returned an empty body; these endpoints spell an empty list as [], "
                "so this is a truncated or dropped response, not an empty result".format(self.status)
            )
        try:
            return jsonlib.loads(self.content)
        except ValueError as exc:
            raise TransportError("HTTP {} returned a body that is not JSON: {}".format(self.status, exc)) from exc


class Client:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        backend_id: str,
        timeout: float = 60.0,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._backend_id = backend_id
        # Held apart from anything that gets logged or repr'd.
        self._auth_header = "Bearer {}".format(api_key)
        self._timeout = timeout
        self._opener = urllib.request.build_opener(_NoCrossOriginRedirect)

    def __repr__(self) -> str:
        # Explicit, so a stack trace or a debugger can never spill the key.
        return "Client(base_url={!r}, backend_id={!r})".format(self._base_url, self._backend_id)

    def request(
        self,
        method: str,
        path: str,
        *,
        json: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
    ) -> Response:
        url = self._base_url + path
        if params:
            url = "{}?{}".format(url, urllib.parse.urlencode(params))

        body: Optional[bytes] = None
        headers: Dict[str, str] = {
            "Authorization": self._auth_header,
            "X-Backend-Id": self._backend_id,
            "Accept": "application/json",
        }
        if json is not None:
            body = jsonlib.dumps(json).encode()
            headers["Content-Type"] = "application/json"

        last_error: Optional[Exception] = None
        for attempt in range(1, _MAX_ATTEMPTS + 1):
            try:
                response = self._send(method, url, body, headers)
            except (urllib.error.URLError, OSError) as exc:
                last_error = exc
                if method.upper() not in _RETRYABLE_METHODS or attempt == _MAX_ATTEMPTS:
                    raise TransportError("{} {} failed: {}".format(method, path, exc)) from exc
            else:
                retryable = response.status >= 500 and method.upper() in _RETRYABLE_METHODS
                if not retryable or attempt == _MAX_ATTEMPTS:
                    return response
                logger.warning(
                    "%s %s -> %s, retrying (attempt %d/%d)", method, path, response.status, attempt, _MAX_ATTEMPTS
                )
            time.sleep(_BACKOFF_SECONDS * attempt)

        # Unreachable: the loop either returns or raises on its final attempt.
        raise TransportError("{} {} failed: {}".format(method, path, last_error))

    def _send(self, method: str, url: str, body: Optional[bytes], headers: Mapping[str, str]) -> Response:
        request = urllib.request.Request(url, data=body, headers=dict(headers), method=method.upper())
        try:
            with self._opener.open(request, timeout=self._timeout) as raw:
                return Response(status=raw.status, content=raw.read())
        except urllib.error.HTTPError as exc:
            # HTTPError IS a readable file object. Normalising it here is what
            # keeps a 404 from surfacing as an exception three layers up, where
            # the caller has no way to tell it from a connection failure.
            return Response(status=exc.code, content=exc.read())
