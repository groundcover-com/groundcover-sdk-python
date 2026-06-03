from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_request_defines_model_for_http_request_auth import HttpRequestDefinesModelForHttpRequestAuth
    from ..models.http_request_defines_model_for_http_request_body import HttpRequestDefinesModelForHttpRequestBody
    from ..models.http_request_defines_model_for_http_request_cookies_item import (
        HttpRequestDefinesModelForHttpRequestCookiesItem,
    )
    from ..models.http_request_defines_model_for_http_request_headers import (
        HttpRequestDefinesModelForHttpRequestHeaders,
    )
    from ..models.http_request_defines_model_for_http_request_query_params import (
        HttpRequestDefinesModelForHttpRequestQueryParams,
    )


T = TypeVar("T", bound="HttpRequestDefinesModelForHttpRequest")


@_attrs_define
class HttpRequestDefinesModelForHttpRequest:
    """
    Attributes:
        allow_insecure (bool | Unset):
        auth (HttpRequestDefinesModelForHttpRequestAuth | Unset):
        body (HttpRequestDefinesModelForHttpRequestBody | Unset):
        cookies (list[HttpRequestDefinesModelForHttpRequestCookiesItem] | Unset):
        follow_redirects (bool | Unset):
        headers (HttpRequestDefinesModelForHttpRequestHeaders | Unset):
        http_version (str | Unset):
        kind (str | Unset):
        method (str | Unset):
        query_params (HttpRequestDefinesModelForHttpRequestQueryParams | Unset):
        timeout (str | Unset):
        url (str | Unset):
    """

    allow_insecure: bool | Unset = UNSET
    auth: HttpRequestDefinesModelForHttpRequestAuth | Unset = UNSET
    body: HttpRequestDefinesModelForHttpRequestBody | Unset = UNSET
    cookies: list[HttpRequestDefinesModelForHttpRequestCookiesItem] | Unset = UNSET
    follow_redirects: bool | Unset = UNSET
    headers: HttpRequestDefinesModelForHttpRequestHeaders | Unset = UNSET
    http_version: str | Unset = UNSET
    kind: str | Unset = UNSET
    method: str | Unset = UNSET
    query_params: HttpRequestDefinesModelForHttpRequestQueryParams | Unset = UNSET
    timeout: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_insecure = self.allow_insecure

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        cookies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cookies, Unset):
            cookies = []
            for cookies_item_data in self.cookies:
                cookies_item = cookies_item_data.to_dict()
                cookies.append(cookies_item)

        follow_redirects = self.follow_redirects

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        http_version = self.http_version

        kind = self.kind

        method = self.method

        query_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_params, Unset):
            query_params = self.query_params.to_dict()

        timeout = self.timeout

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_insecure is not UNSET:
            field_dict["allowInsecure"] = allow_insecure
        if auth is not UNSET:
            field_dict["auth"] = auth
        if body is not UNSET:
            field_dict["body"] = body
        if cookies is not UNSET:
            field_dict["cookies"] = cookies
        if follow_redirects is not UNSET:
            field_dict["followRedirects"] = follow_redirects
        if headers is not UNSET:
            field_dict["headers"] = headers
        if http_version is not UNSET:
            field_dict["httpVersion"] = http_version
        if kind is not UNSET:
            field_dict["kind"] = kind
        if method is not UNSET:
            field_dict["method"] = method
        if query_params is not UNSET:
            field_dict["queryParams"] = query_params
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_request_defines_model_for_http_request_auth import HttpRequestDefinesModelForHttpRequestAuth
        from ..models.http_request_defines_model_for_http_request_body import HttpRequestDefinesModelForHttpRequestBody
        from ..models.http_request_defines_model_for_http_request_cookies_item import (
            HttpRequestDefinesModelForHttpRequestCookiesItem,
        )
        from ..models.http_request_defines_model_for_http_request_headers import (
            HttpRequestDefinesModelForHttpRequestHeaders,
        )
        from ..models.http_request_defines_model_for_http_request_query_params import (
            HttpRequestDefinesModelForHttpRequestQueryParams,
        )

        d = dict(src_dict)
        allow_insecure = d.pop("allowInsecure", UNSET)

        _auth = d.pop("auth", UNSET)
        auth: HttpRequestDefinesModelForHttpRequestAuth | Unset
        if isinstance(_auth, Unset) or _auth is None:
            auth = UNSET
        else:
            auth = HttpRequestDefinesModelForHttpRequestAuth.from_dict(_auth)

        _body = d.pop("body", UNSET)
        body: HttpRequestDefinesModelForHttpRequestBody | Unset
        if isinstance(_body, Unset) or _body is None:
            body = UNSET
        else:
            body = HttpRequestDefinesModelForHttpRequestBody.from_dict(_body)

        _cookies = d.pop("cookies", UNSET)
        cookies: list[HttpRequestDefinesModelForHttpRequestCookiesItem] | Unset = UNSET
        if _cookies is not UNSET:
            cookies = []
            for cookies_item_data in _cookies:
                cookies_item = HttpRequestDefinesModelForHttpRequestCookiesItem.from_dict(cookies_item_data)

                cookies.append(cookies_item)

        follow_redirects = d.pop("followRedirects", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: HttpRequestDefinesModelForHttpRequestHeaders | Unset
        if isinstance(_headers, Unset) or _headers is None:
            headers = UNSET
        else:
            headers = HttpRequestDefinesModelForHttpRequestHeaders.from_dict(_headers)

        http_version = d.pop("httpVersion", UNSET)

        kind = d.pop("kind", UNSET)

        method = d.pop("method", UNSET)

        _query_params = d.pop("queryParams", UNSET)
        query_params: HttpRequestDefinesModelForHttpRequestQueryParams | Unset
        if isinstance(_query_params, Unset) or _query_params is None:
            query_params = UNSET
        else:
            query_params = HttpRequestDefinesModelForHttpRequestQueryParams.from_dict(_query_params)

        timeout = d.pop("timeout", UNSET)

        url = d.pop("url", UNSET)

        http_request_defines_model_for_http_request = cls(
            allow_insecure=allow_insecure,
            auth=auth,
            body=body,
            cookies=cookies,
            follow_redirects=follow_redirects,
            headers=headers,
            http_version=http_version,
            kind=kind,
            method=method,
            query_params=query_params,
            timeout=timeout,
            url=url,
        )

        http_request_defines_model_for_http_request.additional_properties = d
        return http_request_defines_model_for_http_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
